# from tkinter import *
# from tkinter.ttk import Notebook, Frame 
# from tkinter.ttk import Combobox, Checkbutton,Radiobutton
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# import matplotlib
# import matplotlib.pyplot as plt 

# root = Tk() 
# root.title("Currency Exchanger")
# root.geometry('800x500')


# tabs = Notebook(root)
# #!first tab
# t1 = Frame(tabs)
# tabs.add(t1, text = 'Currency Calculator')

# # two combobox is needed, one entry one label and button of conversion 
# def convert():
#     from_currency = combobox1.get()
#     to_currency = combobox2.get()
#     amount  = entry1.get() 
#     exchange_rates = {
#         'USD': {'USD': 1.0, 'Ruble': 79.0, 'euro': 0.83, 'JPY': 139.0, 'GBP':0.80},
#         'Ruble': {'USD': 0.014, 'Ruble': 1.0, 'euro': 0.012, 'JPY': 1.64, 'GBP':0.0098},
#         'euro': {'USD': 1.21, 'Ruble': 83.26, 'euro': 1.0, 'JPY': 147.86, 'GBP':0.88},
#         'GBP': {'USD': 1.39, 'Ruble': 99.64, 'euro': 1.16, 'JPY': 167.57, 'GBP':1.0},
#         'JPY': {'USD': 0.0091, 'Ruble': 0.65, 'euro': 0.0075, 'JPY': 1.0, 'GBP':0.0060}
#     }
#     if from_currency not in exchange_rates or to_currency not in exchange_rates:
#         label2.configure(text="Not found try again! ")
#     try: 
#         usd_amount = float(amount) * exchange_rates[from_currency]['USD']
#         converted_amount = float(usd_amount) * exchange_rates['USD'][to_currency]
#         label2.configure(text=converted_amount)
#     except:
#         raise Exception (label2.configure(text="invalid input!"))
#     # return converted_amount

# combobox1 = Combobox(t1)
# combobox1["values"] = ('USD', 'Ruble', 'euro', 'GBP', 'JPY')
# combobox1.current(0) #! i guess here you can control the function like if the current is this and current of the other is that do this and so on 
# combobox1.grid(row = 0, column = 0, padx=10 , pady=10 )

# combobox2 = Combobox(t1)
# combobox2["values"] = ('USD', 'Ruble', 'euro', 'GBP', 'JPY')
# combobox2.current(0)
# combobox2.grid(row = 2, column = 0, padx=10 , pady=10)

# label = Label (t1, text = "Amount: ")
# label.grid(row = 1 , column = 1, padx=10 , pady=10)

# entry1 = Entry(t1, text="")
# entry1.grid(row = 1 , column = 2, padx=10 , pady=10)

# label2 = Label (t1, text = "")
# label2.grid(row = 2 , column = 1, padx=10 , pady=10)

# button1 = Button(t1, text="Convert", command =convert)
# button1.grid(row = 1 , column = 3, padx=10 , pady=10)


# #!second tab____________________________________________________-
# # graph_frame = Frame(canvas)
# # canvas.create_window((0, 0), window=graph_frame, anchor='nw')
# def make_graph(): 
    
#     currency = combobox3.get()
#     period = selected.get()
    
#     # Define data for the graph based on the selected period
#     if period == 1:  # Week
#         x_values = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
#         y_values = [100, 120, 110, 130, 140]
#         title = f'{currency} Exchange Rate - Weekly'
#     elif period == 2:  # Month
#         x_values = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
#         y_values = [120, 130, 110, 140]
#         title = f'{currency} Exchange Rate - Monthly'
#     elif period == 3:  # Quarter
#         x_values = ['Month 1', 'Month 2', 'Month 3']
#         y_values = [130, 110, 140]
#         title = f'{currency} Exchange Rate - Quarterly'
#     elif period == 4:  # Year
#         x_values = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']
#         y_values = [110, 140, 120, 130]
#         title = f'{currency} Exchange Rate - Yearly'
    
