from .acrostic import IPUZ_ACROSTIC_VALIDATORS
from .answer import IPUZ_ANSWER_VALIDATORS
from .block import IPUZ_BLOCK_VALIDATORS
from .crossword import IPUZ_CROSSWORD_VALIDATORS
from .fill import IPUZ_FILL_VALIDATORS
from .sudoku import IPUZ_SUDOKU_VALIDATORS
from .wordsearch import IPUZ_WORDSEARCH_VALIDATORS


IPUZ_PUZZLEKINDS = {
    "http://ipuz.org/acrostic": {
        "mandatory": (
            "puzzle",
        ),
        "validators": {
            1: IPUZ_ACROSTIC_VALIDATORS,
        },
    },
    "http://ipuz.org/answer": {
        "mandatory": (),
        "validators": {
            1: IPUZ_ANSWER_VALIDATORS,
        },
    },
    "http://ipuz.org/block": {
        "mandatory": (
            "dimensions",
        ),
        "validators": {
            1: IPUZ_BLOCK_VALIDATORS,
        },
    },
    "http://ipuz.org/crossword": {
        "mandatory": (
            "dimensions",
            "puzzle",
        ),
        "validators": {
            1: IPUZ_CROSSWORD_VALIDATORS,
        },
    },
    "http://ipuz.org/fill": {
        "mandatory": (),
        "validators": {
            1: IPUZ_FILL_VALIDATORS,
        },
    },
    "http://ipuz.org/sudoku": {
        "mandatory": (
            "puzzle",
        ),
        "validators": {
            1: IPUZ_SUDOKU_VALIDATORS,
        },
    },
    "http://ipuz.org/wordsearch": {
        "mandatory": (
            "dimensions",
        ),
        "validators": {
            1: IPUZ_WORDSEARCH_VALIDATORS,
        },
    },
}
