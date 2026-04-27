-- =========================================
-- UPsert contact (Practice 8 dependency)
-- =========================================
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET email = email
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name)
        VALUES (p_name);
    END IF;
END;
$$;


-- =========================================
-- Add phone to existing contact
-- =========================================
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    cid INT;
BEGIN
    SELECT id INTO cid
    FROM contacts
    WHERE name = p_contact_name;

    IF cid IS NULL THEN
        RAISE NOTICE 'Contact not found: %', p_contact_name;
        RETURN;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;


-- =========================================
-- Move contact to another group (auto-create group)
-- =========================================
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    gid INT;
BEGIN
    SELECT id INTO gid
    FROM groups
    WHERE name = p_group_name;

    IF gid IS NULL THEN
        INSERT INTO groups(name)
        VALUES (p_group_name)
        RETURNING id INTO gid;
    END IF;

    UPDATE contacts
    SET group_id = gid
    WHERE name = p_contact_name;
END;
$$;


-- =========================================
-- Delete contact by name or phone
-- =========================================
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value
       OR id IN (
            SELECT contact_id
            FROM phones
            WHERE phone = p_value
       );
END;
$$;


-- =========================================
-- Search contacts (name + email + all phones)
-- =========================================
CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, email VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_pattern || '%'
       OR c.email ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- =========================================
-- Pagination function
-- =========================================
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE(name VARCHAR, email VARCHAR, birthday DATE)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, c.birthday
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;