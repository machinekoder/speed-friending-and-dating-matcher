# coding=utf-8
from speed_friending_matcher import server
from speed_friending_matcher.server import app as application

server.configure(
  input_plugin='csv:{}',
  output_plugin='todo:{}:{}',
  matchmaker='simple'
)