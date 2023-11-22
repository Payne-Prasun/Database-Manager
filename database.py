from rich.console import Console
from rich.theme import Theme
import os as o
import pandas as pd
from tabulate import tabulate
# from pynput.keyboard import Key,Listener

#-------------------------------------------------------------------------------------------
def check(file_name):
    if(o.path.isfile(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))):
        console.print("file {} already exists!".format(file_name),style = "error")
        return 1
    return(create(file_name))

def create(file_name):
    headers = []; values = {}
    console.print("enter headers:\n",style = 'input',end = "_")
    headers = input(" ").split()

    if (len(headers) == 1):
        console.print("header has been sucessfully created!",style="sucess")
    else:
        console.print("headers have been sucessfully created",style="sucess")

    for i in headers:
        console.print("enter values for {} column\n".format(i),style="input",end ="_")
        data = input(" ").split()
        values[i] = data
    df = pd.DataFrame(values)
    # print(df)
    df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)
    console.print("{} csv file is successfully saved.".format(file_name),style = "sucess")
    return 1

def show(file_name):
    while True:
        df = pd.read_csv(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))
        console.print("enter [white]headers(hd)[/] to display headers or [white]data(dt)[/] to print entire database\n",style="input",end="_")
        ch = input(" ")
        if (ch.lower()=='headers' or ch.lower() == 'hd'):
            # df = pd.read_csv(r"{}{}.csv".format(o.path.dirname(__file__),file_name))
            # print(tabulate(df,headers=df.columns.tolist()[1:],tablefmt='outline'))
            for i in df.columns.tolist():
                print("|{}".format(i),end="|")
            print("\n")  
            break
        elif(ch.lower() == "data" or ch.lower() == 'dt'):
            print(tabulate(df,headers=df.columns.tolist(),tablefmt="double_grid"))
            break
            
def edit(file_name):
    while True:
        console.print("enter [white]add[/] to add data or [white]del[/] to delete data\n",style="input",end = "_")
        ch = input(" ")
        if (ch.lower() == 'add'):
            while True:
                console.print("to edit data enter [white]row number column name[/] along with [white]new data[/], or to add a new column or row enter [white]col[/] or [white]row[/] to add a new column or row:\n",end="_", style="input")
                ch2 = input(" ").split()
                # print(ch2)
                if (ch2[0].lower() == 'row' or ch2[0].lower() == 'col'):
                    add_rowcol(ch2,file_name)
                    break
                elif (len(ch2) == 3 ):
                     edit_data(file_name,ch2)
                     break
                else:
                    console.print("please enter correct command!",style='error')
                    continue
                break
        
        elif (ch.lower() == 'del'):
            while True:
                console.print("enter [white]row[/] or [white]col[/] to delete entire row or column or enter [white]row number[/] and [white]column name[/] to delete certain data\n",style="input",end="_")
                ch2 = input(" ").split()
                if (ch2[0].lower() == 'row' or ch2[0].lower() == 'col'):
                    del_rowcol(ch2,file_name)
                    break
                elif(ch2[0].isdigit()):
                    del_data(file_name,ch2)
                    break
                else:
                    console.print("please enter correct command!",style='error')
                    continue
                break

        elif(ch.lower() == 'q' or ch.lower() == 'quit'):
            break
            

def edit_data(file_name,ch2):
     df = pd.read_csv(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))
     row = int(ch2[0]) - 1
     col = ch2[1] 
     df.loc[row,col] = ch2[2]
    #  df.loc[int(ch2[0]),int(ch2[1])] = ch2[2]
     df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)
     while True:
         console.print("data has been sucessfully updated!",style="sucess")
         df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)
         console.print("to continue editing renter data to be edit or enter quit(q) to exit",style="input", end = "_")
         ch3 = input(" ").split()
         if(ch3[0].lower() == 'q' or ch3[0].lower() == 'quit'):
             break
         elif(ch3[0].isnumeric()):
            edit_data(file_name,ch3)
         else:
             console.print("please enter appropriate command!",style="error")
             continue
         
def del_data(file_name,ch2):
    df = pd.read_csv(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))
    row = int(ch2[0]) - 11
    # col = int(ch2[1]) 
    # df.loc[row,col] = None
    df.loc[row,ch2[1]] = None
    console.print("row {} col {} has been set to none".format(ch2[0],ch2[1]),style="sucess")
    df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)
    while True:
        #  console.print("data has been sucessfully updated!",style="sucess")
         console.print("to continue editing renter data to be deleted or enter quit(q) to exit",style="input", end = "_")
         ch3 = input(" ").split()
         if(ch3[0].lower() == 'q' or ch3[0].lower() == 'quit'):
             break
         elif(ch3[0].isnumeric()):
            del_data(file_name,ch3)
         else:
             console.print("please enter appropriate command!",style="error")
             continue

  
