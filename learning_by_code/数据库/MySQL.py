数据库(Database) -- 是按照数据结构来组织、存储和管理数据的仓库

RDBMS(Relational Database Management System, 关系型数据库管理系统)--数据元素(行和列)--表()--数据库()
定义

	建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。
特点
	1. 数据以表格的形式出现
	2. 每行为各种记录名称
	3. 每列为记录名称所对应的数据域
	4. 许多的行和列组成一张表单
    5. 若干的表单组成database
RDBMS 术语
	'数据库'--一些关联表的集合
	'数据表'--表是数据的矩阵
	'行'--(=元组，或记录), 数据元素, 每行为各种记录名称
	'列'--数据元素, 每列为记录名称所对应的数据域
	'冗余'--存储两倍数据，使系统速度更快
	'主键'--唯一, 一个数据表中只能包含一个主键, 可以使用主键来查询数据
	'外键'--外键用于关联两个表
	'复合键'--组合键, 将多个列作为一个索引键，一般用于复合索引
	'索引'--使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录
	'参照完整性'--要求关系中不允许引用不存在的实体。目的是保证数据的一致性

MySQL()--最流行关系型数据库管理系统
	定义
		MySQL是一个关系型数据库管理系统，MySQL是一种关联数据库管理系统，关联数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了
		速度并提高了灵活性。MySQL所使用的 SQL 语言是用于访问数据库的最常用标准化语言。
	特点
		1．使用 C和 C++编写，源代码可移植
		2．支持多种操作系统
		3．为多种编程语言提供了 API
		4．支持多线程，充分利用 CPU 资源
		5．优化的 SQL查询算法，有效地提高查询速度
		6．既能够作为一个单独的应用程序应用在客户端服务器网络环境中，也能够作为一个库而嵌入到其他的软件中
		7．提供多语言支持
		8．提供 TCP/IP、ODBC 和 JDBC等多种数据库连接途径
		9．提供用于管理、检查、优化数据库操作的管理工具
		10．支持大型的数据库
		11．支持多种存储引擎
		12. 开源, 可以修改源码来开发自己的MySQL系统
		13. MySQL 使用标准的 SQL数据语言形式
		14. MySQL 对 PHP 有很好的支持，PHP是目前最流行的 Web 开发语言
	安装
		验证安装
			通过"开始" =》在搜索框中输入 " cmd" 命令 =》 在命令提示符上切换到 C:/Program Files/MySQL/MySQL Server 5.7/bin 目录，并输入一下命令：
			mysqld.exe --console
			如果安装成功以上命令将输出一些MySQL启动及InnoDB信息
		验证是否工作正常
			C:/Program Files/MySQL/MySQL Server 5.7/bin>mysqladmin --version
			mysqladmin  Ver 8.42 Distrib 5.7.17, for Win32 on AMD64
			如果以上命令执行后未输入任何信息，说明你的MySQL未安装成功
	管理
		启动及关闭 MySQL 服务器
		使用MySQL数据库过程中常用的命令
			已存在所需数据库的使用方式
			'SHOW DATABASES;'  列出 MySQL 数据库管理系统的数据库列表
				mysql> show databases;
				+--------------------+
				| Database           |
				+--------------------+
				| information_schema |
				| mysql              |
				| performance_schema |
				| sakila             |
				| sys                |
				| test               |
				| world              |
				+--------------------+
				7 rows in set (0.00 sec)			
			'USE 数据库名;' 选择要操作的MySQL数据库，使用该命令后所有MySQL命令都只针对该数据库
				mysql> use test;
				Database changed
			'SHOW TABLES;' 显示指定数据库的所有表，使用该命令前需要使用 use 命令来选择要操作的数据库
				mysql> use test;
				Database changed
				mysql> show tables;
				+----------------+
				| Tables_in_test |
				+----------------+
				| blogs          |
				| comments       |
				| users          |
				+----------------+
				3 rows in set (0.00 sec)
			'SHOW COLUMNS FROM 数据表;' 显示数据表的属性，属性类型，主键信息 ，是否为 NULL，默认值等其他信息
				mysql> show columns from users;
				+------------+--------------+------+-----+---------+-------+
				| Field      | Type         | Null | Key | Default | Extra |
				+------------+--------------+------+-----+---------+-------+
				| id         | varchar(50)  | NO   | PRI | NULL    |       |
				| email      | varchar(50)  | NO   | UNI | NULL    |       |
				| passwd     | varchar(50)  | NO   |     | NULL    |       |
				| admin      | tinyint(1)   | NO   |     | NULL    |       |
				| name       | varchar(50)  | NO   |     | NULL    |       |
				| image      | varchar(500) | NO   |     | NULL    |       |
				| created_at | double       | NO   | MUL | NULL    |       |
				+------------+--------------+------+-----+---------+-------+
				7 rows in set (0.00 sec)
			'SHOW INDEX FROM 数据表;' 显示数据表的详细索引信息，包括PRIMARY KEY（主键）
				mysql> show index from users;
				+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
				| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
				+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
				| users |          0 | PRIMARY        |            1 | id          | A         |           0 |     NULL | NULL   |      | BTREE      |         |               |
				| users |          0 | idx_email      |            1 | email       | A         |           0 |     NULL | NULL   |      | BTREE      |         |               |
				| users |          1 | idx_created_at |            1 | created_at  | A         |           0 |     NULL | NULL   |      | BTREE      |         |               |
				+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
				3 rows in set (0.00 sec)
			'SHOW TABLE STATUS LIKE 数据表\G;' 该命令将输出MySQL数据库管理系统的性能及统计信息
				'mysql> show table status from test;'   # 显示数据库 RUNOOB 中所有表的信息
					'mysql> show table status from test;'
					+----------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					| Name     | Engine | Version | Row_format | Rows | Avg_row_length | Data_length | Max_data_length | Index_length | Data_free | Auto_increment | Create_time         | Update_time | Check_time | Collation       | Checksum | Create_options | Comment |
					+----------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					| blogs    | InnoDB |      10 | Dynamic    |    0 |              0 |       16384 |               0 |        16384 |         0 |           NULL | 2017-03-03 11:05:19 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
					| comments | InnoDB |      10 | Dynamic    |    0 |              0 |       16384 |               0 |        16384 |         0 |           NULL | 2017-03-03 11:05:42 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
					| users    | InnoDB |      10 | Dynamic    |    0 |              0 |       16384 |               0 |        32768 |         0 |           NULL | 2017-03-03 11:05:00 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
					+----------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					3 rows in set (0.00 sec)			
				'mysql> show table status from test like 'users';'     # 表名以runoob开头的表的信息
					mysql> show table status from test like 'users';
					+-------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					| Name  | Engine | Version | Row_format | Rows | Avg_row_length | Data_length | Max_data_length | Index_length | Data_free | Auto_increment | Create_time         | Update_time | Check_time | Collation       | Checksum | Create_options | Comment |
					+-------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					| users | InnoDB |      10 | Dynamic    |    0 |              0 |       16384 |               0 |        32768 |         0 |           NULL | 2017-03-03 11:05:00 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
					+-------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					1 row in set (0.00 sec)	

					mysql> show table status from test like 'use%';
					+-------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					| Name  | Engine | Version | Row_format | Rows | Avg_row_length | Data_length | Max_data_length | Index_length | Data_free | Auto_increment | Create_time         | Update_time | Check_time | Collation       | Checksum | Create_options | Comment |
					+-------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					| users | InnoDB |      10 | Dynamic    |    0 |              0 |       16384 |               0 |        32768 |         0 |           NULL | 2017-03-03 11:05:00 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
					+-------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
					1 row in set (0.00 sec)
				'mysql> show table status from test like 'use%'\G;'   # 加上 \G，查询结果按列打印
					mysql> show table status from test like 'use%'\G;
					*************************** 1. row ***************************
					           Name: users
					         Engine: InnoDB
					        Version: 10
					     Row_format: Dynamic
					           Rows: 0
					 Avg_row_length: 0
					    Data_length: 16384
					Max_data_length: 0
					   Index_length: 32768
					      Data_free: 0
					 Auto_increment: NULL
					    Create_time: 2017-03-03 11:05:00
					    Update_time: NULL
					     Check_time: NULL
					      Collation: utf8_general_ci
					       Checksum: NULL
					 Create_options:
					        Comment:
					1 row in set (0.00 sec)

					ERROR:
					No query specified
			
			不存在所需数据库的使用方式
			'drop database if exists 数据库名;' 若存在 数据库名 则删除该数据库
				mysql> drop database if exists test;
				Query OK, 3 rows affected (0.64 sec)
			'create database 数据库名;' 创建数据库
				mysql> create database test;
				Query OK, 1 row affected (0.00 sec)
			'use 数据库名;' 使用该数据库
				mysql> use test;
				Database changed
			"grant 权限1, 权限2, ..., 权限n on 数据库名.* to '新用户'@'localhost' identified by '新用户密码';" 给指定数据库 test 添加 用户 www-data ，
				密码为 www-data, 授权用户可进行 SELECT, INSERT 和 UPDATE等操作权限, 以上命令会在MySQL数据库中的user表创建一条用户信息记录
				mysql> grant select, insert, update, delete on test.* to 'www-data'@'localhost' identified by 'www-data';
				Query OK, 0 rows affected, 1 warning (0.00 sec)
				可授予的权限有：select, insert, update, delete, Create, Drop, Reload ,Shutdown ,Process ,File ,Grant ,References ,Index, Alter
			'mysql> flush privileges;' 重新载入授权表, 如果不使用该命令，就无法使用新创建的用户来连接MySQL服务器，除非你重启MySQL服务器
				mysql> flush privileges;
				Query OK, 0 rows affected (0.00 sec)
			'create table 表名 (`第一列的名称` 第一列的值域, ..., `第n列的名称` 第n列的值域, key `第几列为索引` (`第几列`), primary key (`第几列为主键`)) engine=innodb default charset=utf8;' 创建表, 并添加数据
				创建表 users
					mysql> use test;
					Database changed
					mysql> create table users (
					    ->     `id` varchar(50) not null,
					    ->     `email` varchar(50) not null,
					    ->     `passwd` varchar(50) not null,
					    ->     `admin` bool not null,
					    ->     `name` varchar(50) not null,
					    ->     `image` varchar(500) not null,
					    ->     `created_at` real not null,
					    ->     unique key `idx_email` (`email`),
					    ->     key `idx_created_at` (`created_at`),
					    ->     primary key (`id`)
					    -> ) engine=innodb default charset=utf8;
					Query OK, 0 rows affected (0.34 sec)
				创建表 blogs
					mysql> create table blogs (
					    ->     `id` varchar(50) not null,
					    ->     `user_id` varchar(50) not null,
					    ->     `user_name` varchar(50) not null,
					    ->     `user_image` varchar(500) not null,
					    ->     `name` varchar(50) not null,
					    ->     `summary` varchar(200) not null,
					    ->     `content` mediumtext not null,
					    ->     `created_at` real not null,
					    ->     key `idx_created_at` (`created_at`),
					    ->     primary key (`id`)
					    -> ) engine=innodb default charset=utf8;
					Query OK, 0 rows affected (0.36 sec)				
				创建表 comments
					mysql> create table comments (
					    ->     `id` varchar(50) not null,
					    ->     `blog_id` varchar(50) not null,
					    ->     `user_id` varchar(50) not null,
					    ->     `user_name` varchar(50) not null,
					    ->     `user_image` varchar(500) not null,
					    ->     `content` mediumtext not null,
					    ->     `created_at` real not null,
					    ->     key `idx_created_at` (`created_at`),
					    ->     primary key (`id`)
					    -> ) engine=innodb default charset=utf8;
					Query OK, 0 rows affected (0.34 sec)
			再按照 '已存在所需数据库的使用方式' 进行操作
	安装与卸载
	用户操作

		创建用户
			grant all on *.* to 'user'@'localhost' identified by "password";  
			with grant option;
					 •all privileges：表示将所有权限授予给用户。也可指定具体的权限，如：SELECT、CREATE、DROP等，以逗号分隔。
					 •on：表示这些权限对哪些数据库和表生效，格式：数据库名.表名，这里写“*”表示所有数据库，所有表。如果我要指定将权限应用到test库的user表中，可以这么写：test.user
					 •to：将权限授予哪个用户。格式：”用户名”@”登录IP或域名”。%表示没有限制，在任何主机都可以登录。比如：”yangxin”@”192.168.0.%”，表示yangxin这个用户只能在192.168.0 IP段登录
					 •identified by：指定用户的登录密码
					 •with grant option：表示允许用户将自己的权限授权给其它用户 				
		用户登录（cmd）
			mysql -h host -u root -p
			host : IP地址（本地为 localhost 或 ）；
			root : 用户名；
			database : 数据库名（可以省略，如果有，跟在-p面）
		恢复或重建默认数据库和表
			How to recover or recreate mysql''s default 'mysql' database
			If you are still able to log in (I assume you aren't since there's no user table) and have databases to save, dump them with
			mysqldump --routines databasename > outfile.sql
			The MySQL database can be recreated with the command (cmd)
			mysqld --initialize

			On Windows, use one of these commands:
			mysqld --initialize
			mysqld --initialize-insecure
		用户权限管理
			用户权限管理主要有以下作用：
				1. 可以限制用户访问哪些库、哪些表
				2. 可以限制用户对哪些表执行SELECT、CREATE、DELETE、DELETE、ALTER等操作
				3. 可以限制用户登录的IP或域名
				4. 可以限制用户自己的权限是否可以授权给别的用户
			用户授权
				使用GRANT给用户添加权限，权限会自动叠加，不会覆盖之前授予的权限
					比如你先给用户添加一个SELECT权限，后来又给用户添加了一个INSERT权限，那么该用户就同时拥有了SELECT和INSERT权限。 
				grant all privileges on *.* to 'point'@'%' identified by '指定用户的登录密码' with grant option;
					 •all privileges：表示将所有权限授予给用户。也可指定具体的权限，如：SELECT、CREATE、DROP等，以逗号分隔。
					 •on：表示这些权限对哪些数据库和表生效，格式：数据库名.表名，这里写“*”表示所有数据库，所有表。如果我要指定将权限应用到test库的user表中，可以这么写：test.user
					 •to：将权限授予哪个用户。格式：”用户名”@”登录IP或域名”。%表示没有限制，在任何主机都可以登录。比如：”yangxin”@”192.168.0.%”，表示yangxin这个用户只能在192.168.0 IP段登录
					 •identified by：指定用户的登录密码
					 •with grant option：表示允许用户将自己的权限授权给其它用户 				
			刷新权限
				对用户做了权限变更之后，一定记得重新加载一下权限，将权限信息从内存中写入数据库。
				flush privileges;
			查看用户权限
				show grants for 'point'@'localhost';
					mysql> show grants for 'point'@'%';
					+-------------------------------------------------+
					| Grants for point@%                              |
					+-------------------------------------------------+
					| GRANT RELOAD, CREATE USER ON *.* TO 'point'@'%' |
					+-------------------------------------------------+
					1 row in set (0.33 sec)
					mysql>		
			回收权限
				mysql> revoke create on *.* from 'point'@'%';
				mysql> flush privileges;	
			删除用户
				drop user 'point'@'%';
					mysql> select host,user from user;
					+-----------+-----------+
					| host      | user      |
					+-----------+-----------+
					| %         | point     |
					| localhost | mysql.sys |
					| localhost | root      |
					+-----------+-----------+
					3 rows in set (0.00 sec)
					mysql> drop user 'point'@'%';
					Query OK, 0 rows affected (0.00 sec)
					mysql> flush privileges;
					Query OK, 0 rows affected (0.00 sec)
					mysql>
		更改用户名
			rename user 'point'@'%' to 'pointttt'@'%';
		重启MySQL
			mysqld restart 
		更改用户密码
			1> 更新mysql.user表
				mysql> use mysql;
				# mysql5.7之前
				mysql> update user set password=password('new_password') where user='root';
				# mysql5.7之后
				mysql> update user set authentication_string= password('new_password') where User='root';
				mysql> flush privileges;		
			2> 用set password命令
				语法：set password for ‘用户名'@'登录地址'=password(‘密码')
				mysql> set password for 'root'@'localhost'=password('123456');
			3> mysqladmin
				语法：mysqladmin -u用户名 -p旧的密码 password 新密码
				mysql> mysqladmin -uroot -p123456 password 1234abcd
				注意：mysqladmin位于mysql安装目录的bin目录下	
			4> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';			
		忘记登录密码  ????
			1> 添加登录跳过权限检查配置
				修改my.ini，在mysqld配置节点添加skip-grant-tables配置
				[mysqld]
				skip-grant-tables
			2> 重新启动mysql服务
			  > mysqld restart
			3> 修改密码
			此时在终端用mysql命令登录时不需要用户密码，然后按照修改密码的第一种方式将密码修改即可。
			MySQL用户权限管理,MySQL用户权限,MySQL权限管理
			4> 还原登录权限跳过检查配置
			将my.ini中mysqld节点的skip-grant-tables配置删除，然后重新启动服务即可。
	MySQL PHP 语法
		PHP--PHP提供多种方式来访问和操作MySQL数据库记录
			PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言
			PHP 脚本以 <?php 开头，以 ?> 结尾：
				<?php
				// 此处是 PHP 代码
				?>
			PHP 文件的默认文件扩展名是 ".php"
			PHP 文件通常包含 HTML 标签以及一些 PHP 脚本代码
				<!DOCTYPE html>
				<html>
				<body>

				<h1>我的第一张 PHP 页面</h1>

				<?php
				echo "Hello World!";
				?>

				</body>
				</html>
			PHP 语句以分号结尾（;）。PHP 代码块的关闭标签也会自动表明分号（因此在 PHP 代码块的最后一行不必使用分号）。
			PHP 支持三种注释--唯一的作用是供代码编辑者阅读
				<!DOCTYPE html>
				<html>
				<body>

				<?php
				// 这是单行注释
				# 这也是单行注释
				/*
				这是多行注释块
				它横跨了
				多行
				*/
				?>

				</body>
				</html>
			变量以 $ 符号开头，其后是变量的名称
		PHP MySQL函数格式如下：

			mysql_function(value,value,...);
		以上格式中 function部分描述了MySQL函数的功能，如
			mysqli_connect($connect);
			mysqli_query($connect,"SQL 语句");
			mysql_fetch_array()
			mysql_connect(),mysql_close()
		以下实例展示了PHP调用MySQL函数的语法：
			<html>
			<head>
			<title>PHP with MySQL</title>
			</head>
			<body>
			<?php
			   $retval = mysql_function(value, [value,...]);
			   if( !$retval )
			   {
				die ( "相关错误信息" );
				}
				// 其他 MySQL 或 PHP 语句
			?>
			</body>
			</html>
	MySQL 连接
		使用MySQL二进制方式连接--进入到MySQL命令提示符下来连接MySQL数据库
			C:\Users\Administrator>mysql -u root -p
			Enter password: ************
			在登录成功后会出现 mysql> 命令提示窗口，你可以在上面执行任何 SQL 语句。
			以上命令执行后，登录成功输出结果如下:
			Welcome to the MySQL monitor.  Commands end with ; or \g.
			Your MySQL connection id is 15
			Server version: 5.7.17-log MySQL Community Server (GPL)

			Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

			Oracle is a registered trademark of Oracle Corporation and/or its
			affiliates. Other names may be trademarks of their respective
			owners.

			Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

			mysql>
			在以上实例中，我们使用了root用户登录到MySQL服务器，当然也可以使用其他MySQL用户登录。
			如果用户权限足够，任何用户都可以在MySQL的命令提示窗口中进行SQL操作。
			退出 mysql> 命令提示窗口可以使用 exit 命令，如下所示：
			mysql> exit
			Bye
			C:\Users\Administrator>
		使用 PHP 脚本连接 MySQL--PHP 提供了 mysql_connect() 函数来连接数据库
			该函数有5个参数，在成功链接到MySQL后返回 连接标识，失败返回 FALSE 。
			语法

				connection mysql_connect(server,user,passwd,new_link,client_flag);
			参数说明：

				参数	     描述

				server	     可选。规定要连接的服务器。可以包括端口号，例如 "hostname:port"，或者到本地套接字的路径，例如对于 localhost 的 ":/path/to/socket"。
				                     如果 PHP 指令 mysql.default_host 未定义（默认情况），则默认值是 'localhost:3306'。
				user	     可选。用户名。默认值是服务器进程所有者的用户名。
				passwd	     可选。密码。默认值是空密码。
				new_link    可选。如果用同样的参数第二次调用 mysql_connect()，将不会建立新连接，而将返回已经打开的连接标识。参数 new_link 改变此行为
				                     并使 mysql_connect() 总是打开新的连接，甚至当 mysql_connect() 曾在前面被用同样的参数调用过。
				client_flag  可选。client_flags 参数可以是以下常量的组合：
				                      MYSQL_CLIENT_SSL - 使用 SSL 加密
				                      MYSQL_CLIENT_COMPRESS - 使用压缩协议
				                      MYSQL_CLIENT_IGNORE_SPACE - 允许函数名后的间隔
				                      MYSQL_CLIENT_INTERACTIVE - 允许关闭连接之前的交互超时非活动时间
			你可以使用PHP的 mysql_close() 函数来断开与MySQL数据库的链接。
				
				该函数只有一个参数为mysql_connect()函数创建连接成功后返回的 MySQL 连接标识符。
			语法

				bool mysql_close ( resource $link_identifier );
				本函数关闭指定的连接标识所关联的到 MySQL 服务器的非持久连接。如果没有指定 link_identifier，则关闭上一个打开的连接。
				提示：通常不需要使用 mysql_close()，因为已打开的非持久连接会在脚本执行完毕后自动关闭。
				注释：mysql_close() 不会关闭由 mysql_pconnect() 建立的持久连接。
			实例

				你可以尝试以下实例来连接到你的 MySQL 服务器:
				<html>
				<head>
				<meta charset="utf-8">
				<title>Connecting MySQL Server</title>
				</head>
				<body>
				<?php
				   $dbhost = 'localhost:3306';  //mysql服务器主机地址
				   $dbuser = 'guest';      //mysql用户名
				   $dbpass = 'guest123';//mysql用户名密码
				   $conn = mysql_connect($dbhost, $dbuser, $dbpass);
				   if(! $conn ) 
				   {
				      die('Could not connect: ' . mysql_error());
				    }
				    echo 'Connected successfully';
				    mysql_close($conn);
				?>
				</body>
				</html>
	MySQL 创建数据库
		使用 mysqladmin 创建数据库--mysqladmin -u root -p create 数据库名
			使用普通用户，你可能需要特定的权限来创建或者删除 MySQL 数据库。
			所以我们使用root用户登录，root用户拥有最高权限，可以使用 mysql mysqladmin 命令来创建数据库
				C:\WINDOWS\system32>mysqladmin -u root -p create W3CSCHOOL1
				Enter password: ************
				C:\WINDOWS\system32>
				以上命令执行成功后会创建 MySQL 数据库 W3CSCHOOL1 
		使用 PHP脚本 创建数据库--mysql_query( sql, connection ) 函数
			PHP使用 mysql_query 函数来创建或者删除 MySQL 数据库
				
				该函数有两个参数，在执行成功时返回 TRUE，否则返回 FALSE。
			语法

				bool mysql_query( sql, connection );
				参数	            描述
				sql	            必需。规定要发送的 SQL 查询。注释：查询字符串不应以分号结束。
				connection	可选。规定 SQL 连接标识符。如果未规定，则使用上一个打开的连接。
			实例

				以下实例演示了使用PHP来创建一个数据库：
				<html>
				<head>
				<meta charset="utf-8">  # meta是html语言head区的一个辅助性标签
				<title>创建 MySQL 数据库</title>
				</head>
				<body>
				<?php
				$dbhost = 'localhost:3036';
				$dbuser = 'root';
				$dbpass = 'rootpassword';
				$conn = mysql_connect($dbhost, $dbuser, $dbpass);
				if(! $conn )
				{
				  die('连接错误: ' . mysql_error());
				}
				echo '连接成功<br />';
				$sql = 'CREATE DATABASE W3CSCHOOL';
				$retval = mysql_query( $sql, $conn );
				if(! $retval )
				{
				  die('创建数据库失败: ' . mysql_error());
				}
				echo "数据库 W3CSCHOOL 创建成功\n";
				mysql_close($conn);
				?>
				</body>
				</html>
	MySQL 初始化数据库
		mysql –u root –p密码 <D:\computer_learning\backup\schema.sql
		或 mysql –u root –p <D:\computer_learning\backup\schema.sql
		再输入密码
	MySQL 删除数据库
		使用 mysqladmin 删除数据库--mysqladmin -u root -p drop W3CSCHOOL1
			使用普通用户，你可能需要特定的权限来创建或者删除 MySQL 数据库。
			所以我们使用root用户登录，root用户拥有最高权限，可以使用 mysql mysqladmin 命令来删除数据库
			在删除数据库过程中，务必要十分谨慎，因为在执行删除命令后，所有数据将会消失。
				以下实例删除数据库 W3CSCHOOL1(该数据库在前一章节已创建)：
				C:\WINDOWS\system32>mysqladmin -u root -p drop W3CSCHOOL1
				Enter password: ************
				
				执行以上删除数据库命令后，会出现一个提示框，来确认是否真的删除数据库：
				Dropping the database is potentially a very bad thing to do.
				Any data stored in the database will be destroyed.

				Do you really want to drop the 'W3CSCHOOL1' database [y/N] y
				Database "W3CSCHOOL1" dropped
				C:\WINDOWS\system32>
		使用 PHP脚本 删除数据库--mysql_query( sql, connection ) 函数
			PHP使用 mysql_query 函数来创建或者删除 MySQL 数据库
				
				该函数有两个参数，在执行成功时返回 TRUE，否则返回 FALSE。
			语法

				bool mysql_query( sql, connection );
				参数	            描述
				sql	            必需。规定要发送的 SQL 查询。注释：查询字符串不应以分号结束。
				connection	可选。规定 SQL 连接标识符。如果未规定，则使用上一个打开的连接。
			实例

				以下实例演示了使用PHP来创建一个数据库：
				<html>
				<head>
				<meta charset="utf-8">  # meta是html语言head区的一个辅助性标签
				<title>删除 MySQL 数据库</title>
				</head>
				<body>
				<?php
				$dbhost = 'localhost:3036';
				$dbuser = 'root';
				$dbpass = 'rootpassword';
				$conn = mysql_connect($dbhost, $dbuser, $dbpass);
				if(! $conn )
				{
				  die('连接错误: ' . mysql_error());
				}
				echo '连接成功<br />';
				$sql = 'DROP DATABASE W3CSCHOOL';
				$retval = mysql_query( $sql, $conn );
				if(! $retval )
				{
				  die('删除数据库失败: ' . mysql_error());
				}
				echo "数据库 W3CSCHOOL 删除成功\n";
				mysql_close($conn);
				?>
				</body>
				</html>
				注意： 在使用PHP脚本删除数据库时，不会出现确认是否删除信息，会直接删除指定数据库，所以你在删除数据库时要特别小心。
	MySQL 选择数据库
		从MySQL命令提示窗口中选择MySQL数据库--use 数据库名;--后续的操作中都会在 该数据库中执行

			在 mysql> 提示窗口中可以很简单的选择特定的数据库。你可以使用SQL命令来选择指定的数据库。
			实例

				以下实例选取了数据库 W3CSCHOOL:
				[root@host]# mysql -u root -p
				Enter password:******
				mysql> use W3CSCHOOL;
				Database changed
				mysql>
			执行以上命令后，你就已经成功选择了 W3CSCHOOL 数据库，在后续的操作中都会在 W3CSCHOOL 数据库中执行。
			注意:所有的数据库名，表名，表字段都是区分大小写的。所以你在使用SQL命令时需要输入正确的名称。 
		使用PHP脚本选择MySQL数据库--bool mysql_select_db( db_name, connection )

			PHP 提供了函数 mysql_select_db 来选取一个数据库。函数在执行成功后返回 TRUE ，否则返回 FALSE 。
			语法

				bool mysql_select_db( db_name, connection );
			参数
				参数	            描述
				db_name	必需。规定要选择的数据库。
				connection	可选。规定 MySQL 连接。如果未指定，则使用上一个连接。
			实例

				以下实例展示了如何使用 mysql_select_db 函数来选取一个数据库：
				<html>
				<head>
				<meta charset="utf-8"> 
				<title>选择 MySQL 数据库</title>
				</head>
				<body>
				<?php
				$dbhost = 'localhost:3036';
				$dbuser = 'guest';
				$dbpass = 'guest123';
				$conn = mysql_connect($dbhost, $dbuser, $dbpass);
				if(! $conn )
				{
				  die('连接失败: ' . mysql_error());
				}
				echo '连接成功';
				mysql_select_db( 'W3CSCHOOL' );
				mysql_close($conn);
				?>
				</body>
				</html>
	MySQL 数据类型
		MySQL中定义数据字段的类型对数据库的优化是非常重要的。
		MySQL支持多种类型，大致可以分为三类：数值、日期/时间和 字符串(字符)类型。
		数据类型
			数值类型--MySQL支持所有标准SQL数值数据类型 
				这些类型包括 严格数值数据类型(INTEGER、SMALLINT、DECIMAL和NUMERIC)，以及近似数值数据类型(FLOAT、REAL和DOUBLE PRECISION)。
				关键字INT是INTEGER的同义词，关键字DEC是DECIMAL的同义词。
				BIT数据类型保存位字段值，并且支持MyISAM、MEMORY、InnoDB和BDB表。
				作为SQL标准的扩展，MySQL也支持整数类型TINYINT、MEDIUMINT和BIGINT。下面的表显示了需要的每个整数类型的存储和范围。
				类型	大小	范围（有符号）	范围（无符号）	用途
				TINYINT	1 字节	(-128，127)	(0，255)	小整数值
				SMALLINT	2 字节	(-32 768，32 767)	(0，65 535)	大整数值
				MEDIUMINT	3 字节	(-8 388 608，8 388 607)	(0，16 777 215)	大整数值
				INT或INTEGER	4 字节	(-2 147 483 648，2 147 483 647)	(0，4 294 967 295)	大整数值
				BIGINT	            8 字节	(-9 233 372 036 854 775 808，9 223 372 036 854 775 807)	(0，18 446 744 073 709 551 615)	极大整数值
				FLOAT	            4 字节	(-3.402 823 466 E+38，1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38)	0，(1.175 494 351 E-38，3.402 823 466 E+38)	单精度浮点数值
				DOUBLE	8 字节	(1.797 693 134 862 315 7 E+308，2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)	0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)	双精度浮点数值
				DECIMAL	对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2	依赖于M和D的值	依赖于M和D的值	小数值
			日期和时间类型

				表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。
				每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。
				TIMESTAMP类型有专有的自动更新特性，将在后面描述。
				类型	大小
				(字节)	范围	格式	用途
				DATE	3	1000-01-01/9999-12-31	YYYY-MM-DD	日期值
				TIME	3	'-838:59:59'/'838:59:59'	HH:MM:SS	时间值或持续时间
				YEAR	1	1901/2155	YYYY	年份值
				DATETIME	8	1000-01-01 00:00:00/9999-12-31 23:59:59	YYYY-MM-DD HH:MM:SS	混合日期和时间值
				TIMESTAMP	8	1970-01-01 00:00:00/2037 年某时	YYYYMMDD HHMMSS	混合日期和时间值，时间戳
			字符串类型

				字符串类型指CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET。该节描述了这些类型如何工作以及如何在查询中使用这些类型。
				类型	                大小                                            	用途
				CHAR	                0-255字节	                                    定长字符串
				VARCHAR	    0-65535 字节	                        变长字符串
				TINYBLOB	    0-255字节	                                    不超过 255 个字符的二进制字符串
				TINYTEXT	    0-255字节	                                    短文本字符串
				BLOB	                0-65 535字节	                        二进制形式的长文本数据
				TEXT	                0-65 535字节	                        长文本数据
				MEDIUMBLOB     0-16 777 215字节	                        二进制形式的中等长度文本数据
				MEDIUMTEXT	    0-16 777 215字节	                        中等长度文本数据
				LOGNGBLOB	    0-4 294 967 295字节	            二进制形式的极大文本数据
				LONGTEXT	    0-4 294 967 295字节	            极大文本数据
				CHAR和VARCHAR类型类似，但它们保存和检索的方式不同。它们的最大长度和是否尾部空格被保留等方面也不同。在存储或检索过程中不进行大小写转换。
				BINARY和VARBINARY类似于CHAR和VARCHAR，不同的是它们包含二进制字符串而不要非二进制字符串。也就是说，它们包含字节字符串而不是字符字符串。这说明它们没有字符集，并且排序和比较基于列值字节的数值值。
				BLOB是一个二进制对象，可以容纳可变数量的数据。有4种BLOB类型：TINYBLOB、BLOB、MEDIUMBLOB和LONGBLOB。它们只是可容纳值的最大长度不同。
				有4种TEXT类型：TINYTEXT、TEXT、MEDIUMTEXT和LONGTEXT。这些对应4种BLOB类型，有相同的最大长度和存储需求。
	MySQL 创建数据表
		创建MySQL数据表需要以下信息：
			表名
			表字段名
			定义每个表字段
		语法--CREATE TABLE 表名 (表字段名 表字段类型);
			创建MySQL数据表的SQL通用语法
			CREATE TABLE table_name (column_name column_type);
		以下例子中我们将在 W3CSCHOOL 数据库中创建数据表w3cschool_tbl：
			w3cschool_tbl(
			   w3cschool_id INT NOT NULL AUTO_INCREMENT,
			   w3cschool_title VARCHAR(100) NOT NULL,
			   w3cschool_author VARCHAR(40) NOT NULL,
			   submission_date DATE,
			   PRIMARY KEY ( w3cschool_id )
			);
		实例解析：
			如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。
			AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
			PRIMARY KEY关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。
			通过命令提示符创建表

			通过 mysql> 命令窗口可以很简单的创建MySQL数据表。你可以使用 SQL 语句 CREATE TABLE 来创建数据表。
		实例
			以下为创建数据表 w3cschool_tbl 实例:
			root@host# mysql -u root -p
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> CREATE TABLE w3cschool_tbl(
			   -> w3cschool_id INT NOT NULL AUTO_INCREMENT,
			   -> w3cschool_title VARCHAR(100) NOT NULL,
			   -> w3cschool_author VARCHAR(40) NOT NULL,
			   -> submission_date DATE,
			   -> PRIMARY KEY ( w3cschool_id )
			   -> );
			Query OK, 0 rows affected (0.16 sec)
			mysql>
			注意：MySQL命令终止符为分号 (;) 。
		使用PHP脚本创建数据表--bool mysql_query( sql, connection );

			你可以使用PHP的 mysql_query() 函数来创建已存在数据库的数据表。
				该函数有两个参数，在执行成功时返回 TRUE，否则返回 FALSE。
			语法
				bool mysql_query( sql, connection );
				参数	                描述
				sql	                必需。规定要发送的 SQL 查询。注释：查询字符串不应以分号结束。
				connection	    可选。规定 SQL 连接标识符。如果未规定，则使用上一个打开的连接。
			实例

				以下实例使用了PHP脚本来创建数据表：
				<html>
				<head>
				<meta charset="utf-8">
				<title>创建 MySQL 数据表</title>
				</head>
				<body>
				<?php
				$dbhost = 'localhost:3036';
				$dbuser = 'root';
				$dbpass = 'rootpassword';
				$conn = mysql_connect($dbhost, $dbuser, $dbpass);
				if(! $conn )
				{
				  die('Could not connect: ' . mysql_error());
				}
				echo 'Connected successfully<br />';
				$sql = "CREATE TABLE tutorials_tbl( ".
				       "tutorial_id INT NOT NULL AUTO_INCREMENT, ".
				       "tutorial_title VARCHAR(100) NOT NULL, ".
				       "tutorial_author VARCHAR(40) NOT NULL, ".
				       "submission_date DATE, ".
				       "PRIMARY KEY ( tutorial_id )); ";
				mysql_select_db( 'TUTORIALS' );
				$retval = mysql_query( $sql, $conn );
				if(! $retval )
				{
				  die('数据表创建失败: ' . mysql_error());
				}
				echo "数据表创建成功\n";
				mysql_close($conn);
				?>
				</body>
				</html>
	MySQL 删除数据表
		MySQL中删除数据表是非常容易操作的， 但是你在进行删除表操作时要非常小心，因为执行删除命令后所有数据都会消失。
		在mysql>命令提示窗口中删除数据表SQL语句为--DROP TABLE table_name;
			
			实例

				以下实例删除了数据表w3cschool_tbl:
				root@host# mysql -u root -p
				Enter password:*******
				mysql> use W3CSCHOOL;
				Database changed
				mysql> DROP TABLE w3cschool_tbl
				Query OK, 0 rows affected (0.8 sec)
				mysql>
		使用PHP脚本删除数据表--bool mysql_query( sql, connection );
			PHP使用 mysql_query 函数来删除 MySQL 数据表。
				该函数有两个参数，在执行成功时返回 TRUE，否则返回 FALSE。
			语法
				bool mysql_query( sql, connection );
				参数	描述
				sql	必需。规定要发送的 SQL 查询。注释：查询字符串不应以分号结束。
				connection	可选。规定 SQL 连接标识符。如果未规定，则使用上一个打开的连接。
			实例

				以下实例使用了PHP脚本删除数据表w3cschool_tbl:
				<html>
				<head>
				<meta charset="utf-8">
				<title>创建 MySQL 数据表</title>
				</head>
				<body>
				<?php
				$dbhost = 'localhost:3036';
				$dbuser = 'root';
				$dbpass = 'rootpassword';
				$conn = mysql_connect($dbhost, $dbuser, $dbpass);
				if(! $conn )
				{
				  die('连接失败: ' . mysql_error());
				}
				echo '连接成功<br />';
				$sql = "DROP TABLE w3cschool_tbl";
				mysql_select_db( 'W3CSCHOOL' );
				$retval = mysql_query( $sql, $conn );
				if(! $retval )
				{
				  die('数据表删除失败: ' . mysql_error());
				}
				echo "数据表删除成功\n";
				mysql_close($conn);
				?>
				</body>
				</html>
	MySQL 插入数据
		MySQL 表中使用 INSERT INTO SQL语句来插入数据。
		通过 mysql> 命令提示窗口中向数据表中插入数据
			语法
				以下为向MySQL数据表插入数据通用的 INSERT INTO SQL语法：
				INSERT INTO table_name ( field1, field2,...fieldN )
				                       VALUES
				                       ( value1, value2,...valueN );
				如果数据是字符型，必须使用单引号或者双引号，如："value"。
			实例

				以下实例中我们将向 w3cschool_tbl 表插入三条数据:
				root@host# mysql -u root -p password;
				Enter password:*******
				mysql> use W3CSCHOOL;
				Database changed
				mysql> INSERT INTO w3cschool_tbl 
				     ->(w3cschool_title, w3cschool_author, submission_date)
				     ->VALUES
				     ->("Learn PHP", "John Poul", NOW());
				Query OK, 1 row affected (0.01 sec)
				mysql> INSERT INTO w3cschool_tbl
				     ->(w3cschool_title, w3cschool_author, submission_date)
				     ->VALUES
				     ->("Learn MySQL", "Abdul S", NOW());
				Query OK, 1 row affected (0.01 sec)
				mysql> INSERT INTO w3cschool_tbl
				     ->(w3cschool_title, w3cschool_author, submission_date)
				     ->VALUES
				     ->("JAVA Tutorial", "Sanjay", '2007-05-06');
				Query OK, 1 row affected (0.01 sec)
				mysql>
				注意： 使用箭头标记(->)不是SQL语句的一部分，它仅仅表示一个新行，如果一条SQL语句太长，我们可以通过回车键来创建一个新行来编写SQL语句，SQL语句的命令结束符为分号（;）。
				在以上实例中，我们并没有提供 w3cschool_id 的数据，因为该字段我们在创建表的时候已经设置它为 AUTO_INCREMENT(自动增加) 属性。 所以，该字段会自动递增而不需要我们去设置。实例中 NOW() 是一个 MySQL 函数，该函数返回日期和时间。
		使用PHP脚本插入数据--bool mysql_query( sql, connection );
			语法

				bool mysql_query( sql, connection );
				参数	             描述
				sql	             必需。规定要发送的 SQL 查询。注释：查询字符串不应以分号结束。
				connection	 可选。规定 SQL 连接标识符。如果未规定，则使用上一个打开的连接。
			实例

				以下实例中程序接收用户输入的三个字段数据，并插入数据表中：
				<html>
				<head>
				<meta charset="utf-8">
				<title>向 MySQL 数据库添加数据</title>
				</head>
				<body>
				<?php
				if(isset($_POST['add']))
				{
				$dbhost = 'localhost:3036';
				$dbuser = 'root';
				$dbpass = 'rootpassword';
				$conn = mysql_connect($dbhost, $dbuser, $dbpass);
				if(! $conn )
				{
				  die('Could not connect: ' . mysql_error());
				}

				if(! get_magic_quotes_gpc() )
				{
				   $w3cschool_title = addslashes ($_POST['w3cschool_title']);
				   $w3cschool_author = addslashes ($_POST['w3cschool_author']);
				}
				else
				{
				   $w3cschool_title = $_POST['w3cschool_title'];
				   $w3cschool_author = $_POST['w3cschool_author'];
				}
				$submission_date = $_POST['submission_date'];

				$sql = "INSERT INTO w3cschool_tbl ".
				       "(w3cschool_title,w3cschool_author, submission_date) ".
				       "VALUES ".
				       "('$w3cschool_title','$w3cschool_author','$submission_date')";
				mysql_select_db('W3CSCHOOL');
				$retval = mysql_query( $sql, $conn );
				if(! $retval )
				{
				  die('Could not enter data: ' . mysql_error());
				}
				echo "Entered data successfully\n";
				mysql_close($conn);
				}
				else
				{
				?>
				<form method="post" action="<?php $_PHP_SELF ?>">
				<table width="600" border="0" cellspacing="1" cellpadding="2">
				<tr>
				<td width="250">Tutorial Title</td>
				<td>
				<input name="w3cschool_title" type="text" id="w3cschool_title">
				</td>
				</tr>
				<tr>
				<td width="250">Tutorial Author</td>
				<td>
				<input name="w3cschool_author" type="text" id="w3cschool_author">
				</td>
				</tr>
				<tr>
				<td width="250">Submission Date [ yyyy-mm-dd ]</td>
				<td>
				<input name="submission_date" type="text" id="submission_date">
				</td>
				</tr>
				<tr>
				<td width="250"> </td>
				<td> </td>
				</tr>
				<tr>
				<td width="250"> </td>
				<td>
				<input name="add" type="submit" id="add" value="Add Tutorial">
				</td>
				</tr>
				</table>
				</form>
				<?php
				}
				?>
				</body>
				</html>
				在我们接收用户提交的数据时，为了数据的安全性我们需要使用 get_magic_quotes_gpc() 函数来判断特殊字符的转义是否已经开启。如果这个选项为off（未开启），返回0，那么我们就必须调用addslashes 这个函数来为字符串增加转义。
				你也可以添加其他检查数据的方法，比如邮箱格式验证，电话号码验证，是否为整数验证等。
	MySQL 查询数据
		MySQL 数据库使用SQL SELECT语句来查询数据。
		通过 mysql> 命令提示窗口中在数据库中查询数据
		语法
			以下为在MySQL数据库中查询数据通用的 SELECT 语法：
			SELECT column_name,column_name
			FROM table_name
			[WHERE Clause]
			[OFFSET M ][LIMIT N]

			查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
			SELECT 命令可以读取一条或者多条记录。
			你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据
			你可以使用 WHERE 语句来包含任何条件。
			你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。
			你可以使用 LIMIT 属性来设定返回的记录数。
			通过命令提示符获取数据
		实例--通过 SQL SELECT 命令来获取 MySQL 数据表 w3cschool_tbl 的数据：

			以下实例将返回数据表w3cschool_tbl的所有记录:
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> SELECT * from w3cschool_tbl;
			+-------------+----------------+-----------------+-----------------+
			| w3cschool_id | w3cschool_title | w3cschool_author | submission_date |
			+-------------+----------------+-----------------+-----------------+
			|           1 | Learn PHP      | John Poul       | 2007-05-21      |
			|           2 | Learn MySQL    | Abdul S         | 2007-05-21      |
			|           3 | JAVA Tutorial  | Sanjay          | 2007-05-21      |
			+-------------+----------------+-----------------+-----------------+
			3 rows in set (0.01 sec)

			mysql>
		使用PHP脚本来获取数据
			使用PHP函数的mysql_query()及SQL SELECT命令来获取数据。
			该函数用于执行SQL命令，然后通过 PHP 函数 mysql_fetch_array() 来使用或输出所有查询的数据。
			mysql_fetch_array() 函数从结果集中取得一行作为关联数组，或数字数组，或二者兼有 返回根据从结果集取得的行生成的数组，如果没有更多行则返回 false。
			以下实例为从数据表 w3cschool_tbl 中读取所有记录。
			实例

			尝试以下实例来显示数据表 w3cschool_tbl 的所有记录。
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT w3cschool_id, w3cschool_title,
			               w3cschool_author, submission_date
			        FROM w3cschool_tbl';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
			{
			    echo "Tutorial ID :{$row['w3cschool_id']}  <br> ".
			         "Title: {$row['w3cschool_title']} <br> ".
			         "Author: {$row['w3cschool_author']} <br> ".
			         "Submission Date : {$row['submission_date']} <br> ".
			         "--------------------------------<br>";
			} 
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
			以上实例中，读取的每行记录赋值给变量$row，然后再打印出每个值。
			注意：记住如果你需要在字符串中使用变量，请将变量置于花括号。
			在上面的例子中，PHP mysql_fetch_array()函数第二个参数为MYSQL_ASSOC， 设置该参数查询结果返回关联数组，你可以使用字段名称来作为数组的索引。
			PHP提供了另外一个函数mysql_fetch_assoc(), 该函数从结果集中取得一行作为关联数组。 返回根据从结果集取得的行生成的关联数组，如果没有更多行，则返回 false。
			实例

			尝试以下实例，该实例使用了mysql_fetch_assoc()函数来输出数据表w3cschool_tbl的所有记录：
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT w3cschool_id, w3cschool_title,
			               w3cschool_author, submission_date
			        FROM w3cschool_tbl';
			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_assoc($retval))
			{
			    echo "Tutorial ID :{$row['w3cschool_id']}  <br> ".
			         "Title: {$row['w3cschool_title']} <br> ".
			         "Author: {$row['w3cschool_author']} <br> ".
			         "Submission Date : {$row['submission_date']} <br> ".
			         "--------------------------------<br>";
			} 
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
			你也可以使用常量 MYSQL_NUM 作为PHP mysql_fetch_array()函数的第二个参数，返回数字数组。
			实例

			以下实例使用MYSQL_NUM参数显示数据表w3cschool_tbl的所有记录:
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT w3cschool_id, w3cschool_title,
			               w3cschool_author, submission_date
			        FROM w3cschool_tbl';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_NUM))
			{
			    echo "Tutorial ID :{$row[0]}  <br> ".
			         "Title: {$row[1]} <br> ".
			         "Author: {$row[2]} <br> ".
			         "Submission Date : {$row[3]} <br> ".
			         "--------------------------------<br>";
			}
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
			以上三个实例输出结果都一样。
			内存释放

			在我们执行完SELECT语句后，释放游标内存是一个很好的习惯。 可以通过PHP函数mysql_free_result()来实现内存的释放。
			以下实例演示了该函数的使用方法。
			实例

			尝试以下实例:
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT w3cschool_id, w3cschool_title,
			               w3cschool_author, submission_date
			        FROM w3cschool_tbl';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_NUM))
			{
			    echo "Tutorial ID :{$row[0]}  <br> ".
			         "Title: {$row[1]} <br> ".
			         "Author: {$row[2]} <br> ".
			         "Submission Date : {$row[3]} <br> ".
			         "--------------------------------<br>";
			}
			mysql_free_result($retval);
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
	MySQL where 子句
		如需有条件地从表中选取数据，可将 WHERE 子句添加到 SELECT 语句中。
			语法

				以下是SQL SELECT 语句使用 WHERE 子句从数据表中读取数据的通用语法：
				SELECT field1, field2,...fieldN FROM table_name1, table_name2...
				[WHERE condition1 [AND [OR]] condition2.....

				查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
				你可以在WHERE子句中指定任何条件。
				你可以使用AND或者OR指定一个或多个条件。
				WHERE子句也可以运用于SQL的 DELETE 或者 UPDATE 命令。
				WHERE 子句类似于程序语言中的if条件，根据 MySQL 表中的字段值来读取指定的数据。
			以下为操作符列表，可用于 WHERE 子句中。
				下表中实例假定 A为10 B为20
				操作符	               描述	                                                                                                                                           实例
				=	               等号，检测两个值是否相等，如果相等返回true	                                                                                (A = B) 返回false。
				<> 或 !=	   不等于，检测两个值是否相等，如果不相等返回true	                                                                    (A != B) 返回 true。
				>	               大于号，检测左边的值是否大于右边的值, 如果左边的值大于右边的值返回true	                                (A > B) 返回false。
				<	               小于号，检测左边的值是否小于右边的值, 如果左边的值小于右边的值返回true	                                (A < B) 返回 true。
				>=	               大于等于号，检测左边的值是否大于或等于右边的值, 如果左边的值大于或等于右边的值返回true	        (A >= B) 返回false。
				<=	               小于等于号，检测左边的值是否小于于或等于右边的值, 如果左边的值小于或等于右边的值返回true        (A <= B) 返回 true。
				如果我们想再MySQL数据表中读取指定的数据，WHERE 子句是非常有用的。
				使用主键来作为 WHERE 子句的条件查询是非常快速的。
				如果给定的条件在表中没有任何匹配的记录，那么查询不会返回任何数据。
				从命令提示符中读取数据

				我们将在SQL SELECT语句使用WHERE子句来读取MySQL数据表 w3cschool_tbl 中的数据：
			实例
				以下实例将读取 w3cschool_tbl 表中 w3cschool_author 字段值为 Sanjay 的所有记录：
				root@host# mysql -u root -p password;
				Enter password:*******
				mysql> use W3CSCHOOL;
				Database changed
				mysql> SELECT * from w3cschool_tbl WHERE w3cschool_author='Sanjay';
				+-------------+----------------+-----------------+-----------------+
				| w3cschool_id | w3cschool_title | w3cschool_author | submission_date |
				+-------------+----------------+-----------------+-----------------+
				|           3 | JAVA Tutorial  | Sanjay          | 2007-05-21      |
				+-------------+----------------+-----------------+-----------------+
				1 rows in set (0.01 sec)

				mysql>
				除非你使用 LIKE 来比较字符串，否则MySQL的WHERE子句的字符串比较是不区分大小写的。 你可以使用 BINARY 关键字来设定WHERE子句的字符串比较是区分大小写的。
				如下实例
				root@host# mysql -u root -p password;
				Enter password:*******
				mysql> use W3CSCHOOL;
				Database changed
				mysql> SELECT * from w3cschool_tbl 
				          WHERE BINARY w3cschool_author='sanjay';
				Empty set (0.02 sec)

				mysql>
		使用PHP脚本读取数据
			你可以使用PHP函数的mysql_query()及相同的SQL SELECT 带上 WHERE 子句的命令来获取数据。
			该函数用于执行SQL命令，然后通过 PHP 函数 mysql_fetch_array() 来输出所有查询的数据。
			实例

			以下实例将从 w3cschool_tbl 表中返回使用 w3cschool_author 字段值为 Sanjay 的记录：
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT w3cschool_id, w3cschool_title,
			               w3cschool_author, submission_date
			        FROM w3cschool_tbl
			        WHERE w3cschool_author="Sanjay"';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
			{
			    echo "Tutorial ID :{$row['w3cschool_id']}  <br> ".
			         "Title: {$row['w3cschool_title']} <br> ".
			         "Author: {$row['w3cschool_author']} <br> ".
			         "Submission Date : {$row['submission_date']} <br> ".
			         "--------------------------------<br>";
			} 
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
	MySQL UPDATE 查询
		语法

			以下是 UPDATE 命令修改 MySQL 数据表数据的通用SQL语法：
			UPDATE table_name SET field1=new-value1, field2=new-value2
			[WHERE Clause]
			你可以同时更新一个或多个字段。
			你可以在 WHERE 子句中指定任何条件。
			你可以在一个单独表中同时更新数据。
			当你需要更新数据表中指定行的数据时 WHERE 子句是非常有用的。
		通过命令提示符更新数据
			以下我们将在 SQL UPDATE 命令使用 WHERE子句来更新w3cschool_tbl表中指定的数据：
			实例

				以下实例将更新数据表中 w3cschool_id 为 2 的 w3cschool_title 字段值：
				root@host# mysql -u root -p password;
				Enter password:*******
				mysql> use W3CSCHOOL;
				Database changed
				mysql> update w3cschool_tbl
				    -> set w3cschool_title='learning java'
				    -> where w3cschool_id=2;
				Query OK, 1 row affected (0.14 sec)
				Rows matched: 1  Changed: 1  Warnings: 0

				mysql>
		使用PHP脚本更新数据
			PHP中使用函数mysql_query()来执行SQL语句，你可以在SQL UPDATE语句中使用或者不使用WHERE子句。
			该函数与在mysql>命令提示符中执行SQL语句的效果是一样的。
			实例

			以下实例将更新 w3cschool_id 为3的 w3cschool_title 字段的数据。
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			} 
			$sql = 'UPDATE w3cschool_tbl
			        SET w3cschool_title="Learning JAVA"
			        WHERE w3cschool_id=3';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not update data: ' . mysql_error());
			}
			echo "Updated data successfully\n";
			mysql_close($conn);
			?>
	MySQL DELETE 语句
		使用 SQL 的 DELETE FROM 命令来删除 MySQL 数据表中的记录。

		语法

			以下是SQL DELETE 语句从MySQL数据表中删除数据的通用语法：
			DELETE FROM table_name [WHERE Clause]
			如果没有指定 WHERE 子句，MySQL表中的所有记录将被删除。
			你可以在 WHERE 子句中指定任何条件
			您可以在单个表中一次性删除记录。
			当你想删除数据表中指定的记录时 WHERE 子句是非常有用的。
		在mysql>命令提示符中删除数据
		这里我们将在 SQL DELETE 命令中使用 WHERE 子句来删除MySQL数据表w3cschool_tbl所选的数据。
		实例

			以下实例将删除 w3cschool_tbl 表中 w3cschool_id 为 3 的记录：
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> DELETE FROM w3cschool_tbl WHERE w3cschool_id=3;
			Query OK, 1 row affected (0.23 sec)

			mysql>
		使用 PHP 脚本删除数据

			PHP使用 mysql_query() 函数来执行SQL语句， 你可以在SQL DELETE命令中使用或不使用 WHERE 子句。
			该函数与 mysql>命令符执行SQL命令的效果是一样的。
			实例

			以下PHP实例将删除w3cschool_tbl表中w3cschool_id为3的记录:
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'DELETE FROM w3cschool_tbl
			        WHERE w3cschool_id=3';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not delete data: ' . mysql_error());
			}
			echo "Deleted data successfully\n";
			mysql_close($conn);
			?>
	MySQL LIKE 子句
		在MySQL中使用 SQL SELECT 命令来读取数据， 同时可以在 SELECT 语句中使用 WHERE 子句来获取指定的记录。
		WHERE 子句中可以使用等号 (=) 来设定获取数据的条件，如 "w3cschool_author = 'Sanjay'"。
		但是有时候我们需要获取 w3cschool_author 字段含有 "jay" 字符的所有记录，这时我们就需要在 WHERE 子句中使用 SQL LIKE 子句。
		SQL LIKE 子句中使用百分号(%)字符来表示任意字符，类似于UNIX或正则表达式中的星号 (*)。
		如果没有使用百分号(%), LIKE 子句与等号（=）的效果是一样的。
		语法

			以下是SQL SELECT 语句使用 LIKE 子句从数据表中读取数据的通用语法：
			SELECT field1, field2,...fieldN table_name1, table_name2...
			WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
			你可以在WHERE子句中指定任何条件。
			你可以在WHERE子句中使用LIKE子句。
			你可以使用LIKE子句代替等号(=)。
			LIKE 通常与 % 一同使用，类似于一个元字符的搜索。
			你可以使用AND或者OR指定一个或多个条件。
			你可以在 DELETE 或 UPDATE 命令中使用 WHERE...LIKE 子句来指定条件。
		在命令提示符中使用 LIKE 子句
		实例--以下我们将在 SQL SELECT 命令中使用 WHERE...LIKE 子句来从MySQL数据表 w3cschool_tbl 中读取数据

			以下是我们将w3cschool_tbl表中获取w3cschool_author字段中以"jay"为结尾的的所有记录：
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> SELECT * from w3cschool_tbl;
			    -> WHERE w3cschool_author LIKE '%jay';
			+--------------+-----------------+------------------+-----------------+
			| w3cschool_id | w3cschool_title | w3cschool_author | submission_date |
			+--------------+-----------------+------------------+-----------------+
			|            2 | learning java   | Sanjay           | 2007-05-06      |
			+--------------+-----------------+------------------+-----------------+
			1 row in set (0.00 sec)

			mysql>
		在PHP脚本中使用 LIKE 子句

			你可以使用PHP函数的mysql_query()及相同的SQL SELECT 带上 WHERE...LIKE 子句的命令来获取数据。
			该函数用于执行SQL命令，然后通过 PHP 函数 mysql_fetch_array() 来输出所有查询的数据。
			但是如果是DELETE或者UPDATE中使用 WHERE...LIKE 子句的SQL语句，则无需使用mysql_fetch_array() 函数。
			实例

			以下是我们使用PHP脚本在w3cschool_tbl表中读取w3cschool_author字段中以"jay"为结尾的的所有记录：
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT w3cschool_id, w3cschool_title,
			               w3cschool_author, submission_date
			        FROM w3cschool_tbl
			        WHERE w3cschool_author LIKE "%jay%"';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
			{
			    echo "Tutorial ID :{$row['w3cschool_id']}  <br> ".
			         "Title: {$row['w3cschool_title']} <br> ".
			         "Author: {$row['w3cschool_author']} <br> ".
			         "Submission Date : {$row['submission_date']} <br> ".
			         "--------------------------------<br>";
			} 
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
	MySQL 排序
		我们知道从MySQL表中使用SQL SELECT 语句来读取数据。
		如果我们需要对读取的数据进行排序，我们就可以使用MySQL的 ORDER BY 子句来设定你想按哪个字段哪中方式来进行排序，再返回搜索结果。
		本章节使用的数据库结构及数据下载：MySQL.sql
		语法

			以下是SQL SELECT 语句使用 ORDER BY 子句将查询数据排序后再返回数据：
			SELECT field1, field2,...fieldN table_name1, table_name2...
			ORDER BY field1, [field2...] [ASC [DESC]]
			你可以使用任何字段来作为排序的条件，从而返回排序后的查询结果。
			你可以设定多个字段来排序。
			你可以使用 ASC 或 DESC 关键字来设置查询结果是按升序或降序排列。 默认情况下，它是按升排列。
			你可以添加 WHERE...LIKE 子句来设置条件。
			在命令提示符中使用 ORDER BY 子句
		实例--以下将在 SQL SELECT 语句中使用 ORDER BY 子句来读取MySQL 数据表 w3cschool_tbl 中的数据：

			尝试以下实例，结果将按升序排列
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> SELECT * from w3cschool_tbl ORDER BY w3cschool_author ASC;
			+-------------+----------------+-----------------+-----------------+
			| w3cschool_id | w3cschool_title | w3cschool_author | submission_date |
			+-------------+----------------+-----------------+-----------------+
			|           2 | Learn MySQL    | Abdul S         | 2007-05-24      |
			|           1 | Learn PHP      | John Poul       | 2007-05-24      |
			|           3 | JAVA Tutorial  | Sanjay          | 2007-05-06      |
			+-------------+----------------+-----------------+-----------------+
			3 rows in set (0.00 sec)

			mysql> SELECT * from w3cschool_tbl ORDER BY w3cschool_author DESC;
			+-----------+------------------+-----------------+-----------------+
			| w3cschool_id | w3cschool_title | w3cschool_author | submission_date |
			+-----------+------------------+-----------------+-----------------+
			|         3 | JAVA Tutorial    | Sanjay          | 2007-05-06      |
			|         1 | Learn PHP        | John Poul       | 2007-05-24      |
			|         2 | Learn MySQL      | Abdul S         | 2007-05-24      |
			3 rows in set (0.00 sec)

			mysql>
			读取 w3cschool_tbl 表中所有数据并按 w3cschool_author 字段的升序排列。
		在PHP脚本中使用 ORDER BY 子句

			你可以使用PHP函数的mysql_query()及相同的SQL SELECT 带上 ORDER BY 子句的命令来获取数据。 该函数用于执行SQL命令，然后通过 PHP 函数 mysql_fetch_array() 来输出所有查询的数据。
			实例

			尝试以下实例，查询后的数据按 w3cschool_author 字段的降序排列后返回。
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT w3cschool_id, w3cschool_title,
			               w3cschool_author, submission_date
			        FROM w3cschool_tbl
			        ORDER BY  w3cschool_author DESC';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
			{
			    echo "Tutorial ID :{$row['w3cschool_id']}  <br> ".
			         "Title: {$row['w3cschool_title']} <br> ".
			         "Author: {$row['w3cschool_author']} <br> ".
			         "Submission Date : {$row['submission_date']} <br> ".
			         "--------------------------------<br>";
			} 
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
	MySQL GROUP BY 语句
		GROUP BY 语句根据一个或多个列对结果集进行分组。
		在分组的列上我们可以使用 COUNT, SUM, AVG,等函数。
		GROUP BY 语法

				SELECT column_name, function(column_name)
				FROM table_name
				WHERE column_name operator value
				GROUP BY column_name;
		实例演示--本章节实例使用到了以下表结构及数据，使用前我们可以先将以下数据导入数据库中。

			SET NAMES utf8;
			SET FOREIGN_KEY_CHECKS = 0;

			-- ----------------------------
			--  Table structure for `employee_tbl`
			-- ----------------------------
			DROP TABLE IF EXISTS `employee_tbl`;
			CREATE TABLE `employee_tbl` (
			  `id` int(11) NOT NULL,
			  `name` char(10) NOT NULL DEFAULT '',
			  `date` datetime NOT NULL,
			  `singin` tinyint(4) NOT NULL DEFAULT '0' COMMENT '登录次数',
			  PRIMARY KEY (`id`)
			) ENGINE=InnoDB DEFAULT CHARSET=utf8;

			-- ----------------------------
			--  Records of `employee_tbl`
			-- ----------------------------
			BEGIN;
			INSERT INTO `employee_tbl` VALUES ('1', '小明', '2016-04-22 15:25:33', '1'), ('2', '小王', '2016-04-20 15:25:47', '3'), ('3', '小丽', '2016-04-19 15:26:02', '2'), ('4', '小王', '2016-04-07 15:26:14', '4'), ('5', '小明', '2016-04-11 15:26:40', '4'), ('6', '小明', '2016-04-04 15:26:54', '2');
			COMMIT;

			SET FOREIGN_KEY_CHECKS = 1;
			导入成功后，执行以下 SQL 语句：
			mysql> set names utf8;
			mysql> SELECT * FROM employee_tbl;
			+----+--------+---------------------+--------+
			| id | name   | date                | singin |
			+----+--------+---------------------+--------+
			|  1 | 小明 | 2016-04-22 15:25:33 |      1 |
			|  2 | 小王 | 2016-04-20 15:25:47 |      3 |
			|  3 | 小丽 | 2016-04-19 15:26:02 |      2 |
			|  4 | 小王 | 2016-04-07 15:26:14 |      4 |
			|  5 | 小明 | 2016-04-11 15:26:40 |      4 |
			|  6 | 小明 | 2016-04-04 15:26:54 |      2 |
			+----+--------+---------------------+--------+
			6 rows in set (0.00 sec)
		接下来我们使用 GROUP BY 语句 将数据表按名字进行分组，并统计每个人有多少条记录：
			mysql> SELECT name, COUNT(*) FROM   employee_tbl GROUP BY name;
			+--------+----------+
			| name   | COUNT(*) |
			+--------+----------+
			| 小丽 |        1 |
			| 小明 |        3 |
			| 小王 |        2 |
			+--------+----------+
			3 rows in set (0.01 sec)

		使用 WITH ROLLUP

			WITH ROLLUP 可以实现在分组统计数据基础上再进行相同的统计（SUM,AVG,COUNT…）。
			例如我们将以上的数据表按名字进行分组，再统计每个人登录的次数：
			mysql> SELECT name, SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
			+--------+--------------+
			| name   | singin_count |
			+--------+--------------+
			| 小丽 |            2 |
			| 小明 |            7 |
			| 小王 |            7 |
			| NULL   |           16 |
			+--------+--------------+
			4 rows in set (0.00 sec)
			其中记录 NULL 表示所有人的登录次数。
			我们可以使用 coalesce 来设置一个可以取代 NUll 的名称，coalesce 语法：
			select coalesce(a,b,c);
			参数说明：如果a==null,则选择b；如果b==null,则选择c；如果a!=null,则选择a；如果a b c 都为null ，则返回为null（没意义）。
			以下实例中如果名字为空我们使用总数代替：
			mysql> SELECT coalesce(name, '总数'), SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
			+--------------------------+--------------+
			| coalesce(name, '总数') | singin_count |
			+--------------------------+--------------+
			| 小丽                   |            2 |
			| 小明                   |            7 |
			| 小王                   |            7 |
			| 总数                   |           16 |
			+--------------------------+--------------+
			4 rows in set (0.01 sec)
	MySQL 连接的使用
		如何使用 MySQL 的 JOIN 在两个或多个表中查询数据。
		可以在SELECT, UPDATE 和 DELETE 语句中使用 Mysql 的 JOIN 来联合多表查询。
		JOIN 按照功能大致分为如下三类：
				INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
				LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
				RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。
		本章节使用的数据库结构及数据下载：W3CSCHOOL.sql。
		在命令提示符中使用 INNER JOIN
			实例--我们在W3CSCHOOL数据库中有两张表 tcount_tbl 和 w3cschool_tbl。两张数据表数据如下：

			尝试以下实例：
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> SELECT * FROM tcount_tbl;
			+-----------------+----------------+
			| w3cschool_author | w3cschool_count |
			+-----------------+----------------+
			| mahran          |             20 |
			| mahnaz          |           NULL |
			| Jen             |           NULL |
			| Gill            |             20 |
			| John Poul       |              1 |
			| Sanjay          |              1 |
			+-----------------+----------------+
			6 rows in set (0.01 sec)
			mysql> SELECT * from w3cschool_tbl;
			+-------------+----------------+-----------------+-----------------+
			| w3cschool_id | w3cschool_title | w3cschool_author | submission_date |
			+-------------+----------------+-----------------+-----------------+
			|           1 | Learn PHP      | John Poul       | 2007-05-24      |
			|           2 | Learn MySQL    | Abdul S         | 2007-05-24      |
			|           3 | JAVA Tutorial  | Sanjay          | 2007-05-06      |
			+-------------+----------------+-----------------+-----------------+
			3 rows in set (0.00 sec)
			mysql>
			接下来我们就使用MySQL的INNER JOIN(也可以省略 INNER 使用 JOIN，效果一样)来连接以上两张表来读取w3cschool_tbl表中所有w3cschool_author字段在tcount_tbl表对应的w3cschool_count字段值：
			mysql> SELECT a.w3cschool_id, a.w3cschool_author, b.w3cschool_count FROM w3cschool_tbl a INNER JOIN tcount_tbl b ON a.w3cschool_author = b.w3cschool_author;
			+-----------+---------------+--------------+
			| w3cschool_id | w3cschool_author | w3cschool_count |
			+-----------+---------------+--------------+
			|         1 | John Poul     |            1 |
			|         3 | Sanjay        |            1 |
			+-----------+---------------+--------------+
			2 rows in set (0.00 sec)
			以上 SQL 语句等价于：
			mysql> SELECT a.w3cschool_id, a.w3cschool_author, b.w3cschool_count FROM w3cschool_tbl a, tcount_tbl b WHERE a.w3cschool_author = b.w3cschool_author;
			+-------------+-----------------+----------------+
			| w3cschool_id | w3cschool_author | w3cschool_count |
			+-------------+-----------------+----------------+
			|           1 | John Poul       |              1 |
			|           3 | Sanjay          |              1 |
			+-------------+-----------------+----------------+
			2 rows in set (0.01 sec)
			mysql>
		MySQL LEFT JOIN

			MySQL left join 与 join 有所不同。 MySQL LEFT JOIN 会读取左边数据表的全部数据，即便右边表无对应数据。
			实例

			尝试以下实例，以 w3cschool_tbl 为左表，tcount_tbl 为右表，理解MySQL LEFT JOIN的应用：
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> SELECT a.w3cschool_id, a.w3cschool_author, b.w3cschool_count FROM w3cschool_tbl a LEFT JOIN tcount_tbl b ON a.w3cschool_author = b.w3cschool_author;
			+-------------+-----------------+----------------+
			| w3cschool_id | w3cschool_author | w3cschool_count |
			+-------------+-----------------+----------------+
			|           1 | John Poul       |              1 |
			|           2 | Abdul S         |           NULL |
			|           3 | Sanjay          |              1 |
			+-------------+-----------------+----------------+
			3 rows in set (0.02 sec)
			以上实例中使用了LEFT JOIN，该语句会读取左边的数据表w3cschool_tbl的所有选取的字段数据，即便在右侧表tcount_tbl中没有对应的w3cschool_author字段值。
		MySQL RIGHT JOIN

			MySQL RIGHT JOIN 会读取右边数据表的全部数据，即便左边边表无对应数据。
			实例

			尝试以下实例，以 tcount_tbl 为左表，w3cschool_tbl 为右表，理解MySQL RIGHT JOIN的应用：
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> SELECT b.w3cschool_id, b.w3cschool_author, a.w3cschool_count FROM tcount_tbl a RIGHT JOIN w3cschool_tbl b ON a.w3cschool_author = b.w3cschool_author;
			+-------------+-----------------+----------------+
			| w3cschool_id | w3cschool_author | w3cschool_count |
			+-------------+-----------------+----------------+
			|           1 | John Poul       |              1 |
			|           2 | Abdul S         |           NULL |
			|           3 | Sanjay          |              1 |
			+-------------+-----------------+----------------+
			3 rows in set (0.02 sec)
			以上实例中使用了 RIGHT JOIN，该语句会读取右边的数据表 w3cschool_tbl 的所有选取的字段数据，即便在左侧表tcount_tbl中没有对应的w3cschool_author字段值。
		在PHP脚本中使用JOIN

			PHP 中使用mysql_query()函数来执行SQL语句，你可以使用以上的相同的SQL语句作为mysql_query()函数的参数。
			尝试如下实例:
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			$sql = 'SELECT a.w3cschool_id, a.w3cschool_author, b.w3cschool_count FROM w3cschool_tbl a INNER JOIN tcount_tbl b ON a.w3cschool_author = b.w3cschool_author';

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
			{
			    echo "Author:{$row['w3cschool_author']}  <br> ".
			         "Count: {$row['w3cschool_count']} <br> ".
			         "Tutorial ID: {$row['w3cschool_id']} <br> ".
			         "--------------------------------<br>";
			} 
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
	MySQL NULL 值处理
		我们已经知道MySQL使用 SQL SELECT 命令及 WHERE 子句来读取数据表中的数据,但是当提供的查询条件字段为 NULL 时，该命令可能就无法正常工作。
		为了处理这种情况，MySQL提供了三大运算符:
				IS NULL: 当列的值是NULL,此运算符返回true。
				IS NOT NULL: 当列的值不为NULL, 运算符返回true。
				<=>: 比较操作符（不同于=运算符），当比较的的两个值为NULL时返回true。
				关于 NULL 的条件比较运算是比较特殊的。你不能使用 = NULL 或 != NULL 在列中查找 NULL 值 。
				在MySQL中，NULL值与任何其它值的比较（即使是NULL）永远返回false，即 NULL = NULL 返回false 。
				MySQL中处理NULL使用IS NULL和IS NOT NULL运算符。
		在命令提示符中使用 NULL 值
			以下实例中假设数据库 W3CSCHOOL 中的表 tcount_tbl 含有两列 w3cschool_author 和 w3cschool_count, w3cschool_count 中设置插入NULL值。
			实例

			尝试以下实例:
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> create table tcount_tbl
			    -> (
			    -> w3cschool_author varchar(40) NOT NULL,
			    -> w3cschool_count  INT
			    -> );
			Query OK, 0 rows affected (0.05 sec)
			mysql> INSERT INTO tcount_tbl
			    -> (w3cschool_author, w3cschool_count) values ('mahran', 20);
			mysql> INSERT INTO tcount_tbl
			    -> (w3cschool_author, w3cschool_count) values ('mahnaz', NULL);
			mysql> INSERT INTO tcount_tbl
			    -> (w3cschool_author, w3cschool_count) values ('Jen', NULL);
			mysql> INSERT INTO tcount_tbl
			    -> (w3cschool_author, w3cschool_count) values ('Gill', 20);

			mysql> SELECT * from tcount_tbl;
			+-----------------+----------------+
			| w3cschool_author | w3cschool_count |
			+-----------------+----------------+
			| mahran          |             20 |
			| mahnaz          |           NULL |
			| Jen             |           NULL |
			| Gill            |             20 |
			+-----------------+----------------+
			4 rows in set (0.00 sec)

			mysql>
			以下实例中你可以看到 = 和 != 运算符是不起作用的：
			mysql> SELECT * FROM tcount_tbl WHERE w3cschool_count = NULL;
			Empty set (0.00 sec)
			mysql> SELECT * FROM tcount_tbl WHERE w3cschool_count != NULL;
			Empty set (0.01 sec)
			查找数据表中 w3cschool_count 列是否为 NULL，必须使用IS NULL和IS NOT NULL，如下实例：
			mysql> SELECT * FROM tcount_tbl 
			    -> WHERE w3cschool_count IS NULL;
			+-----------------+----------------+
			| w3cschool_author | w3cschool_count |
			+-----------------+----------------+
			| mahnaz          |           NULL |
			| Jen             |           NULL |
			+-----------------+----------------+
			2 rows in set (0.00 sec)
			mysql> SELECT * from tcount_tbl 
			    -> WHERE w3cschool_count IS NOT NULL;
			+-----------------+----------------+
			| w3cschool_author | w3cschool_count |
			+-----------------+----------------+
			| mahran          |             20 |
			| Gill            |             20 |
			+-----------------+----------------+
			2 rows in set (0.00 sec)
		使用PHP脚本处理 NULL 值

			PHP脚本中你可以在 if...else 语句来处理变量是否为空，并生成相应的条件语句。
			以下实例中PHP设置了$w3cschool_count变量，然后使用该变量与数据表中的 w3cschool_count 字段进行比较：
			<?php
			$dbhost = 'localhost:3036';
			$dbuser = 'root';
			$dbpass = 'rootpassword';
			$conn = mysql_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			  die('Could not connect: ' . mysql_error());
			}
			if( isset($w3cschool_count ))
			{
			   $sql = 'SELECT w3cschool_author, w3cschool_count
			           FROM  tcount_tbl
			           WHERE w3cschool_count = $w3cschool_count';
			}
			else
			{
			   $sql = 'SELECT w3cschool_author, w3cschool_count
			           FROM  tcount_tbl
			           WHERE w3cschool_count IS $w3cschool_count';
			}

			mysql_select_db('W3CSCHOOL');
			$retval = mysql_query( $sql, $conn );
			if(! $retval )
			{
			  die('Could not get data: ' . mysql_error());
			}
			while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
			{
			    echo "Author:{$row['w3cschool_author']}  <br> ".
			         "Count: {$row['w3cschool_count']} <br> ".
			         "--------------------------------<br>";
			} 
			echo "Fetched data successfully\n";
			mysql_close($conn);
			?>
	MySQL 正则表达式
		在前面的章节我们已经了解到MySQL可以通过 LIKE ...% 来进行模糊匹配。
		MySQL 同样也支持其他正则表达式的匹配， MySQL中使用 REGEXP 操作符来进行正则表达式匹配。
			如果您了解PHP或Perl，那么操作起来就非常简单，因为MySQL的正则表达式匹配与这些脚本的类似。
		下表中的正则模式可应用于 REGEXP 操作符中。
			模式	描述
			^	匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。
			$	匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。
			.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
			[...]	字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
			[^...]	负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'。
			p1|p2|p3	匹配 p1 或 p2 或 p3。例如，'z|food' 能匹配 "z" 或 "food"。'(z|f)ood' 则匹配 "zood" 或 "food"。
			*	匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
			+	匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
			{n}	n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
			{n,m}	m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。
		实例

			了解以上的正则需求后，我们就可以更加自己的需求来编写带有正则表达式的SQL语句。以下我们将列出几个小实例(表名：person_tbl )来加深我们的理解：
			查找name字段中以'st'为开头的所有数据：
			mysql> SELECT name FROM person_tbl WHERE name REGEXP '^st';
			查找name字段中以'ok'为结尾的所有数据：
			mysql> SELECT name FROM person_tbl WHERE name REGEXP 'ok$';
			查找name字段中包含'mar'字符串的所有数据：
			mysql> SELECT name FROM person_tbl WHERE name REGEXP 'mar';
			查找name字段中以元音字符开头且以'ok'字符串结尾的所有数据：
			mysql> SELECT name FROM person_tbl WHERE name REGEXP '^[aeiou]|ok$';
	MySQL 事务
		MySQL 事务主要用于处理操作量大，复杂度高的数据。比如说，在人员管理系统中，你删除一个人员，你即需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，这样，这些数据库操作语句就构成一个事务！
		在MySQL中只有使用了Innodb数据库引擎的数据库或表才支持事务
		事务处理可以用来维护数据库的完整性，保证成批的SQL语句要么全部执行，要么全部不执行
		事务用来管理insert,update,delete语句
		一般来说，事务是必须满足4个条件（ACID）： Atomicity（原子性）、Consistency（稳定性）、Isolation（隔离性）、Durability（可靠性）
			1、事务的原子性：一组事务，要么成功；要么撤回。
			2、稳定性 ： 有非法数据（外键约束之类），事务撤回。
			3、隔离性：事务独立运行。一个事务处理后的结果，影响了其他事务，那么其他事务会撤回。事务的100%隔离，需要牺牲速度。
			4、可靠性：软、硬件崩溃后，InnoDB数据表驱动会利用日志文件重构修改。可靠性和高速度不可兼得， innodb_flush_log_at_trx_commit选项 决定什么时候吧事务保存到日志里。
		在MySQL控制台使用事务来操作

			1，开始一个事务
			start transaction
			2, 做保存点
			savepoint 保存点名称
			3, 操作
			4，可以回滚，可以提交，没有问题，就提交，有问题就回滚。
		PHP中使用事务实例

			<?php
			$handler=mysql_connect("localhost","root","password");
			mysql_select_db("task");
			mysql_query("SET AUTOCOMMIT=0");//设置为不自动提交，因为MYSQL默认立即执行 mysql_query("BEGIN");//开始事务定义
			if(!mysql_query("insert into trans (id) values('2')"))
			{
			mysql_query("ROOLBACK");//判断当执行失败时回滚
			}
			if(!mysql_query("insert into trans (id) values('4')"))
			{
			mysql_query("ROOLBACK");//判断执行失败回滚
			}
			mysql_query("COMMIT");//执行事务
			mysql_close($handler);
			?>
	MySQL ALTER命令
		当我们需要修改数据表名或者修改数据表字段时，就需要使用到MySQL ALTER命令。
		开始本章教程前让我们先创建一张表，表名为：testalter_tbl。
			root@host# mysql -u root -p password;
			Enter password:*******
			mysql> use W3CSCHOOL;
			Database changed
			mysql> create table testalter_tbl
			    -> (
			    -> i INT,
			    -> c CHAR(1)
			    -> );
			Query OK, 0 rows affected (0.05 sec)
			mysql> SHOW COLUMNS FROM testalter_tbl;
			+-------+---------+------+-----+---------+-------+
			| Field | Type    | Null | Key | Default | Extra |
			+-------+---------+------+-----+---------+-------+
			| i     | int(11) | YES  |     | NULL    |       |
			| c     | char(1) | YES  |     | NULL    |       |
			+-------+---------+------+-----+---------+-------+
			2 rows in set (0.00 sec)
		删除，添加或修改表字段

			如下命令使用了 ALTER 命令及 DROP 子句来删除以上创建表的 i 字段：
			mysql> ALTER TABLE testalter_tbl  DROP i;
			如果数据表中只剩余一个字段则无法使用DROP来删除字段。
			MySQL 中使用 ADD 子句来想数据表中添加列，如下实例在表 testalter_tbl 中添加 i 字段，并定义数据类型:
			mysql> ALTER TABLE testalter_tbl ADD i INT;
			执行以上命令后，i 字段会自动添加到数据表字段的末尾。
			mysql> SHOW COLUMNS FROM testalter_tbl;
			+-------+---------+------+-----+---------+-------+
			| Field | Type    | Null | Key | Default | Extra |
			+-------+---------+------+-----+---------+-------+
			| c     | char(1) | YES  |     | NULL    |       |
			| i     | int(11) | YES  |     | NULL    |       |
			+-------+---------+------+-----+---------+-------+
			2 rows in set (0.00 sec)
			如果你需要指定新增字段的位置，可以使用MySQL提供的关键字 FIRST (设定位第一列)， AFTER 字段名（设定位于某个字段之后）。
			尝试以下 ALTER TABLE 语句, 在执行成功后，使用 SHOW COLUMNS 查看表结构的变化：
			ALTER TABLE testalter_tbl DROP i;
			ALTER TABLE testalter_tbl ADD i INT FIRST;
			ALTER TABLE testalter_tbl DROP i;
			ALTER TABLE testalter_tbl ADD i INT AFTER c;
			FIRST 和 AFTER 关键字只占用于 ADD 子句，所以如果你想重置数据表字段的位置就需要先使用 DROP 删除字段然后使用 ADD 来添加字段并设置位置。
		修改字段类型及名称

			如果需要修改字段类型及名称, 你可以在ALTER命令中使用 MODIFY 或 CHANGE 子句 。
			例如，把字段 c 的类型从 CHAR(1) 改为 CHAR(10)，可以执行以下命令:
			mysql> ALTER TABLE testalter_tbl MODIFY c CHAR(10);
			使用 CHANGE 子句, 语法有很大的不同。 在 CHANGE 关键字之后，紧跟着的是你要修改的字段名，然后指定新字段的类型及名称。尝试如下实例：
			mysql> ALTER TABLE testalter_tbl CHANGE i j BIGINT;
			<p如果你现在想把字段 j 从 BIGINT 修改为 INT，SQL语句如下：
			mysql> ALTER TABLE testalter_tbl CHANGE j j INT;
			ALTER TABLE 对 Null 值和默认值的影响

			当你修改字段时，你可以指定是否包含只或者是否设置默认值。
			以下实例，指定字段 j 为 NOT NULL 且默认值为100 。
			mysql> ALTER TABLE testalter_tbl 
			    -> MODIFY j BIGINT NOT NULL DEFAULT 100;
			如果你不设置默认值，MySQL会自动设置该字段默认为 NULL。
		修改字段默认值

			你可以使用 ALTER 来修改字段的默认值，尝试以下实例：
			mysql> ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
			mysql> SHOW COLUMNS FROM testalter_tbl;
			+-------+---------+------+-----+---------+-------+
			| Field | Type    | Null | Key | Default | Extra |
			+-------+---------+------+-----+---------+-------+
			| c     | char(1) | YES  |     | NULL    |       |
			| i     | int(11) | YES  |     | 1000    |       |
			+-------+---------+------+-----+---------+-------+
			2 rows in set (0.00 sec)
			你也可以使用 ALTER 命令及 DROP子句来删除字段的默认值，如下实例：
			mysql> ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;
			mysql> SHOW COLUMNS FROM testalter_tbl;
			+-------+---------+------+-----+---------+-------+
			| Field | Type    | Null | Key | Default | Extra |
			+-------+---------+------+-----+---------+-------+
			| c     | char(1) | YES  |     | NULL    |       |
			| i     | int(11) | YES  |     | NULL    |       |
			+-------+---------+------+-----+---------+-------+
			2 rows in set (0.00 sec)
			Changing a Table Type:
		修改数据表类型，可以使用 ALTER 命令及 TYPE 子句来完成。尝试以下实例，我们将表 testalter_tbl 的类型修改为 MYISAM ：
			注意：查看数据表类型可以使用 SHOW TABLE STATUS 语句。
			mysql> ALTER TABLE testalter_tbl TYPE = MYISAM;
			mysql>  SHOW TABLE STATUS LIKE 'testalter_tbl'\G
			*************************** 1. row ****************
			           Name: testalter_tbl
			           Type: MyISAM
			     Row_format: Fixed
			           Rows: 0
			 Avg_row_length: 0
			    Data_length: 0
			Max_data_length: 25769803775
			   Index_length: 1024
			      Data_free: 0
			 Auto_increment: NULL
			    Create_time: 2007-06-03 08:04:36
			    Update_time: 2007-06-03 08:04:36
			     Check_time: NULL
			 Create_options:
			        Comment:
			1 row in set (0.00 sec)
		修改表名

			如果需要修改数据表的名称，可以在 ALTER TABLE 语句中使用 RENAME 子句来实现。
			尝试以下实例将数据表 testalter_tbl 重命名为 alter_tbl：
			mysql> ALTER TABLE testalter_tbl RENAME TO alter_tbl;
			ALTER 命令还可以用来创建及删除MySQL数据表的索引，该功能我们会在接下来的章节中介绍。
	MySQL 索引
				MySQL索引的建立对于MySQL的高效运行是很重要的，索引可以大大提高MySQL的检索速度。
				索引分单列索引和组合索引。单列索引，即一个索引只包含单个列，一个表可以有多个单列索引，但这不是组合索引。组合索引，即一个索包含多个列。
				创建索引时，你需要确保该索引是应用在 SQL 查询语句的条件(一般作为 WHERE 子句的条件)。
				实际上，索引也是一张表，该表保存了主键与索引字段，并指向实体表的记录。
				上面都在说使用索引的好处，但过多的使用索引将会造成滥用。因此索引也会有它的缺点：虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行INSERT、UPDATE和DELETE。因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。
				建立索引会占用磁盘空间的索引文件。
				普通索引

				创建索引

				这是最基本的索引，它没有任何限制。它有以下几种创建方式：
				CREATE INDEX indexName ON mytable(username(length)); 
				如果是CHAR，VARCHAR类型，length可以小于字段实际长度；如果是BLOB和TEXT类型，必须指定 length。
				修改表结构

				ALTER mytable ADD INDEX [indexName] ON (username(length)) 
				创建表的时候直接指定

				CREATE TABLE mytable(  
				 
				ID INT NOT NULL,   
				 
				username VARCHAR(16) NOT NULL,  
				 
				INDEX [indexName] (username(length))  
				 
				);  
				删除索引的语法

				DROP INDEX [indexName] ON mytable; 
				唯一索引

				它与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一。它有以下几种创建方式：
				创建索引

				CREATE UNIQUE INDEX indexName ON mytable(username(length)) 
				修改表结构

				ALTER mytable ADD UNIQUE [indexName] ON (username(length)) 
				创建表的时候直接指定

				CREATE TABLE mytable(  
				 
				ID INT NOT NULL,   
				 
				username VARCHAR(16) NOT NULL,  
				 
				UNIQUE [indexName] (username(length))  
				 
				);  
				使用ALTER 命令添加和删除索引

				有四种方式来添加数据表的索引：
				ALTER TABLE tbl_name ADD PRIMARY KEY (column_list): 该语句添加一个主键，这意味着索引值必须是唯一的，且不能为NULL。
				ALTER TABLE tbl_name ADD UNIQUE index_name (column_list): 这条语句创建索引的值必须是唯一的（除了NULL外，NULL可能会出现多次）。
				ALTER TABLE tbl_name ADD INDEX index_name (column_list): 添加普通索引，索引值可出现多次。
				ALTER TABLE tbl_name ADD FULLTEXT index_name (column_list):该语句指定了索引为 FULLTEXT ，用于全文索引。
				以下实例为在表中添加索引。
				mysql> ALTER TABLE testalter_tbl ADD INDEX (c);
				你还可以在 ALTER 命令中使用 DROP 子句来删除索引。尝试以下实例删除索引:
				mysql> ALTER TABLE testalter_tbl DROP INDEX (c);
				使用 ALTER 命令添加和删除主键

				主键只能作用于一个列上，添加主键索引时，你需要确保该主键默认不为空（NOT NULL）。实例如下：
				mysql> ALTER TABLE testalter_tbl MODIFY i INT NOT NULL;
				mysql> ALTER TABLE testalter_tbl ADD PRIMARY KEY (i);
				你也可以使用 ALTER 命令删除主键：
				mysql> ALTER TABLE testalter_tbl DROP PRIMARY KEY;
				删除指定时只需指定PRIMARY KEY，但在删除索引时，你必须知道索引名。
				显示索引信息

				你可以使用 SHOW INDEX 命令来列出表中的相关的索引信息。可以通过添加 \G 来格式化输出信息。
				尝试以下实例:
				mysql> SHOW INDEX FROM table_name\G
				........
	MySQL 临时表
			MySQL 临时表在我们需要保存一些临时数据时是非常有用的。临时表只在当前连接可见，当关闭连接时，MySQL会自动删除表并释放所有空间。
			临时表在MySQL 3.23版本中添加，如果你的MySQL版本低于 3.23版本就无法使用MySQL的临时表。不过现在一般很少有再使用这么低版本的MySQL数据库服务了。
			MySQL临时表只在当前连接可见，如果你使用PHP脚本来创建MySQL临时表，那没当PHP脚本执行完成后，该临时表也会自动销毁。
			如果你使用了其他MySQL客户端程序连接MySQL数据库服务器来创建临时表，那么只有在关闭客户端程序时才会销毁临时表，当然你也可以手动销毁。
			实例

			以下展示了使用MySQL 临时表的简单实例，以下的SQL代码可以适用于PHP脚本的mysql_query()函数。
			mysql> CREATE TEMPORARY TABLE SalesSummary (
			    -> product_name VARCHAR(50) NOT NULL
			    -> , total_sales DECIMAL(12,2) NOT NULL DEFAULT 0.00
			    -> , avg_unit_price DECIMAL(7,2) NOT NULL DEFAULT 0.00
			    -> , total_units_sold INT UNSIGNED NOT NULL DEFAULT 0
			);
			Query OK, 0 rows affected (0.00 sec)

			mysql> INSERT INTO SalesSummary
			    -> (product_name, total_sales, avg_unit_price, total_units_sold)
			    -> VALUES
			    -> ('cucumber', 100.25, 90, 2);

			mysql> SELECT * FROM SalesSummary;
			+--------------+-------------+----------------+------------------+
			| product_name | total_sales | avg_unit_price | total_units_sold |
			+--------------+-------------+----------------+------------------+
			| cucumber     |      100.25 |          90.00 |                2 |
			+--------------+-------------+----------------+------------------+
			1 row in set (0.00 sec)
			当你使用 SHOW TABLES命令显示数据表列表时，你将无法看到 SalesSummary表。
			如果你退出当前MySQL会话，再使用 SELECT命令来读取原先创建的临时表数据，那你会发现数据库中没有该表的存在，因为在你退出时该临时表已经被销毁了。
			删除MySQL 临时表

			默认情况下，当你断开与数据库的连接后，临时表就会自动被销毁。当然你也可以在当前MySQL会话使用 DROP TABLE 命令来手动删除临时表。
			以下是手动删除临时表的实例：
			mysql> CREATE TEMPORARY TABLE SalesSummary (
			    -> product_name VARCHAR(50) NOT NULL
			    -> , total_sales DECIMAL(12,2) NOT NULL DEFAULT 0.00
			    -> , avg_unit_price DECIMAL(7,2) NOT NULL DEFAULT 0.00
			    -> , total_units_sold INT UNSIGNED NOT NULL DEFAULT 0
			);
			Query OK, 0 rows affected (0.00 sec)

			mysql> INSERT INTO SalesSummary
			    -> (product_name, total_sales, avg_unit_price, total_units_sold)
			    -> VALUES
			    -> ('cucumber', 100.25, 90, 2);

			mysql> SELECT * FROM SalesSummary;
			+--------------+-------------+----------------+------------------+
			| product_name | total_sales | avg_unit_price | total_units_sold |
			+--------------+-------------+----------------+------------------+
			| cucumber     |      100.25 |          90.00 |                2 |
			+--------------+-------------+----------------+------------------+
			1 row in set (0.00 sec)
			mysql> DROP TABLE SalesSummary;
			mysql>  SELECT * FROM SalesSummary;
			ERROR 1146: Table 'W3CSCHOOL.SalesSummary' doesn\'t exist
	MySQL 复制表
			如果我们需要完全的复制MySQL的数据表，包括表的结构，索引，默认值等。 如果仅仅使用CREATE TABLE ... SELECT 命令，是无法实现的。
			本章节将为大家介绍如何完整的复制MySQL数据表，步骤如下：
			使用 SHOW CREATE TABLE 命令获取创建数据表(CREATE TABLE) 语句，该语句包含了原数据表的结构，索引等。
			复制以下命令显示的SQL语句，修改数据表名，并执行SQL语句，通过以上命令 将完全的复制数据表结构。
			如果你想复制表的内容，你就可以使用 INSERT INTO ... SELECT 语句来实现。
			实例

			尝试以下实例来复制表 w3cschool_tbl 。
			步骤一：
			获取数据表的完整结构。
			mysql> SHOW CREATE TABLE w3cschool_tbl \G;
			*************************** 1. row ***************************
			       Table: w3cschool_tbl
			Create Table: CREATE TABLE `w3cschool_tbl` (
			  `w3cschool_id` int(11) NOT NULL auto_increment,
			  `w3cschool_title` varchar(100) NOT NULL default '',
			  `w3cschool_author` varchar(40) NOT NULL default '',
			  `submission_date` date default NULL,
			  PRIMARY KEY  (`w3cschool_id`),
			  UNIQUE KEY `AUTHOR_INDEX` (`w3cschool_author`)
			) ENGINE=InnoDB
			1 row in set (0.00 sec)

			ERROR:
			No query specified
			步骤二：
			修改SQL语句的数据表名，并执行SQL语句。
			mysql> CREATE TABLE `clone_tbl` (
			  -> `w3cschool_id` int(11) NOT NULL auto_increment,
			  -> `w3cschool_title` varchar(100) NOT NULL default '',
			  -> `w3cschool_author` varchar(40) NOT NULL default '',
			  -> `submission_date` date default NULL,
			  -> PRIMARY KEY  (`w3cschool_id`),
			  -> UNIQUE KEY `AUTHOR_INDEX` (`w3cschool_author`)
			-> ) ENGINE=InnoDB;
			Query OK, 0 rows affected (1.80 sec)
			步骤三：
			执行完第二步骤后，你将在数据库中创建新的克隆表 clone_tbl。 如果你想拷贝数据表的数据你可以使用 INSERT INTO... SELECT 语句来实现。
			mysql> INSERT INTO clone_tbl (w3cschool_id,
			    ->                        w3cschool_title,
			    ->                        w3cschool_author,
			    ->                        submission_date)
			    -> SELECT w3cschool_id,tutorial_title,
			    ->        w3cschool_author,submission_date
			    -> FROM w3cschool_tbl;
			Query OK, 3 rows affected (0.07 sec)
			Records: 3  Duplicates: 0  Warnings: 0
			执行以上步骤后，你将完整的复制表，包括表结构及表数据。
	MySQL 元数据
		你可能想知道MySQL以下三种信息：
		查询结果信息： SELECT, UPDATE 或 DELETE语句影响的记录数。
		数据库和数据表的信息： 包含了数据库及数据表的结构信息。
		MySQL服务器信息： 包含了数据库服务器的当前状态，版本号等。
		在MySQL的命令提示符中，我们可以很容易的获取以上服务器信息。 但如果使用Perl或PHP等脚本语言，你就需要调用特定的接口函数来获取。 接下来我们会详细介绍。
		获取查询语句影响的记录数

		PERL 实例

		在 DBI 脚本中， 语句影响的记录数通过函数 do( ) 或 execute( )返回：
		# 方法 1
		# 使用do( ) 执行  $query 
		my $count = $dbh->do ($query);
		# 如果发生错误会输出 0
		printf "%d rows were affected\n", (defined ($count) ? $count : 0);

		# 方法 2
		# 使用prepare( ) 及 execute( ) 执行  $query 
		my $sth = $dbh->prepare ($query);
		my $count = $sth->execute ( );
		printf "%d rows were affected\n", (defined ($count) ? $count : 0);
		PHP 实例

		在PHP中，你可以使用 mysql_affected_rows( ) 函数来获取查询语句影响的记录数。
		$result_id = mysql_query ($query, $conn_id);
		# 如果查询失败返回 
		$count = ($result_id ? mysql_affected_rows ($conn_id) : 0);
		print ("$count rows were affected\n");
		数据库和数据表列表

		你可以很容易的在MySQL服务器中获取数据库和数据表列表。 如果你没有足够的权限，结果将返回 null。
		你也可以使用 SHOW TABLES 或 SHOW DATABASES 语句来获取数据库和数据表列表。
		PERL 实例

		# 获取当前数据库中所有可用的表。
		my @tables = $dbh->tables ( );
		foreach $table (@tables ){
		   print "Table Name $table\n";
		}
		PHP 实例

		<?php
		$con = mysql_connect("localhost", "userid", "password");
		if (!$con)
		{
		  die('Could not connect: ' . mysql_error());
		}

		$db_list = mysql_list_dbs($con);

		while ($db = mysql_fetch_object($db_list))
		{
		  echo $db->Database . "<br />";
		}
		mysql_close($con);
		?>
		获取服务器元数据

		以下命令语句可以在MySQL的命令提示符使用，也可以在脚本中 使用，如PHP脚本。
		命令	描述
		SELECT VERSION( )	服务器版本信息
		SELECT DATABASE( )	当前数据库名 (或者返回空)
		SELECT USER( )	当前用户名
		SHOW STATUS	服务器状态
		SHOW VARIABLES	服务器配置变量
	MySQL 序列使用

				MySQL序列是一组整数：1, 2, 3, ...，由于一张数据表只能有一个字段自增主键， 如果你想实现其他字段也实现自动增加，就可以使用MySQL序列来实现。
				使用AUTO_INCREMENT

				MySQL中最简单使用序列的方法就是使用 MySQL AUTO_INCREMENT 来定义列。
				实例

				以下实例中创建了数据表insect， insect中id无需指定值可实现自动增长。
				mysql> CREATE TABLE insect
				    -> (
				    -> id INT UNSIGNED NOT NULL AUTO_INCREMENT,
				    -> PRIMARY KEY (id),
				    -> name VARCHAR(30) NOT NULL, # type of insect
				    -> date DATE NOT NULL, # date collected
				    -> origin VARCHAR(30) NOT NULL # where collected
				);
				Query OK, 0 rows affected (0.02 sec)
				mysql> INSERT INTO insect (id,name,date,origin) VALUES
				    -> (NULL,'housefly','2001-09-10','kitchen'),
				    -> (NULL,'millipede','2001-09-10','driveway'),
				    -> (NULL,'grasshopper','2001-09-10','front yard');
				Query OK, 3 rows affected (0.02 sec)
				Records: 3  Duplicates: 0  Warnings: 0
				mysql> SELECT * FROM insect ORDER BY id;
				+----+-------------+------------+------------+
				| id | name        | date       | origin     |
				+----+-------------+------------+------------+
				|  1 | housefly    | 2001-09-10 | kitchen    |
				|  2 | millipede   | 2001-09-10 | driveway   |
				|  3 | grasshopper | 2001-09-10 | front yard |
				+----+-------------+------------+------------+
				3 rows in set (0.00 sec)
				获取AUTO_INCREMENT值

				在MySQL的客户端中你可以使用 SQL中的LAST_INSERT_ID( ) 函数来获取最后的插入表中的自增列的值。
				在PHP或PERL脚本中也提供了相应的函数来获取最后的插入表中的自增列的值。
				PERL实例

				使用 mysql_insertid 属性来获取 AUTO_INCREMENT 的值。 实例如下：
				$dbh->do ("INSERT INTO insect (name,date,origin)
				VALUES('moth','2001-09-14','windowsill')");
				my $seq = $dbh->{mysql_insertid};
				PHP实例

				PHP 通过 mysql_insert_id ()函数来获取执行的插入SQL语句中 AUTO_INCREMENT列的值。
				mysql_query ("INSERT INTO insect (name,date,origin)
				VALUES('moth','2001-09-14','windowsill')", $conn_id);
				$seq = mysql_insert_id ($conn_id);
				重置序列

				如果你删除了数据表中的多条记录，并希望对剩下数据的AUTO_INCREMENT列进行重新排列，那么你可以通过删除自增的列，然后重新添加来实现。 不过该操作要非常小心，如果在删除的同时又有新记录添加，有可能会出现数据混乱。操作如下所示：
				mysql> ALTER TABLE insect DROP id;
				mysql> ALTER TABLE insect
				    -> ADD id INT UNSIGNED NOT NULL AUTO_INCREMENT FIRST,
				    -> ADD PRIMARY KEY (id);
				设置序列的开始值

				一般情况下序列的开始值为1，但如果你需要指定一个开始值100，那我们可以通过以下语句来实现：
				mysql> CREATE TABLE insect
				    -> (
				    -> id INT UNSIGNED NOT NULL AUTO_INCREMENT = 100,
				    -> PRIMARY KEY (id),
				    -> name VARCHAR(30) NOT NULL, # type of insect
				    -> date DATE NOT NULL, # date collected
				    -> origin VARCHAR(30) NOT NULL # where collected
				);
				或者你也可以在表创建成功后，通过以下语句来实现：
				mysql> ALTER TABLE t AUTO_INCREMENT = 100;
	MySQL 处理重复数据

		有些 MySQL 数据表中可能存在重复的记录，有些情况我们允许重复数据的存在，但有时候我们也需要删除这些重复的数据。
		本章节我们将为大家介绍如何防止数据表出现重复数据及如何删除数据表中的重复数据。
		防止表中出现重复数据

		你可以在MySQL数据表中设置指定的字段为 PRIMARY KEY（主键） 或者 UNIQUE（唯一） 索引来保证数据的唯一性。
		让我们尝试一个实例：下表中无索引及主键，所以该表允许出现多条重复记录。
		CREATE TABLE person_tbl
		(
		    first_name CHAR(20),
		    last_name CHAR(20),
		    sex CHAR(10)
		);
		如果你想设置表中字段first_name，last_name数据不能重复，你可以设置双主键模式来设置数据的唯一性， 如果你设置了双主键，那么那个键的默认值不能为NULL，可设置为NOT NULL。如下所示：
		CREATE TABLE person_tbl
		(
		   first_name CHAR(20) NOT NULL,
		   last_name CHAR(20) NOT NULL,
		   sex CHAR(10),
		   PRIMARY KEY (last_name, first_name)
		);
		如果我们设置了唯一索引，那么在插入重复数据时，SQL语句将无法执行成功,并抛出错。
		INSERT IGNORE INTO与INSERT INTO的区别就是INSERT IGNORE会忽略数据库中已经存在的数据，如果数据库没有数据，就插入新的数据，如果有数据的话就跳过这条数据。这样就可以保留数据库中已经存在数据，达到在间隙中插入数据的目的。
		以下实例使用了INSERT IGNORE INTO，执行后不会出错，也不会向数据表中插入重复数据：
		mysql> INSERT IGNORE INTO person_tbl (last_name, first_name)
		    -> VALUES( 'Jay', 'Thomas');
		Query OK, 1 row affected (0.00 sec)
		mysql> INSERT IGNORE INTO person_tbl (last_name, first_name)
		    -> VALUES( 'Jay', 'Thomas');
		Query OK, 0 rows affected (0.00 sec)
		INSERT IGNORE INTO当插入数据时，在设置了记录的唯一性后，如果插入重复数据，将不返回错误，只以警告形式返回。 而REPLACE INTO into如果存在primary 或 unique相同的记录，则先删除掉。再插入新记录。
		另一种设置数据的唯一性方法是添加一个UNIQUE索引，如下所示：
		CREATE TABLE person_tbl
		(
		   first_name CHAR(20) NOT NULL,
		   last_name CHAR(20) NOT NULL,
		   sex CHAR(10)
		   UNIQUE (last_name, first_name)
		);
		查询重复记录

		select user_name,count(*) as count from user_table group by user_name having count>1;

		select * from people 
		where peopleId in (select peopleId from people group by peopleId having count(peopleId) > 1) 

		统计重复数据

		以下我们将统计表中 first_name 和 last_name的重复记录数：
		mysql> SELECT COUNT(*) as repetitions, last_name, first_name
		    -> FROM person_tbl
		    -> GROUP BY last_name, first_name
		    -> HAVING repetitions > 1;
		以上查询语句将返回 person_tbl 表中重复的记录数。 一般情况下，查询重复的值，请执行以下操作：
		确定哪一列包含的值可能会重复。
		在列选择列表使用COUNT(*)列出的那些列。
		在GROUP BY子句中列出的列。
		HAVING子句设置重复数大于1。
		过滤重复数据

		如果你需要读取不重复的数据可以在 SELECT 语句中使用 DISTINCT 关键字来过滤重复数据。
		mysql> SELECT DISTINCT last_name, first_name
		    -> FROM person_tbl
		    -> ORDER BY last_name;
		你也可以使用 GROUP BY 来读取数据表中不重复的数据：
		mysql> SELECT last_name, first_name
		    -> FROM person_tbl
		    -> GROUP BY (last_name, first_name);
		删除重复数据

		如果你想删除数据表中的重复数据，你可以使用以下的SQL语句：
		mysql> CREATE TABLE tmp SELECT last_name, first_name, sex
		    ->                  FROM person_tbl;
		    ->                  GROUP BY (last_name, first_name);
		mysql> DROP TABLE person_tbl;
		mysql> ALTER TABLE tmp RENAME TO person_tbl;
		当然你也可以在数据表中添加 INDEX（索引） 和 PRIMAY KEY（主键）这种简单的方法来删除表中的重复记录。方法如下：
		mysql> ALTER IGNORE TABLE person_tbl
		    -> ADD PRIMARY KEY (last_name, first_name);
	MySQL 及 SQL 注入

		如果您通过网页获取用户输入的数据并将其插入一个MySQL数据库，那么就有可能发生SQL注入安全的问题。
		本章节将为大家介绍如何防止SQL注入，并通过脚本来过滤SQL中注入的字符。
		所谓SQL注入，就是通过把SQL命令插入到Web表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令。
		我们永远不要信任用户的输入，我们必须认定用户输入的数据都是不安全的，我们都需要对用户输入的数据进行过滤处理。
		以下实例中，输入的用户名必须为字母、数字及下划线的组合，且用户名长度为 8 到 20 个字符之间：
		if (preg_match("/^\w{8,20}$/", $_GET['username'], $matches))
		{
		   $result = mysql_query("SELECT * FROM users 
		                          WHERE username=$matches[0]");
		}
		 else 
		{
		   echo "username 输入异常";
		}
		让我们看下在没有过滤特殊字符时，出现的SQL情况：
		// 设定$name 中插入了我们不需要的SQL语句
		$name = "Qadir'; DELETE FROM users;";
		mysql_query("SELECT * FROM users WHERE name='{$name}'");
		以上的注入语句中，我们没有对 $name 的变量进行过滤，$name 中插入了我们不需要的SQL语句，将删除 users 表中的所有数据。
		在PHP中的 mysql_query() 是不允许执行多个SQL语句的，但是在 SQLite 和 PostgreSQL 是可以同时执行多条SQL语句的，所以我们对这些用户的数据需要进行严格的验证。
		防止SQL注入，我们需要注意以下几个要点：
		1.永远不要信任用户的输入。对用户的输入进行校验，可以通过正则表达式，或限制长度；对单引号和 双"-"进行转换等。
		2.永远不要使用动态拼装sql，可以使用参数化的sql或者直接使用存储过程进行数据查询存取。
		3.永远不要使用管理员权限的数据库连接，为每个应用使用单独的权限有限的数据库连接。
		4.不要把机密信息直接存放，加密或者hash掉密码和敏感的信息。
		5.应用的异常信息应该给出尽可能少的提示，最好使用自定义的错误信息对原始错误信息进行包装
		6.sql注入的检测方法一般采取辅助软件或网站平台来检测，软件一般采用sql注入检测工具jsky，网站平台就有亿思网站安全平台检测工具。MDCSOFT SCAN等。采用MDCSOFT-IPS可以有效的防御SQL注入，XSS攻击等。
		防止SQL注入

		在脚本语言，如Perl和PHP你可以对用户输入的数据进行转义从而来防止SQL注入。
		PHP的MySQL扩展提供了mysql_real_escape_string()函数来转义特殊的输入字符。
		if (get_magic_quotes_gpc()) 
		{
		  $name = stripslashes($name);
		}
		$name = mysql_real_escape_string($name);
		mysql_query("SELECT * FROM users WHERE name='{$name}'");
		Like语句中的注入

		like查询时，如果用户输入的值有"_"和"%"，则会出现这种情况：用户本来只是想查询"abcd_"，查询结果中却有"abcd_"、"abcde"、"abcdf"等等；用户要查询"30%"（注：百分之三十）时也会出现问题。
		在PHP脚本中我们可以使用addcslashes()函数来处理以上情况，如下实例：
		$sub = addcslashes(mysql_real_escape_string("%something_"), "%_");
		// $sub == \%something\_
		mysql_query("SELECT * FROM messages WHERE subject LIKE '{$sub}%'");
		addcslashes() 函数在指定的字符前添加反斜杠。
		语法格式:
		addcslashes(string,characters)
		参数	描述
		string	必需。规定要检查的字符串。
		characters	可选。规定受 addcslashes() 影响的字符或字符范围。
		具体应用可以查看：PHP addcslashes() 函数
	MySQL 导出数据
		使用SELECT...INTO OUTFILE语句来简单的导出数据到文本文件上。
			以下实例中我们将数据表 w3cschool_tbl 数据导出到 /tmp/tutorials.txt 文件中:
				mysql> SELECT * FROM tutorials_tbl 
				    -> INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/w3c_tbl.txt';
			你可以通过命令选项来设置数据输出的指定格式，以下实例为导出 CSV 格式：
				mysql> SELECT * FROM passwd INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/w3c_tbl.txt'
				    -> FIELDS TERMINATED BY ',' ENCLOSED BY '"'
				    -> LINES TERMINATED BY '\r\n';
			在下面的例子中，生成一个文件，各值用逗号隔开。这种格式可以被许多程序使用。
				SELECT a,b,a+b INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/w3c_tbl.txt'
				FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
				LINES TERMINATED BY '\n'
				FROM test_table;
			MySQL查询出错提示 --secure-file-priv解决方法
					2016-12-22 16:06 by 0xAC, 586 阅读, 0 评论, 收藏, 编辑
					原文

					在某台DB上准备运行一个SQL语句，就是用SELECT INTO OUTFILE把查询结果写入到文件的时候提示以下信息：

					The MySQL server is running with the --secure-file-priv option so it cannot execute this statement

					出现这个问题的原因是因为启动MySQL的时候使用了--secure-file-priv这个参数，这个参数的主要目的就是限制LOAD DATA INFILE或者SELECT INTO OUTFILE之类文件的目录位置，我们可以使用

					SELECT @@global.secure_file_priv;
					查询到你当前设置的路径，默认应该是/var/lib/mysql-files

					如果要解决这个问题，我们可以通过下面2种方式：

					将你要导入或导出的文件位置指定到你设置的路径里

					由于不能动态修改，我们可以修改my.cnf里关于这个选项的配置，然后重启即可。
			SELECT ... INTO OUTFILE 语句有以下属性:

				LOAD DATA INFILE是SELECT ... INTO OUTFILE的逆操作，SELECT句法。为了将一个数据库的数据写入一个文件，使用SELECT ... INTO OUTFILE，为了将文件读回数据库，使用LOAD DATA INFILE。
				SELECT...INTO OUTFILE 'file_name'形式的SELECT可以把被选择的行写入一个文件中。该文件被创建到服务器主机上，因此您必须拥有FILE权限，才能使用此语法。
				输出不能是一个已存在的文件。防止文件数据被篡改。
				你需要有一个登陆服务器的账号来检索文件。否则 SELECT ... INTO OUTFILE 不会起任何作用。
				在UNIX中，该文件被创建后是可读的，权限由MySQL服务器所拥有。这意味着，虽然你就可以读取该文件，但可能无法将其删除。
				导出表作为原始数据

				mysqldump是MySQL用于转存储数据库的实用程序。它主要产生一个SQL脚本，其中包含从头重新创建数据库所必需的命令CREATE TABLE INSERT等。
				使用mysqldump导出数据需要使用 --tab 选项来指定导出文件指定的目录，该目标必须是可写的。
				以下实例将数据表 tutorials_tbl 导出到 /tmp 目录中：
				$ mysqldump -u root -p --no-create-info \
				            --tab=/tmp W3CSCHOOL w3cschool_tbl
				password ******
		导出SQL格式的数据到指定文件，如下所示：
				$ mysqldump -u root -p W3CSCHOOL w3cschool_tbl > dump.txt
				password ******
				以上命令创建的文件内容如下：
				-- MySQL dump 8.23
				--
				-- Host: localhost    Database: W3CSCHOOL
				---------------------------------------------------------
				-- Server version       3.23.58

				--
				-- Table structure for table `w3cschool_tbl`
				--

				CREATE TABLE w3cschool_tbl (
				  w3cschool_id int(11) NOT NULL auto_increment,
				  w3cschool_title varchar(100) NOT NULL default '',
				  w3cschool_author varchar(40) NOT NULL default '',
				  submission_date date default NULL,
				  PRIMARY KEY  (w3cschool_id),
				  UNIQUE KEY AUTHOR_INDEX (w3cschool_author)
				) TYPE=MyISAM;

				--
				-- Dumping data for table `w3cschool_tbl`
				--

				INSERT INTO w3cschool_tbl 
				       VALUES (1,'Learn PHP','John Poul','2007-05-24');
				INSERT INTO w3cschool_tbl 
				       VALUES (2,'Learn MySQL','Abdul S','2007-05-24');
				INSERT INTO w3cschool_tbl 
				       VALUES (3,'JAVA Tutorial','Sanjay','2007-05-06');
		如果你需要导出整个数据库的数据，可以使用以下命令：
				$ mysqldump -u root -p W3CSCHOOL > database_dump.txt
				password ******
		如果需要备份所有数据库，可以使用以下命令：
				$ mysqldump -u root -p --all-databases > database_dump.txt
				password ******
				--all-databases 选项在 MySQL 3.23.12 及以后版本加入。
				该方法可用于实现数据库的备份策略。
		将数据表及数据库拷贝至其他主机

				如果你需要将数据拷贝至其他的 MySQL 服务器上, 你可以在 mysqldump 命令中指定数据库名及数据表。
				在源主机上执行以下命令，将数据备份至 dump.txt 文件中:
				$ mysqldump -u root -p database_name table_name > dump.txt
				password *****
				如果完整备份数据库，则无需使用特定的表名称。
				如果你需要将备份的数据库导入到MySQL服务器中，可以使用以下命令，使用以下命令你需要确认数据库已经创建：
				$ mysql -u root -p database_name < dump.txt password ***** 
		你也可以使用以下命令将导出的数据直接导入到远程的服务器上，但请确保两台服务器是相通的，是可以相互访问的：</p>
				$ mysqldump -u root -p database_name \
				       | mysql -h other-host.com database_name
				以上命令中使用了管道来将导出的数据导入到指定的远程主机上。
		导出一个数据库结构：		

			mysqldump -u user_name -p -d --add-drop-table database_name > file_name  	

			例如：mysqldump -u root -p -d --add-drop-table test_db > test_db.sql					
	MySQL 导入数据
		source file_name;   
		或  
		mysql -u user_name -p database_name < file_name 
		例如：	
			source /tmp/bbs.sql；	
			source d:/bbs.sql；	
			mysql -u root -p bbs < "d:/bbs.sql"	
			mysql -u root -p bbs < "/tmp/bbs.sql"	

		使用 LOAD DATA 导入数据

				MySQL 中提供了LOAD DATA INFILE语句来插入数据。 以下实例中将从当前目录中读取文件 dump.txt ，将该文件中的数据插入到当前数据库的 mytbl 表中。
				mysql> LOAD DATA LOCAL INFILE 'dump.txt' INTO TABLE mytbl;
				如果指定LOCAL关键词，则表明从客户主机上按路径读取文件。如果没有指定，则文件在服务器上按路径读取文件。
				你能明确地在LOAD DATA语句中指出列值的分隔符和行尾标记，但是默认标记是定位符和换行符。
				两个命令的 FIELDS 和 LINES 子句的语法是一样的。两个子句都是可选的，但是如果两个同时被指定，FIELDS 子句必须出现在 LINES 子句之前。
				如果用户指定一个 FIELDS 子句，它的子句 （TERMINATED BY、[OPTIONALLY] ENCLOSED BY 和 ESCAPED BY) 也是可选的，不过，用户必须至少指定它们中的一个。
				mysql> LOAD DATA LOCAL INFILE 'dump.txt' INTO TABLE mytbl
				  -> FIELDS TERMINATED BY ':'
				  -> LINES TERMINATED BY '\r\n';
				LOAD DATA 默认情况下是按照数据文件中列的顺序插入数据的，如果数据文件中的列与插入表中的列不一致，则需要指定列的顺序。
				如，在数据文件中的列顺序是 a,b,c，但在插入表的列顺序为b,c,a，则数据导入语法如下：
				mysql> LOAD DATA LOCAL INFILE 'dump.txt' 
				    -> INTO TABLE mytbl (b, c, a);
				使用 mysqlimport 导入数据

				mysqlimport客户端提供了LOAD DATA INFILEQL语句的一个命令行接口。mysqlimport的大多数选项直接对应LOAD DATA INFILE子句。
				从文件 dump.txt 中将数据导入到 mytbl 数据表中, 可以使用以下命令：
				$ mysqlimport -u root -p --local database_name dump.txt
				password *****
				mysqlimport命令可以指定选项来设置指定格式,命令语句格式如下：
				$ mysqlimport -u root -p --local --fields-terminated-by=":" \
				   --lines-terminated-by="\r\n"  database_name dump.txt
				password *****
				mysqlimport 语句中使用 --columns 选项来设置列的顺序：
				$ mysqlimport -u root -p --local --columns=b,c,a \
				    database_name dump.txt
				password *****
				mysqlimport的常用选项介绍

				选项	功能
				-d or --delete	新数据导入数据表中之前删除数据数据表中的所有信息
				-f or --force	不管是否遇到错误，mysqlimport将强制继续插入数据
				-i or --ignore	mysqlimport跳过或者忽略那些有相同唯一 关键字的行， 导入文件中的数据将被忽略。
				-l or -lock-tables	数据被插入之前锁住表，这样就防止了， 你在更新数据库时，用户的查询和更新受到影响。
				-r or -replace	这个选项与－i选项的作用相反；此选项将替代 表中有相同唯一关键字的记录。
				--fields-enclosed- by= char	指定文本文件中数据的记录时以什么括起的， 很多情况下 数据以双引号括起。 默认的情况下数据是没有被字符括起的。
				--fields-terminated- by=char	指定各个数据的值之间的分隔符，在句号分隔的文件中， 分隔符是句号。您可以用此选项指定数据之间的分隔符。 默认的分隔符是跳格符（Tab）
				--lines-terminated- by=str	此选项指定文本文件中行与行之间数据的分隔字符串 或者字符。 默认的情况下mysqlimport以newline为行分隔符。 您可以选择用一个字符串来替代一个单个的字符： 一个新行或者一个回车。
				mysqlimport命令常用的选项还有-v 显示版本（version）， -p 提示输入密码（password）等。


'数据库'--专门用于集中存储和查询的软件--便于程序保存和读取数据，能直接通过条件快速查询到指定的数据


	程序运行时，数据都是在内存中的。当程序终止时，通常需要将数据保存到磁盘上，无论是本地磁盘，还是通过网络保存到服务器上，最终都会将数据写入磁盘文件。
	而如何定义数据的存储格式就是一个大问题
			比如保存一个班级所有学生的成绩单：

				名字	成绩
				Michael      99
				Bob	85
				Bart	59
				Lisa	87
			你可以用一个文本文件保存，一行保存一个学生，用,隔开：

				Michael,99
				Bob,85
				Bart,59
				Lisa,87
			你还可以用JSON格式保存，也是文本文件：

				[
				    {"name":"Michael","score":99},
				    {"name":"Bob","score":85},
				    {"name":"Bart","score":59},
				    {"name":"Lisa","score":87}
				]
			你还可以定义各种保存格式，但是问题来了：
	存储和读取需要自己实现，JSON还是标准，自己定义的格式就各式各样了；

		不能做快速查询，只有把数据全部读到内存中才能自己遍历，但有时候数据的大小远远超过了内存（比如蓝光电影，40GB的数据），根本无法全部读入内存。
	为了便于程序保存和读取数据，而且，能直接通过条件快速查询到指定的数据，就出现了数据库（Database）这种专门用于集中存储和查询的软件。

			数据库软件诞生的历史非常久远，早在1950年数据库就诞生了。经历了网状数据库，层次数据库，我们现在广泛使用的关系数据库是20世纪70年代
			基于关系模型的基础上诞生的。
		关系模型有一套复杂的数学理论，但是从概念上是十分容易理解的。举个学校的例子：

			假设某个XX省YY市ZZ县第一实验小学有3个年级，要表示出这3个年级，可以在Excel中用一个表格画出来：

			grade

			每个年级又有若干个班级，要把所有班级表示出来，可以在Excel中再画一个表格：

			class

			这两个表格有个映射关系，就是根据Grade_ID可以在班级表中查找到对应的所有班级：

			grade-classes

			也就是Grade表的每一行对应Class表的多行，在关系数据库中，这种基于表（Table）的一对多的关系就是关系数据库的基础。

			根据某个年级的ID就可以查找所有班级的行，这种查询语句在关系数据库中称为SQL语句，可以写成：

			SELECT * FROM classes WHERE grade_id = '1';
			结果也是一个表：

			---------+----------+----------
			grade_id | class_id | name
			---------+----------+----------
			1        | 11       | 一年级一班
			---------+----------+----------
			1        | 12       | 一年级二班
			---------+----------+----------
			1        | 13       | 一年级三班
			---------+----------+----------
			类似的，Class表的一行记录又可以关联到Student表的多行记录：

			class-students

			由于本教程不涉及到关系数据库的详细内容，如果你想从零学习关系数据库和基本的SQL语句，如果你想从零学习关系数据库和基本的SQL语句，请自行搜索
			相关课程。
	NoSQL

			你也许还听说过NoSQL数据库，很多NoSQL宣传其速度和规模远远超过关系数据库，所以很多同学觉得有了NoSQL是否就不需要SQL了呢？千万不要被
			他们忽悠了，连SQL都不明白怎么可能搞明白NoSQL呢？
	数据库类别

			既然我们要使用关系数据库，就必须选择一个关系数据库。目前广泛使用的关系数据库也就这么几种：

			付费的商用数据库：

			Oracle，典型的高富帅；

			SQL Server，微软自家产品，Windows定制专款；

			DB2，IBM的产品，听起来挺高端；

			Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。

			这些数据库都是不开源而且付费的，最大的好处是花了钱出了问题可以找厂家解决，不过在Web的世界里，常常需要部署成千上万的数据库服务器，当然不能
			把大把大把的银子扔给厂家，所以，无论是Google、Facebook，还是国内的BAT，无一例外都选择了免费的开源数据库：

			MySQL，大家都在用，一般错不了；

			PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；

			sqlite，嵌入式数据库，适合桌面和移动应用。

			作为Python开发工程师，选择哪个免费数据库呢？当然是MySQL。因为MySQL普及率最高，出了错，可以很容易找到解决方法。而且，围绕MySQL有一大堆
			监控和运维的工具，安装和使用很方便。

			为了能继续后面的学习，你需要从MySQL官方网站下载并安装MySQL Community Server 5.6，这个版本是免费的，其他高级版本是要收钱的（请放心，
			收钱的功能我们用不上）。


'使用SQLite'--嵌入式数据库--体积小--易集成到各种应用程序中--Python内置SQLite3模块

	SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。

	Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

		在使用SQLite前，我们先要搞清楚几个概念：

			'表'是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。

			要操作关系数据库，首先需要连接到数据库，'一个数据库连接'称为'Connection'；

			连接到数据库后，需要打开'游标'，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

			Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。

			由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

		我们在Python交互式命令行实践一下：

			# 导入SQLite驱动:
			>>> import sqlite3
			# 连接到SQLite数据库
			# 数据库文件是test.db
			# 如果文件不存在，会自动在当前目录创建:
			>>> conn = sqlite3.connect('test.db')
			# 创建一个Cursor:
			>>> cursor = conn.cursor()
			# 执行一条SQL语句，创建user表:
			>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
			<sqlite3.Cursor object at 0x10f8aa260>
			# 继续执行一条SQL语句，插入一条记录:
			>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
			<sqlite3.Cursor object at 0x10f8aa260>
			# 通过rowcount获得插入的行数:
			>>> cursor.rowcount
			1
			# 关闭Cursor:
			>>> cursor.close()
			# 提交事务:
			>>> conn.commit()
			# 关闭Connection:
			>>> conn.close()
		我们再试试查询记录：

			>>> conn = sqlite3.connect('test.db')
			>>> cursor = conn.cursor()
			# 执行查询语句:
			>>> cursor.execute('select * from user where id=?', ('1',))
			<sqlite3.Cursor object at 0x10f8aa340>
			# 获得查询结果集:
			>>> values = cursor.fetchall()
			>>> values
			[('1', 'Michael')]
			>>> cursor.close()
			>>> conn.close()
		使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

			使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

			使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

			如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：

			cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
			SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。

	小结

			在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。

			要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

			如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。

	练习

			请编写函数，在Sqlite中根据分数段查找指定的名字：

			# -*- coding: utf-8 -*-

			import os, sqlite3

			db_file = os.path.join(os.path.dirname(__file__), 'test.db')
			if os.path.isfile(db_file):
			    os.remove(db_file)

			# 初始数据:
			conn = sqlite3.connect(db_file)
			cursor = conn.cursor()
			cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
			cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
			cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
			cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
			cursor.close()
			conn.commit()
			conn.close()

			def get_score_in(low, high):
			    ' 返回指定分数区间的名字，按分数从低到高排序 '

			    pass

			# 测试:
			assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
			assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
			assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

			print('Pass')
			 Run
	参考源码

			do_sqlite.py
'使用MySQL'--为服务器端设计的数据库--能承受高并发访问
	MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
		而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。		

		此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。
	安装MySQL

		可以直接从MySQL官方网站下载最新的Community Server 5.7.x版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。			

			安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。			

		在Windows上，安装时请选择utf8编码，以便正确地处理中文。			

		在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者
			/etc/mysql/my.cnf：			

			[client]
			default-character-set = utf8			

			[mysqld]
			default-storage-engine = INNODB
			character-set-server = utf8
			collation-server = utf8_general_ci			

		重启MySQL后，可以通过MySQL的客户端命令行检查编码：			

			$ mysql -u root -p
			Enter password: 
			Welcome to the MySQL monitor...
			...			

			mysql> show variables like '%char%';
			+--------------------------+--------------------------------------------------------+
			| Variable_name            | Value                                                  |
			+--------------------------+--------------------------------------------------------+
			| character_set_client     | utf8                                                   |
			| character_set_connection | utf8                                                   |
			| character_set_database   | utf8                                                   |
			| character_set_filesystem | binary                                                 |
			| character_set_results    | utf8                                                   |
			| character_set_server     | utf8                                                   |
			| character_set_system     | utf8                                                   |
			| character_sets_dir       | /usr/local/mysql-5.1.65-osx10.6-x86_64/share/charsets/ |
			+--------------------------+--------------------------------------------------------+
			8 rows in set (0.00 sec)			

			看到utf8字样就表示编码设置正确。			

			注：如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。
	安装MySQL驱动

		由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方
		提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：		

		$ pip install mysql-connector-python --allow-external mysql-connector-python
		如果上面的命令安装失败，可以试试另一个驱动：		

		$ pip install mysql-connector
		pip install mysql-connector-python-rf
		sudo pip3 install --extra-index-url https://pypi.python.org/pypi/mysql-connector-python/2.0.4 mysql-connector-python
	我们演示如何连接到MySQL服务器的test数据库：

			# 导入MySQL驱动:
			>>> import mysql.connector
			# 注意把password设为你的root口令:
			>>> conn = mysql.connector.connect(user='root', password='password', database='test')
			>>> cursor = conn.cursor()
			# 创建user表:
			>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
			# 插入一行记录，注意MySQL的占位符是%s:
			>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
			>>> cursor.rowcount
			1
			# 提交事务:
			>>> conn.commit()
			>>> cursor.close()
			# 运行查询:
			>>> cursor = conn.cursor()
			>>> cursor.execute('select * from user where id = %s', ('1',))
			>>> values = cursor.fetchall()
			>>> values
			[('1', 'Michael')]
			# 关闭Cursor和Connection:
			>>> cursor.close()
			True
			>>> conn.close()
			由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。
	小结

		执行INSERT等操作后要调用commit()提交事务；		

		MySQL的SQL占位符是%s。
	参考源码

		do_mysql.py		

		#!/usr/bin/env python3
		# -*- coding: utf-8 -*-		

		########## prepare ##########		

		# install mysql-connector-python:
		# pip3 install mysql-connector-python --allow-external mysql-connector-python		

		import mysql.connector		

		# change root password to yours:
		conn = mysql.connector.connect(user='root', password='password', database='test')		

		cursor = conn.cursor()
		# 创建user表:
		cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
		# 插入一行记录，注意MySQL的占位符是%s:
		cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
		print('rowcount =', cursor.rowcount)
		# 提交事务:
		conn.commit()
		cursor.close()		

		# 运行查询:
		cursor = conn.cursor()
		cursor.execute('select * from user where id = %s', ('1',))
		values = cursor.fetchall()
		print(values)
		# 关闭Cursor和Connection:
		cursor.close()
		conn.close()
'使用SQLAlchemy'

		数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，list的每一个元素是tuple，表示一行记录，比如，包含id和name的user表：

		[
		    ('1', 'Michael'),
		    ('2', 'Bob'),
		    ('3', 'Adam')
		]
		Python的DB-API返回的数据结构就是像上面这样表示的。

		但是用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来：

		class User(object):
		    def __init__(self, id, name):
		        self.id = id
		        self.name = name

		[
		    User('1', 'Michael'),
		    User('2', 'Bob'),
		    User('3', 'Adam')
		]
		这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。是不是很简单？

		但是由谁来做这个转换呢？所以ORM框架应运而生。

		在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。

		首先通过pip安装SQLAlchemy：

		$ pip install sqlalchemy
		然后，利用上次我们在MySQL的test数据库中创建的user表，用SQLAlchemy来试试：

		第一步，导入SQLAlchemy，并初始化DBSession：

		# 导入:
		from sqlalchemy import Column, String, create_engine
		from sqlalchemy.orm import sessionmaker
		from sqlalchemy.ext.declarative import declarative_base

		# 创建对象的基类:
		Base = declarative_base()

		# 定义User对象:
		class User(Base):
		    # 表的名字:
		    __tablename__ = 'user'

		    # 表的结构:
		    id = Column(String(20), primary_key=True)
		    name = Column(String(20))

		# 初始化数据库连接:
		engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
		# 创建DBSession类型:
		DBSession = sessionmaker(bind=engine)
		以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如School：

		class School(Base):
		    __tablename__ = 'school'
		    id = ...
		    name = ...
		create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：

		'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
		你只需要根据需要替换掉用户名、口令等信息即可。

		下面，我们看看如何向数据库表中添加一行记录。

		由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：

		# 创建session对象:
		session = DBSession()
		# 创建新User对象:
		new_user = User(id='5', name='Bob')
		# 添加到session:
		session.add(new_user)
		# 提交即保存到数据库:
		session.commit()
		# 关闭session:
		session.close()
		可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。

		如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：

		# 创建Session:
		session = DBSession()
		# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
		user = session.query(User).filter(User.id=='5').one()
		# 打印类型和对象的name属性:
		print('type:', type(user))
		print('name:', user.name)
		# 关闭Session:
		session.close()
		运行结果如下：

		type: <class '__main__.User'>
		name: Bob
		可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。

		由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。

		例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

		class User(Base):
		    __tablename__ = 'user'

		    id = Column(String(20), primary_key=True)
		    name = Column(String(20))
		    # 一对多:
		    books = relationship('Book')

		class Book(Base):
		    __tablename__ = 'book'

		    id = Column(String(20), primary_key=True)
		    name = Column(String(20))
		    # “多”的一方的book表是通过外键关联到user表的:
		    user_id = Column(String(20), ForeignKey('user.id'))
		当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

		小结

		ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

		正确使用ORM的前提是了解关系数据库的原理。

		参考源码

		do_sqlalchemy.py  


为了避免MySQL中的安全隐患，将默认的root用户重命名。

使用 rename user 命令修改root用户名失败，

提示错误：ERROR 1396 (HY000): Operation RENAME USER failed for 'root'@'%'

改用update mysql用户下的user表后修改成功。

 

mysql> use mysql;

Database changed

 

mysql> select host,  user, password from user;

+-----------+------+-------------------------------------------+

| host      | user | password                                  |

+-----------+------+-------------------------------------------+

| localhost | root | *81F5E21E35407D884A6CD4A731AEBFB6AF209E1B |

| 127.0.0.1 | root | *81F5E21E35407D884A6CD4A731AEBFB6AF209E1B |

| ::1       | root | *81F5E21E35407D884A6CD4A731AEBFB6AF209E1B |

+-----------+------+-------------------------------------------+

3 rows in set (0.00 sec)

 

mysql> rename user root to admin;

ERROR 1396 (HY000): Operation RENAME USER failed for 'root'@'%'

 但用同样的命令重命名普通用户却没问题。

 

mysql> update  user set user='admin' where user='root';

Query OK, 3 rows affected (0.09 sec)

Rows matched: 3  Changed: 3  Warnings: 0

 

 

mysql> flush privileges;

Query OK, 0 rows affected (0.00 sec)

 

 

mysql> select host,  user, password from user;

+-----------+-------+-------------------------------------------+

| host      | user  | password                                  |

+-----------+-------+-------------------------------------------+

| localhost | admin | *81F5E21E35407D884A6CD4A731AEBFB6AF209E1B |

| 127.0.0.1 | admin | *81F5E21E35407D884A6CD4A731AEBFB6AF209E1B |

| ::1       | admin | *81F5E21E35407D884A6CD4A731AEBFB6AF209E1B |

+-----------+-------+-------------------------------------------+

3 rows in set (0.00 sec)		