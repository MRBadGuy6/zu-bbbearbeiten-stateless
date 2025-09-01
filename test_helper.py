import helper

def test_get_csv_returns_valid_string():
    # Dummy-Daten simulieren
    data = [
        {"title": "Traktandum 1", "category": "Info", "description": "Einfacher Text"},
        {"title": "Traktandum 2", "category": "Beschluss", "description": "Mit, Komma"}
    ]

    csv_str = helper.get_csv(data)

    # Der Rückgabewert soll ein String sein
    assert isinstance(csv_str, str)

    # Erste Zeile sollte die Header enthalten
    assert "title,category,description" in csv_str.splitlines()[0]

    # Zweite Zeile: erster Datensatz
    assert "Traktandum 1" in csv_str
    assert "Info" in csv_str
