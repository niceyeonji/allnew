use testdb;

select NAME, DEPT from st_info;
select NAME, DEPT from st_info where ST_ID=202301;

select NAME, DEPT from st_info where DEPT='Game';

select Linux from st_grade where ST_ID=202301;

# NAME Linux DB DEPT => 202301
select st_info.NAME, st_grade.Linux, st_grade.DB, st_info.DEPT
from st_info, st_grade
where st_info.ST_ID=202301 and st_grade.ST_ID=202301;

update st_grade set Linux=90 where ST_ID=202301;

select st_info.NAME, st_grade.Linux, st_grade.DB, st_info.DEPT
from st_info, st_grade
where st_info.ST_ID=202301 and st_grade.ST_ID=202301;

update st_info set DEPT="Computer" where ST_ID=202301;

select st_info.NAME, st_grade.Linux, st_grade.DB, st_info.DEPT
from st_info, st_grade
where st_info.ST_ID=202301 and st_grade.ST_ID=202301;