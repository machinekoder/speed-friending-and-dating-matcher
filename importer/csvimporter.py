import csv
from importer import Importer
from core.person import Person, MatchingFlags


class CsvImporter(Importer):
    def __init__(self, filename):
        Importer.__init__(self)
        self._filename = filename

    def import_data(self):
        return self._read_and_verify_file(self._filename)

    def _read_and_verify_file(self, filename):
        people = []

        with open(filename, 'rb') as f:
            csvreader = csv.DictReader(f, delimiter=';')

            for row in csvreader:
                self._verify_row(row)
                people.append(self._parse_row(row))

        return people

    def _verify_row(self, row):
        needed_rows = ['#', 'Name', 'Email', 'Phone', 'All', 'Interested']
        for need in needed_rows:
            if need not in row or row[need] is None:
                raise ValueError('Row in CSV file does not contain required field: %s' % need)

    def _parse_row(self, row):
        if len(row) < 6:
            raise RuntimeError('Error parsing CSV line: to few arguments')
        nr = int(row['#'])
        name = row['Name'].strip()
        email = row['Email'].strip()
        phone = row['Phone'].strip()
        match_all = bool(int(row['All']))
        interested_in = set()
        for interest in row['Interested'].split(','):
            interested_in.add(int(interest))

        if match_all:
            flags = MatchingFlags.no_flags
        else:
            flags = MatchingFlags.match_all

        person = Person(number=nr, name=name, email=email, phone=phone, flags=flags, interested_in=interested_in)
        return person
