import streamlit as st
from view.user.create import create
# from controller.train import create_table
# from view.usee.delete import delete
from view.user.read import read
from view.user.update import update
from view.page.create import create_u_page,create_sub_page,add_page_collaborators
import view.page.read as page_read
from view.user.delete import delete as delete_user
from view.page.delete import delete as delete_page
from view.page.update import add_content
import view.subscription.create as create_sub
import view.subscription.read as read_sub
def admin_view():
    domains=["User","Subscription"]
    selected_domain=st.sidebar.selectbox("Domain",domains)
    
    # create_table()
    if selected_domain == "User":
        menu = ["Add", "View", "Edit", "Remove"]
        choice = st.sidebar.selectbox("Menu", menu)
        
        if choice == "Add":
            st.subheader("Enter User Details:")
            create()
        elif choice == "View":
            st.subheader("View All Users")
            read()
        elif choice == "Edit":
            st.subheader("Update User")
            update()
        elif choice == "Remove":
            st.subheader("Delete User")
            delete_user()
            
    elif selected_domain=="Subscription":
        st.subheader("Create Subscriptions")
        create_sub.create()
        st.subheader("View User Subscription")
        read_sub.read()
        st.subheader("Extend User Subscriptions")
         
        
