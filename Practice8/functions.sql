-- Task 1: Function to search contacts by pattern
-- Returns all records where name or phone matches the pattern
CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || p_pattern || '%'  -- match part of name
       OR c.phone ILIKE '%' || p_pattern || '%'; -- match part of phone
END;
$$ LANGUAGE plpgsql;


-- Task 4: Function with pagination (LIMIT & OFFSET)
-- Returns limited number of rows starting from offset

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM contacts c
    ORDER BY c.name             
    LIMIT p_limit               
    OFFSET p_offset;            
END;
$$ LANGUAGE plpgsql;