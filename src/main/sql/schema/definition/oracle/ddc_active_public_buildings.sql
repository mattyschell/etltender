-- CREATE BLUE TABLE
create table ddc_public_buildings_b (
    objectid                NUMBER PRIMARY KEY
   ,projectid               VARCHAR2(16)
   ,description             VARCHAR2(4000)
   ,client_agency           VARCHAR2(32)
   ,division                VARCHAR2(32)
   ,phase                   VARCHAR2(32)
   ,projectedconstrcompl    DATE
   ,webscope                VARCHAR2(4000)
   ,dollar_amount           VARCHAR2(32)
   ,shape                   SDO_GEOMETRY
);
delete from 
    user_sdo_geom_metadata a
where
    a.table_name = UPPER('ddc_public_buildings_b')
and a.column_name = UPPER('shape'); 
insert into user_sdo_geom_metadata a 
    (table_name
    ,column_name
    ,srid
    ,diminfo) 
values
    (UPPER('ddc_public_buildings_b')
    ,UPPER('shape')
    ,2263
    ,SDO_DIM_ARRAY (MDSYS.SDO_DIM_ELEMENT ('X', 900000, 1090000, .0005)
                   ,MDSYS.SDO_DIM_ELEMENT ('Y', 110000,  295000, .0005 )));
create index 
    ddc_public_buildings_bsidx
on
    ddc_public_buildings_b (shape)
indextype is mdsys.spatial_index;
-- CREATE GREEN TABLE
create table ddc_public_buildings_g (
    objectid                NUMBER PRIMARY KEY
   ,projectid               VARCHAR2(16)
   ,description             VARCHAR2(4000)
   ,client_agency           VARCHAR2(32)
   ,division                VARCHAR2(32)
   ,phase                   VARCHAR2(32)
   ,projectedconstrcompl    DATE
   ,webscope                VARCHAR2(4000)
   ,dollar_amount           VARCHAR2(32)
   ,shape                   SDO_GEOMETRY
);
delete from 
    user_sdo_geom_metadata a
where
    a.table_name = UPPER('ddc_public_buildings_g')
and a.column_name = UPPER('shape'); 
insert into user_sdo_geom_metadata a 
    (table_name
    ,column_name
    ,srid
    ,diminfo) 
values
    (UPPER('ddc_public_buildings_g')
    ,UPPER('shape')
    ,2263
    ,SDO_DIM_ARRAY (MDSYS.SDO_DIM_ELEMENT ('X', 900000, 1090000, .0005)
                   ,MDSYS.SDO_DIM_ELEMENT ('Y', 110000,  295000, .0005 )));
create index 
    ddc_public_buildings_gsidx
on
    ddc_public_buildings_g (shape)
indextype is mdsys.spatial_index;
-- INITIALIZE VIEW ON BLUE
-- historically these DDC ESRI services from their project browser service (pb)
-- were called structures projects (strpro)
create or replace force view
pb_strpro
    (objectid                
    ,projectid               
    ,description             
    ,client_agency           
    ,division                
    ,phase                   
    ,projectedconstrcompl
    ,webscope                
    ,dollar_amount           
    ,shape)
as select
     objectid                
    ,projectid               
    ,description             
    ,client_agency           
    ,division                
    ,phase                   
    ,projectedconstrcompl
    ,webscope                
    ,dollar_amount           
    ,shape     
from ddc_public_buildings_b;
delete from 
    user_sdo_geom_metadata a
where
    a.table_name = UPPER('pb_strpro')
and a.column_name = UPPER('shape'); 
insert into user_sdo_geom_metadata a 
    (table_name
    ,column_name
    ,srid
    ,diminfo) 
values
    (UPPER('pb_strpro')
    ,UPPER('shape')
    ,2263
    ,SDO_DIM_ARRAY (MDSYS.SDO_DIM_ELEMENT ('X', 900000, 1090000, .0005)
                   ,MDSYS.SDO_DIM_ELEMENT ('Y', 110000,  295000, .0005 )));
EXIT