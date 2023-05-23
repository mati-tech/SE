from tkinter import * 

window = Tk() 
window.title("first window")
window.geometry('299x299')
# btn = Button(window, text = "button")
# btn.pack()


#! method of grid 
# btn1 = Button(window, text="Button #1")
# btn1.grid(column=0, row=0, padx=10, pady=15)
# btn2 = Button(window, text="Button #2")
# btn2.grid(column=1, row=0, padx=10, pady=15)
# btn3 = Button(window, text="Button #3")
# btn3.grid(column=2, row=0, rowspan=2, padx=5, pady=15)
# btn4 = Button(window, text="Button #4")
# btn4.grid(column=0, row=1, columnspan=2, padx=5,pady=15)
# btn5 = Button(window, text="Button #5")
# btn5.grid(column=0, row=2, padx=10, pady=15)
# btn6 = Button(window, text="Button #6")
# btn6.grid(column=1, row=2, padx=10, pady=15)

#! method of pack 
# Метод pack позиционирует элемент внутри родительского контейнера 
# по одной из сторон. Это наиболее простой сполсоб размещения. Этот метод 
# принимает три стандартных аргумента:
# – expand: логичекая переменная, определяющая заполнит ли элемент все 
# пространство контейнера;
# – fill: принимает одно из значений (NONE, X, Y, BOTH) в зависимости 
# от того по какой оси будет растягиваться элемент;
# – side: принимает одно из значений (TOP, LEFT, RIGHT, BOTTOM) в 
# зависимости от того, по какой стороне контейнера будет выровнен элемент. 
# Также дополнительно могут указываться парметры ipadx, ipady, padx и 
# pady, определяющие то же, что и в предыдущем методе.

# btn1 = Button(window, text="Button #1")
# btn1.pack(side=TOP, padx=10, pady=15)
# btn2 = Button(window, text="Button #2")
# btn2.pack(side=BOTTOM, padx=10, pady=15)
# btn3 = Button(window, text="Button #3")
# btn3.pack(side=RIGHT, padx=10, pady=15)
# btn4 = Button(window, text="Button #4")
# btn4.pack(side=LEFT, padx=10, pady=15)


#! Однако, применяя данный метод над элементами, невозможно 
# добиться более сложного размещения. Например, при желании разместить 
# элементы квадратом (два сверху и ровно над ними два снизу) необходимо 
# объединять элементы в группы – Frame.

# top_frame = Frame(window , bg="red")
# bottom_frame = Frame(window, bg="green")
# top_frame.grid( row = 0 , column =0)
# bottom_frame.grid( row = 1 , column =0)

# top_frame.pack( side = "top")
# bottom_frame.pack ( side = "bottom")

# btn1 = Button(top_frame, text="Button #1")
# btn1.pack(side=LEFT)
# btn2 = Button(top_frame, text="Button #2")
# btn2.pack(side=RIGHT)
# btn3 = Button(bottom_frame, text="Button #3")
# btn3.pack(side=RIGHT)
# btn4 = Button(bottom_frame, text="Button #4")
# btn4.pack(side=LEFT)


# !И, наконец, третий метод place позволяет применять точное 
# позиционирование элементов. Он принимает следующие параметры:
# – height и width (или relheight и relwidth): высота и ширина элемента в 
# пикселях или доля от высоты и ширины родительского контейнера в 
# промежутке от 0.0 до 1.0;
# – x и y (или relx и rely): смещение элемента по горизонтали и вертикали 
# относительно верхнего левого угла в пикселях или в доле от высоты и ширины 
# родительского контейнера;
# – anchor: растяжение элемента (n, e, s, w, ne, nw, se, sw, c – сокращения 
# от сторон света, где, например, nw (северозапад) – верхний левый угол, а с –
# центр)).


# relativex and relativey 
#! relx and rely 


# btn1 = Button(window, text="Button #1")
# btn1.place(relheight=0.2, relwidth=0.4, relx=0.5,rely=0.5)
# btn2 = Button(window, text="Button #2")
# btn2.place(relheight=0.1, relwidth=0.2, relx=0.1,rely=0.1)

