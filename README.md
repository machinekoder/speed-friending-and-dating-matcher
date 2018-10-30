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

## Extending the software
You can extend the software by adding new import and export plugins. Take a look the default plugins [csvimporter](./importer/csvimporter.py) and [todoexporter](./exporter/todoexporter.py) for more details.
