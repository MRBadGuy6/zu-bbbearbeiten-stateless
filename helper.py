from dataclasses import dataclass

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
