import sqlite3
import tkinter.messagebox
import re
from tkinter import ttk
import csv
from sqlite3 import OperationalError


class MyGUI:
 def __init__(self):
   self.main_window = tkinter.Tk()
   self.main_window.title('Tawakkalna')
   self.tab = ttk.Notebook(self.main_window)
   self.main_window.geometry('600x550')
   self.tab.pack(expan=True,ipadx='300',ipady="300")
   self.main_window.iconphoto(True, tkinter.PhotoImage(file='image.png'))

   # -------------------------
   # the first tab
   # -------------------------
   self.label_frame1= tkinter.LabelFrame(self.main_window)
   self.top_frame = tkinter.Frame(self.label_frame1)
   self.First_Name_label = tkinter.Label(self.top_frame, text='Enter First Name')
   self.First_Name_entry = tkinter.Entry(self.top_frame, width=20)


   self.Last_Name_label = tkinter.Label(self.top_frame, text='Enter Last Name')
   self.Last_Name_entry = tkinter.Entry(self.top_frame, width=20)


   self.ID_label = tkinter.Label(self.top_frame, text='Enter your ID')
   self.ID_entry = tkinter.Entry(self.top_frame, width=20)


   self.Gen_label = tkinter.Label(self.top_frame, text='Enter your Gender')
   self.optionList = ['Male', 'Female']
   self.variable1 = tkinter.StringVar(self.top_frame)
   self.variable1.set(self.optionList[0])
   self.opt = tkinter.OptionMenu(self.top_frame, self.variable1, *self.optionList)


   self.birth_label = tkinter.Label(self.top_frame,text='Enter the year of birth')
   self.birth_entry = tkinter.Entry(self.top_frame, width=20)


   self.vaccine_label = tkinter.Label(self.top_frame,text='Enter the Type of Vaccine')
   self.OptionList = [
     "Pfizer",
     "AstraZeneca",
     "Moderna",
     "J&J"
   ]

   self.variable = tkinter.StringVar(self.top_frame)
   self.variable.set(self.OptionList[0])
   self.dropDown_vaccine = tkinter.OptionMenu(self.top_frame, self.variable, *self.OptionList)

   self.phone_label = tkinter.Label(self.top_frame,text='Enter the phone number')
   self.phone_entry = tkinter.Entry(self.top_frame,width=20)



   self.Date_label = tkinter.Label(self.top_frame, text='Date')
   self.Date_entry = tkinter.Entry(self.top_frame,width=20)

   self.Time_label = tkinter.Label(self.top_frame, text='Time')
   self.Time_entry = tkinter.Entry(self.top_frame,width=20)


   self.submit_button = tkinter.Button(self.top_frame, text="submit",foreground='Black', font= ('Arial',20,'bold'), command=self.action)
   self.quit_button = tkinter.Button(self.top_frame, text='Quit',foreground='Black', font= ('Arial',20,'bold'), command=self.main_window.destroy)

   self.label_frame1.pack()
   self.top_frame.pack(side='left')

   self.First_Name_label.grid(row=0, column=0,sticky='NW', pady="10", padx="10")
   self.First_Name_entry.grid(row=0, column=1,sticky='NW', pady="10", padx="100")
   self.Last_Name_label.grid(row=1, column=0,sticky='NW', pady="10", padx="10")
   self.Last_Name_entry.grid(row=1, column=1,sticky='NW', pady="10", padx="100")
   self.ID_label.grid(row=2, column=0,sticky='NW', pady="10", padx="10")
   self.ID_entry.grid(row=2, column=1,sticky='NW', pady="10", padx="100")
   self.Gen_label.grid(row=3, column=0,sticky='NW', pady="10", padx="10")
   self.opt.grid(row=3, column=1,sticky='NW', pady="10", padx="100")
   self.birth_label.grid(row=4, column=0,sticky='NW', pady="10", padx="10")
   self.birth_entry.grid(row=4, column=1,sticky='NW', pady="10", padx="100")
   self.vaccine_label.grid(row=5, column=0,sticky='NW', pady="10", padx="10")
   self.dropDown_vaccine.grid(row=5, column=1,sticky='NW', pady="10", padx="100")
   self.phone_label.grid(row=6, column=0,sticky='NW', pady="10", padx="10")
   self.phone_entry.grid(row=6, column=1,sticky='NW', pady="10", padx="100")
   self.Date_label.grid(row=7, column=0, sticky='NW', pady="10", padx="10")
   self.Date_entry.grid(row=7, column=1, sticky='NW', pady="10", padx="100")
   self.Time_label.grid(row=8, column=0, sticky='NW', pady="10", padx="10")
   self.Time_entry.grid(row=8, column=1, sticky='NW', pady="10", padx="100")
   self.submit_button.grid(row=9, column=0)
   self.quit_button.grid(row=9, column=1)
   self.tab.add(self.label_frame1, text='Check-in')
