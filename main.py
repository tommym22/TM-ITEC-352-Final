#!/usr/bin/env python3/3.10
#imports
import csv
import itertools as it
import sv_ttk
import tkinter as tk
from tkinter import messagebox, ttk, Tk, BooleanVar, IntVar, StringVar

#create the root window and set the theme
root = tk.Tk()
sv_ttk.set_theme("dark")

#Global variables
storeInfoFile = 'account_data.csv'
prevEntry = ""
fname = StringVar()
lname = StringVar()
email = StringVar()
country = StringVar()
age = IntVar()
username = StringVar()
password = StringVar()
confPassword = StringVar()
newsletter = BooleanVar()
tac = BooleanVar()

#Stores all the frames   
class MainFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self,parent)
        self.parent = parent
        self.parent.title("Tommy Data Entry Form")

        # Create a frame for each page and display a welcome message
        self.piFrame = PersonalInformationFrame(self.parent).grid()
        self.aiFrame = AccountInformationFrame(self.parent).grid()
        self.tcFrame = TermsConditionsFrame(self.parent).grid()
        self.btsFrame = ButtonsFrame(self.parent).grid()
        messagebox.showinfo("Welcome", "To create an account, fill in all the fields and click Submit. To login, fill out the username and password fields and then click Login.")

#stores fname, lname, email, country, age     
class PersonalInformationFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
    
        #Label Frame
        self.labelFrame = ttk.LabelFrame(self.parent, text="Personal Information")
        self.labelFrame.grid(padx=15,pady=15, row=0, column=0)

        #First Name
        self.fname_label = ttk.Label(self.labelFrame, text="First Name")
        self.fname_entry = ttk.Entry(self.labelFrame, textvariable=fname)
        self.fname_entry.focus_set()
        self.fname_label.grid(row=0, column=0, padx = 5, pady = 5)
        self.fname_entry.grid(row=0, column=1, padx = 5, pady = 5)
        
        
        #Last Name
        self.lname_label = ttk.Label(self.labelFrame, text="Last Name")
        self.lname_entry = ttk.Entry(self.labelFrame, textvariable=lname)
        self.lname_label.grid(row=1, column=0, padx = 5, pady = 5)
        self.lname_entry.grid(row=1, column=1, padx = 5, pady = 5)
        
        
        #Email
        self.email_label = ttk.Label(self.labelFrame, text="Email")
        self.email_entry = ttk.Entry(self.labelFrame,textvariable=email)
        self.email_label.grid(row=2, column=0, padx = 5, pady = 5)
        self.email_entry.grid(row=2, column=1, padx = 5, pady = 5)
        
        #Gets a list of countries from a csv file and appends to a list
        def getCountries():
            with open('countries.csv') as file:
                csvFile = csv.reader(file)
                countriesList = []
                for row in it.islice(csvFile, 2, None):
                    country = (str(row) [2:-2])
                    countriesList.append(country) 
            file.close() 
            return countriesList
        
        #takes the list of countries and makes them the values
        self.country_entry = ttk.Combobox(self.labelFrame, values=getCountries(),textvariable=country, state="readonly")
        
        #setup as normal
        self.country_label = ttk.Label(self.labelFrame, text="Country")
        self.country_label.grid(row=0, column=2, padx = 5, pady = 5)
        self.country_entry.grid(row=0, column=3, sticky="we", padx = 5, pady = 5)
        
        #Age
        self.age_label = ttk.Label(self.labelFrame, text="Age")
        self.age_entry = ttk.Spinbox(self.labelFrame, from_=0, to_=99, increment=1, textvariable=age)
        
        self.age_label.grid(row=1, column=2, padx = 5, pady = 5)
        self.age_entry.grid(row=1, column=3,padx = 5, pady = 5)
   
#stores username, password, confpassword
class AccountInformationFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        #Label Frame
        self.labelFrame = ttk.LabelFrame(self.parent, text="Account Information")
        self.labelFrame.grid(padx=(0,15),pady=(15), row=0, column=1,sticky="E")

        #Username
        self.fname_label = ttk.Label(self.labelFrame, text="Username")
        self.fname_entry = ttk.Entry(self.labelFrame,textvariable=username)
        self.fname_label.grid(row=0, column=0, padx = 5, pady = 5)
        self.fname_entry.grid(row=0, column=1, padx = 5, pady = 5)
        
        #Password
        self.lname_label = ttk.Label(self.labelFrame, text="Password")
        self.lname_entry = ttk.Entry(self.labelFrame, show="*",textvariable=password)
        self.lname_label.grid(row=1, column=0, padx = 5, pady = 5)
        self.lname_entry.grid(row=1, column=1, padx = 5, pady = 5)
        
        #ConfPassword
        self.email_label = ttk.Label(self.labelFrame, text="Confirm Password")
        self.email_entry = ttk.Entry(self.labelFrame, show="*",textvariable=confPassword)
        self.email_label.grid(row=2, column=0, padx = 5, pady = 5)
        self.email_entry.grid(row=2, column=1, padx = 5, pady = 5)

