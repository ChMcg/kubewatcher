
drop schema public cascade;
create schema public;

create table analyzed_data (
    analyzed_data_id serial not null primary key,
    object text
);

create table analyzed_metadata (
    analyzed_metadata_id serial not null primary key,
    analyzed_data_id int not null,
    severity text,
    score int,

    foreign key (analyzed_data_id) references analyzed_data (analyzed_data_id)
);
