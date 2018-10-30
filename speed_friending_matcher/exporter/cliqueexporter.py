# -*- coding: utf-8 -*-
from .exporter import Exporter
from .export_tools import create_person_simple_string


HEADER = '''\
Following cliques have been found:

'''

GROUP_TEMPLATE = '''\
TEAM {number}: {count} friends
{friends}
'''


class CliqueExporter(Exporter):
    def __init__(self, output_filename, header_filename=None, template_filename=None):
        """
        This exporter plugin outputs a list of found cliques in the input data.
        :param output_filename: Name of the output txt file which will be generated.
        :param header_filename: Name of an optional header template file.
        :param template_filename: Name of an optional template file describing the output format.
        """
        Exporter.__init__(self)
        self._filename = output_filename

        if header_filename:
            with open(header_filename, 'rt') as f:
                self._header = f.read()
        else:
            self._header = HEADER

        if template_filename:
            with open(template_filename, 'rt') as f:
                self._group_template = f.read()
        else:
            self._group_template = GROUP_TEMPLATE

    def export_data(self, data):
        groups = self._extract_groups(data)
        groups = self._sort_groups_from_biggest(groups)
        with open(self._filename, 'wt') as f:
            f.write(self._header)
            for i, group in enumerate(groups):
                f.write(self._create_group_string(group, i + 1))

    def _create_group_string(self, group, number):
        friend_strings = (create_person_simple_string(friend) for friend in group)
        return self._group_template.format(
            number=number, count=len(group), friends='\n'.join(friend_strings)
        )

    @staticmethod
    def _extract_groups(all_people):
        groups = set()
        for person in all_people:
            try:
                group = set(person.results.clique)
            except AttributeError:
                continue
            if len(group) <= 1:
                continue
            group.add(person)
            groups.add(tuple(sorted(group, key=lambda p: p.number)))
        return groups

    @staticmethod
    def _sort_groups_from_biggest(groups):
        return sorted(groups, key=lambda x: len(x), reverse=True)


exporter = CliqueExporter
