-- 创建测试表
CREATE TABLE Table1 (
	id INTEGER NOT NULL,
	name VARCHAR(50)
);

insert into Table1 values(1,'table1_table2');
insert into Table1 values(2,'table1');


CREATE TABLE Table2 (
	id INTEGER NOT NULL,
	name VARCHAR(50)
);

insert into Table2 values(1,'table1_table2');
insert into Table2 values(3,'table2');


-- Inner join 结果返回两张表都能关联上的记录
mysql> SELECT Table1.id, Table1.name, Table2.id, Table2.name
    -> FROM Table1
    -> INNER JOIN Table2
    -> ON Table1.id = Table2.id;
+----+---------------+----+---------------+
| id | name          | id | name          |
+----+---------------+----+---------------+
|  1 | table1_table2 |  1 | table1_table2 |
+----+---------------+----+---------------+
1 row in set (0.01 sec)

-- Left join 返回左表的全部数据和右表能关联上的记录
mysql> SELECT Table1.id, Table1.name, Table2.id, Table2.name
    -> FROM Table1
    -> LEFT JOIN Table2
    -> ON Table1.id = Table2.id;
+----+---------------+------+---------------+
| id | name          | id   | name          |
+----+---------------+------+---------------+
|  1 | table1_table2 |    1 | table1_table2 |
|  2 | table1        | NULL | NULL          |
+----+---------------+------+---------------+
2 rows in set (0.00 sec)

-- right join 返回右表的全部数据和左能关联上的记录
mysql> SELECT Table1.id, Table1.name, Table2.id, Table2.name
    -> FROM Table1
    -> RIGHT JOIN Table2
    -> ON Table1.id = Table2.id;
+------+---------------+----+---------------+
| id   | name          | id | name          |
+------+---------------+----+---------------+
|    1 | table1_table2 |  1 | table1_table2 |
| NULL | NULL          |  3 | table2        |
+------+---------------+----+---------------+
2 rows in set (0.00 sec)
