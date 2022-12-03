import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
host="localhost", user="root", password="mysql", database="notionproject"
)


def create_user(email,password,fname,lname,photoURL):
    c = mydb.cursor()
    c.execute(f'INSERT INTO USER(email,fname,lname,photoURL,password) VALUES ("{email}","{fname}","{lname}","{photoURL}","{password}")')
    mydb.commit()
    
def view_all_data():
    c = mydb.cursor()
    c.execute('SELECT * FROM USER')
    data = c.fetchall()
    return data

def view_only_names():
    c = mydb.cursor()
    c.execute('SELECT email from USER')
    data = c.fetchall()
    return data

def view_premium_only_names():
    c = mydb.cursor()
    
    c.execute('SELECT email from SUBSCRIPTION,USER WHERE user.id=subscription.userId') 
    data = c.fetchall()
    return data

def view_user(email):
    c = mydb.cursor()
    
    c.execute(f'SELECT * from USER WHERE email="{email}"')
    data=c.fetchall()
    return data

    
def update_user(new_email,new_fname,new_lname,new_photoURL,new_password,email):
    c = mydb.cursor()
    
    c.execute(f'UPDATE USER SET email="{new_email}", fname="{new_fname}", lname="{new_lname}", photoURL="{new_photoURL}",password="{new_password}" WHERE email="{email}"')
    mydb.commit()
    data=c.fetchall()
    return data


def delete_user(email):
    c = mydb.cursor()
    try:
        c.execute('DELETE FROM USER WHERE email="{}"'.format(email))
        mydb.commit()
        st.success("Deleted user: {}".format(email))
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))
    
