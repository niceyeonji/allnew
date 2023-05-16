load data
infile 'myterror.csv'
insert into table myterror
fields terminated by ','
trailing nullcols(
	eventid,
	iyear,
	imonth,
	iday,
	country,
	country_txt,
	region,
	region_txt,
	provstate,
	city,
	latitude,
	longitude
)