def add_rowcol(ch2,file_name):
    df = pd.read_csv(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))
    # console.print("enter col for entering new column or enter row to add new row:",style="input",end = "_")
    # ch = input(" ")
    if(ch2[0].lower() == 'col'):
        console.print("enter new column name:",end="_",style="input")
        col = input(" ")
        console.print("column {} has been created!".format(col),style="sucess")
       
        while True:
            try:
                console.print("enter data for {}".format(col),style="input",end="_")
                data = input(" ").split()
                df[col] = data
            # df.to_csv()
                df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)
                console.print("data has been sucessfully pushed!",style="sucess")
                break
            except:
                console.print("please enter equal number of data!",style="error")
                continue

    else:        # console.
        while True:
            # data = {}
            data = []
            col = 0
            for i in (df.columns.tolist()):
                col = col + 1
                console.print("enter data for {} column".format(i),style="input",end="_")
                value = input(" ")
                data.append(value) 
            # df = df.concat(data,ignore_index = True)
            df.loc[len(df.index)] = data
            console.print("row has been sucessfully added!",style="sucess")
            df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)

            console.print("to keep entering data enter [white]row[/] or [white]q[/] to quit",style="input",end = "_")
            ch = input(" ")
            if (ch.lower() == 'q'):
                break

def del_rowcol(ch2,file_name):
    df = pd.read_csv(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))
    if(ch2[0].lower()=='col'):
        while True:
            console.print("enter column name to be deleted",style="input",end = "_")
            col = input(" ")
            try:
                del df[col]
                console.print("column {} has been sucessfully deleted".format(file_name),style="sucess")
                df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)
                
            except:
                console.print("enter correct column name!",style="error")
                del_rowcol(ch2,file_name)

            console.print("to delete more columns enter name or enter q to quit",style="input")
            ch3 = input(" ") 
                
            if (ch3.lower() == 'q' or ch3.lower() == "quit"):
                break

            del_rowcol(ch3,file_name)
        
    elif(ch2[0].lower()=='row'):
        while True:
            console.print("enter row number to be deleted:",style="input",end="_")
            row = int(input(" "))
            for i in (df.columns.tolist()):
                df.loc[row-1,i] = None

            console.print("{} row has been set to none".format(row),style="sucess")
            df.to_csv("{}/{}.csv".format(o.path.dirname(__file__),file_name),index=False)

            console.print("to keep deleting row enter row number or enter q to quit",style="input",end="_")
            ch3 = input(" ")
            if(ch3.lower() == 'q'):
                break
            

#-------------------------------------------------------------------
#main
custom_theme = Theme({"note":"yellow","sucess":"bold green","error":"bold red","input":"cyan"})
console = Console(theme = custom_theme)

console.print("enter [white]help(hp)[/] for help")
while True:
    console.print("_",end = " ")
    ch = input(" ")
    if (ch.lower() == 'create' or ch.lower() == 'ct' or ch == '1'):
        console.print("enter file name: \n",end = "_" ,style="input")
        # console.print(" ",end ="_", style = "input")
        file_name = input(" ")
        d = check(file_name)
       
        while True:
            console.print("enter [white]show(sh)[/] to display database or [white]edit(ed)[/] to enter edit mod\n",end="_",style="input")
            ch2 = input(" ")
            if (ch2.lower() == 'show' or ch2.lower()== "sh"):
                show(file_name)
                break
            elif (ch2.lower() == 'edit' or ch2.lower() == 'ed'):
                edit(file_name)
                break
            elif (ch2.lower() == 'q' or ch2.lower() == "quit"):
                break
            else:
                console.print("please enter correct command!",style="error")
                continue

        # continue
        continue

    elif (ch.lower()=='q' or ch.lower()=='quit' or ch =='0'):
        break

    elif (ch.lower() == 'show' or ch.lower() == 'sh' or ch == '2'):
        console.print("enter file name: \n",end = "_" ,style="input")
        # console.print(" ",end ="_", style = "input")
        file_name = input(" ")
        if(o.path.isfile(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))):
            show(file_name)
        else:
            console.print("No such file found!",style="error")
            console.print("enter [white]create[/] to create a file with {} name or else enter [white]q[/] to exit:\n".format(file_name),style="input",end="_")
            choice = input(" ")
            if (choice.lower() == 'create' or choice.lower()== 'ct'):
                d = create(file_name)
                # print("fuck my life")
            else:
                continue
        continue

    elif (ch.lower() == 'ed' or ch.lower() == 'edit' or ch == '3'):
        # edit(file_name)
        # continue
        console.print("enter file name:\n",style="input",end ="_")
        file_name = input(" ")
        if(o.path.isfile(r"{}\{}.csv".format(o.path.dirname(__file__),file_name))):
            edit(file_name)
        else:
            console.print("No such file found!",style="error")
            console.print("enter [white]create(ct)[/] to create a file with {} name or else enter [white]q[/] to exit:\n".format(file_name),style="input",end="_")
            choice = input(" ")
            if (choice.lower() == 'create' or choice.lower()== 'ct'):
                d = create(file_name)
                # print("fuck my life")
            else:
                continue
        continue


    else:
        console.print("no such command found!",style="error")
        continue



