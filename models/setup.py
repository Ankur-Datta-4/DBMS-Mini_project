import mysql.connector
mydb = mysql.connector.connect(
host="localhost", user="root", password="mysql", database="notionproject"
)

cur = mydb.cursor()

def setup_db():    
    with open('index.sql', 'r') as sql_file:
        result_iterator = cur.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            print("Running query: ", res)  # Will print out a short representation of the query
            print(f"Affected {res.rowcount} rows" )

        mydb.commit()  # Remember to commit all your changes!
    print('Successfully created')

setup_db()