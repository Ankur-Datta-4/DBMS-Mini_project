import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..',"..",'controller')
sys.path.append(controller_path)
from page import create_user_page,view_only_titles,view_page,create_premium_page,add_collaborators,view_all_user_page_titles
from user import view_only_names,view_user,view_premium_only_names
from subscription import view_user_subscriptions
# from database import add_data

def create_u_page():
    # col1 = st.columns(1)
    content = "Hey there! This is a new page"
    page_types=["plain","database"]
    # with col1:
    title = st.text_input("title : ")
    list_of_users = [i[0] for i in view_only_names()]
    selected_user = st.selectbox("Owner User", list_of_users)
    selected_result = view_user(selected_user)
    selected_type=st.selectbox("type",page_types)
    all_pages=[i[0] for i in view_all_user_page_titles(selected_user)]
    temp=[0]
    all_pages=temp+all_pages
    parent_page=st.selectbox("Parent_page",all_pages)
    parent_pageId=0
    creatorId=0
    result_page=view_page(parent_page)
    if(result_page):
        parent_pageId=result_page[0][0]
    if(selected_result):
        creatorId=selected_result[0][0]
    # parent_page = st.number_input("parent page Id")

        
    if st.button("Create Standard Page"):
        create_user_page(title,content,selected_type,parent_pageId,creatorId)
        # create_user(user_email,password,user_fname,user_lname,photoURL)
        # st.success("Successfully added user page: {}".format(title))
        
def create_sub_page():
    # col1 = st.columns(1)
    content = "Hey there! This is a new page"
    page_types=["plain","database"]
    # with col1:
    title = st.text_input("title : ",key="sub-page")
    list_of_users = [i[0] for i in view_premium_only_names()]
    selected_user = st.selectbox("Owner User", list_of_users,key="sub-page3")
    selected_result = view_user_subscriptions(selected_user)
    selected_type=st.selectbox("type",page_types,key="sub-page1")
    all_pages=[i[0] for i in view_only_titles()]
    temp=[0]
    all_pages=temp+all_pages
    parent_page=st.selectbox("Parent_page",all_pages,key="sub-page2")
    parent_pageId=0
    creatorId=0 
    result_page=view_page(parent_page)
   
    if(result_page):
        parent_pageId=result_page[0][0]
    if(selected_result):
        subscriptionId=selected_result[0][2]
    # parent_page = st.number_input("parent page Id")

        
    if st.button("Create Premium Page"):
        create_premium_page(title,content,selected_type,parent_pageId,subscriptionId)

def add_page_collaborators(selected_user):
    all_pages=[i[0] for i in view_all_user_page_titles(selected_user)]
    page=st.selectbox("Choose Page",all_pages,key="collaborators-title")
    list_of_users = [i[0] for i in view_only_names()]
    collaborator = st.selectbox("Add User", list_of_users)
    if st.button("Add Collaborator"):
        add_collaborators(page,collaborator)
    
    