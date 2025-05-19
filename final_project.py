import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as sqltor
from datetime import date, datetime
from prettytable import PrettyTable as pt
from prettytable import DOUBLE_BORDER,SINGLE_BORDER
import fontstyle as fst

pd.set_option("display.max_column",None)
pd.set_option("display.width",500)

con=sqltor.connect(host="localhost",user="root",password="kv123",database="project")

while True:
    main = fst.apply(' TEACHER MANAGEMENT SYSTEM ', 'bold/Georgia/black/Yellow_BG')
    print("\n\n",'*'*10,main,'*'*10,"\n")


     #table

    tbl = pt()
    tbl.set_style(DOUBLE_BORDER)


    # first table
    tbl.field_names = ["PRESS","TO"]

    tbl.add_row([1,'DISPLAY ALL RECORDS'])
    tbl.add_row([2,'DISPLAY SPECIFIC RECORDS BY TEACHER ID'])
    tbl.add_row([3,'INSERT A NEW RECORD'])
    tbl.add_row([4,'UPDATE DATABASE'])
    tbl.add_row([5,'DELETE SPECIFIC RECORDS'])
    tbl.add_row([6,'GRAPHICAL REPRESENTATION'])
    tbl.add_row([7,'EXIT'])
    print(tbl)

    print("\n",'*'*50,"\n")
    ch=int(input("Enter your choice : "))
   
    if ch==1:
        
        print("-"*93)
        # DISPLAYING ALL RECORDS
        query="select * from project;"
        df=pd.read_sql(query,con)
        print('\n','\n')
        if df.empty:         
            txt = fst.apply(' ⚠  No teacher data available, Kindly insert the data ⚠  ', 'bold//white/RED_BG') 
            print(txt)

        else:
            
            tb = pt()
            tb.set_style(SINGLE_BORDER)

            txt = fst.apply(' DISPLAYING ALL RECORDS ', 'bold//black/CYAN_BG')
            
            tb.field_names = [txt]

            tb.add_row([df])
   
            print(tb)
            
        print('\n')
        
   
    elif ch==2:
        
        print("-"*55)
        # DISPLAYING SPECIFICS RECORDS BASED ON TEACHER ID
        id=int(input("Enter teacher id: "))
        query="select * from project where id=%s;" %(id,)
        df=pd.read_sql(query,con)
        print('\n','\n')

        if df.empty:
            
            txt = fst.apply(' ⚠  No teacher data available, Kindly insert the data ⚠  ', 'bold//white/RED_BG') 
            print(txt)
            
            
        else:
            
            tb = pt()
            tb.set_style(SINGLE_BORDER)   
            txt = fst.apply(' DISPLAYING RECORD ', 'bold//black/CYAN_BG') 
            tb.field_names = [txt]        
            tb.add_row([df])
   
            print(tb)
            print()    
        print('\n')

    elif ch==3:
        
        print("-"*55)
        print('\n')
        # INSERTING RECORD IN A TABLE

        id=int(input("Enter teacher id: "))
        name=input("Enter teacher Name:")
        
        #for date 1
        year = int(input('Enter year of birth : '))
        print("year:", year)
        month = int(input('Enter month of birth : '))
        if month>12:
            month=12
        elif month<1:
            month=1
        print("month:", month)
        day = int(input('Enter day of birth : '))
        if day>31:
            day=31
        elif day<1:
            day=1
        print("day:", day)
        date = datetime(year,month,day)

        fname=input("Enter Father's Name:")
        experience=int(input("Enter Years of teaching experience:"))
        post=input("Enter post:")
        salary=int(input("Enter salary:"))

        #for date 2
        
        yyyy = int(input('Enter year of join : '))
        print("year:", yyyy)
        mm = int(input('Enter month of join : '))
        if mm>12:
            mm=12
        elif mm<1:
            mm=1
        print("month:", mm)
        
        dd = int(input('Enter day of join : '))
        if dd>12:
            dd=12
        elif dd<1:
            dd=1
        print("day:", dd)
        
        DoJ = datetime(yyyy,mm,dd)

        query="insert into project values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor=con.cursor()
        cursor.execute(query,(id,name,date,fname,experience,post,salary,DoJ))
        con.commit()

        print()
        print("-"*31,'\n')
        txt = fst.apply(' ✔  Data Added Successfully ✔  ', 'bold//black/GREEN_BG') 
        print(txt)
        print()
        print("-"*31)

  
    elif ch==4:    

        print('-'*93)
        # UPDATING RECORDS IN A TABLE
        query="select * from project;"
        df=pd.read_sql(query,con)
        print('\n','\n')   
        if df.empty:
            txt = fst.apply(' ⚠  No Teacher data available ⚠  ', 'bold//white/RED_BG')
            print(txt)
        else:
            id=int(input("Enter Teacher ID : "))
            salary=int(input("Enter the Salary to be updated : "))
            query="update project set salary=%s where id=%s;"
            cursor=con.cursor()
            cursor.execute(query,(salary,id))
            con.commit()
            print("-"*93)
            print('\n','\n')
            txt = fst.apply(' ✔  Data Updated Successfully ✔  ', 'bold//black/GREEN_BG') 
            print(txt)
            print('\n')
        
    elif ch==5:
        
        print("-"*93)
        # DELETING RECORDS IN A TABLE
        query="select * from project;"
        df=pd.read_sql(query,con) 
        print('\n')  
        if df.empty:
            print('\n') 
            txt = fst.apply(' ⚠  No Teacher data available ⚠  ', 'bold//white/RED_BG')
            print(txt)
            
        else:
            id=int(input("Enter Teacher ID : "))
            query="delete from project where id=%s;"
            cursor=con.cursor()
            cursor.execute(query,(id,))
            con.commit()
            print('\n') 
            txt = fst.apply(' ✔  Data DELETED Successfully ✔  ', 'bold//black/GREEN_BG') 
            print(txt)
            print('\n')
        
       
    elif ch==6:
        
        print("-"*93)
        # GRAPHICAL REPRESENTATION
        query="select * from project;"
        df=pd.read_sql(query,con)
        name=df['name']
        salary=df['salary']

        tb = pt()
        tb.set_style(DOUBLE_BORDER)

        tb.field_names = ["PRESS",'FOR']
         
        tb.add_row([1,'BAR GRAPH'])
        tb.add_row([2,'HISTOGRAM'])
        tb.add_row([3,'STEM GRAPH'])

        print(tb)
 
        graph=int(input('Enter yor choice : '))
        if graph==1:
            plt.bar(name,salary)
        elif graph==2:
            plt.hist(salary,bins=[20000,40000,60000,80000,100000],edgecolor = "black")
        elif graph==3:
            plt.stem(name,salary)
        else :
            print('\n')
            txt = fst.apply(' ⚠  DISPLAYING BAR GRAPH DUE TO INVALID INPUT ⚠  ', 'bold//white/RED_BG')
            print('\n',txt)
            
            plt.bar(name,salary)

        plt.show()
        print('\n')
        
        
    else:
        
        print('\n')
        txt = fst.apply(' Program closed successfully ', 'bold//black/YELLOW_BG')
        print(txt)
        
        print('\n')
        break
