import mysql.connector
mydb = mysql.connector.connect(
host="localhost", user="root", password="mysql", database="notionproject"
)
import streamlit as st


c = mydb.cursor()
from user import view_user,view_premium_only_names

def create_subscription(paymentId,amount,currency,email,tier_name,tier_price,validity_days):
    # use transaction
    userId=view_user(email)[0][0]
    try:
        print("Reached")   
        if(not check_if_valid_sub(email)): 
            c.execute(f'INSERT INTO SUBSCRIPTION(userId) VALUES({userId})')
            c.execute(f'SELECT * from SUBSCRIPTION WHERE userId={userId}')
            subscription=c.fetchall()[0]
            c.execute(f'INSERT INTO TRANSACTION(paymentId,amount,currency,subscriptionId) VALUES("{paymentId}",{amount},"{currency}",{subscription[0]})')
            c.execute(f'INSERT INTO TIER(subscriptionId,Tier_name,Tier_price,validity_days) VALUES({subscription[0]},"{tier_name}",{tier_price},{validity_days})')
            mydb.commit()
            st.success("Successfully added subscription: {}".format(email))
            
        else:
            raise Exception("User owns an active subscription")
            
    except mysql.connector.Error as error:
        print('Error occured, rolling back changes')
        print(error)
        mydb.rollback()
        st.exception(error.msg)
    except Exception as e:
        print(e)
        st.exception(RuntimeError(e))
        

## JOIN WITH tier
def view_user_subscriptions(email):
    userId=view_user(email)[0][0]
    c.execute(f"SELECT startsAt,userId,subscriptionId,Tier_name,Tier_price,validity_days,createdAt from SUBSCRIPTION,TIER WHERE subscription.id=tier.subscriptionId AND subscription.userId={userId}")
    data=c.fetchall()
    return data

def view_all_subscriptions():
    c.execute(f'SELECT startsAt,userId,email,subscriptionId,Tier_name,Tier_price,validity_days,createdAt from SUBSCRIPTION,TIER,USER WHERE subscription.id=tier.subscriptionId AND user.id=subscription.userId')
    data=c.fetchall()
    return data
    
def extend_subscription(email,tier_name,tier_price,validity_days):
    ## Create new transaction->Update the tier
    userId=view_user(email)[0][0]
    c.execute(f'SELECT subscriptionId FROM SUBSCRIPTION WHERE userId={userId}')
    subscriptionId=c.fetchall()[0]
    # if(not subscriptionId):
    c.execute(f'UPDATE TIER SET tier_name="{tier_name}",tier_price="{tier_price},validity_days={validity_days} WHERE subscriptionId={subscriptionId}"')

    
def check_if_valid_sub(email):
    subs=view_user_subscriptions(email)
    if(len(subs)):
        userId=subs[0][1]
        c.execute(f"SELECT subscriptionId from SUBSCRIPTION,TIER,USER WHERE subscription.id=tier.subscriptionId AND user.id=subscription.userId AND (CURDATE()+interval validity_days day)>CURDATE() AND user.id={userId}")
        active_sub=c.fetchall()
        if(len(active_sub)):
            return True
    return False 
     
    

