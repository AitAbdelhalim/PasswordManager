import random 
from  cryptography.fernet import Fernet

'''
def write_key(): 
    key = Fernet.generate_key() 
    with open("key.key", "wb") as key_file:
        key_file.write(key) 
'''

'''
version simplifiée 
def load_key(): 
    file = open("key.key", "rb")
    key= file.read() 
    file.close 
    return key

'''

def load_key(): 
            with open("key.key", "rb") as f: 
                return f.read() 
         

key = load_key() 
fer = Fernet(key)

    

def View(): 
        with open("passowrd.txt", "r") as f: 
            for line in f.readlines(): 
                data = line.rstrip() 
                name, password = data.split("|")
                print ("User : ", name, ", Password : ", fer.decrypt(password.encode()).decode() )
                
                
def Add(): 
        name = input("Account Name : ")
        pwd = input("Password : ")
        
        with open("passowrd.txt", "a") as f: 
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 
                
                
                   


while True: 
        mode = input ("Would you like to add a nex passoword or view existing ones (view, add) press q to quit ? ").lower() 
        
        if mode == "q": 
                break 
        
        if mode == "view": 
            View() 
        elif mode == "add":
            Add() 
        else : 
                print ("Invalid option.") 
                continue 
                
                        

                