#     # # Plot the graph
#     # plt.plot(x_values, y_values)
#     # plt.title(title)
#     # plt.xlabel('Period')
#     # plt.ylabel('Exchange Rate')
#     # plt.show()
    
#     fig, ax = plt.subplots(figsize = (4,3))
#     ax.plot(x_values, y_values)
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.set_title('Sample Graph')

#     # Clear any existing graph
#     for widget in t2.winfo_children():
#         if isinstance(widget, FigureCanvasTkAgg):
#             widget.destroy()

#     # Create the FigureCanvasTkAgg widget
#     canvas = FigureCanvasTkAgg(fig, master=t2)
#     canvas.draw()

#     # Display the FigureCanvasTkAgg widget
#     canvas.get_tk_widget().grid(row=5, column=3)
#     width, height = fig.get_size_inches()
#     window_width = int(width * 800)  # Multiply by a scaling factor to adjust the size
#     window_height = int(height * 800)
#     # root.geometry('800x500')
#     root.geometry(f"{window_width}x{window_height}")
#     # Add any additional widgets or functionality to the window as needed
#     # Start the Tkinter event loop
#     # convas.configure(scrollregion = convas.bbox('all'))
#     root.mainloop()


# t2 = Frame(tabs)
# tabs.add(t2, text = 'Course dynamics')

# # Scrollable frame for the second tab
# # scrollable_frame = Frame(t2)
# # scrollable_frame.grid(row = 0, column = 0, sticky = 'nsew')

# # Configure the scrollbar
# # scrollbar = Scrollbar(scrollable_frame)
# # scrollbar.grid(row = 0 , column = 1, sticky ='ns')

# # canvas = Canvas(scrollable_frame)
# # canvas.grid(row=0, column=0, sticky='nsew')
# # canvas.configure(yscrollcommand=scrollbar.set)
# # scrollbar.config(command=canvas.yview)

# lab1 = Label(t2, text = 'Currency', fg = 'gray')
# lab1.grid(row = 0 , column= 0, padx=10 , pady= 5 )
# lab2 = Label(t2, text = 'Period',  fg = 'gray')
# lab2.grid(row = 0 , column= 1, padx=10 , pady= 5)
# lab3 = Label(t2, text = 'Select period',  fg = 'gray')
# lab3.grid(row = 0 , column= 2, padx=10 , pady= 5)

# combobox3 = Combobox(t2)
# combobox3["values"] = ('USD', 'Ruble', 'euro', 'GBP', 'JPY')
# combobox3.current(0) #! i guess here you can control the function like if the current is this and current of the other is that do this and so on 
# combobox3.grid(row = 1, column = 0, padx=10 , pady=10 )

# selected = IntVar()
# def radio_buttons(): 
#     # Hide all comboboxes
#     comboboxweek.grid_forget()
#     comboboxmonth.grid_forget()
#     comboboxquarter.grid_forget()
#     comboboxyear.grid_forget()
#     if selected.get()==1:
#         comboboxweek.grid(row = 1, column = 2, padx=5 , pady=5 ) 
#     elif selected.get()==2: 
#         comboboxmonth.grid(row = 2, column = 2, padx=5 , pady=5 )
#     elif selected.get() ==3: 
#         comboboxquarter.grid(row = 3, column = 2, padx=5 , pady=5 )
#     elif selected.get() ==4:
#         comboboxyear.grid(row = 4, column = 2, padx=5 , pady=5 ) 

# radiobutton1 = Radiobutton(t2, text = "Week",value = 1, variable= selected, command=radio_buttons)
# radiobutton1.grid(row = 1, column = 1, padx=5 , pady=5)
# radiobutton2 = Radiobutton(t2, text = "Month",value = 2, variable= selected, command=radio_buttons)
# radiobutton2.grid(row = 2, column = 1, padx=5 , pady=5)
# radiobutton3 = Radiobutton(t2, text = "Quarter",value = 3,variable= selected, command=radio_buttons)
# radiobutton3.grid(row = 3, column = 1, padx=5 , pady=5)
# radiobutton4 = Radiobutton(t2, text = "Year",value = 4,variable= selected, command=radio_buttons)
# radiobutton4.grid(row = 4, column = 1, padx=5 , pady=5)

