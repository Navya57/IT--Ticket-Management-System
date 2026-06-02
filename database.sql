create database ticket_system;
use ticket_system;
create table users(user_id int  primary key auto_increment ,name varchar(100) , email varchar(100), password varchar(100));
create table ticket( ticket_id int primary key auto_increment,issue_title varchar(255),description text,priority varchar(20),status varchar(20),
created_date timestamp default current_timestamp);
show tables;
insert into ticket (issue_title,description,priority,status)values
('Login Issue','Unable to login into system','High','Open'),
('Printer Error','Printer not responding','Medium','In Progress');
select*from ticket;
update ticket set status='Resolved' where ticket_id=1;
delete from ticket where ticket_id=2;
