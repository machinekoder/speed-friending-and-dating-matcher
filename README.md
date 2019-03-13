# Matching Software for Speed Friending and Dating Events
[![Build Status](https://travis-ci.org/DiffSK/configobj.svg?branch=master)](https://travis-ci.org/machinekoder/speed-friending-and-dating-matcher)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/machinekoder/speed-friending-matcher/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This application is designed to make your life as organizer of speed friending or speed dating events easier. I created this software for a [local speed friending event in Vienna, Austria](https://www.meetup.com/de-DE/speed-friending-events/) to give back value to the event organizers. For me, the project additionally serves as a playground for software engineering best practices. The application was implemented in an agile, test-driven development process applying all development best practices so far known to me.

## Installing the application
To install the live coding environment run:

```bash
python setup.py install
```

or install it via pip

```bash
pip install speed-friending-matcher
```

## How to use it
Run the speed-friending-matcher from the command line:
```
usage: speed_friending_matcher [-h] -i INPUT -o OUTPUT [-m MATCHMAKER] [-s]

Matchmaking application for speed friending events

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input plugin and parameters e.g. csv:somefile.csv
  -o OUTPUT, --output OUTPUT
                        Output plugins and parameters e.g. todo:mytodo.txt
  -m MATCHMAKER, --matchmaker MATCHMAKER
                        Matchmaker, simple or clique
  -s, --server          Starts a local webserver with a web GUI.
```

For example:
```bash
speed_friending_matcher -i csv:example/sample.csv -o todo:test.txt
```

## Importer Plugins

* **csv:<filename>.csv:** imports a CSV file with partipants data

## Exporter Plugins

`[]` means optional

* todo - exports a TODO file
```
todo:<filename>.txt:[<template_filename>.txt]
```

* onexlsx - exports a single Excel sheet containing matching information
```
onexlsx:<filename>.xlsx
```

* clique - exports a file containing all found cliques, to be used with the clique matchmaker
```
clique:<filename>.txt:[<header_filename>.txt]:[<template_filename.txt]
```

* graph - exports a graphical representation of the match graph, supports any export formats supported by [GraphViz](https://www.graphviz.org/)
```
graph:<filename>.<png, dot, ...>
```

## Matchmakers

* **simple:** Simple I liked you, you liked me matchmaking
* **clique:** Finds cliques of people liking each other

## Run on your Server

The application can be started in server mode with the optional command line argument `-s`.
However, please be aware that this starts a development server which is not recommended
to be used for production.

If you want to run the application on your webserver please refer to 
the [WSGI Guide for Flask.](http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/) or 
use [gunicorn](https://gunicorn.org/).

For example:
```bash
pip3 install gunicorn --user
gunicorn -w 4 wsgi:application
```

Use your Apache or other webservers `.htaccess` to forward the port.

### Detailed instructions

The following instructions were tested on a server with root access.

If you are running these steps in a production environment, make sure you have a back-up in place. I'm not responsible for any damages or losses.

If you have a webmaster, let your webmaster do the job.

#### Ensure Python and pip are installed

1. Open a root terminal on your server
2. Check if Python is installed

```bash
which python
```

Should return something along the lines of

```
/usr/bin/python
```

If not please refer to your web hosts manual for installing Python.

3. Check if pip is installed

```bash
which pip
```

Should return 

```
/usr/bin/pip
```

If not you can install pip with the `get-pip.py` script.

```bash
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py
```

4. Install the Python dependencies

```bash
pip install gunicorn aenum flask
```

#### Set-up the Script

1. Log in with your user account

Either via the root shell `su - <username>` or via your webhosts login shell.

2. Download the speed-friending matcher

```bash
cd ~
mdkir repos
cd repos
git clone https://github.com/machinekoder/speed-friending-and-dating-matcher.git
``

3. Create a start script

```bash
cd ~
mkdir scripts
cd scripts
nano start-speed-friending-matcher.sh
```

```

#!/bin/bash
pgrep -x gunicorn
if [ $? -ne 0 ]; then
cd ~/repos/speed-friending-and-dating-matcher
gunicorn -w 4 wsgi:application -b localhost:5000
fi
```

```bash
chmod +x start-speed-friending-matcher.sh
```

4. Set up crontab to start the script

```bash
crontab -e
```

Insert

```
* * * * * ~/scripts/start-speed-friending-matcher.sh
```

Now wait one minute and your server should be up and running.


#### Configure Apache

Use the `.htaccess` of your website to create a `RewriteRule` to the running `gunicorn` instance.

In this example we place the speed-friending script on the route `/script/*`, every other route is redirected to `/index.php`.

```.htaccess
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^script/(.*)$ http://localhost:5000/$1 [P,L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^.*$ /index.php [L]
</IfModule>
```

#### Stopping everything

First, you need to remove the start script from crontab `crontab -e`.

Then kill all running gunicorn instances `killall gunicorn`.


## Extending the software
You can extend the software by adding new import and export plugins. Take a look the default plugins
 [csvimporter](./importer/csvimporter.py) and [todoexporter](./exporter/todoexporter.py) for more details.
