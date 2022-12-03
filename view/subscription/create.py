import streamlit as st
import sys
import os 
import pandas as pd

view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..','controller')
sys.path.append(controller_path)
from subscription import create_subscription,view_user_subscriptions
from user import view_only_names
def create():
    col1, col2 = st.columns(2)
    with col1:
        list_of_users = [i[0] for i in view_only_names()]
        email = st.selectbox("User Email", list_of_users)
        paymentId = st.text_input("PaymentId :")        
    with col2:
        tier_name=st.selectbox("Subscription Type: ",["Silver","Gold","Platinum"])
        price=0.0
        validity=0
        if(tier_name=="Silver"):
            st.code("Price : 99",language="markdown")
            st.code("Validity days: 30",language="markdown")
            price=price+99
            validity=validity+30
        elif(tier_name=="Gold"):
            st.code("Price : 299",language="markdown")
            st.code("Validity days: 180",language="markdown")
            price=price+299
            validity=validity+180
        elif(tier_name=="Platinum"):
            st.code("Price : 599",language="markdown")
            st.code("Validity days: 800",language="markdown")
            price=price+599
            validity=validity+800
        

    if st.button("Add A New Subscription"):
        currency="INR"
        create_subscription(paymentId,price,currency,email,tier_name,int(price),validity)
        with st.expander("View Subscriptions"):
            result=view_user_subscriptions(email)   
            df = pd.DataFrame(result, columns=['startsAt','userId','subscriptionId','Tier_name','Tier_price','validity_days','createdAt'])
            st.dataframe(df)
        



