#!/usr/bin/env python
import argparse
import sys
from application import Application


def main():
    parser = argparse.ArgumentParser(description="""
    Matchmaking application for speed friending events
    """)
    parser.add_argument('-i', '--input', help='Input plugin and parameters e.g. csv:somefile.csv', required=True)
    parser.add_argument('-o', '--output', help='Output plugins and parameters e.g. todo:mytodo.txt', required=True)
    args = parser.parse_args()

    app = Application(args.input, args.output)
    app.process()

    sys.exit(0)


if __name__ == '__main__':
    main()
