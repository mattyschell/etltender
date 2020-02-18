CREATE OR REPLACE PROCEDURE GEOSERVER.REWIRE_VIEW (
   p_view                IN VARCHAR2
)
AUTHID CURRENT_USER AS
   -- Mschell!
   -- rewire a view from blue to green or green to blue
   -- makes lazy but firm assumptions about naming conventions
   -- locked in throughout this project
   psql                 VARCHAR2(4000);
   cols                 VARCHAR2(12000);
   text_long            LONG; --ick
   new_select           VARCHAR2(12000);
   view_sql             VARCHAR2(12000);
   new_color            VARCHAR2(1);
BEGIN
    psql := 'SELECT LISTAGG(a.column_name, :p1) '
         || 'WITHIN GROUP (ORDER BY a.column_id) '
         || 'FROM user_tab_cols a '
         || 'WHERE a.table_name = :p2';
    --produces 'SHAPE,OBJECTID,ID,BIN,BBL...'
    EXECUTE IMMEDIATE psql INTO cols USING ',',
                                          UPPER(p_view);
    psql := 'SELECT a.text '
         || 'FROM user_views a '
         || 'WHERE a.view_name = :p1 ';
    --includes the select
    EXECUTE IMMEDIATE psql INTO text_long USING UPPER(p_view);
    --dbms_output.put_line('text long is ');
    --dbms_output.put_line(text_long);
    IF UPPER(TO_CHAR(text_long)) LIKE '%B'
    THEN
        --dbms_output.put_line('feeling blue!');
        new_color := 'G';
    ELSE
        --dbms_output.put_line('feeling green!');
        new_color := 'B';
    END IF;
    -- chomp off last char and replace with B or G
    new_select := SUBSTR(UPPER(TO_CHAR(text_long))
                         ,0
                         ,LENGTH(UPPER(TO_CHAR(text_long))) - 1) || new_color;
    --dbms_output.put_line('new select is ' || new_select);
    psql :=  'create or replace force view '
                    || p_view || ' ('
                    || cols || ') AS '
                    || new_select;
    --dbms_output.put_line(psql);
    EXECUTE IMMEDIATE psql;
END REWIRE_VIEW;
/
EXIT