1.Write a python program to create a class Student whose objects have properties namely: Name, Roll number,Marks of 6 subjects and SGPA. Take user input to fill in the fields. Display the class of the student depending upon his sgpa. (>8 = Distinction; >6 & <8 = First Class;  >4 & <6 = Second class, Else fail).If the candidate has failed, display the total number of subjects in which he/she has failed along with the list of subjects. Marks should be limited from 0 to 100.
class Student:
    def __init__(self):
        self.name=input("Enter your name")
        self.roll_no=int(input("Enter your roll_no"))
        self.sub1=self.input_subjects()
        self.sub2 = self.input_subjects()
        self.sub3 = self.input_subjects()
        self.sub4 = self.input_subjects()
        self.sub5 = self.input_subjects()
        self.sub6 = self.input_subjects()
    def input_subjects(self):
        n=int(input("Enter subject marks:"))
        if(n<=100 and n>=0):
            return n
        else:
            n=int(input("Enter correct marks:"))
            while n not in range(0,101):
                n=int(input("Enter correct marks:"))
            return n

    def check_marks(self,sub1,sub2,sub3,sub4,sub5,sub6):
        subject=["Subject1","Subject2","Subject3","Subject4","Subject5","Subject6","Subject7"]
        marks=[sub1,sub2,sub3,sub4,sub5,sub6]
        fail_subject=[]
        pass_subject=[]
        for i,j in zip(marks,subject):
            if i<40:
                fail_subject.append([i,j])
            else:
                pass_subject.append([i,j])

        if fail_subject==[]:
            total=sub1+sub2+sub3+sub4+sub5+sub6
            percent=(total/600)*100
            if percent>80:
                print("Name:",self.name,"Roll number",self.roll_no," Passed with distinction")
            elif percent<80 and percent>60:
                print("Name:",self.name,"Roll number",self.roll_no," Passed with First class")
            elif percent<60 and percent>40:
                print("Name:",self.name,"Roll number",self.roll_no," Passed with Second Class")
        else:
            print("Failed,Failed in subjects:")
            for i in range(len(fail_subject)):
                print(fail_subject[i][1])
while(True):
    st = Student()
    #print("Name", st.name, "Roll no.", st.roll_no)
    st.check_marks(st.sub1, st.sub2, st.sub3, st.sub4, st.sub5,st.sub6)
    ch=input("Do you wish to continue Y/N?")
    if(ch=='n' or ch=='N'):
        break

2.Write a python program to create a class Employee whose objects have properties namely: Name, Id, Salary, Tax and Total Salary. Take user input to fill in the fields.  Deduct Tax from Total Salary to get Salary. If Total Salary > 25000, tax = 10%, 25000<= Total Salary< 15000, Tax = 5%. If Total Salary <= 15000, then no tax.Display the Employee id, name and salary together.
class Employee:
    def __init__(self):
        self.name=input("Enter your name")
        self.id=int(input("Enter your ID"))
        self.total_salary=int(input("Enter total salary"))
        self.salary=0

    def calc_salary(self,total_sal):
        if total_sal>=25000:
            tax=(total_sal*10)/100
            self.salary=total_sal-tax
        elif total_sal<25000 and total_sal>=15000:
            tax = (total_sal * 5) / 100
            self.salary = total_sal - tax
        else:
            self.salary=total_sal
emp=Employee()
emp.calc_salary(emp.total_salary)
print("Name:",emp.name,"Id:",emp.id,"Salary",emp.salary)

3. Write a python program to read contents of a file and display them with and without punctuation marks. Store it in another file.
import pickle
f=open('demo.txt','w')
n=int(input('How many lines in File?'))
print('Enter Lines of your Choice: ')
for i in range(n):
    f.write(input())
    f.write('\n')

f.close()
f=open('demo.txt','r')
print('Your File with Punctuation Marks will look like: ')
print(f.read())
print('Without Punctuation, your file will look like this: ')

