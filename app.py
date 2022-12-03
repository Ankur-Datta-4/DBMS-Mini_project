import streamlit as st
from user_access import user_view
from admin_access import admin_view
def main():
    st.title("Notion Infra")
    domains=["User","Admin"]
    selected_domain=st.sidebar.selectbox("Access",domains)
    
    # create_table()
    if selected_domain == "User":
        user_view()
    elif selected_domain =="Admin":
        admin_view()
         
        
if __name__ == '__main__':
    main()