#stores newsletter, terms and conditions
class TermsConditionsFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        #Label Frame
        self.labelFrame = ttk.LabelFrame(self.parent, text="Terms and Conditions")
        self.labelFrame.grid(padx=15, pady=(5,10), row=1, column=0,sticky='nesw', columnspan=2)

        #Newsletter
        self.news_check = ttk.Checkbutton(self.labelFrame, variable=newsletter)
        self.news_label = ttk.Label(self.labelFrame, text="Please don't not sign me up for a hourly newsletter!")
        self.news_check.grid(row=0, column=0, padx = 5)
        self.news_label.grid(row=0, column=1, padx = 5)
        
        #TermsAndConditions
        self.tac_check = ttk.Checkbutton(self.labelFrame,variable=tac)
        self.tac_label = ttk.Label(self.labelFrame, text="I've definitely read the Terms and Conditions")
        self.tac_check.grid(row=1, column=0,sticky="we", padx = 5)
        self.tac_label.grid(row=1, column=1, sticky="we", padx = 5)

#stores all the buttons  
class ButtonsFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        #Store all these variables
        
        #Label Frame
        self.Frame = ttk.Frame(self.parent)
        self.Frame.grid(padx=(15),pady=(8),  row=3, column=1)

        #Submit Button Frame
        self.submit_button = ttk.Button(self.Frame, text="Submit", command=ButtonsFrame.checkAndStoreFields, width=10)
        self.submit_button.grid(row=0, column=0, padx=(8))
        
        self.login_button = ttk.Button(self.Frame, text="Login", command=ButtonsFrame.checkAndFillFields, width=10)
        self.login_button.grid(row=0, column=1, padx=(8))
        
        #Clear Button Frame
        self.clear_button = ttk.Button(self.Frame, text="Clear",command=ButtonsFrame.clearFields,width=10)
        self.clear_button.grid(row=0, column=2, padx=(8))
   
    #runs a series of checks and then stores the information
    def checkAndStoreFields():
        fn = fname.get()
        ln = lname.get()
        em = email.get()
        ct = country.get()
        ag = str(age.get())
        us = username.get()
        pa= password.get()
        co = confPassword.get()
        ne = str(newsletter.get())
        te = str(tac.get())
        fullString = [fn,ln,em,ct,ag,us,pa,co,ne,te]
        if fn == "" or ln =="" or em =="" or ct=="" or int(ag)<1 or us=="" or pa=="" or co=="" or te=="False":
            messagebox.showwarning("Error","One or more of the fields are blank!")
        elif pa!=co:
            messagebox.showwarning("Error", "Passwords must match!")
        else:
            with open(storeInfoFile, "a", newline="") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(fullString)
            file.close()
            messagebox.showinfo("Success","Account was created sucessfully!")
    
    #fills in all fields based on login information       
    def checkAndFillFields():
        us = username.get()
        pa= password.get()
        try: 
            with open(storeInfoFile, newline="") as file:
                fullString=[]
                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    if row[5] == us and row[6]==pa:
                        fullString = row
                        break
                fname.set(fullString[0])
                lname.set(fullString[1])
                email.set(fullString[2])
                country.set(fullString[3])
                age.set(fullString[4])
                username.set(fullString[5])
                password.set(fullString[6])
                confPassword.set(fullString[7])
                newsletter.set(fullString[8])
                tac.set(fullString[9])
            file.close()
        except:
            messagebox.showerror("Error", "There is no stored data. Why don't you create an account?") 
     #clears the fields       
    def clearFields():
        fname.set("")
        lname.set("")
        email.set("")
        country.set("")
        age.set(0)
        username.set("")
        password.set("")
        confPassword.set("")
        newsletter.set(False)
        tac.set(False)
        messagebox.showinfo("Cleared", "Fields have been cleared.")

#Main Function
if __name__ == "__main__":
    root.resizable(width=False,height=False)
    app = MainFrame(root)
    app.mainloop()
