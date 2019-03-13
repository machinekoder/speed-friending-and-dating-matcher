# coding=utf-8
import os
import shutil
import codecs
from tempfile import mkdtemp

from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

from ..application import Application

DEBUG = True

_input_plugin = ''
_output_plugin = ''
_matchmaker = ''
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_file('index.html')

@app.route('/convert', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        tmp_dir = mkdtemp()
        try:
            file_data = request.files['file']
            input_file = os.path.join(tmp_dir, secure_filename(file_data.filename))
            file_data.save(input_file)
            template = request.form['template']
            template_file = os.path.join(tmp_dir, 'template.txt')
            with codecs.open(template_file, 'w',  encoding="utf-8") as f:
                f.write(template)

            result_file = os.path.join(tmp_dir, 'output.txt')
            application = Application(
                input_plugin=_input_plugin.format(input_file),
                output_plugin=_output_plugin.format(result_file, template_file),
                matchmaker=_matchmaker,
            )
            application.process()

            return send_file(result_file)  # 'file uploaded successfully'         
        finally:
            shutil.rmtree(tmp_dir)


def configure(input_plugin, output_plugin, matchmaker):
    global _input_plugin
    global _output_plugin
    global _matchmaker
    _input_plugin = input_plugin
    _output_plugin = output_plugin
    _matchmaker = matchmaker


def start():
    app.run(debug=DEBUG)
