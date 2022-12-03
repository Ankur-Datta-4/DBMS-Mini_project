import pandas as pd
import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..','controller')
sys.path.append(controller_path)
from page import view_all_pages,view_all_user_pages,view_collaborators,view_only_titles,view_all_user_page_titles,view_collab_page
from user import view_only_names
def read(selected_user):
    # st.write(result)
    # list_of_users = [i[0] for i in view_only_names()]
    # selected_user = st.selectbox("Owner User", list_of_users,key="user-pages")
    if(selected_user):
        result=view_all_user_pages(selected_user)
    
    df = pd.DataFrame(result, columns=['id','title','content','page_type','publicURL','parentPageId','creatorId','subscribedCreatorId','createdAt','updatedAt'])
    with st.expander("View all Pages"):
        st.dataframe(df)

def read_collab(selected_user):
    if(selected_user):
        result=view_collab_page(selected_user)
    
    df = pd.DataFrame(result, columns=['id','title','content','page_type','publicURL','parentPageId','creatorId','subscribedCreatorId','createdAt','updatedAt'])
    with st.expander("View all Pages"):
        st.dataframe(df)
        
def display_collaborators(selected_user):
    all_pages=[i[0] for i in view_all_user_page_titles(selected_user)]
    page=st.selectbox("Choose Page",all_pages,key="collaborators-title-1")
    if(page):
        result=view_collaborators(page)
        df = pd.DataFrame(result, columns=['userId','email','fname','lname','photoURL','joiningDate','Tier_name','startsAt','validity_days'])
        with st.expander("View all Collaborators"):
            st.dataframe(df)
   