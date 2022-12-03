import streamlit as st
from view.user.create import create
# from controller.train import create_table
# from view.usee.delete import delete
from view.user.read import read_user
from view.user.update import update_user
from view.page.create import create_u_page,create_sub_page,add_page_collaborators
from view.user.delete import delete as delete_user
import view.page.read as page_read
from view.page.delete import delete as delete_page
from view.page.delete import delete_page_collaborators
from view.page.update import add_content
import view.subscription.create as create_sub
import view.subscription.read as read_sub
from controller.user import view_only_names

def user_view():
    domains=["Page","User","Subscription"]
    selected_domain=st.sidebar.selectbox("Domain",domains)
    
    # create_table()
    if selected_domain == "User":
        st.subheader("Create Your Account: ")
        create()
        st.subheader("You")
        read_user()
        st.subheader("Update Your Details")
        update_user()
        st.subheader("Delete Your Account")
        delete_user()
        
    elif selected_domain =="Page":
        menu=["Create STD Page","Create Premium Page","View Page"]
        selected_menu=st.sidebar.selectbox("Menu",menu)
        if(selected_menu=="Create STD Page"): 
            st.subheader("Create Standard Page")
            create_u_page()
        elif(selected_menu=="Create Premium Page"):
            st.subheader("Create Premium Page")
            create_sub_page()
        elif(selected_menu=="View Page"):
            list_of_users = [i[0] for i in view_only_names()]
            selected_user = st.selectbox("Owner User", list_of_users,key="main_subpage")
            if(selected_user):
                st.subheader("All Pages")
                page_read.read(selected_user)
                st.subheader("Collaborated Pages")
                page_read.read_collab(selected_user)
                st.subheader("Add/Edit Content")
                add_content(selected_user)
                st.subheader("View Collaborators")
                page_read.display_collaborators(selected_user)
                st.subheader("Add Collaborators")
                add_page_collaborators(selected_user)
                st.subheader("Remove Collaborator")
                delete_page_collaborators(selected_user)
                st.subheader("Delete page")
                delete_page(selected_user)
        
    elif selected_domain=="Subscription":
        st.subheader("Create Subscriptions")
        create_sub.create()
        st.subheader("View User Subscription")
        read_sub.read()
         
        
