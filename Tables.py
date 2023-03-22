import sqlite3

with sqlite3.connect('Food.db') as sf:
    cursor = sf.cursor()
    query = """ CREATE TABLE IF NOT EXISTS Food(
                id INTEGER,
                solid_liquid REAL,
                name REAL,
                calories INTEGER,
                fire INTEGER,
                boil INTEGER
    )"""
    cursor.execute(query)
    sf.commit()

with sqlite3.connect('Food.db') as sf:
    cursor = sf.cursor()
    query1 = """ INSERT INTO Food(id, solid_liquid, name, calories, fire, boil) VALUES(4, 'liquid', 'Свинина', 242, 35, 40)"""

    cursor.execute(query1)

    sf.commit()


