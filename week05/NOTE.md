- [作业](#作业)
  - [Task1](#task1)
    - [思路：使用redis的hash类型，唯一存放视频对应的key值，当调用函数时，将value值增加1](#思路使用redis的hash类型唯一存放视频对应的key值当调用函数时将value值增加1)
    - [代码：task1_redis_counter.py](#代码task1_redis_counterpy)
    - [输出：](#输出)
  - [Task2](#task2)
    - [思路：使用redis的expire功能，并利用字典的value值存放发送次数。如果key在字典中表示还没有过期，发送消息并将value值+1；如果key不在字典中，则增加一个key并设置过期时间。](#思路使用redis的expire功能并利用字典的value值存放发送次数如果key在字典中表示还没有过期发送消息并将value值1如果key不在字典中则增加一个key并设置过期时间)
    - [代码：task2_redis_phone.py](#代码task2_redis_phonepy)
    - [输出](#输出-1)
  - [Task3](#task3)
    - [在你目前的工作场景中，哪个业务适合使用 rabbitmq？ 引入 rabbitmq 主要解决什么问题?（非相关工作可以以设计淘宝购物和结账功能为例来描述）](#在你目前的工作场景中哪个业务适合使用-rabbitmq-引入-rabbitmq-主要解决什么问题非相关工作可以以设计淘宝购物和结账功能为例来描述)
    - [如何避免消息重复投递或重复消费？](#如何避免消息重复投递或重复消费)
    - [交换机 fanout、direct、topic 有什么区别？](#交换机-fanoutdirecttopic-有什么区别)
    - [架构中引入消息队列是否利大于弊？你认为消息队列有哪些缺点？](#架构中引入消息队列是否利大于弊你认为消息队列有哪些缺点)
- [Issue](#issue)
  - [用wget下载Redis时提示“-bash: wget: 未找到命令”](#用wget下载redis时提示-bash-wget-未找到命令)
  - [连接 Redis报错](#连接-redis报错)
  - [安装 RabbitMQ报错](#安装-rabbitmq报错)
    - [错误1：没有可用软件包 rabbitmq-server](#错误1没有可用软件包-rabbitmq-server)
    - [报错2：没有可用软件包 erlang](#报错2没有可用软件包-erlang)
    - [报错3：需要：libstdc++.so.6](#报错3需要libstdcso6)
    - [报错4： 错误：依赖检测失败：socat 被 rabbitmq-server-3.8.9-1.el7.noarch 需要](#报错4-错误依赖检测失败socat-被-rabbitmq-server-389-1el7noarch-需要)
  - [启动RabbitMQ报错](#启动rabbitmq报错)
  - [rabbitmq使用guest登陆报错User can only log in via localhost](#rabbitmq使用guest登陆报错user-can-only-log-in-via-localhost)
- [Tip](#tip)
  - [Copy文件到虚拟机](#copy文件到虚拟机)
  - [启动Redis命令](#启动redis命令)
  

# 作业

## Task1
### 思路：使用redis的hash类型，唯一存放视频对应的key值，当调用函数时，将value值增加1
### 代码：task1_redis_counter.py
### 输出：
``` 
PS D:\Ellen\Python\Geek\practise> & C:/Users/myfoz/AppData/Local/Programs/Python/Python37/python.exe d:/Ellen/Python/Geek/practise/week5/task1_redis_counter.py
1
2
1
3
2
```
## Task2
### 思路：使用redis的expire功能，并利用字典的value值存放发送次数。如果key在字典中表示还没有过期，发送消息并将value值+1；如果key不在字典中，则增加一个key并设置过期时间。
### 代码：task2_redis_phone.py
### 输出
``` 
PS D:\Ellen\Python\Geek\practise> & C:/Users/myfoz/AppData/Local/Programs/Python/Python37/python.exe d:/Ellen/Python/Geek/practise/week5/task2_redis_phone.py
phone number：12345654321 send no.0 message in 1 minute:hello1
发送成功
phone number：12345654321 send no.1 message in 1 minute:hello2
发送成功
phone number：12345654321 send no.2 message in 1 minute:hello3
发送成功
phone number：12345654321 send no.3 message in 1 minute:hello4
发送成功
phone number：12345654321 send no.4 message in 1 minute:hello5
发送成功
1 分钟内发送次数超过 5 次, 请等待 1 分钟
phone number：88887777666 send no.0 message in 1 minute:hello1
发送成功
phone number：88887777666 send no.1 message in 1 minute:hello2
发送成功
```

## Task3
作业三：请用自己的语言描述如下问题：

### 在你目前的工作场景中，哪个业务适合使用 rabbitmq？ 引入 rabbitmq 主要解决什么问题?（非相关工作可以以设计淘宝购物和结账功能为例来描述）
目前工作中使用了消息中间件Kafka，上游生成的生产数据会写入Kafka，下游的数据仓库和Redis会从Kafka消费数据并提供数据报表和数据访问服务。
消息中间件主要解决了
1. 模块解耦。上游应用程序不用关心下游的存储是什么，下游的ETL也不用适配上游的不同数据产生方式，各自具有独立性和灵活性。
2. 可扩展性。上游应用程序产生一次数据，放入中间件即可。下游目前是两个消费方：数据仓库和Redis，以后可能会有更多的消费方例如数据分析、合规模块等，都可能消费数据。这样的话，上游应用程序在消费者增加的情况下不需要修改。
3. 流量控制。上游应用程序的数据产生速度和下游ETL的速度可能不一样，使用中间件可以保护下游消费方按照自己的能力消费数据，而不需要与上游速度保持完全一致。
4. 提高应用程序响应速度。上游应用程序产生数据后，只需要写入中间件就可以确认操作成功，不用等待下游存储成功才能结束。
   
### 如何避免消息重复投递或重复消费？
利用数据库的唯一键解决。
具体是对每一条消息生成唯一的一个业务Id，通过日志或者消息落库来做消息的重复控制，比如每消费成功一条消息，就把这条消息落库，然后消费者每次消费消息时，就看库中有没有该消息的业务Id，有就是已经消费过了，就不重复消费了。如果为了提高效率还可以把消息落入类似redis之类的缓存中。
参考：https://blog.csdn.net/qq_40837310/article/details/109033000

### 交换机 fanout、direct、topic 有什么区别？
Direct Exchange - 处理路由键。需要将一个队列绑定到交换机上，要求该消息与一个特定的路由键完全匹配。Producer(生产者)投递的消息被DirectExchange (交换机)转发到通过routingkey绑定到具体的某个Queue(队列)，把消息放入队列,然后Consumer从Queue中订阅消息。
Fanout Exchange – 不处理路由键。你只需要简单的将队列绑定到交换机上。一个发送到交换机的消息都会被转发到与该交换机绑定的所有队列上。
Topic Exchange – 将路由键和某模式进行匹配。此时队列需要绑定要一个模式上。符号“#”匹配一个或多个词，符号“*”匹配不多不少一个词。
参考：https://www.cnblogs.com/shenyixin/p/9084249.html

### 架构中引入消息队列是否利大于弊？你认为消息队列有哪些缺点？
引入消息队列有诸多优点，比如服务间异步通信，流量削峰， 解耦，异步下单等，当然凡事有利就有弊，消息队列也会增加系统的复杂性（比如要考虑消息重复的问题，考虑中间件的高可用性），增加性能开销（对中间件的调用），可能造成数据的不一致（由于系统、网络等故障带来数据在不同消费者中可能存在不一致）。
但架构是否引入消息队列要取决于要实现的业务场景。如果对性能和数据一致性要求很高，那可能并不适合用中间件，否则如果更需要引入消息队列带来的好处，建议使用消息队列。

# Issue

## 用wget下载Redis时提示“-bash: wget: 未找到命令”
解决：安装wget
yum -y install wget
参考文档：https://blog.csdn.net/djj_alice/article/details/80407769

下载Redis：
[root@192 ~]# wget https://download.redis.io/releases/redis-6.0.9.tar.gz?_ga=2.183928358.1428341305.1608890092-1709885980.1608890092
[root@192 ~]# mv redis-6.0.9.tar.gz?_ga=2.183928358.1428341305.1608890092-1709885980.1608890092 redis-6.0.9.tar.gz
解压：
[root@192 ~]# tar -zxvf redis-6.0.9.tar.gz

## 连接 Redis报错
错误：redis.exceptions.ConnectionError: Error 10060 connecting to 192.168.3.155:6379. 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。.
原因：虚拟机的6379端口没有打开
解决：1. 编辑/etc/sysconfig/iptables增加“-A INPUT -p tcp -m state --state NEW -m tcp --dport 6379 -j ACCEPT”
2.重启：[root@192 ~]# service iptables restart

## 安装 RabbitMQ报错
### 错误1：没有可用软件包 rabbitmq-server
原因：没有下载rpm包
解决：
1. 下载rabbitMQ的rpm包
wget https://dl.bintray.com/rabbitmq/all/rabbitmq-server/3.8.9/rabbitmq-server-3.8.9-1.el7.noarch.rpm
2. 安装 rpm -ivh rabbitmq-server-3.8.9-1.el7.noarch.rpm
[root@192 ~]# rpm -ivh rabbitmq-server-3.8.9-1.el7.noarch.rpm
警告：rabbitmq-server-3.8.9-1.el7.noarch.rpm: 头V4 RSA/SHA256 Signature, 密钥 ID 6026dfca: NOKEY
准备中...                          ################################# [100%]
正在升级/安装...
   1:rabbitmq-server-3.8.9-1.el7      ################################# [100%]

### 报错2：没有可用软件包 erlang
解决：
1. 下载erlang
http://packages.erlang-solutions.com/erlang/rpm/centos/7/x86_64/esl-erlang_23.1.5-1~centos~7_amd64.rpm
2. 安装依赖包
yum install -y epel-release
3. 安装erlang
yum install esl-erlang_23.1.5-1~centos~7_amd64.rpm

### 报错3：需要：libstdc++.so.6
解决：
https://blog.csdn.net/qiaoliang328/article/details/79266008
1. 查看哪个包需要libstdc++.so.6
yum provides libstdc++.so.6
找到libstdc++-4.8.5-44.el7.i686需要此包
2. 下载及安装
wget http://mirror.centos.org/centos/7/os/x86_64/Packages/libstdc++-4.8.5-44.el7.i686.rpm
yum install libstdc++-4.8.5-44.el7.i686.rpm

### 报错4： 错误：依赖检测失败：socat 被 rabbitmq-server-3.8.9-1.el7.noarch 需要
wget http://mirrors.aliyun.com/repo/epel-7.repo
yum -y install socat
参考：https://blog.csdn.net/lzxlfly/article/details/79406929

## 启动RabbitMQ报错
[root@192 ~]# systemctl start rabbitmq-server
错误：Job for rabbitmq-server.service failed because the control process exited with error code. See "systemctl status rabbitmq-server.service" and "journalctl -xe" for details.
解决：
1. 创建配置文件 /etc/rabbitmq/rabbitmq-env.conf
2. 添加内容：NODENAME=rabbit@localhost
参考：https://www.cnblogs.com/libra0920/p/12905270.html

## rabbitmq使用guest登陆报错User can only log in via localhost
解决：
1. 手动增加rabbitmq.conf文件，并设置文件内容为https://www.cnblogs.com/masy-lucifer/p/13551090.html
2. 修改rabbitmq.conf中的“loopback_users.guest“为false
3. 重启rabbitmq: systemctl restart rabbitmq-server
参考：https://www.imooc.com/article/305858

# Tip

## Copy文件到虚拟机
用pscp命令 https://www.cnblogs.com/weihua2020/p/13727131.html
D:\Program Files\PuTTY>pscp -P 22 D:\Ellen\Python\Geek\tool\libstdc++-4.8.5-44.el7.aarch64.rpm root@192.168.3.155:/root/

使用pscp， 用法：https://www.jianshu.com/p/101d42cd686b

## 启动Redis命令

[root@192 ~]# rabbitmq-plugins enable rabbitmq_management
Enabling plugins on node rabbit@192:
rabbitmq_management
The following plugins have been configured:
  rabbitmq_management
  rabbitmq_management_agent
  rabbitmq_web_dispatch
Applying plugin configuration to rabbit@192...
The following plugins have been enabled:
  rabbitmq_management
  rabbitmq_management_agent
  rabbitmq_web_dispatch

[root@192 rabbitmq]# systemctl start rabbitmq-server.service

[root@192 rabbitmq]# ss -ntpl | grep 5672
LISTEN     0      128          *:15672                    *:*                                                                                                users:(("beam.smp",pid=20635,fd=94))
LISTEN     0      128          *:25672                    *:*                                                                                                users:(("beam.smp",pid=20635,fd=81))
LISTEN     0      128       [::]:5672                  [::]:*                                                                                                users:(("beam.smp",pid=20635,fd=95))


