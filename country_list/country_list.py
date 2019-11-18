import csv
from operator import itemgetter
from os.path import dirname
from pathlib2 import Path

data_dir = Path(__file__).parent / "country_data" / "data"


def available_languages():
    return sorted(x.name for x in data_dir.iterdir() if (x / "country.csv").exists())


def countries_for_language(lang, encoding='utf8'):
    path = data_dir / _clean_lang(lang) / "country.csv"
    with path.open(encoding=encoding) as file_:
        return list(map(itemgetter("id", "value"), csv.DictReader(file_)))


def _clean_lang(lang):
    cleaned_lang = lang.replace("-", "_").lower()
    try:
        return _languages()[cleaned_lang]
    except KeyError:
        raise ValueError("Language {} not found".format(lang))


def _languages():
    return {language.lower(): language for language in available_languages()}