# you can use the mix of them but it is not recomended 

# Текстовая метка
# Самым простым из элементов является Label, который позволяет 
# выводить статический текст, без возможности ручного редактирования. 
# Создаем экземпляр класса Label, конструктор которого принимает два 
# аргумента. Первый – ссылка на родительский контейнер, а второй аргумент 
# принимает необходимое количество именованных параметров. В наиболее 
# простом случае достаточно одного опционального параметра text (текст 
# метки). 
# Рисунок 7 – Текстовая метка
# Доступных опциональных элементов гораздо больше:
# – anchor, height, width, padx, pady: рассмотрены ранее;
# 9
# – bg: фоновый цвет;
# – fg: цвет текста;
# – font: шрифт текста;
# – bd: толщина границы метки;
# – justify: устанавливает выравнивание текста (LEFT, CENTER, RIGHT);
# – wraplength: при положительном значении строки текста будут 
# переносится для вмещения в пространство элемента.

# label1 = Label(window, text = "Label\t\n#1",
# bg = "Indigo", fg = "White",
# font = ("Courier New", 20, "bold"),
# bd = 10, justify = RIGHT,
# height = 2, width= 15)
# label1.grid(column=0, row=0)


# Кнопка 
# Одним из наиболее важных элементов является кнопка – Button. 
# Создается также, как, например, метка и обладает примерно тем же набором 
# опциональных параметров. Но добавляется важный параметр:
# – command: название функции-обработчика нажатия на кнопку. 


# def btn1_click():
#     print ('i am clicked')
# window.title("Button #1")
# button1 = Button(window, text="Button #1", command =
# btn1_click)
# button1.pack()


#! Поле ввода
# Кроме вывода информации в окне у пользователя должна быть 
# возможность ввода информации для дальнейшей обработки. Для этого 
# существует элемент Entry. Механизм создания и основные параметры опять 
# же совпадают с таковыми у текстовой метки. Дополнительно:
# – show: задает маску для вводимых символов (может применяться для 
# скрытия символов пароля на экране, например, звездочками);
# – state: состояние элемента (NORMAL – по умолчанию активный и 
# DISABLED – неактивный);
# – focus(): установка элемента в фокус, который позволяет сразу писать 
# текст без необходимости ставить курсор на поле ввода. 

# Элемент Entry обладает рядом методов:
# – get(): основной метод, возвращающий введенный в поле ввода текст;
# – insert(index, str): вставляет в поле ввода по индексу index строку str;
# – delete(first, last): удаляет символы с first до last (если он указан, также 
# last может принимать значение END, тогда будут удалены все символы до 
# конца).
# Часто необходимо изменять какие-то свойства элементов, например, 
# изменить текст метки, для этого можно воспользоваться следующим методом: 
# – configure(): параметрами являются изменяемые свойства элемента.
# Так, в следующем примере при нажатии на кнопку происходит 
# изменение текста метки на содержимое поля ввода.




# entry1 = Entry(window, show = "*")
# entry1.focus()
# entry1.pack()
# entry1.grid()

# def button1_click():
#     # global a
#     # a = entry1.get()
#     label1.configure(text=entry1.get())
# label1 = Label(window, text="")
# label1.pack()
# entry1 = Entry(window, text="")
# entry1.pack()
# button1 = Button(window, text="Click!", command =
# button1_click)
# button1.pack()

# def click ():
#     clicks.set(clicks.get() + 1)

# clicks = IntVar()
# clicks.set(0)

# button1 = Button(window, textvariable=clicks, command =
# click) 
# button1.pack()

# Messagebox
# Для вывода на экран различных данных или информационных 
# сообщений конечно же можно воспользоваться текстовыми метками, однако 
# для большей наглядности или для более важных сообщений можно вызывать 
# методы объекта как Messagebox:
# – showinfo(title, text): обычное окно, в качестве параметров должны 
# идти две строки для заголовка и сообщения;
# – showwarning(title, text): окно для предупредительных сообщений;
# – showerror(title, text): окно для ошибок.

