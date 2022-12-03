import mysql.connector
mydb = mysql.connector.connect(
host="localhost", user="root", password="mysql", database="pes1ug20cs537_train"
)

c = mydb.cursor()
c.execute('CREATE DATABASE IF NOT EXISTS pes1ug20cs537_train')
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS TRAIN(train_no INT primary key,train_name VARCHAR(20) DEFAULT NULL,train_type varchar(10) DEFAULT NULL,source varchar(20) DEFAULT NULL,destination varchar(20) DEFAULT NULL,availability varchar(10) DEFAULT NULL)')
    mydb.commit()
    
def add_data(train_no, train_name, train_type,source, destination, availability):
    c.execute(f'INSERT INTO TRAIN(train_no, train_name, train_type, source, destination, availability) VALUES ({train_no},{train_name},{train_type},{source},{destination},{availability})')
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM TRAIN')
    data = c.fetchall()
    return data

def view_only_train_names():
    c.execute('SELECT train_name from TRAIN')
    data = c.fetchall()
    return data

def view_train_id(train_no):
    c.execute(f'SELECT * from TRAIN WHERE train_no={train_no}')
    data=c.fetchall()
    return data

def get_details(name_of_train):
    c.execute('SELECT * FROM train WHERE train_name="{}"'.format(name_of_train))
    data = c.fetchall()
    return data

# def update_train(train_no,train_name, train_type,source, destination, availability):
#     c.execute(f'UPDATE TRAIN SET train_name={train_name}, train_type={train_type}, source={source}, destination={destination}, availability={availability} WHERE train_no={train_no}')
#     mydb.commit()
#     data=c.fetchall()
#     return data
def update_train(new_train_no, new_train_name, new_train_type, new_source, new_dest, new_available, train_no, train_name, train_type, source, dest, available):
    c.execute("UPDATE train SET train_no=%s, train_name=%s, train_type=%s, source=%s, destination=%s, availability=%s WHERE train_no=%s and train_name=%s and train_type=%s and source=%s and destination=%s and availability=%s",
              (new_train_no, new_train_name, new_train_type, new_source, new_dest, new_available, train_no, train_name, train_type, source, dest, available))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_train(train_name):
    c.execute('DELETE FROM train WHERE train_name="{}"'.format(train_name))
    # c.execute(f'DELETE from train WHERE train_name={train_name}')
    mydb.commit()
    
def auto_populate():
    c.execute("INSERT INTO train (train_no, train_name, train_type, source, destination, availability) VALUES\
        (25261, 'Managaluru Mail', 'Mail', 'Chennai ', 'Mangaluru', 'Yes'),\
        (58451, 'BEN-MAN Express', 'Fast', 'Bengaluru', 'Mangaluru', 'yes'),\
        (62620, 'CHE-BEN Shatabdi', 'Superfast', 'Chennai ', 'Bengaluru', 'No')")
    mydb.commit()