# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test3.py
# __time__  : 2019/11/27 1:46 PM

from operator import itemgetter
from operator import attrgetter
from itertools import groupby

from collections import defaultdict
from typing import Mapping

rows_by_date = defaultdict(list)

print(rows_by_date)


def lookup_name(mapping: Mapping[map, str], key: map, default: str) -> str:
    try:
        return mapping[key]
    except KeyError:
        return default


if __name__ == '__main__':
    lookup_name()