f2=open('democopy.txt','w+')
with open("demo.txt") as fileobj:
    for line in fileobj:  
        for ch in line:
            if ch.isalnum() or ch==' ' or ch=='\n':
#                 print(ch,end='')
                f2.write(ch)

f2.seek(0,0)
print(f2.read())
f.close()
f2.close()

4.Write a python program to implement a student class having object properties as name, rollno, marks. Take input of 5 students from the user. Store it in a file and display the contents of the file one by one.
import pickle
class Student:
    def __init__(self):
        self.name=input("Enter your name")
        self.roll_number=int(input("Enter your roll_number"))
        self.marks1=int(input("Enter your marks in subject 1"))
        self.marks2 = int(input("Enter your marks in subject 2"))
        self.marks3 = int(input("Enter your marks in subject 3"))

    def display(self):
        print("Name:",self.name,"Roll_number:",self.roll_number,"Marks1",self.marks1,"Marks2",self.marks2,"Marks3",self.marks3)

with open("Students.txt","a+b") as f:
    n=1
    while n<=5:
        st=Student()
        pickle.dump(st,f)
        n=n+1
    print("Reading the contents of file:")
    f.seek(0,0)
    while 1:
        try:
            temp=pickle.load(f)
            temp.display()
        except EOFError:
            print("End of file")
            break