# #!here i guess you need to bind with a function to choose the date of the month
# comboboxweek = Combobox(t2, values=["Week 1", "Week 2", "Week 3", "Week 4"], state="readonly")
# comboboxweek.current(0) #! i guess here you can control the function like if the current is this and current of the other is that do this and so on 

# comboboxmonth = Combobox(t2, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state="readonly")
# comboboxmonth.current(0) #! i guess here you can control the function like if the current is this and current of the other is that do this and so on 

# comboboxquarter = Combobox(t2, values=["Q1", "Q2", "Q3", "Q4"], state="readonly")
# comboboxquarter.current(0) #! i guess here you can control the function like if the current is this and current of the other is that do this and so on 

# comboboxyear = Combobox(t2, values=list(range(2018, 2024)), state="readonly")
# comboboxyear.current(5) #! i guess here you can control the function like if the current is this and current of the other is that do this and so on 


# button2 = Button(t2, text="Make graph", command =make_graph)
# button2.grid(row = 4 , column = 0, padx=5 , pady=5)

# tabs.pack(fill = 'both', expand = True)

# root.mainloop()

#!==============================================================================


import locale
from tkinter import *
import tkinter.ttk as ttk
import datetime 
import matplotlib
import matplotlib.pyplot as plt
import urllib.request
import xml.dom.minidom
import xml.etree.ElementTree as ET
import re

class Window:
    def __init__(self):
        self.window = Tk() 
        self.window.title("Currency converter")
        self.width = "600"
        self.length = "250"
        self.window.resizable(False, False)
        self.tab_control = ttk.Notebook(self.window) #this changes the tabs
        self.tab_control.bind("<<NotebookTabChanged>>", self.change_resolution) #to resize the tabs 

    def change_resolution(self, event):
        current_tab = self.tab_control.index("current")
        if current_tab == 0:
            self.window.geometry("600x225")
        elif current_tab == 1:
            self.window.geometry(f"{self.width}x{self.length}")


