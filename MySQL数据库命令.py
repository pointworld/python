编程常见命令集合

MySQL数据库命令
	登录到MySQL
		mysql -h localhost -u root -p
		localhost:IP地址；
		root:用户名；
		database:数据库名（可以省略，如果有，跟在-p面）
	删除数据库：
		
		mysqladmin -u root -pwrf956750621 drop awesome
	初始化数据库: 
		mysql –u root –p密码 <D:\computer_learning\backup\schema.sql
		mysql -u root -p   
		2.mysql -h localhost -u root -p database_name  	
	列出数据库：
		
		show databases;  	
	选择数据库：		

		use databases_name;  	
	列出数据表：		

		show tables;  	
	显示表格列的属性：		

		show columns from table_name;   
		describe table_name;  	
	导出整个数据库：		

		mysqldump -u user_name -p database_name > path_file_name	

		例如：mysqldump -u root -p test_db > d:/test_db.sql	
	导出一个表：		

		mysqldump -u user_name -p database_name table_name > /tmp/file_name  	

		例如：mysqldump -u root -p test_db table1 > d:/table1.sql	
	导出一个数据库结构：		

		mysqldump -u user_name -p -d --add-drop-table database_name > file_name  	

		例如：mysqldump -u root -p -d --add-drop-table test_db > test_db.sql	
	导入数据库：		

		source file_name;   
		或   
		mysql -u user_name -p database_name < file_name  	

		例如：	

		source /tmp/bbs.sql；	

		source d:/bbs.sql；	

		mysql -u root -p bbs < "d:/bbs.sql"	

		mysql -u root -p bbs < "/tmp/bbs.sql"	
	将文本文件导入数据表中（excel与之相同）		

		load data infile "tables.txt" into table table_name;  	

		例如：	

		load data infile "/tmp/bbs.txt" into table bbs；	

		load data infile "/tmp/bbs.xls" into table bbs；	

		load data infile "d:/bbs.txt" into table bbs；	

		load data infile "d:/bbs.xls" into table bbs；	
	将数据表导出为文本文件（excel与之相同）		

		select * into outfile "path_file_name" from table_name;  	

		例如：	

		select * into outfile "/tmp/bbs.txt" from bbs；	

		select * into outfile "/tmp/bbs.xls" from bbs where id=1;	

		select * into outfile "d:/bbs.txt" from bbs;	

		select * into outfile "d:/bbs.xls" from bbs where id=1;	
	创建数据库时先判断数据库是否存在：		

		create database if not exists database_name;  	

		例如：create database if not exists bbs	
	创建数据库：		

		create database database_name;  	

		例如：create database bbs;	
	删除数据库：		

		1.drop database database_name;  	

		例如：drop database bbs;	
	创建数据表：		

		1.mysql> create table <table_name> ( <column 1 name> <col. 1 type> <col. 1 details>,<column 2 name> <col. 2 type> <col. 2 details>, ...);  	

		例如：create table (id int not null auto_increment primary key,name char(16) not null default "jack",date_year date not null);	
	删除数据表中数据：		

		delete from table_name;  	

		例如：	

		delete from bbs;	

		delete from bbs where id=2;	
	删除数据库中的数据表：		

		drop table table_name;  	

		例如：	

		drop table test_db;	

		rm -f database_name/table_name.* (linux下）	

		例如：	

		rm -rf bbs/accp.*	
	向数据库中添加数据：		

		insert into table_name set column_name1=value1,column_name2=value2;  	

		例如：insert into bbs set name="jack",date_year="1993-10-01";	

		insert into table_name values (column1,column2,...);  	

		例如：insert into bbs ("2","jack","1993-10-02")	

		insert into table_name (column_name1,column_name2,...) values (value1,value2);  	

		例如：insert into bbs (name,data_year) values ("jack","1993-10-01");	
	查询数据表中的数据：		

		select * from table_name;  	

		例如：select * from bbs where id=1;	
	修改数据表中的数据：		

		update table_name set col_name=new_value where id=1;  	

		例如：update bbs set name="tom" where name="jack";	
	增加一个字段：		

		alter table table_name add column field_name datatype not null default "1";  	

		例如：alter table bbs add column tel char(16) not null;	
	增加多个字段：(column可省略不写）		
		alter table table_name add column filed_name1 datatype,add column filed_name2 datatype;  

		例如：alter table bbs add column tel char(16) not null,add column address text;

		删除一个字段：

		alter table table_name drop field_name;  
		例如：alter table bbs drop tel;
	修改字段的数据类型：	

		alter table table_name modify id int unsigned;//修改列id的类型为int unsigned    
		alter table table_name change id sid int unsigned;//修改列id的名字为sid，而且把属性修改为int unsigned  
	修改一个字段的默认值：	

		alter table table_name modify column_name datatype not null default "";  

		例如：alter table test_db modify name char(16) default not null "yourname";
	对表重新命名：	

		alter table table_name rename as new_table_name;  

		例如：alter table bbs rename as bbs_table;

		rename table old_table_name to new_table_name;  
		例如：rename table test_db to accp;
	从已经有的表中复制表的结构：	

		create table table2 select * from table1 where 1<>1;  

		例如：create table test_db select * from accp where 1<>1;
	查询时间：	

		select now();  
	查询当前用户：	

		select user();  
	查询数据库版本：	

		select version();  
	创建索引：
		alter table table1 add index ind_id(id);   
		create index ind_id on table1(id);   
		create unique index ind_id on table1(id);//建立唯一性索引  
	删除索引：
		drop index idx_id on table1;   
		alter table table1 drop index ind_id;  
		联合字符或者多个列（将id与":"和列name和"="连接）
		select concat(id，':',name,'=') from table;  
		limit（选出10到20条）
		select * from bbs order by id limit 9,10;  
		（从查询结果中列出第几到几条的记录）
	增加一个管理员账号：	

		grant all on *.* to user@localhost identified by "password";  
	创建表是先判断表是否存在	

		create table if not exists students(……);  
	复制表：
		create table table2 select * from table1;  
		例如：create table test_db select * from accp;
	授于用户远程访问mysql的权限	

		grant all privileges on *.* to "root"@"%" identified by "password" with grant option;  
	或者是修改mysql数据库中的user表中的host字段
		use mysql;   
		select user,host from user;   
		update user set host="%" where user="user_name";  
	查看当前状态	

		show status;  
	查看当前连接的用户
		show processlist;  	
		（如果是root用户，则查看全部的线程，得到的用户连接数同show status;里的 Threads_connected值是相同的）

qq邮箱授权密码： xgyphxmyyntjbfbg