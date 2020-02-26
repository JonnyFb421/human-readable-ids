from human_readable_ids import __version__
from human_readable_ids.nouns import get_nouns
from human_readable_ids.adjectives import get_adjectives
from human_readable_ids.random_word import get_new_id


def test_version():
    assert __version__ == '0.1.2'


def test_nouns_are_not_empty():
    nouns = get_nouns()
    for noun in nouns:
        assert noun
    assert nouns is not None


def test_adjectives_are_not_empty():
    adjectives = get_adjectives()
    for adjective in adjectives:
        assert adjective
    assert adjectives is not None


def test_random_word_randomness():
    id1, id2, id3 = [get_new_id() for _ in range(3)]
    assert id1 != id2
    assert id1 != id3
    assert id2 != id3
