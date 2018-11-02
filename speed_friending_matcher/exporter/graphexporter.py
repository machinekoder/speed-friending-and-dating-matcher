# coding=utf-8
import os

from .exporter import Exporter
import pydot


class GraphExporter(Exporter):
    def __init__(self, filename):
        Exporter.__init__(self)
        self._filename = filename

    def export_data(self, data):
        people_graph = {person: set(person.results.matches) for person in data}
        graph = pydot.Dot(graph_type='graph')
        edges = set()
        for person, matches in people_graph.items():
            for match in matches:
                edges.add(frozenset([person.name, match.name]))

        for source, target in edges:
            source = source.decode('utf-8') if isinstance(source, bytes) else source
            target = target.decode('utf-8') if isinstance(target, bytes) else target
            edge = pydot.Edge(source, target)
            graph.add_edge(edge)

        _, extension = os.path.splitext(self._filename)
        graph.write(self._filename, format=extension[1:])


exporter = GraphExporter
