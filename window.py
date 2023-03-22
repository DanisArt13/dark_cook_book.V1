import tkinter as tk
import table_function as tf
import math


window = tk.Tk()
window.title('My Products')
window.geometry('800x600')
window.resizable(width=0, height=0)
# Фон
frame_date_in = tk.Frame(window, bg='burlywood2')
frame_date_now = tk.Frame(window, bg='cornsilk1')
frame_date_out = tk.Frame(window, bg='LightBlue1')

frame_date_in.grid(column=0, row=0, sticky='nesw')
frame_date_now.grid(column=1, row=0, sticky='nesw', ipadx=150, ipady=100)
frame_date_out.grid(column=0, row=1, columnspan=2, sticky='nesw', ipadx=300, ipady=100)

# Окно с выбором продукта
food_date = {}
calories_date = {}

food_variable = tk.StringVar(window)
food_variable.set('Продукт')
var = tk.OptionMenu(frame_date_in, food_variable, *tf.food_list())
var.grid(row='1', column='0', sticky='nesw', pady=10, padx=10, ipadx=30)

# Список выбранных продуктов/Вывод списка/Обновление списка
def food_date_list():
    f_lst = []
    for i in food_date:
        f_lst.append(f'{i}: {food_date[i]} гр.')
    return f_lst


def ok():
    for widget in frame_date_now.winfo_children():
        widget.destroy()

    # проверка на выбор продукта
    if food_variable.get() == 'Продукт':
        err_f_label = tk.Label(frame_date_now, text='Выберете продукт')
        err_f_label.grid(row=0, column=0, padx=10, pady=10)

    # проверка на ввод веса
    else:
        if gr_out() == '':
            err_gr_lable = tk.Label(frame_date_now, text='Введите вес продукта')
            err_gr_lable.grid(row='1', column='0', pady=10, padx=10, ipadx=30)

        # проверка на выбор типа готовки
        else:
            if variable.get() not in ['Сырой','Жаренный','Вареный']:
                err_t_label = tk.Label(frame_date_now, text='Выберете тип обработки')
                err_t_label.grid(row=0, column=0, padx=10, pady=10)

            else:
                food_add_gr = math.ceil(tf.cook_type_calc(variable.get(), food_variable.get()) * int(gr_out()))
                food_date[food_variable.get()] = food_add_gr
                calories_date[food_variable.get()] =  tf.sum_calories(food_variable.get())

                f_text = "\n".join(food_date_list())
                f_label = tk.Label(frame_date_now, text=f_text)
                f_label.grid(row='1', column='4', pady=10, padx=10, ipadx=30)




add_button = tk.Button(frame_date_in, text="Добавить продукт", command=ok)
add_button.grid(row='1', column='3',sticky='nesww', pady=10, padx=10)

# Окно с выбором типа обработки
variable = tk.StringVar(window)
variable.set('Способ обработки')
var1 = tk.OptionMenu(frame_date_in, variable, 'Сырой','Жаренный','Вареный')
var1.grid(row='2', column='0', sticky='nesww', pady=10, padx=10)


# Ввод веса продукта
gr_in = tk.Text(frame_date_in, height=1, width=10)
gr_in.grid(row='1', column='1', padx=10, pady=20)

def get_gr(t):
    x=t.get('1.0','end-1c')
    return x

def gr_out():
    a=get_gr(gr_in)
    return a

# Вывод данных о продукте после Пуска
def display():
    sum_gr = sum([int(food_date[i]) for i in food_date])
    sum_cals = sum([int(calories_date[i]) for i in calories_date])
    label_out = tk.Label(frame_date_out)
    label_out["text"] = f'Калорий в блюде: {sum_cals} гр. \n Вес блюда: {sum_gr} Кал.'

    label_out.grid(row='1', column='1', sticky='s', pady=10, padx=10)
    food_date.clear()
    calories_date.clear()

# Кнопка запуска
display_button = tk.Button(frame_date_in, text='Вычислить', command=display)
display_button.grid(row='2', column='3', sticky='s', pady=10, padx=10)

# Названия блоков
l_date_in_text = tk.Label(frame_date_in, text='Выберите необходимые ингридиенты')
l_date_out_text = tk.Label(frame_date_out, text='Результат:')

l_date_in_text.grid(row='0', column='1',  padx=10, pady=10)
l_date_out_text.grid(row='0', column='1',  padx=10, pady=10, sticky='n')

window.mainloop()

