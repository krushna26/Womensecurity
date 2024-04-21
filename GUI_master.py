from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Women Security")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('heart.jpg')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image



background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Women Security System", font=('times', 35,'bold'), height=1, width=32,bg="violet Red",fg="Black")
lbl.place(x=300, y=10)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv("D:/Women_Security/route1.csv")



data = data.dropna()

le = LabelEncoder()
data['Status'] = le.fit_transform(data['Status'])
data['Source'] = le.fit_transform(data['Source'])
data['Destination'] = le.fit_transform(data['Destination'])
data['Intermediate1'] = le.fit_transform(data['Intermediate1'])
data['Intermediate2'] = le.fit_transform(data['Intermediate2'])
data['Intermediate3'] = le.fit_transform(data['Intermediate3'])
data['Intermediate4'] = le.fit_transform(data['Intermediate4'])

data.head()

"""Feature Selection => Manual"""
x = data.drop(['Status', 'id'], axis=1)


def Data_Preprocessing():
    data = pd.read_csv("D:/Women_Security/route1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['Status'] = le.fit_transform(data['Status'])
    data['Source'] = le.fit_transform(data['Source'])
    data['Destination'] = le.fit_transform(data['Destination'])
    data['Intermediate1'] = le.fit_transform(data['Intermediate1'])
    data['Intermediate2'] = le.fit_transform(data['Intermediate2'])
    data['Intermediate3'] = le.fit_transform(data['Intermediate3'])
    data['Intermediate4'] = le.fit_transform(data['Intermediate4'])

    """Feature Selection => Manual"""
    x = data.drop(['Status', 'id'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Status']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=80)


def Model_Training():
    data = pd.read_csv("D:/Women_Security/route1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    #data['Status'] = le.fit_transform(data['Status'])
    data['Source'] = le.fit_transform(data['Source'])
    data['Destination'] = le.fit_transform(data['Destination'])
    data['Intermediate1'] = le.fit_transform(data['Intermediate1'])
    data['Intermediate2'] = le.fit_transform(data['Intermediate2'])
    data['Intermediate3'] = le.fit_transform(data['Intermediate3'])
    data['Intermediate4'] = le.fit_transform(data['Intermediate4'])

    """Feature Selection => Manual"""
    x = data.drop(['Status', 'id'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Status']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=1)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as HEART_DISEASE_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"D:/Women_Security/Route_MODEL.joblib")
    print("Model saved as Route_MODEL.joblib")



def call_file():
    import Check_route
    Check_route.test()


def Data_Display():
    columns = ['Source', 'Destination', 'Intermediate1', 'Intermediate2', 'Intermediate3', 'Intermediate4']

    data1 = pd.read_csv('route.csv')

    data1.shape

    data1.shape

    data1.head()

    data1

    data1

    Source = data1.ix[:, 1]
    Destination = data1.ix[:, 2]
    Intermediate1 = data1.ix[:, 3]
    Intermediate2 = data1.ix[:, 4]
    Intermediate3 = data1.ix[:, 5]
    Intermediate4 = data1.ix[:, 6]
   

    display = tk.LabelFrame(root, width=100, height=400, )
    display.place(x=200, y=100)

    tree = ttk.Treeview(display, columns=(
    'Source', 'Destination', 'Intermediate1', 'Intermediate2', 'Intermediate3', 'Intermediate4'))

    style = ttk.Style()
    style.configure('Treeview', rowheight=50)
    style.configure("Treeview.Heading", font=("Tempus Sans ITC", 15, "bold italic"))
    style.configure(".", font=('Helvetica', 15), background="blue")
    style.configure("Treeview", foreground='white', background="black")

    tree["columns"] = ("1", "2", "3", "4", "5", "6")
    tree.column("1", width=50)
    tree.column("2", width=50)
    tree.column("3", width=50)
    tree.column("4", width=50)
    tree.column("5", width=50)
    tree.column("6", width=50)
    

    tree.heading("1", text="Source")
    tree.heading("2", text="Destination")
    tree.heading("3", text="Intermediate1")
    tree.heading("4", text="Intermediate2")
    tree.heading("5", text="Intermediate3")
    tree.heading("6", text="Intermediate4")
    

    treeview = tree

    tree.grid(row=0, column=0, sticky=tk.NSEW)

    print("Data Displayed")
    for i in range(0, 304):
        tree.insert("", 'end', values=(
        Source[i], Destination[i], Intermediate1[i], Intermediate2[i], Intermediate3[i], Intermediate4[i]
        ))
        i = i + 1


check = tk.Frame(root, w=100)
check.place(x=700, y=100)


def window():
    root.destroy()

'''
button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=5, y=170)
'''
button4 = tk.Button(root, foreground="white", background="skyblue", font=("Tempus Sans ITC", 14, "bold"),
                    text="Best Route Prediction", command=call_file, width=25, height=2)
button4.place(x=15, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=15, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