class Tab1(Window):            
    def __init__(self):
        super().__init__()
        self.tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab, text = "Currency calculator")

        #list of first currency
        self.spisok_valut1 = ttk.Combobox(self.tab)
        self.spisok_valut1.config(width=45)
        self.spisok_valut1.state(['readonly'])
        self.spisok_valut1["values"] = self.get_list_with_currency() #list of currency 
        self.spisok_valut1.current(0)
        self.spisok_valut1.grid(column=0, row=0 , padx=10,pady=10)

        #list of the second currency 
        self.spisok_valut2 = ttk.Combobox(self.tab)
        self.spisok_valut2.state(['readonly'])
        self.spisok_valut2.config(width=45)
        self.spisok_valut2["values"] = self.get_list_with_currency() # сюда надо залить список из валют
        self.spisok_valut2.current(4)
        self.spisok_valut2.grid(column=0, row=1 , padx=10,pady=10)

        #for inputing values 
        vcmd = (self.window.register(self.validate_input),'%P')

        self.vvod_valut = Entry(self.tab, validate="key", validatecommand= vcmd)
        self.vvod_valut.grid(column=1, row=0 , padx=10,pady=10)

        #button of conversion
        btn_convertation = Button(self.tab, text="Convert", command = self.btn_convertation_func )
        btn_convertation.grid(column = 2, row = 0, padx=10,pady=10)

        #output of the conversion
        self.label_valut = Label(self.tab , text = "Result")
        self.label_valut.grid(column = 1 , row= 1 , padx=10,pady=10)
    
    #for validation of the input of numbers only
    @staticmethod
    def validate_input(inp):
        pattern = r'^[0-9]*[\.]?[0-9]*$'
        if re.match(pattern, inp):
            if inp.count(".") <= 1:
                return True
        elif inp == "":
            return True
        return False

    #button of conversion 
    def btn_convertation_func(self):
        value1 = str(self.spisok_valut1.get())
        value2 = str(self.spisok_valut2.get())
        #getting the value of ruble for them 
        value1 = self.get_currency_val(value1)
        value2 = self.get_currency_val(value2)
        #formula for changing from one to another 
        result = self.formula_currency(value1,value2, self)
        #bringing the result of the conversion
        self.change_label_valut(result,self)
        
    def blink(self,label , count):
        if count % 2 == 0:
            label.config(fg="black")
        else:
            label.config(fg="red")
        if count>0:
            label.after(500, self.blink, label , count-1)

    @staticmethod
    def change_label_valut(result,self):
        if isinstance(result, str):
            self.label_valut["text"] = f"{result}"
            self.blink(self.label_valut, 7)
        elif isinstance(result, int) or isinstance(result, float):
            self.label_valut["text"] = f"{result:.3f}"

    # for finding the value of ruble
    @staticmethod
    def formula_currency(value1, value2, self):
        value3 = self.vvod_valut.get()
        if not value3:
            return "Введите значение"
        else:
            result = value1 * float(value3) / value2 
            return result 
        
    #getting the latest values     
    @staticmethod
    def get_list_with_currency():
        url = "http://www.cbr.ru/scripts/XML_daily.asp"
        response = urllib.request.urlopen(url)
        dom = xml.dom.minidom.parseString(response.read())
        nodeArray = dom.getElementsByTagName("Valute")
        result_list = [node.getElementsByTagName("Name")[0].childNodes[0].nodeValue for node in nodeArray]
        result_list.append("Russian Ruble")
        return result_list
        
    #according to the name of the currency, we return its value
    
    @staticmethod
    def get_currency_val(currency_name):
        try:
            url = f"https://www.cbr.ru/scripts/XML_daily.asp"
            with urllib.request.urlopen(url) as response:
                xml_data = response.read()
            root = ET.fromstring(xml_data)
            currency_element = None
            for elem in root.findall(".//Valute"):
                name_elem = elem.find("Name")
                if name_elem is not None and currency_name in name_elem.text:
                    currency_element = elem
                    break


            if currency_element is None:
                # Check if currency_name is "Russian Ruble" and return 1.0
                if currency_name == "Russian Ruble":
                    return 1.0
                return None
            # if currency_element is None:
                
            #     return None

            value_elem = currency_element.find("Value")
            nominal_elem = currency_element.find("Nominal")

            if value_elem is None or nominal_elem is None:
                return None

            value = float(value_elem.text.replace(",", "."))
            nominal = float(nominal_elem.text)

            return value / nominal
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
        
