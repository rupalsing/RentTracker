create table home_schema.rent_tracker
(
	link text not null
		constraint rent_tracker_pk
			primary key,
	title text,
	prop_over text,
	lease text,
	description text,
	facilities text,
	phone text,
	rent text,
	latitude text,
	longitude text,
	stores text
);

create unique index rent_tracker_link_uindex
	on home_schema.rent_tracker (link);

