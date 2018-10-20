# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def results():
    from speed_friending_matcher.core.results import Results

    return Results()


def test_adding_marked_by_me_works(results):
    x = object()

    results.add_marked_by_me(x)

    assert x in results.marked_by_me


def test_adding_marked_me_works(results):
    x = object()

    results.add_marked_me(x)

    assert x in results.marked_me


def test_adding_match_works(results):
    x = object()

    results.add_match(x)

    assert x in results.matches


def test_clearing_results_works(results):
    x = object()
    y = object()
    z = object()

    results.add_marked_by_me(x)
    results.add_marked_by_me(y)
    results.add_marked_me(y)
    results.add_marked_me(z)
    results.add_match(x)
    results.clear()

    assert x not in results.marked_by_me
    assert y not in results.marked_by_me
    assert y not in results.marked_me
    assert z not in results.marked_me
    assert x not in results.matches


def test_added_data_is_accessible_as_attribute(results):
    results.clique = ["olpe", "janapa", "oricycle", "hoblob", "getas"]

    assert results.clique == ["olpe", "janapa", "oricycle", "hoblob", "getas"]
