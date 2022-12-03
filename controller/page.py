import streamlit as st
import mysql.connector
mydb = mysql.connector.connect(
host="localhost", user="root", password="mysql", database="notionproject"
)
from user import view_user
from subscription import view_user_subscriptions

c = mydb.cursor()

"""
OPS: 
1. Create page 
    a. Normal page: free page
    b. Subscription page
    c. Subpage
CREATE trigger--> If no. of free pages > 5: reject creation
2. Get all pages
3. Edit page
4. Add collaborator
"""
def create_page(title,content,page_type,parentPageId,creatorId,subscribedCreatorId):
    try:
        c.execute(f'INSERT INTO PAGE(title,content,page_type,parentPageId,creatorId,subscribedCreatorId) VALUES ("{title}","{content}","{page_type}",{"NULL" if parentPageId==0 else parentPageId},{"NULL" if creatorId==0 else creatorId},{"NULL" if subscribedCreatorId==0 else subscribedCreatorId})')
        mydb.commit()
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback()
        
        
 
def create_user_page(title,content,page_type,parentPageId,creatorId):
    # Add trigger
    try:
        c.execute(f'INSERT INTO PAGE(title,content,page_type,parentPageId,creatorId) VALUES ("{title}","{content}","{page_type}",{"NULL" if parentPageId==0 else parentPageId},{"NULL" if creatorId==0 else creatorId})')
        mydb.commit()
        st.success("Successfully added user page: {}".format(title))
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))
        
        
def create_premium_page(title,content,page_type,parentPageId,subscribedCreatorId):
    try:
        c.execute(f'INSERT INTO PAGE(title,content,page_type,parentPageId,subscribedCreatorId) VALUES ("{title}","{content}","{page_type}",{"NULL" if parentPageId==0 else parentPageId},{"NULL" if subscribedCreatorId==0 else subscribedCreatorId})')
        mydb.commit()
        st.success("Successfully added premium page: {}".format(title))
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))
   
def view_parent_pages():
    c.execute('SELECT * FROM PAGE WHERE parentPageId>0')
    data = c.fetchall()
    return data

def view_all_pages():
    c.execute('SELECT * FROM PAGE')
    data = c.fetchall()
    return data

def view_all_user_pages(email):
    try:
        userId=view_user(email)[0][0]
        subscription=view_user_subscriptions(email)
        if(len(subscription)):
            subscriptionId=subscription[0][2]
            c.execute(f'(SELECT * FROM PAGE WHERE creatorId={userId}) UNION (SELECT * FROM PAGE WHERE subscribedCreatorId={subscriptionId}) UNION (SELECT page.id AS id,title,content,page_type,publicURL,parentPageId,creatorId,subscribedCreatorId,createdAt,updatedAt FROM collaborator,page WHERE userId={userId} AND collaborator.pageId=page.id)')
            data = c.fetchall()
            return data
        else:
            c.execute(f'(SELECT * FROM PAGE WHERE creatorId={userId})')
            data = c.fetchall()
            return data
            
        # Display both premium and standard pages
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))
    except Exception as e:
        st.exception(RuntimeError(f"{e}"))
        
        
def view_only_titles():
    c.execute('SELECT title from PAGE')
    data = c.fetchall()
    return data

def view_all_user_page_titles(email):
    try:
        userId=view_user(email)[0][0]
        subscription=view_user_subscriptions(email)
        if(len(subscription)):
            subscriptionId=subscription[0][2]
            c.execute(f'(SELECT title FROM PAGE WHERE creatorId={userId}) UNION (SELECT title FROM PAGE WHERE subscribedCreatorId={subscriptionId}) UNION (SELECT title FROM collaborator,page WHERE userId={userId} AND collaborator.pageId=page.id)')
            data = c.fetchall()
            return data
        else:
            c.execute(f'(SELECT title FROM PAGE WHERE creatorId={userId})')
            data = c.fetchall()
            return data
            
        # Display both premium and standard pages
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))
    except Exception as e:
        st.exception(RuntimeError(f"{e}"))
   
def view_page(title):
    c.execute(f'SELECT * from PAGE WHERE title="{title}"')
    data=c.fetchall()
    return data

def update_page(new_title,new_content,new_page_type,new_publicURL,title):
    c.execute(f'UPDATE PAGE SET title="{new_title}", content="{new_content}", page_type="{new_page_type}", publicURL="{new_publicURL}" WHERE title="{title}"')
    mydb.commit()
    data=c.fetchall()
    return data

def change_content(new_content, title):
    c.execute(f'UPDATE PAGE SET content="{new_content}" WHERE title="{title}"')
    mydb.commit()
    data=c.fetchall()
    return data

def delete_page(title):
    try:
        c.execute('DELETE FROM PAGE WHERE title="{}"'.format(title))
        mydb.commit()
        st.success("Deleted page: {}".format(title))
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))

def view_collaborators(title):
    try:
        page=view_page(title)
        if(len(page)):
            c.callproc('get_page_collabs',[page[0][0]])
            for result in c.stored_results():
                return(result.fetchall())
    except mysql.connector.Error as error:
        print(error)
        st.exception(RuntimeError(f"{error.msg}"))

def add_collaborators(title,email):
    try:
        userId=view_user(email)[0][0]
        pageId=view_page(title)[0][0]
        c.execute(f'INSERT INTO Collaborator(userId,pageId) VALUES ({userId},{pageId})')
        mydb.commit()
        st.success("Added collaborator: {}".format(email))
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))
    
def view_collaborators_name(title):
    page=view_page(title)
    if(len(page)):
        c.execute(f'SELECT email from Collaborator,page,user WHERE Collaborator.pageId={page[0][0]} AND Collaborator.userId=user.id AND page.id=Collaborator.pageId;')
        return c.fetchall()
    else:
        st.exception(RuntimeError('Couldnt find page'))
        return []
    
def remove_collaborators(title,email):
    try:
        userId=view_user(email)[0][0]
        pageId=view_page(title)[0][0]
        c.execute(f'DELETE FROM Collaborator WHERE userId={userId} AND pageId={pageId}')
        mydb.commit()
        st.success("Removed collaborator: {}".format(email))
    except mysql.connector.Error as error:
        print(error)
        print('Error occured, rolling back changes')
        mydb.rollback() 
        st.exception(RuntimeError(f"{error.msg}"))

def view_collab_page(email):
    # display all the collaborated pages
    userId=view_user(email)[0][0]
    c.execute(f'SELECT page.id AS id,title,content,page_type,publicURL,parentPageId,creatorId,subscribedCreatorId,createdAt,updatedAt FROM collaborator,page WHERE userId={userId} AND collaborator.pageId=page.id')
    return c.fetchall()