# -------------------------
# the second tab
# -------------------------
   self.label_frame2 = tkinter.LabelFrame(self.main_window)
   self.top_frame2 = tkinter.Frame(self.label_frame2)


   self.ID_label2 = tkinter.Label(self.top_frame2, text='Enter your ID:')
   self.ID_entry2 = tkinter.Entry(self.top_frame2, width=10)

   self.l10 = tkinter.Label(self.top_frame2, text="Status:")
   self.t10 = tkinter.Label(self.top_frame2, text='                           ')
   self.comment = tkinter.Label(self.top_frame2)

   self.submit_button2 = tkinter.Button(self.top_frame2, text="submit",foreground='Black', font= ('Arial',20,'bold'), command=self.ac)

   self.label_frame2.pack()
   self.top_frame2.pack()
   self.ID_label2.grid(row=0, column=0,sticky='NW', pady="10", padx="10")
   self.ID_entry2.grid(row=0, column=1,sticky='NW', pady="10", padx="10")
   self.l10.grid(row=1, column=0)
   self.t10.grid(row=1, column=1)
   self.comment.grid(row=1, column=2)
   self.submit_button2.grid(row=2, column=1)
   self.tab.add(self.label_frame2, text='Immunity Check')

#-------------------------
#the third tab
#-------------------------
   self.label_frame3 = tkinter.LabelFrame(self.main_window)
   self.top_frame3 = tkinter.Frame(self.label_frame3)

   self.l11 = tkinter.Label(self.top_frame3, text='Directory', font= ('Arial',20,'bold'))
   self.t11 = tkinter.Entry(self.top_frame3, width=20)

   self.b3 = tkinter.Button(self.top_frame3, text="Import", foreground='Black', font= ('Arial',20,'bold'), command=self.Import)
   self.btn2 = tkinter.Button(self.top_frame3, text='Export', foreground='Black', font= ('Arial',20,'bold'), command=self.Export)

   self.label_frame3.pack()
   self.top_frame3.pack()
   self.l11.grid(row=0, column=0,sticky='NW', pady="10", padx="10")
   self.t11.grid(row=0, column=1,sticky='NW', pady="10", padx="10")
   self.b3.grid(row=4, column=0)
   self.btn2.grid(row=4, column=1)
   self.tab.add(self.label_frame3, text='Import & Export')
   tkinter.mainloop()

 # -------------------------
 # validation funtions
 # -------------------------
 def birth_validation(self):
   year = int(self.birth_entry.get())

   if len(str(year)) == 0:
     return False
   if year > 1900 and year < 2003:
     return True
   return False

 def Phone_number(self):
   regex1 = "^05\d{8}$"
   flag2=False
   if re.search(regex1, self.phone_entry.get()):
     flag2 = True
   return flag2

 def name(self):
   regex3 = "^[a-zA-Z]+$"
   flag3=False
   if re.search(regex3, self.First_Name_entry.get()):
     if re.search(regex3, self.Last_Name_entry.get()):
        flag3 = True
   return flag3

 def ID(self):
   regex1 ="^\d{10}$"
   flag2=False
   if re.search(regex1, self.ID_entry.get()):
     flag2 = True
   return flag2
 def ID2(self):
   regex1 = "^\d{10}$"
   flag2=False
   if re.search(regex1, self.ID_entry2.get()):
     flag2 = True
   return flag2

 def date_validation(self):
   regex = "\d{2}-\d{2}-\d{4}$"
   flag2 = False
   if re.search(regex, self.Date_entry.get()):
     flag2 = True
   return flag2

 def time_validation(self):
   regex = "^(0?[1-9]|1[012])(:[0-5]\d) [APap][mM]$"
   flag2 = False
   if re.search(regex, self.Time_entry.get()):
     flag2 = True
   return flag2

 def action(self):
   try:
     if(self.birth_validation()):
       if(self.Phone_number()):
         if(self.name()):
           if(self.ID()):
             if(self.time_validation()):
               if(self.date_validation()):
                 conn = sqlite3.connect("users.db")
                 conn.execute('''CREATE TABLE IF NOT EXISTS vaccinated
                    (ID INT PRIMARY KEY   NOT NULL,
                 FirstName TEXT  NOT NULL,
                 LastName TEXT  NOT NULL,
                 Sex  TEXT  NOT NULL,
                 year_birth INT  NOT NULL,
                 Vaccine TEXT  NOT NULL,
                 Vaccine2 TEXT   NULL,
                 Date TEXT NOT NULL,
                 Time TEXT NOT NULL,
                 Phone BLOB NOT NULL,
                 Dose INT NOT NULL);''')
                 try:
                   conn.execute("INSERT INTO vaccinated (ID,FirstName,LastName,Sex,year_birth,Vaccine,Date,Time,Phone,Dose) VALUES (?,?,?,?,?,?,?,?,?,?)",(self.ID_entry.get(),self.First_Name_entry.get(),self.Last_Name_entry.get(),self.variable1.get(),self.birth_entry.get(),self.variable.get(),self.Date_entry.get(),self.Time_entry.get(),self.phone_entry.get(),1))
                   conn.commit()
                   tkinter.messagebox.showinfo('Response', 'first dose done')
                   conn.close()
                 except sqlite3.IntegrityError:
                   cursor = conn.cursor()
                   cursor.execute("SELECT Dose FROM vaccinated WHERE ID=?", [self.ID_entry.get(), ])
                   results = cursor.fetchall()
                   if(results[0][0] == 1):
                     conn.execute("UPDATE vaccinated set Dose = 2 WHERE ID=?", [self.ID_entry.get(), ])
                     conn.execute("UPDATE vaccinated set Vaccine2 =?  WHERE ID=?", [self.variable.get(),self.ID_entry.get(),])
                     conn.commit()
                     tkinter.messagebox.showinfo('Response', 'second dose done')
                     conn.close()
                   else:
                     tkinter.messagebox.showinfo('Response', 'you are fully vaccinated')
                     conn.close()
               else:
                 tkinter.messagebox.showinfo('Response', 'Please enter the Date correctly')
             else:
               tkinter.messagebox.showinfo('Response', 'Please enter the Time correctly')
           else:
             tkinter.messagebox.showinfo('Response', 'Please enter the ID correctly')
         else:
           tkinter.messagebox.showinfo('Response', 'Please enter the name correctly')
       else:
         tkinter.messagebox.showinfo('Response', 'Please enter the Phone number correctly')
     else:
       tkinter.messagebox.showinfo('Response', 'Please enter the Year of Birth correctly')
   except ValueError:
     tkinter.messagebox.showinfo('Response', 'Try again')

 def ac(self):
   if(self.ID2()):
     conn = sqlite3.connect("users.db")
     c = conn.cursor()
     try:
       c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students' ''')
       conn.commit()
       cursor = conn.execute("SELECT Dose FROM vaccinated WHERE ID=?", [self.ID_entry2.get(), ])
       results = cursor.fetchall()
       conn.commit()
       try:
           if(results[0][0] == 1):
             self.t10.config(bg="Yellow")
             self.comment.configure(text="vaccinated")
           elif (results[0][0] == 2):
             self.t10.config(bg="Green")
             self.comment.configure(text="Fully vaccinated")
       except sqlite3.OperationalError:
           self.t10.config(bg="Red")
           self.comment.configure(text="Not vaccinated")
       except IndexError:
           self.t10.config(bg="Red")
           self.comment.configure(text="Not vaccinated")
     except OperationalError:
       tkinter.messagebox.showinfo('Response', 'there are No data')

   else:
     tkinter.messagebox.showinfo('Response', 'enter the ID correctly')

 def Export(self):
   conn = sqlite3.connect("users.db")
   try:
     cursor = conn.execute("SELECT * FROM vaccinated")
     rows = cursor.fetchall()
     file = open(f'{self.t11.get()}', 'a')
     csvwriter = csv.writer(file)
     for row in rows:
      csvwriter.writerow(list(row))
     conn.commit()
     tkinter.messagebox.showinfo('Response', 'Done')
     file.close()
   except OperationalError:
     tkinter.messagebox.showinfo('Response', 'there are No data')
   except FileNotFoundError:
     tkinter.messagebox.showinfo('Response', 'enter the name of the file')
   conn.close()

 def Import(self):
   conn = sqlite3.connect("users.db")
   try:
     file = open(f'{self.t11.get()}', 'r')
     csvreader = csv.reader(file)
     i = 0
     for row in csvreader:
       conn.execute('''CREATE TABLE IF NOT EXISTS imported
       (ID INT PRIMARY KEY   NOT NULL,
       FirstName TEXT  NOT NULL,
       LastName TEXT  NOT NULL,
       Sex  TEXT  NOT NULL,
       year_birth INT  NOT NULL,
       Vaccine TEXT  NOT NULL,
       Vaccine2 TEXT   NULL,
       Date TEXT NOT NULL,
       Time TEXT NOT NULL,
       Phone BLOB NOT NULL,
       Dose INT NOT NULL);''')
       conn.execute("INSERT INTO imported (ID,FirstName,LastName,Sex,year_birth,Vaccine,Vaccine2,Date,Time,Phone,Dose) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
         (row[int(i)], row[int(i + 1)], row[int(i + 2)], row[int(i + 3)],
          row[int(i + 4)], row[int(i + 5)], row[int(i + 6)], row[int(i + 7)],
          row[int(i + 8)],row[int(i + 9)],row[int(i + 10)]
          ))
       conn.commit()
     tkinter.messagebox.showinfo('Response', 'Done')
     file.close()
   except FileNotFoundError:
     tkinter.messagebox.showinfo('Response', 'file not Found')
   conn.close()


my_gui = MyGUI()