class Tab2(Tab1, Window):
    def __init__(self):
        super().__init__()
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text="Currency Dynamic")
        # label of the currency
        currency_label = ttk.Label(self.tab2, text="Currency")
        currency_label.grid(column=0, row=0, padx=10, pady=10)

        # selection of currency
        self.currency_list = ttk.Combobox(self.tab2, values=self.get_list_with_currency(), width=45)
        self.currency_list.state(['readonly'])
        self.currency_list.current(0)
        self.currency_list.grid(column=0, row=1, padx=10, pady=10)

        # button of making the graph 
        build_button = ttk.Button(self.tab2, text="Make graph", command=self.build_button_command)
        build_button.grid(column=0, row=4, padx=10, pady=10)

        # Period label
        period_label = ttk.Label(self.tab2, text="Period")
        period_label.grid(column=1, row=0, padx=10, pady=10)

        # Radiobutton week, month, quarter, year
        period_var = IntVar(value=0)
        self.period_var = period_var

        radiobutton_week = ttk.Radiobutton(self.tab2, text="Week", variable=period_var, value=0, command=self.show_list_week)
        radiobutton_week.grab_current()
        radiobutton_week.grid(column=1, row=1, padx=10, pady=10)
        self.show_list_week()

        radiobutton_month = ttk.Radiobutton(self.tab2, text="Month", variable=period_var, value=1, command=self.show_list_month)
        radiobutton_month.grid(column=1, row=2, padx=10, pady=10)

        radiobutton_quarter = ttk.Radiobutton(self.tab2, text="Quarter", variable=period_var, value=2, command=self.show_list_quarter)
        radiobutton_quarter.grid(column=1, row=3, padx=10, pady=10)

        radiobutton_year = ttk.Radiobutton(self.tab2, text="Year", variable=period_var, value=3, command=self.show_list_year)
        radiobutton_year.grid(column=1, row=4, padx=10, pady=10)

        # label of choosing period 
        period_label = ttk.Label(self.tab2, text="Choose period")
        period_label.grid(column=2, row=0, padx=10, pady=10)

        # run 
        self.tab_control.pack(expand=True, fill=BOTH)
        self.window.mainloop()  # mainloop 
    

    #func of making graph 
    def build_button_command(self):
        value = None
        list_value = None
        handle_click = self.handle_button_click()
        if handle_click == 0:
            value = self.list_week.get()
            list_value = self.get_date_range_for_week(value)
        elif handle_click == 1:
            value = self.list_month.get()
            list_value = self.get_date_range_for_month(value)
        elif handle_click == 2:
            value = self.list_period.get()
            list_value = self.get_mondays_of_quarter(value)
        elif handle_click == 3:
            value = self.list_year.get()
            list_value = self.get_first_days_of_months(value)
        else:
            return None

        if list_value is None:
            return None

        currency_name = self.currency_list.get()
        list_value2 = [self.get_currency_for_date_and_name(date, currency_name) for date in list_value]
        self.graph(list_value, list_value2)
        
    def handle_button_click(self):
        selected_value = self.period_var.get()
        return selected_value

    @staticmethod
    def get_date_range_for_week(date_range):
        date_range = str(date_range)
        start_date, end_date = map(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'), date_range.split())
        delta = end_date - start_date
        dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
        return [date.strftime('%d/%m/%Y') for date in dates]
    
    @staticmethod #method can be called without making the instance of class 
    def get_date_range_for_month(month_year_str):
        # преобразуем строку в объект datetime
        month_year_obj = datetime.datetime.strptime(month_year_str, "%B %Y")
        # month and year definition
        year = month_year_obj.year
        month = month_year_obj.month
        # firsy day of month 
        first_day = datetime.date(year, month, 1)
        # last day of the month 
        last_day = datetime.date(year, month, 28) + datetime.timedelta(days=4)
        last_day = last_day - datetime.timedelta(days=last_day.day)
        # making list off dates 
        dates = [(first_day + datetime.timedelta(days=i)).strftime('%d/%m/%Y') for i in range((last_day - first_day).days + 1)]
        return dates
    
    @staticmethod
    def get_currency_for_date_and_name(date, currency_name):
        url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={}".format(date)
        with urllib.request.urlopen(url) as response:
            tree = ET.parse(response)
        root = tree.getroot()
        for valute in root.iter('Valute'):
            name = valute.find('Name').text
            if name == currency_name:
                value_str = valute.find('Value').text.replace(',', '.')
                nominal_str = valute.find('Nominal').text.replace(',', '.')
                return float(value_str) / float(nominal_str)
        return None


    def show_list_week(self):
        self.hide_list()
        self.list_week = ttk.Combobox(self.tab2, values = self.get_weekly_dates())
        self.list_week.state(['readonly'])
        self.list_week.config(width=20)
        self.list_week.grid(column=2, row=1,  padx=10, pady=10)
        self.list_week.current(0)
    
    @staticmethod
    def get_weekly_dates():
        dates = []
        current_date = datetime.date.today()
        for i in range(12):
            # вычисляем дату начала текущей недели
            start_date = current_date - datetime.timedelta(days=current_date.weekday())
            # вычисляем дату конца текущей недели
            end_date = start_date + datetime.timedelta(days=6)
            # добавляем даты начала и конца недели в список
            dates.append((start_date.strftime("%d/%m/%Y"), end_date.strftime("%d/%m/%Y")))
            # переходим к предыдущей неделе
            current_date -= datetime.timedelta(weeks=1)
        # возвращаем список дат
        return dates

    def show_list_month(self):
        self.hide_list()
        self.list_month = ttk.Combobox(self.tab2, value = self.get_monthly_dates())
        self.list_month.state(['readonly'])
        self.list_month.grid(column=2, row=2,  padx=10, pady=10)
        self.list_month.current(0)
    
    @staticmethod
    def get_monthly_dates():
        locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
        today = datetime.date.today()
        dates = []
        for i in range(24):
            date = today - datetime.timedelta(days=30*i)
            dates.append(date.strftime("%B %Y"))
        return dates
    
    def show_list_quarter(self):
        self.hide_list()
        self.list_period = ttk.Combobox(self.tab2, values = self.get_quarter_dates())
        self.list_period.state(['readonly'])
        self.list_period.grid(column=2, row=3,  padx=10, pady=10)
        self.list_period.current(0)

    @staticmethod
    def get_mondays_of_quarter(quarter):
        year = int(quarter.split()[-1])
        quarter_num = int(quarter.split()[0])
        if quarter_num == 1:
            start_date = datetime.datetime(year, 1, 1)
        elif quarter_num == 2:
            start_date = datetime.datetime(year, 4, 1)
        elif quarter_num == 3:
            start_date = datetime.datetime(year, 7, 1)
        elif quarter_num == 4:
            start_date = datetime.datetime(year, 10, 1)
        else:
            return []
        end_date = start_date + datetime.timedelta(days=91)
        monday_dates = []
        while start_date <= end_date:
            if start_date.weekday() == 0: # если это понедельник
                monday_dates.append(start_date.strftime('%d/%m/%Y'))
            start_date += datetime.timedelta(days=1)
        return monday_dates

    @staticmethod
    def get_quarter_dates():
        quarters = []
        for i in range(12):
            now = datetime.date.today() - datetime.timedelta(days=i*365/4)
            quarter = (now.month-1)//3 + 1
            quarters.append(str(quarter) + " квартал " + str(now.year))
        return quarters
    
    def show_list_year(self):
        self.hide_list()
        self.list_year = ttk.Combobox(self.tab2, values = self.get_years_list())
        self.list_year.state(['readonly'])
        self.list_year.grid(column=2, row=4,padx=10, pady=10)
        self.list_year.current(0)

    @staticmethod
    def get_years_list():
        now = datetime.date.today()
        years = [now.year - i for i in range(12)]
        return years
    
    @staticmethod
    def get_first_days_of_months(year):
        date_list = []
        year = int(year)
        for month in range(1, 13):
            date = datetime.datetime(year, month, 1)
            date_list.append(date.strftime('%d/%m/%Y'))
        return date_list

    def hide_list(self):
        for widget in self.tab2.winfo_children():
            if isinstance(widget, ttk.Combobox):
                if widget != self.currency_list:
                    widget.destroy()
                    
    def graph(self,x,y):
        plt.rc('font', size=6)
        matplotlib.use('TkAgg')
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = self.tab2)
        self.plot_widget = canvas.get_tk_widget()
        fig.clear()
        today = datetime.datetime.now().date() # current dates 
        valid_dates = [] # valid dates that can be used 
        for date_str in x:
            date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
            if date <= today:
                valid_dates.append(date_str)
        valid_indices = [x.index(date_str) for date_str in valid_dates] # valid dates, indexes 
        valid_y = [y[i] for i in valid_indices] # values of the dates 
        plt.plot(valid_dates, valid_y)
        plt.grid()
        plt.xticks(rotation=45)
        self.width = "1225"
        self.length = "725"
        self.window.geometry(f"{self.width}x{self.length}")
        self.plot_widget.grid(row=10, column=10)

if __name__ == '__main__':
    Tab2()
    