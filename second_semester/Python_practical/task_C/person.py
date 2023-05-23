import pickle 
import datetime 

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # self.log("CRE", f"Person created with the following name: {self.first_name} {self.last_name}")
        
    def log(self, key, comment):
        now = datetime.datetime.now()
        log_data= f"{key} --- {now} --- {comment}"
        with open('log.txt', 'a') as f:
            f.write(log_data + '\n')
            
    def __str__(self):
        # self.log("INF", f"Information about person: {self.first_name} {self.last_name} printed")
        return f"Name & Surname: {self.first_name} {self.last_name}\n\tAge: {self.age}\n"
