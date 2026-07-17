import json
from pathlib import Path


class ApplicationRegistry:

    def __init__(self):

        path = Path("data/apps.json")

        with open(path, "r", encoding="utf-8") as f:
            self.apps = json.load(f)

    def names(self):
        return list(self.apps.keys())

    def executable(self, app):
        return self.apps[app]["exe"]

    def aliases(self):

        result = {}

        for app, info in self.apps.items():

            for alias in info["aliases"]:
                result[alias] = app

        return result