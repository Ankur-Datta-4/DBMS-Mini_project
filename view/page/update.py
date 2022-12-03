import datetime

import pandas as pd
import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..',"..",'controller')
sys.path.append(controller_path)
# from train import view_all_data, view_only_train_names, get_details, update_train
# from user import view_all_data, view_only_names, view_user, update_user
from page import change_content,view_page,view_all_user_page_titles,view_all_user_pages
from user import view_only_names

def add_content(selected_user):
    result=view_all_user_pages(selected_user)
    
    df = pd.DataFrame(result, columns=['id','title','content','page_type','publicURL','parentPageId','creatorId','subscribedCreatorId','createdAt','updatedAt'])
    with st.expander("View all Pages"):
        st.dataframe(df)
    # list_of_users = [i[0] for i in view_only_titles()]
    all_pages=[i[0] for i in view_all_user_page_titles(selected_user)]
    parent_page=st.selectbox("Choose page",all_pages)
    result_page=view_page(parent_page)
    title=""
    content=""
    if result_page:
        title=result_page[0][1]
        content=result_page[0][2]
    # st.write(selected_result)

    # Layout of Create
    content = st.text_area("content : ",content)

    if st.button("Save changes"):
        change_content(content,title)
        st.success("Successfully updated")

    result2 = view_page(title)
    df2 = pd.DataFrame(result2, columns=['id','title','content','page_type','publicURL','parentPageId','creatorId','subscribedCreatorId','createdAt','updatedAt'])
    with st.expander("On Updation"):
        st.dataframe(df2)