# from tkinter import messagebox
# def show_message():
#     messagebox.showinfo("Title", "Info")
#     messagebox.showwarning("Title", "Warning")
#     messagebox.showerror("Title", "Error")

# button1 = Button(window, text="MessageBox",
# command=show_message) 
# button1.pack()

# Для более сложных информационных сообщений, которые будут 
# предоставлять пользователю выбор можно вызывать один из следующий 
# методов: askquestion, askyesno, askyesnocancel, askokcancel, askretrycancel. Эти
# методы в зависимости от выбора пользователя возвращают одно из значений:
# True, False, None.


#! Дополнительные виджеты
# Разобравшись с базовыми графическими элементами, перейдем к более 
# сложными виджетам, таким как поле с выпадающим списком (Combobox), 
# поле выбора (Checkbutton), переключатель (Radiobutton). Они определены в 
# модуле tkinter.ttk. 
# Для создания поля с выпадающим значением создадим экземпляр класса 
# Combobox. Предустановленные значения можно задать разных типов и 
# предать в экземпляр класса кортежем. Также можно воспользоваться 
# следующими методами:
# – current(index): устанавливает выбранный элемент, в метод передается 
# его индекс;
# – get(): возвращает выбранное значение элемента.
# 15
# Для установки переключателя создадим экземпляр класса Checkbutton, 
# для него можно задать текст вывода, кроме того воспользуемся объектом 
# BooleanVar или IntVar для определения состояния флажка. 
# Для установки значения в объекты BooleanVar и IntVar воспользуемся 
# методом:
# – set(index): в качестве индекса передается 0 (False, т.е. не выбрано,) или 
# 1 (True, т.е. выбрано).
# Для создания radio-кнопок воспользуемся классом Radiobutton, для 
# данного объекта помимо текста необходимо задать уникальное значение для 
# поля value. Работа с выбранным значением осуществляется также через 
# дополнительные объекты, например, IntVar. А также для radio-кнопок можно 
# устанавливать параметр command (функция-обработчик) по аналогии с 
# обычными кнопками



# from tkinter import * 
from tkinter.ttk import Combobox, Checkbutton,Radiobutton


# window = Tk()
# window.title("Название приложения")
# window.geometry("300x200")

# combobox1 = Combobox(window)
# combobox1["values"] = (1, "two", 3, "four", 5)
# combobox1.current(3)
# combobox1.grid(row = 0, column = 0)

# check_state = BooleanVar()
# check_state.set(True)
# checkbutton1 = Checkbutton(window, text = "Check",
# variable = check_state)
# checkbutton1.grid(row = 0, column = 1)

# radio_state = IntVar()
# radio_state.set(2)


# radiobutton1 = Radiobutton(window, text = "Radio 1",
# value = 1, variable = radio_state)
# radiobutton1.grid(row = 1, column = 1)
# radiobutton2 = Radiobutton(window, text = "Radio 2",
# value = 2, variable = radio_state)
# radiobutton2.grid(row = 2, column = 1)
#!----------------------------------------------------------
# import tkinter as tk

# root = tk.Tk()

# # Create a variable to store the value of the selected radio button
# var = tk.IntVar()

# # Create the radio buttons
# rb1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
# rb2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
# rb3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3)

# # Pack the radio buttons
# rb1.pack()
# rb2.pack()
# rb3.pack()

# # Create a function to get the value of the selected radio button
# def get_selected():
#     print(var.get())

# # Create a button to trigger the function
# button = tk.Button(root, text="Get selected", command=get_selected)
# button.pack()

# root.mainloop()


# from tkinter import filedialog


#! file = filedialog.askopenfilename(initialdir ="C://Users",filetypes = (("txt files","*.txt"),("allfiles","*.*")))

# u should bind it with a button and a function to browse the file from the computer 


#! Иногда для удобства пользователя логичным является разделить 
# функционал приложения на части и сгруппировать соответствующие 
# элементы на разных вкладках. Для управления вкладками можно 
# воспользоваться элементом Notebook, а вкладками будут являться экземпляры 
# классов Frame.

