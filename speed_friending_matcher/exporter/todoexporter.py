# -*- coding: utf-8 -*-
from .cliqueexporter import CliqueExporter
from .export_tools import create_person_simple_string

TEXT_TEMPLATE = '''\
============================
Send to {name}, {email}, {phone} the following message:

Hi {name}, here are your contacts with people you can reach out to
(people that marked you with an "x" and you marked them with an "x"):

You marked:
{marked}

You got marked by:
{got_marked}

Your matches:
{matches}

Your cliques:
{cliques}

You can also find all other contacts here: http://goo.gl/123xyz
or on meetup here: https://www.meetup.com/speed-friending-events/members/

'''


class TodoExporter(CliqueExporter):
    def __init__(self, output_filename, template_filename=None):
        """
        This exporter plugin creates a list of to do tasks for each user.
        :param output_filename: Name of the output txt file which will be generated.
        :param template_filename: Name of an optional template file describing the output format.
        """
        super(TodoExporter, self).__init__(output_filename)
        self._filename = output_filename
        self._groups = []

        if template_filename:
            with open(template_filename, 'rt') as f:
                self._text_template = f.read()
        else:
            self._text_template = TEXT_TEMPLATE

    def export_data(self, data):
        self._groups = self._extract_groups(data)
        with open(self._filename, 'wt') as todo_file:
            for person in data:
                self._export_person(person, todo_file)

    def _export_person(self, person, todo_file):
        groups = self._find_all_groups_for_person(person, self._groups)
        groups = self._sort_groups_from_biggest(groups)
        todo_file.write(self._create_person_todo_string(person, groups))

    def _create_person_todo_string(self, person, groups):
        def sort(results):
            return sorted(results, key=lambda x: x.number)

        marked_by_me = []
        for p in sort(person.results.marked_by_me):
            marked_by_me.append(create_person_simple_string(p))
        marked_me = []
        for p in sort(person.results.marked_me):
            marked_me.append(create_person_simple_string(p))
        matches = []
        for p in sort(person.results.matches):
            matches.append(create_person_simple_string(p))
        cliques = [
            self._create_group_string(group, i + 1) for i, group in enumerate(groups)
        ]
        return self._text_template.format(
            name=person.name,
            email=person.email,
            phone=person.phone,
            marked='\n'.join(marked_by_me),
            got_marked='\n'.join(marked_me),
            matches='\n'.join(matches),
            cliques='\n'.join(cliques),
        )

    @staticmethod
    def _find_all_groups_for_person(person, groups):
        return [group for group in groups if person in group]


exporter = TodoExporter
