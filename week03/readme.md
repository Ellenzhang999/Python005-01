# 作业

## 1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。

* 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
* 将增加远程用户的 SQL 语句作为作业内容提交

Answer: 修改配置文件：/etc/my.cnf，增加或修改下面字符集后重启mysql  
> [root@192 sysconfig]# vi /etc/my.cnf
 ``` 
    [client]
    default_character_set = utf8mb4

    [mysql]
    default_character_set = utf8mb4

    character_set_server = utf8mb4
    init_connect = 'SET NAMES utf8mb4'
    character_set_client_handshake = false
    collation_server = utf8mb4_unicode_ci
```
> [root@192 sysconfig]# systemctl restart mysqld #重启mysql

> mysql> create database testdb;

> mysql> grant all privileges on testdb.* to 'testuser'@'%' identified by 'testpass';

> mysql> show variables like '%character%';

## 2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取: 
* 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
* 将 ORM、插入、查询语句作为作业内容提交

Answer: 详见文件: task2_create_tbl.py, task2_update_tbl.py

## 3. 为以下 sql 语句标注执行顺序：
```
	1 SELECT DISTINCT player_id, player_name, count(*) as num 
    2 FROM player JOIN team ON player.team_id = team.team_id 
    3 WHERE height > 1.80 
    4 GROUP BY player.team_id 
    5 HAVING num > 2 
    6 ORDER BY num DESC 
    7 LIMIT 2
```
Answer: 2->3->4->5->1->6->7

## 4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?
Answer: 具体代码见task4_join_statement.sql
* Inner join 结果返回两张表都能关联上的记录
* Left join 返回左表的全部数据和右表能关联上的记录
* right join 返回右表的全部数据和左能关联上的记录

## 5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。
Answer：当数据量比较多，并且查询的结果数据占总数据量比较小的情况下，索引可以比较好的发挥作用，提高查询性能。
Index增加查询速度是因为索引的存储结构是B+ Tree，只存储索引字段（一个或多个）和对应数据地址；首先，索引较小，比较容易全部加载入内存并实现快速查询，IO开销小；其次，当查询在某（些）索引字段时，数据库会先查询索引，找到真正数据的地址，再去提取数据，避免了把全量数据加载入内容产生的大量IO。
阅读官当文档： https://dev.mysql.com/doc/refman/8.0/en/optimization-indexes.html
参考的中文文档：https://blog.csdn.net/weixin_38168760/article/details/102041617

## 6. 张三给李四通过网银转账 100 极客币，现有数据库中三张表：一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

* 请合理设计三张表的字段类型和表结构；
* 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

Answer：三张表的创建脚本：task6_transfer.sql
        转账代码：task6_transfer.py



