from dataclasses import dataclass
import io
import csv


def get_csv(data=None):
    """
    Gibt die Traktanden als CSV-String zurück.
    data: Liste von Dicts mit keys: title, category, description
    """
    if data is None:
        # Hier müsstest du deine Traktanden holen, z. B. aus DB oder globaler Liste
        data = []

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["title", "category", "description"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

    return output.getvalue()

items = []


@dataclass
class Item:
    text: str
    isCompleted: bool = False


def add(text):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted

def test_add():
    add("test")
    assert len(items) == 1
    assert items[0].text == "test"
    assert not items[0].isCompleted
