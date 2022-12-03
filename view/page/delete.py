import pandas as pd
import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..',"..",'controller')
sys.path.append(controller_path)
from page import delete_page,view_only_titles,view_all_user_page_titles,view_collaborators_name,remove_collaborators

def delete(selected_user):
    all_pages=[i[0] for i in view_all_user_page_titles(selected_user)]
    selected_page=st.selectbox("Select Page",all_pages)
    if st.button('Delete page?'):
        delete_page(selected_page)

def delete_page_collaborators(selected_user):
    all_pages=[i[0] for i in view_all_user_page_titles(selected_user)]
    page=st.selectbox("Choose Page",all_pages,key="remove-collab")
    list_of_users = [i[0] for i in view_collaborators_name(page)]
    collaborator = st.selectbox("Collaborator", list_of_users)
    if collaborator and st.button("Remove Collaborator"):
        remove_collaborators(page,collaborator)
    