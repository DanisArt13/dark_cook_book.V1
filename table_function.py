import sqlite3

def hz(x):
    lol = []
    [lol.append(*i) for i in x]
    return lol

# Список продуктов
def food_list():
    with sqlite3.connect('Food.db') as sf:
        sf.row_factory = sqlite3.Row
        cursor = sf.cursor()
        query = """ SELECT name FROM Food """
        cursor.execute(query)
    return hz(cursor)

#изменение веса при термической обработке (tp = тип обработки, nm = название продукта)
def cook_type_calc(tp, nm):
    if tp == 'Сырой':
        return 1

    elif tp == 'Жаренный':
        with sqlite3.connect('Food.db') as sf:
            sf.row_factory = sqlite3.Row
            cursor = sf.cursor()
            query = f""" SELECT fire FROM Food WHERE name = '{nm}'"""
            cursor.execute(query)
        cls = hz(cursor)[0]
        return 1 - cls / 100

    elif tp == 'Вареный':
        with sqlite3.connect('Food.db') as sf:
            sf.row_factory = sqlite3.Row
            cursor = sf.cursor()
            query = f""" SELECT boil FROM Food WHERE name = '{nm}'"""
            cursor.execute(query)
        cls = hz(cursor)[0]
        return 1 - cls/100

def clc():
    if variable.get() == 'Сырой':
        food_date[food_variable.get()] = gr_out()
    else:
        food_date[food_variable.get()] = tf.cook_type_calc(variable.get(), food_variable.get()) * int(gr_out())

# Вытаскивает из таблицы/суммипует калории
def sum_calories(fc):
    with sqlite3.connect('Food.db') as sf:
        sf.row_factory = sqlite3.Row
        cursor = sf.cursor()
        query = f""" SELECT calories FROM Food WHERE name = '{fc}'"""
        cursor.execute(query)
    cls = hz(cursor)[0]
    return cls


