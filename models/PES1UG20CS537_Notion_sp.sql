DELIMITER &&  
CREATE PROCEDURE get_page_collabs (IN pageIdx INT)  
BEGIN  
    SELECT Collaborator.userId,email,fname,lname,photoURL,joiningDate,Tier_name,subscription.startsAt,validity_days from 
    Collaborator,page,user,subscription,tier WHERE Collaborator.pageId=pageIdx AND Collaborator.userId=user.id
     AND page.id=Collaborator.pageId AND subscription.userId=user.id AND tier.subscriptionId=subscription.id;
END &&  
DELIMITER ;



-- Get emails of collabs

DELIMITER &&  
CREATE PROCEDURE get_page_collabs_cur (IN pageIdx INT, INOUT allEmails varchar(2000) )  
BEGIN  
    DECLARE presentMail varchar(100) DEFAULT "";
    DECLARE finished INTEGER DEFAULT 0;
    DECLARE curEmail CURSOR FOR SELECT email 
    FROM Collaborator,page,user,subscription,tier 
    WHERE Collaborator.pageId=pageIdx AND Collaborator.userId=user.id
    AND page.id=Collaborator.pageId AND subscription.userId=user.id AND tier.subscriptionId=subscription.id;

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND SET finished=1;

    OPEN curEmail;

    getEmail: LOOP
        FETCH curEmail INTO presentMail;
        IF finished=1 THEN
            LEAVE getEmail;
        END IF;
        SET allEmails=CONCAT(presentMail,",",allEmails);
    END LOOP getEmail;

    CLOSE curEmail;
END &&  
DELIMITER ;

SELECT email 
    FROM Collaborator,page,user,subscription,tier 
    WHERE Collaborator.pageId=11 AND Collaborator.userId=user.id
    AND page.id=Collaborator.pageId AND subscription.userId=user.id AND tier.subscriptionId=subscription.id;



DELIMITER &&  
CREATE PROCEDURE get_subscribed_users (INOUT allEmails varchar(2000) )  
BEGIN  
    DECLARE presentMail varchar(100) DEFAULT "";
    DECLARE finished INTEGER DEFAULT 0;
    DECLARE curEmail CURSOR FOR SELECT email from SUBSCRIPTION,USER WHERE user.id=subscription.userId;

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND SET finished=1;

    OPEN curEmail;

    getEmail: LOOP
        FETCH curEmail INTO presentMail;
        IF finished=1 THEN
            LEAVE getEmail;
        END IF;
        SET allEmails=CONCAT(presentMail,",",allEmails);
    END LOOP getEmail;

    CLOSE curEmail;
END &&  
DELIMITER ;
