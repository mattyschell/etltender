-- CREATE BLUE TABLE
create table ddc_infra_projects_b (
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
    a.table_name = UPPER('ddc_infra_projects_b')
and a.column_name = UPPER('shape'); 
insert into user_sdo_geom_metadata a 
    (table_name
    ,column_name
    ,srid
    ,diminfo) 
values
    (UPPER('ddc_infra_projects_b')
    ,UPPER('shape')
    ,2263
    ,SDO_DIM_ARRAY (MDSYS.SDO_DIM_ELEMENT ('X', 900000, 1090000, .0005)
                   ,MDSYS.SDO_DIM_ELEMENT ('Y', 110000,  295000, .0005 )));
create index 
    ddc_infra_projects_bsidx
on
    ddc_infra_projects_b (shape)
indextype is mdsys.spatial_index;
-- CREATE GREEN TABLE
create table ddc_infra_projects_g (
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
    a.table_name = UPPER('ddc_infra_projects_g')
and a.column_name = UPPER('shape'); 
insert into user_sdo_geom_metadata a 
    (table_name
    ,column_name
    ,srid
    ,diminfo) 
values
    (UPPER('ddc_infra_projects_g')
    ,UPPER('shape')
    ,2263
    ,SDO_DIM_ARRAY (MDSYS.SDO_DIM_ELEMENT ('X', 900000, 1090000, .0005)
                   ,MDSYS.SDO_DIM_ELEMENT ('Y', 110000,  295000, .0005 )));
create index 
    ddc_infra_projects_gsidx
on
    ddc_infra_projects_g (shape)
indextype is mdsys.spatial_index;
-- INITIALIZE VIEW ON BLUE
-- historically these DDC ESRI services from their project browser service (pb)
-- were called infrastructure projects (strpro)
create or replace force view
pb_ifrpro
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
from ddc_infra_projects_b;
-- Geoserver may still need metadata for views
delete from 
    user_sdo_geom_metadata a
where
    a.table_name = UPPER('pb_ifrpro')
and a.column_name = UPPER('shape'); 
insert into user_sdo_geom_metadata a 
    (table_name
    ,column_name
    ,srid
    ,diminfo) 
values
    (UPPER('pb_ifrpro')
    ,UPPER('shape')
    ,2263
    ,SDO_DIM_ARRAY (MDSYS.SDO_DIM_ELEMENT ('X', 900000, 1090000, .0005)
                   ,MDSYS.SDO_DIM_ELEMENT ('Y', 110000,  295000, .0005 )));
EXIT