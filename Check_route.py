
# def mail():
#     from subprocess import call
#     call(["python3", "mail1.py"])
    
# def gmap():
#     from subprocess import call
#     call(["python3", "display_route_on_gmap.py"])
    
def test():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()
    #root = tk.Tk()
    root.title("Women Security")


    root.geometry("800x850+250+5")
    root.title("Check Route")
    root.configure(background="purple")
    
    Source = tk.StringVar()
    Destination = tk.StringVar()
    Intermediate1 = tk.StringVar()
    Intermediate2 = tk.StringVar()
    Intermediate3 = tk.StringVar()
    Intermediate4 = tk.StringVar()
   
    #===================================================================================================================



    def Detect():
        e1=Source.get()
        print(e1)
        print(type(e1))
        e2=Destination.get()
        print(e2)
        e3=Intermediate1.get()
        print(e3)
        e4=Intermediate2.get()
        print(e4)
        e5=Intermediate3.get()
        print(e5)
        e6=Intermediate4.get()
        print(e6)
        
        
       
        #########################################################################################
        
        from joblib import dump , load
        a1=load('Route_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6]])
        print(v)
        print(type(v))
        if v == 0:
            print("Yes")
            yes = tk.Label(root,text="Root is Safe !\nReport is Generated",background="green",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=300,y=400)
            file = open(r"D:/Women_Security/Report.txt", 'w')
            file.write("-----Report-----\n As per input data and system give safe route."
                       "\n***Kindly Follow Route***"
                    
                    )
            file.close()
            listOfStrings = [e1, e2, e3, e4, e5, e6]

            finalString = "".join(listOfStrings)
            print(finalString)
            if finalString == '11392845':
                 yes = tk.Label(root,text="Route is:- \n Kasarwadi-Dapodi-Bopodi-Khadki-Sancheti-Shivaji_Nagar",background="green",foreground="white",font=('times', 20, ' bold '))
                 yes.place(x=20,y=500)
            elif finalString =='11392637':
                 yes = tk.Label(root,text="Route is:- \n Kasarwadi-Dapodi-Pragati_Nagar-University_Road-Khaire_Vasti-Shivaji_Nagar",background="green",foreground="white",font=('times', 20, ' bold '))
                 yes.place(x=20,y=500)
            elif finalString =='13917362':
                 yes = tk.Label(root,text="Route is:- \n Shivaji Nagar-Khaire_Vasti-University_Road-Pragati_Nagar-Dapodi-Kasarwadi",background="green",foreground="white",font=('times', 20, ' bold '))
                 yes.place(x=20,y=500)

            
            
        else:
            print("No")
            no = tk.Label(root, text="Route unsafe \nDetected", background="red", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=300, y=400)
            file = open(r"D:/21CG136-Women_Security/Women_Security/heart/Report.txt", 'w')
            file.write("-----Report-----\n As per input data and system give unsafe route."    
                    )
            file.close()



    l1=tk.Label(root,text="Source",background="purple",font=('times', 20, ' bold '),width=10,foreground = "white")
    l1.place(x=50,y=1)
    Source=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Source)
    Source.place(x=300,y=1)

    l2=tk.Label(root,text="Destination",background="purple",font=('times', 20, ' bold '),width=10,foreground = "white")
    l2.place(x=50,y=50)
    Destination=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Destination)
    Destination.place(x=300,y=50)

    l3=tk.Label(root,text="Intermediate1",background="purple",font=('times', 20, ' bold '),width=10,foreground = "white")
    l3.place(x=50,y=100)
    Intermediate1=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Intermediate1)
    Intermediate1.place(x=300,y=100)
   
    l4=tk.Label(root,text="Intermediate2",background="purple",font=('times', 20, ' bold '),width=10,foreground = "white")
    l4.place(x=50,y=150)
    Intermediate2=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Intermediate2)
    Intermediate2.place(x=300,y=150)

    l5=tk.Label(root,text="Intermediate3",background="purple",font=('times', 20, ' bold '),width=10,foreground = "white")
    l5.place(x=50,y=200)
    Intermediate3=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Intermediate3)
    Intermediate3.place(x=300,y=200)

    l6=tk.Label(root,text="Intermediate4",background="purple",font=('times', 20, ' bold '),width=10,foreground = "white")
    l6.place(x=50,y=250)
    Intermediate4=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Intermediate4)
    Intermediate4.place(x=300,y=250)

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=20)
    button1.place(x=250,y=300)
    
    # button2 = tk.Button(root,text="Emergency Mail",command=mail,font=('times', 20, ' bold '),width=20)
    # button2.place(x=250,y=400)
    
    # button3 = tk.Button(root,text="Display Google Map",command=gmap,font=('times', 20, ' bold '),width=20)
    # button3.place(x=250,y=500)


    root.mainloop()

