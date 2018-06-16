# -*- coding: utf-8 -*-


def create_person_simple_string(person):
    data = [str(person.number), person.name]
    if person.email is not '':
        data.append(person.email)
    if person.phone is not '':
        data.append(person.phone)
    return ', '.join(data)
