-- know number of pages
DELIMITER $$
CREATE FUNCTION findNumStdDocuments(userId int) RETURNS INT DETERMINISTIC
BEGIN 
    DECLARE NumDocuments int;
    SELECT count(*) into NumDocuments FROM PAGE WHERE creatorId=userId AND ISNULL(parentPageId);
    RETURN NumDocuments;
END$$

DELIMITER ;

-- Trigger while creating page
DELIMITER $$
CREATE TRIGGER validate_std_page_create BEFORE INSERT
ON page FOR EACH ROW
BEGIN
    DECLARE NumDocuments int;
    DECLARE message_text varchar(255);
    IF ISNULL(new.parentPageId) THEN
    IF NOT ISNULL(new.creatorId) THEN
        SELECT count(*) into NumDocuments FROM PAGE WHERE creatorId=new.creatorId AND ISNULL(parentPageId);
        IF NumDocuments+1>4 then 
            SIGNAL SQLSTATE '45000'
            set message_text = 'Upgrade to premium subscription. Cant create';
        END IF;
    END IF;
    END IF;
END$$

DELIMITER ;

-- Trigger to add collaborators: can only add 2 collaborators for a standard page
DELIMITER $$
CREATE FUNCTION findIfPremium(pageId int) RETURNS INT DETERMINISTIC
BEGIN 
    DECLARE isPremium int;
    SELECT ISNULL(creatorId) INTO isPremium FROM PAGE where id=pageId;
    RETURN isPremium;
END$$

DELIMITER ;


-- 


-----
DELIMITER $$
CREATE TRIGGER validate_collaborator_add BEFORE INSERT
ON Collaborator FOR EACH ROW
BEGIN   
    DECLARE NumCollaborators INT;
    SELECT count(*) into NumCollaborators FROM Collaborator WHERE pageId=new.pageId;
    IF NumCollaborators>0 then 
        IF findIfPremium(new.pageId)=0 then 
            SIGNAL SQLSTATE '45000'
            set message_text = 'Upgrade to premium subscription. Cant add more than 1 collaborator to std page';
        END IF;
    END IF;
END$$

DELIMITER ;



