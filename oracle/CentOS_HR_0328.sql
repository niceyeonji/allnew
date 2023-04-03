select * from usertbl where userName='김경호';

select userid, username from usertbl
where birthyear >= 1970 and height >= 182;

select userid, username from usertbl
where height between 178 and 183;

select username, addr from usertbl
where addr='경남' or addr='전남' or addr='경북';

select username, addr from usertbl
where addr in ('경남', '전남', '경북');

select username, height from usertbl
where username like '김%';

select username, height from usertbl
where username like '_종신';

select username, height from usertbl
where height > 177;

select username, height from usertbl
where height > (select height from usertbl where username='김경호');

-- error
select username, height from usertbl
where height >= (select height from usertbl where addr='경남');

-- or
select username, height from usertbl
where height >= any (select height from usertbl where addr='경남');

-- and
select username, height from usertbl
where height >= all (select height from usertbl where addr='경남');

select username, height from usertbl
where height = any (select height from usertbl where addr='경남');

select username, height from usertbl
where height in (select height from usertbl where addr='경남');

select username, mdate from usertbl order by mdate desc;

select addr from usertbl;

select addr from usertbl order by addr;

select distinct addr from usertbl order by addr;

select * from
(select emp_no, hire_date from bigemp order by hire_date asc)
where rownum <=5;

select emp_no, hire_date from bigemp sample(0.001);

select count(*) from usertbl;

select * from usertbl sample(10);