#! from tkinter.ttk import Notebook, Frame 
# #the frame is recommended to be managed 
# tab = Notebook(window)
# tab1 = Frame(tab)
# tab.add(tab1, text = 'first tab')
# btn = Button(tab1, text  = 'button1')
# btn.pack()
# tab2 = Frame(tab)
# tab.add(tab2, text = '2 tab')
# btn2 = Button(tab2, text  = 'button2')
# btn2.pack() 

# tab.pack(expand = True, fill = 'both')
# import urllib.request


# URL of the XML file
# url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=22/04/2022"



# import urllib.request
# import xml.etree.ElementTree as ET

# url = 'https://www.example.com/example.xml'

# try:
#     # response = urllib.request.urlopen(url)
#     data = response.read()
#     if not data:
#         print('Error: Empty response')
#     else:
#         root = ET.fromstring(data)
#         # Process the root element here
# except Exception as e:
#     print('Error:', e)

# # Retrieve data from the website
# response = urllib.request.urlopen(url)
# xml_data = response.read()

# if response.getcode() == 200:
#     print('Data successfully retrieved')
#     root = ET.fromstring(response.read())
#     # continue with parsing the XML data
# else:
#     print('Failed to retrieve data')
# #!=-=-=-=-=-=-=-= XML files-=-=-=-=-=-=-=-=
# import os 
# import xml.etree.ElementTree as ET
# # Parse the XML data
# file = 'currencyxml.xml'
# full_path = os.path.abspath(file )
# # xml_data = read()
# print (full_path)
# root = ET.parse(full_path)
# # name  = root.findall('name')
# # value = root.findall('value')
# # print (root)

# for currency in root.findall('Valute'):
#     name = currency.find('Name').text
#     value = currency.find('Value').text
#     print(name, value)
# #!-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# import requests
# import tkinter as tk
# from tkinter import ttk


# class CurrencyConverter:
#     def __init__(self, url):
#         self.data = requests.get(url).json()
#         self.currencies = self.data['rates']

#     def convert(self, from_currency, to_currency, amount):
#         initial_amount = amount
#         if from_currency != 'USD':
#             amount = amount / self.currencies[from_currency]
#         amount = round(amount * self.currencies[to_currency], 4)
#         return amount


# class CurrencyConverterGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title('Currency Converter')

#         # create currency converter object
#         url = 'https://api.exchangerate-api.com/v4/latest/USD'
#         self.converter = CurrencyConverter(url)

#         # create UI elements
#         self.from_currency_label = ttk.Label(master, text='From currency:')
#         self.from_currency_label.grid(row=0, column=0, padx=10, pady=10)
#         self.from_currency_combobox = ttk.Combobox(master, values=list(self.converter.currencies.keys()))
#         self.from_currency_combobox.current(0)
#         self.from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)

#         self.to_currency_label = ttk.Label(master, text='To currency:')
#         self.to_currency_label.grid(row=1, column=0, padx=10, pady=10)
#         self.to_currency_combobox = ttk.Combobox(master, values=list(self.converter.currencies.keys()))
#         self.to_currency_combobox.current(0)
#         self.to_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

#         self.amount_label = ttk.Label(master, text='Amount:')
#         self.amount_label.grid(row=2, column=0, padx=10, pady=10)
#         self.amount_entry = ttk.Entry(master)
#         self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

#         self.convert_button = ttk.Button(master, text='Convert', command=self.convert_currency)
#         self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#         self.result_label = ttk.Label(master, text='')
#         self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#     def convert_currency(self):
#         from_currency = self.from_currency_combobox.get()
#         to_currency = self.to_currency_combobox.get()
#         amount = float(self.amount_entry.get())
#         result = self.converter.convert(from_currency, to_currency, amount)
#         self.result_label.config(text=f'{amount} {from_currency} = {result} {to_currency}')


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = CurrencyConverterGUI(root)
#     root.mainloop()
