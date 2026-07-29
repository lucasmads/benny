from utils import read_json, write_json


class JsonRepository:

    def __init__(self, path):

        self.path = path

    def all(self):

        return read_json(self.path)

    def save(self, items):

        write_json(self.path, items)

    def add(self, item):

        items = self.all()

        items.append(item)

        self.save(items)

    def remove(self, key, value):

        items = self.all()

        filtered = [
            item
            for item in items
            if item.get(key) != value
        ]

        self.save(filtered)

    def update(self, key, value, new_data):

        items = self.all()

        updated = []

        for item in items:

            if item.get(key) == value:

                item.update(new_data)

            updated.append(item)

        self.save(updated)

    def find(self, key, value):

        items = self.all()

        for item in items:

            if item.get(key) == value:

                return item

        return None
