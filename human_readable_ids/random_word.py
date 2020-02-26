import random

from human_readable_ids.nouns import get_nouns
from human_readable_ids.adjectives import get_adjectives


def get_new_id():
    return f"{random.choice(get_adjectives()).capitalize()} {random.choice(get_nouns()).capitalize()} {random.randrange(1, 100)}"
