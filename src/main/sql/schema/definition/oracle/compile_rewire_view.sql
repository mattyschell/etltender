 create or replace PROCEDURE REWIRE_VIEW (
   p_view                IN VARCHAR2
) 
AUTHID CURRENT_USER AS
   --Mschell! 
   -- rewire a view from blue to green or green to blue
   -- makes lazy but firm assumptions about naming conventions
   -- locked in throughout this project
   psql                 VARCHAR2(4000);
   cols                 VARCHAR2(12000);
   text_long            LONG; --ick
   new_select           VARCHAR2(12000);
   view_sql             VARCHAR2(12000);
   current_table        VARCHAR2(64);
   new_table            VARCHAR2(64);
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
    IF UPPER(TO_CHAR(text_long)) LIKE ('%FROM%' || UPPER(p_view) || '_B')
    THEN
        current_table := p_view || '_b';
        new_table     := p_view || '_g';
    ELSE
        current_table := p_view || '_g';
        new_table     := p_view || '_b';
    END IF;
    new_select := REPLACE(UPPER(TO_CHAR(text_long))
                         ,UPPER(current_table)
                         ,UPPER(new_table));
    EXECUTE IMMEDIATE 'create or replace view '
                    || p_view || ' ('
                    || cols || ') AS '
                    || new_select;
END REWIRE_VIEW;
/
EXIT