5.Write a python program to draw scenery with a house using tkinter.
from tkinter import *
root=Tk()
c=Canvas(root,height=500,width=500,bg="light blue")
c.pack()
c.create_line(0,400,500,400)
c.create_rectangle(300,300,400,400,fill="wheat",activefill="red")
c.create_polygon(300,300,350,230,400,300,fill="wheat",activefill="red",outline="black")
c.create_arc(5,350,100,450,start=0,extent=180,fill="green")
c.create_arc(100,350,195,450,start=0,extent=180,fill="green")
c.create_arc(195,350,300,450,start=0,extent=180,fill="green")
c.create_arc(400,350,500,450,start=0,extent=180,fill="green")
c.create_oval(100,50,200,150,fill="yellow",outline="orange",width=2)
c.create_text(350,350,text="Home",font=("Times",13,"bold"))
'''img=PhotoImage(file="joker")
c.create_image(500,0,image=img,anchor=NE)
‘’’
root.mainloop()


6. Write a python program to create a login form using tkinter. It should display the username upon successful login and clear details when “reset” button is pressed.

from tkinter import *
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_1 = Label(root, text="Enter your username",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)


label_2 = Label(root, text="Enter your password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_4 = Label(root, text="",width=20,font=("bold", 10))
label_4.place(x=150,y=250)

label_5 = Label(root, text="",width=20,font=("bold", 10))
label_5.place(x=150,y=300)

label_6 = Label(root, text="",width=20,font=("bold", 10))
label_6.place(x=150,y=325)

def login():
    label_4["text"]=entry_1.get()
    #label_5["text"]=entry_2.get()
    label_5.config(text=entry_2.get())
    label_6.config(text="Login Successful")
def reset():
    label_4["text"]=""
    label_5["text"] = ""
    label_6.config(text="")
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
b1=Button(text="Login",command= login).place(x=100,y=350)
b2=Button(text="RESET",command= reset).place(x=300,y=350)
root.mainloop()

7. Write a python program to change the background of a frame using four colour buttons placed at four corners of the frame
from tkinter import *
r=Tk()
r.title("Change Bg")
f=Frame(r,width=400,height=400,bg='ghost white')
f.grid()
f.propagate(0)
def handle(x):
    if x=='red':
        f['bg']='red'
    elif x=='blue':
        f['bg'] = 'blue'
    elif x=='green':
        f['bg'] = 'green'
    elif x=='yellow':
        f['bg'] = 'yellow'

b1=Button(f,text='Red',bg='white',fg='black',command=lambda:handle('red'))
b1.place(x=5,y=5)

b1=Button(f,text='blue',bg='white',fg='black',command=lambda:handle('blue'))
b1.place(x=350,y=5)

b1=Button(f,text='green',bg='white',fg='black',command=lambda:handle('green'))
b1.place(x=5,y=360)

b1=Button(f,text='yellow',bg='white',fg='black',command=lambda:handle('yellow'))
b1.place(x=350,y=360)
r.mainloop()

8.Write a python program to develop a Multiple Choice Quiz which displays a message of success when correct option is selected by the user. (Hint: Use Radiobutton)
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Quiz")

info_label=ttk.Label(root, text='Select the correct option')
info_label.grid(row=0,column=0)

# question1 label
que1_label=ttk.Label(root, text='2+3= ?')
que1_label.grid(row=1, column=0, columnspan=3, sticky=tk.W)

# question 1 options
usertype=tk.IntVar()

radiobtn1=ttk.Radiobutton(root, text='1', value=1, variable=usertype)
radiobtn1.grid(row=2, column=0)

radiobtn2=ttk.Radiobutton(root, text='4', value=4,variable=usertype)
radiobtn2.grid(row=3, column=0)

radiobtn3=ttk.Radiobutton(root, text='5', value=5, variable=usertype)
radiobtn3.grid(row=4, column=0)

radiobtn4=ttk.Radiobutton(root, text='6', value=6, variable=usertype)
radiobtn4.grid(row=5, column=0)

output_label=ttk.Label(root)
output_label.grid(row=8, column=0, sticky=tk.W)

def action():
    if usertype.get() == 5:
        output_label.config(text='Success!!!')
    else:
        output_label.config(text='Wrong answer')

submit_button= ttk.Button(root, text='Submit', command=action)
submit_button.grid(row=7, column=0, sticky=tk.W)

def clear():
    output_label.config(text='')

clear_button= ttk.Button(root, text='Answer again', command=clear)
clear_button.grid(row=7, column=1, sticky=tk.W)

root.mainloop()


9.Write a python program to develop a Basket App.  The App allows user to add multiple fruits from the given set of fruits. 
from tkinter import *
r = Tk()
f = Frame(r)
f.pack()
applecount = 0


def acount(x):
    global applecount
    if x == 'add':
        applecount = applecount + 1
        l1.config(text=applecount)
    elif x == 'sub':
        applecount = applecount - 1
        if applecount < 0:
            l1.config(text='You cant choose fruits in negative quatities')
        else:
            #applecount = applecount - 1
            l1.config(text=applecount)


Applelabel = Label(f, text='Apples')
Applelabel.pack()
add1 = Button(f, text='+', command=lambda: acount('add'))
add1.pack()
sub1 = Button(f, text='-', command=lambda: acount('sub'))
sub1.pack()
l1 = Label(f)
l1.pack()

mangocount = 0


def mcount(x):
    global mangocount
    if mangocount < 0:
        l2.config(text='You cant choose fruits in negative quatities')
    else:
        if x == 'add':
            mangocount = mangocount + 1
            l2.config(text=mangocount)
        elif x == 'sub':
            mangocount = mangocount - 1
            if mangocount < 0:
                l2.config(text='You cant choose fruits in negative quatities')
            else:
                #mangocount = mangocount - 1
                l2.config(text=mangocount)


mangolabel = Label(f, text='Mango')
mangolabel.pack()
add2 = Button(f, text='+', command=lambda: mcount('add'))
add2.pack()
sub2 = Button(f, text='-', command=lambda: mcount('sub'))
sub2.pack()
l2 = Label(f)
l2.pack()

orangecount = 0


def ocount(x):
    global orangecount
    if x == 'add':
        orangecount = orangecount + 1
        l3.config(text=orangecount)
    elif x == 'sub':
        orangecount = orangecount - 1
        if orangecount < 0:
            l3.config(text='You cant choose fruits in negative quatities')
        else:
            #orangecount = orangecount - 1
            l3.config(text=orangecount)


orangelabel = Label(f, text='Orange')
orangelabel.pack()
add3 = Button(f, text='+', command=lambda: ocount('add'))
add3.pack()
sub3 = Button(f, text='-', command=lambda: ocount('sub'))
sub3.pack()
l3 = Label(f)
l3.pack()

r.mainloop()

10.Write a python program which displays formula of a geometrical  shape when the shape is active. Take square, triangle, circle and rectangle as the four shapes.
from tkinter import *
r=Tk()
c=Canvas(r,width=500,height=500)
c.pack()

def formula():
    print('Square!!!!')
c.create_rectangle(10,10,110,110,fill='red')
c.create_text(22,45,text='Area=\nside x side',anchor='w',fill='red',activefill='black')
c.create_rectangle(120,10,250,110,fill='lightblue')
c.create_text(122,45,text='Area=\nlength x breadth',anchor='w',fill='lightblue',activefill='black')
c.create_polygon(260,110,310,10,360,110,fill='lightgreen')
c.create_text(300,75,text='Area\n=\n0.5 \nx base \nx height',anchor='w',fill='lightgreen',activefill='black')
c.create_oval(370,10,470,110,fill='yellow')
c.create_text(375,50,text='Area=\n3.14 X radius X \nradius',anchor='w',fill='yellow',activefill='black')

r.mainloop()

11. circle calculation
from tkinter import *
r=Tk()
r.geometry('400x400+100+100')
r.title("Area Calculation")

def cir():
    rad=txtlab1.get()
    area=(3.142)*int(rad)*int(rad)
    txtlab3.delete(0,END)
    txtlab3.insert(END, area)

frame=Frame(r)
frame.grid()
butframe=Frame(frame,height=100,width=400,bd=2,bg="cadet blue",padx=10,pady=10)
butframe.pack(side=BOTTOM)
data=Frame(frame,height=300,width=400,bd=2,bg="ghost white",padx=10,pady=10)
data.pack(side=TOP)
but1=Button(butframe,height=5,width=7,text='Calculate',relief=RIDGE,bg="ghost white",padx=10,pady=10,command= cir)
but1.grid(row=0,column=0)

lab1=Label(data,height=3,width=7,text='Radius',bg="ghost white",relief=RIDGE)
lab1.grid(row=0,column=0)
txtlab1=Entry(data,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab1.grid(row=0,column=1)

txtlab3=Entry(butframe,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab3.grid(row=2,column=0)

r.mainloop()

12. square calculation
from tkinter import *
r=Tk()
r.geometry('400x400+100+100')
r.title("Area Calculation")

def squ():
    side=txtlab1.get()
    area=int(side)*int(side)
    txtlab3.delete(0,END)
    txtlab3.insert(END, area)

frame=Frame(r)
frame.grid()
butframe=Frame(frame,height=100,width=400,bd=2,bg="cadet blue",padx=10,pady=10)
butframe.pack(side=BOTTOM)
data=Frame(frame,height=300,width=400,bd=2,bg="ghost white",padx=10,pady=10)
data.pack(side=TOP)
but1=Button(butframe,height=5,width=7,text='Calculate',relief=RIDGE,bg="ghost white",padx=10,pady=10,command=squ)
but1.grid(row=0,column=0)

lab1=Label(data,height=3,width=7,text='Side',bg="ghost white",relief=RIDGE)
lab1.grid(row=0,column=0)
txtlab1=Entry(data,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab1.grid(row=0,column=1)

txtlab3=Entry(butframe,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab3.grid(row=2,column=0)

r.mainloop()


13. rectangle calculation
from tkinter import *
r=Tk()
r.geometry('400x400+100+100')
r.title("Area Calculation")

def rec():
    len=txtlab1.get()
    bred=txtlab2.get()
    area=int(bred)*int(len)
    txtlab3.delete(0,END)
    txtlab3.insert(END, area)

frame=Frame(r)
frame.grid()
butframe=Frame(frame,height=100,width=400,bd=2,bg="cadet blue",padx=10,pady=10)
butframe.pack(side=BOTTOM)
data=Frame(frame,height=300,width=400,bd=2,bg="ghost white",padx=10,pady=10)
data.pack(side=TOP)
but1=Button(butframe,height=5,width=7,text='Calculate',relief=RIDGE,bg="ghost white",padx=10,pady=10,command=rec)
but1.grid(row=0,column=0)

lab1=Label(data,height=3,width=7,text='Length',bg="ghost white",relief=RIDGE)
lab1.grid(row=0,column=0)
txtlab1=Entry(data,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab1.grid(row=0,column=1)
lab2=Label(data,height=3,width=7,text='Breadth',bg="ghost white",relief=RIDGE)
lab2.grid(row=1,column=0)
txtlab2=Entry(data,width=10,textvariable='name',font=('arial','20','bold'),relief=RIDGE)
txtlab2.grid(row=1,column=1)

txtlab3=Entry(butframe,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab3.grid(row=2,column=0)

r.mainloop()


14.Triangle Calculation
from tkinter import *
r=Tk()
r.geometry('400x400+100+100')
r.title("Area Calculation")

def tri():
    base=txtlab1.get()
    height=txtlab2.get()
    area=(1/2)*int(base)*int(height)
    txtlab3.delete(0,END)
    txtlab3.insert(END, area)

frame=Frame(r)
frame.grid()
butframe=Frame(frame,height=100,width=400,bd=2,bg="cadet blue",padx=10,pady=10)
butframe.pack(side=BOTTOM)
data=Frame(frame,height=300,width=400,bd=2,bg="ghost white",padx=10,pady=10)
data.pack(side=TOP)
but1=Button(butframe,height=5,width=7,text='Calculate',relief=RIDGE,bg="ghost white",padx=10,pady=10,command=tri)
but1.grid(row=0,column=0)

lab1=Label(data,height=3,width=7,text='Height',bg="ghost white",relief=RIDGE)
lab1.grid(row=0,column=0)
txtlab1=Entry(data,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab1.grid(row=0,column=1)
lab2=Label(data,height=3,width=7,text='Width',bg="ghost white",relief=RIDGE)
lab2.grid(row=1,column=0)
txtlab2=Entry(data,width=10,textvariable='name',font=('arial','20','bold'),relief=RIDGE)
txtlab2.grid(row=1,column=1)

txtlab3=Entry(butframe,width=10,font=('arial','20','bold'),relief=RIDGE)
txtlab3.grid(row=2,column=0)

r.mainloop()



15.Write a python program to determine whether the string input by the user is a palindrome or not. The input should be taken from the user on a UI and the output should be displayed on the UI
from tkinter import *
from tkinter import ttk

root=Tk()
root.configure(background="powder blue")
root.title("To check string is pallindrome or not")
root.geometry("500x400")

l=ttk.Label(root,text="Enter string", background="powder blue", font=("arial",14,"bold"))
l.grid(row=0, column=0, sticky=W)

l_var=StringVar()
l_entry=ttk.Entry(root, textvariable=l_var, font=("arial",14,"bold"), background="powder blue", width=20)
l_entry.grid(row=0, column=1, padx=20,sticky=W)


def action():
    s=l_var.get()
    p=s[::-1] #reverse of string is stored in p
        
    for (k,q) in zip(s,p):
        flag=0
        if k!=q:
            flag=1
            break

    if flag==0:
        l2=ttk.Label(root,text="PALLINDROME", background="powder blue", font=("arial",14,"bold"))
        l2.grid(row=5, column=0, sticky=W)

    if flag==1:
        l2=ttk.Label(root,text=" NOT PALLINDROME", background="powder blue", font=("arial",14,"bold"))
        l2.grid(row=5, column=0, sticky=W)
check=Button(root, command=action,font=("arial",12,"bold"), text="CHECK")
check.grid(row=3,column=0,sticky=W)

root.mainloop()

16. Develop a UI to implement addition and subtraction of two numbers taken as input from the user.UI should display sum of the numbers when “ADD” button is clicked and should display its subtraction when “SUB” button is clicked.
from tkinter import *
from tkinter import ttk

r=Tk()
r.title("Add subtract")

label1=ttk.Label(r,text="Enter first number")
label1.grid(row=1,column=2)

entry1=ttk.Entry(r)
entry1.grid(row=1,column=5)

label2=ttk.Label(r,text="Enter second number")
label2.grid(row=2,column=2)

entry2=ttk.Entry(r)
entry2.grid(row=2,column=5)

label3=ttk.Label(r,text="")
label3.grid(row=3,column=2)

def add():
    label3.config(text='')
    var = str(int(entry1.get()) + int(entry2.get()))
    label3.config(text=("Sum is "+var))

def subtract():
    label3.config(text='')
    var = str(int(entry1.get()) - int(entry2.get()))
    label3.config(text=("Difference is "+var))

def clear():
    label3.config(text="")
    entry1.delete(0,'end')
    entry2.delete(0, 'end')
button1=ttk.Button(r,text="Add",command=add)
button1.grid(row=8,column=2)

button3=ttk.Button(r,text="Subtract",command=subtract)
button3.grid(row=10,column=2)

button2=ttk.Button(r,text="Clear",command=clear)
button2.grid(row=12,column=2)
r.mainloop()



18. Write a python program to add multiple employee records in the employee table having columns. EmpId     EmpName      Basic     HRA    DA    PF      EmpSalary
Calculate the gross salary and display it for all the employees
import sqlite3
conn = sqlite3.connect('Employee_detail1.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Employee (Eno int,Ename varchar,Basic float,HRA float,DA float,PF float,Dno int,Dname varchar )')

while True:
    print("1. New entry\n2. View details\n3. Gross Salary ")
    ch = int(input("Enter decision [1/2/3]: "))
    if ch == 1:
        n = int(input("Enter no of Employees"))
        for i in range(n):
            Eno = int(input("Enter Id of Employee" + str(i + 1) + ":"))
            Ename = input("Enter Employee Name" + str(i + 1) + ":")
            Basic = float(input("Enter Salary of employee" + str(i + 1) + ":"))
            HRA = 0.1 * Basic
            DA = 0.5 * Basic
            PF = 0.05 * Basic
            Dno = int(input("Enter Department No" + ":"))
            Dname = input("Enter Department Name" + ":")
            cursor = conn.cursor()
            tup1 = (Eno, Ename, Basic, HRA, DA, PF, Dno, Dname)
            query1 = ('INSERT INTO Employee (Eno,Ename,Basic,HRA,DA,PF,Dno,Dname) VALUES("%d","%s","%f","%f","%f","%f","%d","%s")')
            cursor.execute(query1 % tup1)
            conn.commit()

    elif ch == 2:
        cursor.execute("SELECT * FROM Employee")
        print(cursor.fetchall())
    elif ch == 3:
        print("Gross Salary")
        cursor.execute("SELECT Ename,(Basic+HRA+DA+PF) As Gross_sal from Employee GROUP BY Ename")
        print(cursor.fetchall())
    else:
        break


19, 20, 21. Write a python program to add multiple and display all the employee records in the employee table having columns 
EmpId     EmpName     EmpDept     EmpSalary      Experience
Write a python program to increase employee salary by 10%  in the employee table having columnsEmpId     EmpName      EmpDept      EmpSalary      Experience

import sqlite3
conn=sqlite3.connect(database='Employee.db')
c=conn.cursor()
while True:
    choice=int(input("Choose an Option: \n1.Insert\t2.View\t3.Increase Salary\t4.Exit\n"))
    if choice==1:
        c.execute("create table if not exists Employee(EmpId int primary key, EmpName varchar(30),EmpDept varchar(30),EmpSalary int,Experience varchar(30))")
        name=input('Name:')
        eid=int(input('ID:'))
        dep=input('Department:')
        sal=int(input('Salary:'))
        ep=input('Experience:')
        qi="insert into Employee(EmpId , EmpName,EmpDept,EmpSalary,Experience) values ('%d','%s','%s','%d','%s')"
        c.execute(qi%(eid,name,dep,sal,ep))
        conn.commit()
        
        
    if choice ==2:
        qv="select * from Employee"
        c.execute(qv)
        print(c.fetchall())
        
        
    if choice ==3:
        up_id=int(input('Enter the ID of Employee '))

        
        qu="update Employee set EmpSalary= 1.1*EmpSalary where EmpId='%d' "
        c.execute(qu%(up_id))
        conn.commit()
        
        
    if choice ==4:
        break
        
conn.commit()  #Commits the changes to database
conn.close() #Closes the database connection



CALCULATOR(NOT IN QB)
from tkinter import *
r=Tk()
r.geometry("300x400+100+100")
r.title("Calculator")
frame=Frame(r)
frame.pack()

###functions
def equals():
    fetch=txt.get()
    try:
        # evaluate the expression using the eval function
        value=eval(fetch)
    except SyntaxError or NameError:
        txt.delete(0, END)
        txt.insert(0, 'Invalid Input!')
    else:
        txt.delete(0, END)
        txt.insert(0, value)
def action(var):
    txt.insert(END, var)

def clearAC():
    txt.delete(0, END)

def dele():
    e = txt.get()[:-1]
    txt.delete(0, END)
    txt.insert(0, e)

###display field
txt=Entry(frame,font=('arial','12'))
txt.grid(row=0,column=0,columnspan=6,pady=3,padx=10)
txt.focus_set()

####Buttons
b1=Button(frame,text='AC',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=clearAC)
b1.grid(row=2,column=2)
b1=Button(frame,text='C',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=clearAC)
b1.grid(row=2,column=3)
b1=Button(frame,text='Del',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=dele)
b1.grid(row=2,column=4)
b1=Button(frame,text='0',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('0'))
b1.grid(row=6,column=1)
b1=Button(frame,text='1',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('1'))
b1.grid(row=5,column=0)
b1=Button(frame,text='2',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('2'))
b1.grid(row=5,column=1)
b1=Button(frame,text='3',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('3'))
b1.grid(row=5,column=2)
b1=Button(frame,text='4',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('4'))
b1.grid(row=4,column=0)
b1=Button(frame,text='5',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('5'))
b1.grid(row=4,column=1)
b1=Button(frame,text='6',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('6'))
b1.grid(row=4,column=2)
b1=Button(frame,text='7',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('7'))
b1.grid(row=3,column=0)
b1=Button(frame,text='8',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('8'))
b1.grid(row=3,column=1)
b1=Button(frame,text='9',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('9'))
b1.grid(row=3,column=2)
b1=Button(frame,text='+',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('+'))
b1.grid(row=3,column=3)
b1=Button(frame,text='-',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('-'))
b1.grid(row=3,column=4)
b1=Button(frame,text='*',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('*'))
b1.grid(row=4,column=3)
b1=Button(frame,text='/',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('/'))
b1.grid(row=4,column=4)
b1=Button(frame,text='%',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('%'))
b1.grid(row=6,column=2)
b1=Button(frame,text='.',height=2,width=5,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=lambda:action('.'))
b1.grid(row=6,column=0)
b1=Button(frame,text='=',height=5,width=10,padx=1,pady=1,bg='Ghost white',relief=RIDGE,command=equals)
b1.grid(row=5,column=3,rowspan=2,columnspan=2)

r.mainloop()
