# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:46:50 2018

@author: laura
"""

#%%

#Add a print_student method in the Student class that prints a 
#line like follows for the object

#Pepe García is a 55 year old student of the MCSDBI masters programme

#Create a list of all 28 Students representing all students in this class.  
#Then iterate over all of them and call print_student on each one to print its description.

class Class:
    
    def __init__(self,name,lastname,age,master):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.master=master
    
    def print_student(self):
        print(str(self.name)+" "+str(self.lastname)+" is a "+str(self.age)+ " old student of the " + str(self.master)+ " masters programme")
    #Alternative:
       #print("{} {} is a {} old student of the {} masters programme".format(self.name,self.lastname,self.age,self.master))
        
def iteratingandprinting(list):
    for classmate in list:
        classmate.print_student()
            
            

#students          
alejandro=Class("Alejandro", "Meneses", "27", "MCSBT")
agata=Class("Agata", "Kaczmarek", "31","MDBI")
anastasia=Class("Anastasia", "Lasunina", "25", "MDBI")
anniken=Class("Anikken", "Barstad Gjeruldsen", "27", "MDBI")
candela=Class("Candela", "Noya", "24", "MDBI")
daniil=Class("Daniil", "Osipov", "21", "MDBI")
david=Class("David", "Barrero Gonzalez", "31", "MCSBT")
edem=Class("Edem", "Francois", "28", "MCSBT")
eduardo=Class("Eduardo", "Paraja", "23", "MDBI")
florian=Class("Florian", "Diegruber", "25", "MCSBT")
hannah=Class("Hannah", "Oldorf", "23", "MCBT")
isabella=Class("Isabella", "Rosenthal", "27", "MDBI")
javier=Class("Javier", "Fernandez", "24", "MCSBT")
lukas=Class("Lukas", "Hauser", "28","MDBI")
leila=Class("Leila", "Tazi", "27", "MCSBT")
laura=Class("Laura", "Kageneck", "23", "MCSBT")
monica=Class("Monica", "Alvarenga","28", "MDBI")
natalie=Class("Natalie", "Cedeno", "26", "MDBI")
octacio=Class("Octavio", "Ramírez", "28", "MDBI")
tancredi=Class("Tancredi", "Bernard", "21", "MCSBT")
yasmine=Class("Yasmine", "Lyagoubi", "23", "MDBI")

#list of students
classmates=[Class("Alejandro", "Meneses", "27", "MCSBT"),
            Class("Agata", "Kaczmarek", "31","MDBI"),
            Class("Anastasia", "Lasunina", "25", "MDBI"),
            Class("Anikken", "Barstad Gjeruldsen", "27", "MDBI"),
            Class("Candela", "Noya", "24", "MDBI"),
            Class("Daniil", "Osipov", "21", "MDBI"),
            Class("David", "Barrero Gonzalez", "31", "MCSBT"),
            Class("Edem", "Francois", "28", "MCSBT"),
            Class("Eduardo", "Paraja", "23", "MDBI"),
            Class("Florian", "Diegruber", "25", "MCSBT"),
            Class("Hannah", "Oldorf", "23", "MCBT"),
            Class("Isabella", "Rosenthal", "27", "MDBI"),
            Class("Javier", "Fernandez", "24", "MCSBT"),
            Class("Lukas", "Hauser", "28","MDBI"),
            Class("Leila", "Tazi", "27", "MCSBT"),
            Class("Laura", "Kageneck", "23", "MCSBT"),
            Class("Monica", "Alvarenga","28", "MDBI"),
            Class("Natalie", "Cedeno", "26", "MDBI"),
            Class("Octavio", "Ramírez", "28", "MDBI"),
            Class("Tancredi", "Bernard", "21", "MCSBT"),
            Class("Yasmine", "Lyagoubi", "23", "MDBI")]