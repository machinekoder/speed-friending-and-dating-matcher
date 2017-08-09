# Matching Software for Speed Friending Events
This application is designed to make your life as organizer of speed friending events easier. I created this software for a local speed friending event in Vienna, Austria to give back value to the event organizers. For me, the project additionally serves as a playground for software engineering best practices. The application was implemented in an agile, test-driven development process applying all development best practices so far known to me.

## Installing the application
Install the application dependencies using pip:
```bash
sudo pip install -r requirements.txt
```

## How to use it
Run the speed-friending-matcher from the command line:
```
usage: speed-friending-matcher.py [-h] -i INPUT -o OUTPUT

Matchmaking application for speed friending events

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input plugin and parameters e.g. csv:somefile.csv
  -o OUTPUT, --output OUTPUT
                        Output plugins and parameters e.g. todo:mytodo.txt
```

For example:
```bash
./speed-friending-matcher.py -i csv:example/sample.csv -o todo:test.txt
```

## Extending the software
You can extend the software by adding new import and export plugins. Take a look the default plugins [csvimporter](./importer/csvimporter.py) and [todoexporter](./exporter/todoexporter.py) for more details.
