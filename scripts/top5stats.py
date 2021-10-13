#!/usr/bin/env python
"""Collect top5 stats and generate a data file.

Requires:

    * Python 3.6+
    * pyyaml
"""
import operator
import sys
from pathlib import Path

import yaml


top5data = {}


def top5stats(path):
    with path.open() as handler:
        lines = handler.readlines()

    start = 0
    try:
        while start < len(lines):
            while not lines[start].startswith("{{< top5"):
                start += 1

            end = start
            while not lines[end].startswith("{{< /top5"):
                end += 1

            top5 = ''
            for line in lines[start+1:end]:
                if line.strip().startswith("*"):
                    top5 += line.strip().replace("* ", "- \"") + "\"\n"
                else:
                    top5 += line

            for key, value in yaml.safe_load(top5).items():
                for i in value:
                    top5data[key][i].setdefault("count", 0)
                    top5data[key][i]["count"] += 1
                    top5data[key][i]["name"] = i

            start = end
    except IndexError:
        pass

if __name__ == "__main__":
    episodesdir = Path(sys.argv[1])
    datadir = Path(sys.argv[2])
    top5 = datadir / "top5.yaml"

    if not episodesdir.exists() or not datadir.exists():
        print(f"Make sure both {episodesdir} and {datadir} exist.")
        sys.exit(1)
    if not episodesdir.is_dir() or not datadir.is_dir():
        print(f"Make sure both {episodesdir} and {datadir} are dirs.")
        sys.exit(1)

    with top5.open() as handler:
        top5data.update(yaml.safe_load(handler))

    for child in episodesdir.iterdir():
        top5stats(child)

    result = {}
    for key in top5data.keys():
        result[key] = sorted(
            top5data[key].values(),
            key=operator.methodcaller("get", 'count', 0),
            reverse=True,
        )[:5]

    with open(datadir / "top5stats.yaml", "w") as handler:
        handler.write(yaml.dump(result))
