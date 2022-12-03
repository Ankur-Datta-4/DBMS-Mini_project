-- CREATING USERS

-- USER 1
INSERT INTO USER(email,fname,lname,photoURL,password) VALUES ("jessicapearson@suits.in","jessica","pearson",
"https://www.tvguide.com/a/img/hub/2018/04/26/b631e23f-addc-42ed-bfc3-76cc139215a0/180425-suits-gina-torres.jpg","mypassword");

-- USER 2
INSERT INTO USER(email,fname,lname,photoURL,password) VALUES ("harveyspectre@suits.in","harvey","spectre",
"https://theenemyofaverage.com/wp-content/uploads/2021/09/blog-post-featured-image-harvey-specter-quotes.jpeg","myharvey0699");

-- USER 3
INSERT INTO USER(email,fname,lname,photoURL,password) VALUES ("mikeross@suits.in","mike","ross",
"https://theenemyofaverage.com/wp-content/uploads/2021/09/blog-post-featured-image-mike-ross-quotes.jpeg","mikerachel098");

-- CREATING PAGE

-- USER PAGE
INSERT INTO PAGE(title,content,page_type,parentPageId,creatorId)
VALUES ("my-first-page","This is jessicas first page","database",NULL,1);

INSERT INTO PAGE(title,content,page_type,parentPageId,creatorId)
VALUES ("my-second-page","This is jessicas second page","normal",NULL,1);

INSERT INTO PAGE(title,content,page_type,parentPageId,creatorId)
VALUES ("folsom-foods","This doc is about folsom-foods of harvey","normal",NULL,2);

INSERT INTO PAGE(title,content,page_type,parentPageId,creatorId)
VALUES ("housing court","I lost in housing court-mike","normal",NULL,3);

-- CREATE COLLABORATOR
INSERT INTO Collaborator(userId,pageId) VALUES (1,3);

-- CREATE SUBSCRIPTION
DELIMITER &&
CREATE PROCEDURE add_subscription(IN paymentIdx VARCHAR(191),IN currencyx VARCHAR(191),IN userIdx INT, IN tier_namex VARCHAR(191), 
 IN tier_pricex INT, IN validity_daysx INT, IN amountx INT)
BEGIN
    DECLARE subscriptionId INT;
    SELECT subscriptionId from SUBSCRIPTION,TIER,USER WHERE
     subscription.id=tier.subscriptionId AND user.id=subscription.userId AND
      (CURDATE()+interval validity_days day)>CURDATE() AND user.id=2;
    IF subscriptionId == 0 THEN
    -- create new one
        INSERT INTO SUBSCRIPTION(userId) VALUES(userIdx);
        SELECT id INTO subscriptionId FROM subscription WHERE userId=userIdx;
        INSERT INTO TRANSACTION(paymentId,amount,currency,subscriptionId) VALUES(paymentIdx,amountx,currency,subscriptionId);
        INSERT INTO TIER(subscriptionId,Tier_name,Tier_price,validity_days) VALUES(subscriptionId,tier_namex,tier_pricex,validity_daysx);
    END IF;
END &&

DELIMITER ;

SELECT email from Collaborator,page,user WHERE
 Collaborator.pageId=pageId AND Collaborator.userId=user.id AND page.id=Collaborator.pageId;

SELECT startsAt,userId,subscriptionId,Tier_name,Tier_price,validity_days,createdAt from SUBSCRIPTION,TIER
 WHERE subscription.id=tier.subscriptionId AND subscription.userId=userId;

SELECT page.id AS id,title,content,page_type,publicURL,parentPageId,creatorId,subscribedCreatorId,
createdAt,updatedAt FROM collaborator,page WHERE userId=userIdx AND collaborator.pageId=page.id;


SELECT count(*) AS NumDocuments FROM PAGE WHERE creatorId=userId AND ISNULL(parentPageId);

-- FOR ANALYSIS
SELECT avg(*) as NumDocuments FROM PAGE WHERE ISNULL(parentPageId) GROUP BY creatorId;

SELECT creatorId,avg(*) from PAGE WHERE ISNULL(parentPageId) GROUP BY creatorId;


WITH (SELECT creatorId,count(*) AS numDocs from PAGE WHERE ISNULL(parentPageId) GROUP BY creatorId ) AS temp:
SELECT avg(numDocs) FROM temp;


SELECT avg(numDocs) FROM (SELECT creatorId, count(*) AS numDocs FROM PAGE WHERE ISNULL(parentPageId) GROUP BY creatorId) AS derived;

SELECT max(numDocs) FROM (SELECT creatorId, count(*) AS numDocs FROM PAGE WHERE ISNULL(parentPageId) GROUP BY creatorId) AS derived;

-- FIND user email with maximum transactions
SELECT email,max(num_trans) AS max_transactions FROM
 (SELECT email,count(*) AS num_trans from USER,SUBSCRIPTION,TRANSACTION WHERE user.id=subscription.userId AND
 transaction.subscriptionId=subscription.id GROUP BY user.email) AS email_count;


(SELECT title FROM PAGE WHERE creatorId=userIdx) 
UNION
(SELECT title FROM PAGE WHERE subscribedCreatorId=subscriptionIdx);

(SELECT title FROM PAGE WHERE creatorId={userId})
UNION
(SELECT title FROM collaborator,page WHERE userId={userId} AND collaborator.pageId=page.id);

-- find email of the user, who also own a subscription
(SELECT email FROM USER )
EXCEPT
(SELECT email FROM USER,SUBSCRIPTION WHERE subscription.userId=user.id);

