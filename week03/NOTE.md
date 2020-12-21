# 学习笔记

## Key command
### 启动mysql
systemctl start mysqld.service
systemctl enable mysqld
systemctl status mysqld.service

### Login mysql
[root@192 ~]# mysql -u root -p
Enter password:

### 查看和设置字符集
mysql> show variables like '%character_%';
utf8mb4_unicode_ci
ci: case insensitive 大小写不敏感
cs: case sensitive 大小写敏感

### 修改密码等级
mysql> show variables like 'validate_password%';
set global validate_password_policy = low;
set global validate_password_special_char_count = 0;
set global validate_password_mixed_case_count = 0;
set global validate_password_number_count = 0;
set global validate_password_length = 6;

### 更改密码
mysql> ALTER USER 'root'@'localhost' identified by '123456';
grant all privileges on testdb.* to 'testuser'@'%' identified by 'testpass';
grant all on testdb.* to admin@'%' identified by '123456';

## Restart mysql
[root@192 etc]# systemctl restart mysqld
[root@192 etc]# systemctl status mysqld.service

## 扩展知识
### 查看所有系统设置
https://www.cnblogs.com/jiangxiaobo/p/6110647.html
### 连接池
https://www.cnblogs.com/aspirant/p/6747238.html


## 错误1：连接数据库报错
db = pymysql.connect(host="192.168.3.155",user="root",password="123456",database='testdb',port=3306)
报错1：pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '192.168.3.155' (timed out)")
报错2：pymysql.err.InternalError: Packet sequence number wrong - got 45 expected 0

### Root Cause；虚拟机上的mysql端口3306没有暴露出来
### 解决：根据下面link步骤操作解决
参考https://www.cnblogs.com/dump/p/9238543.html
步骤：
1. 打开本地的Telnet服务
2. 开通虚拟机的3306端口
查看Linux ip addr commend “ifconfig” 或者 "ip addr"
[root@192 sysconfig]# ifconfig
3. 检查虚拟机上的防火墙状态
[root@192 etc]# service iptables status
Redirecting to /bin/systemctl status iptables.service
Unit iptables.service could not be found.
解决步骤：https://blog.csdn.net/qiushisoftware/article/details/90691460

## 错误2
### 报错：Instance of Session has no Add member
### 解决：https://blog.csdn.net/weixin_42236031/article/details/106960189
击设置-settings,点击右上角"打开设置Json"切换到json，添加下面代码：
{
    "python.linting.pylintArgs": [
        "--load-plugins",
        "pylint-flask"
    ]
}
### Root cause：不清楚