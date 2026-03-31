-- Task 2: Insert or update contact (UPSERT)
-- If user exists -> UPDATE, else -> INSERT

CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
    
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- Task 3: Insert many users with validation
-- Uses LOOP and IF, prints incorrect data

CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;  
BEGIN
    FOR i IN 1..array_length(p_names, 1)
    LOOP
        
        IF p_phones[i] ~ '^\+7[0-9]{10}$' THEN
            
            CALL upsert_contact(p_names[i], p_phones[i]);
        ELSE
            
            RAISE NOTICE 'Invalid phone: % (%)', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;



-- Task 5: Delete contact by name OR phone

CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value; 
END;
$$;