from tkinter import *
import pandas

window = Tk()
window.title("Unit Converter")
window.config(padx=30, pady=10)

conversions = {}
conversion_table = pandas.read_csv('conversions.csv')
for key in conversion_table:
    conversions[key] = conversion_table[key].tolist()


def calculate():
    convert = float(entry.get())
    index = conversions['units'].index(select_unit_b.get())
    converter = conversions[select_unit_a.get()][index]
    print(select_unit_b.get())
    print(select_unit_a.get())
    print(index)
    print(convert)
    print(type(convert))
    print(converter)
    print(type(converter))
    converted = convert * converter
    converted_number['text'] = round(converted, 2)


button = Button(text="Calculate", command=calculate)
entry = Entry()
entry.configure(width=10)
text = Label(text=f"is equal to")
converted_number = Label(text=0)

select_unit_a = StringVar()
select_unit_b = StringVar()

select_unit_a.set('miles')
select_unit_b.set('miles')


def selected_unit_1(value):
    select_unit_a.set(value)


def selected_unit_2(value):
    select_unit_b.set(value)


drop_down_1 = OptionMenu(None, select_unit_a, 'miles', 'km', 'inches', 'AU', 'feet', command=selected_unit_1)
drop_down_2 = OptionMenu(None, select_unit_b, 'miles', 'km', 'inches', 'AU', 'feet', command=selected_unit_2)

entry.grid(column=1, row=0)
drop_down_1.grid(column=2, row=0)
text.grid(column=0, row=1)
converted_number.grid(column=1, row=1)
drop_down_2.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()
