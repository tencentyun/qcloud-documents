## 1 数据量限制

由于资源的有限性，腾讯对各种类型的MySQL实例做了数据量限制。下面从技术角度谈谈云数据库在大数据量下的单个实例以及单个表使用的影响：

**大数据量表**：单表数据量过大后，MySQL对单表资源的管理成本（数据、索引等）变更，将直接影响表的处理效率。

**大数据量实例**：云数据库默认存储引擎是Innodb，当实例中的数据及索引页都能被innodb 的cache buffer 缓存住时，MySQL实例能够支持很大的并发访问。如果实例数据量过大，会导致cache buffer 频繁的数据换出换进，MySQL瓶颈很快转到IO上，访问吞吐量直趋下降（例如，某云数据库实例本可以支持8000次访问，当数据量为cache buffer 大小的两倍时，仅能支持700次每秒左右的访问）。

## 2 连接数限制

云数据库的连接数上限为MySQL的系统变量max_connections，当云数据库实例连接数量超过max_connections时，新的连接将无法建立。

云数据库最大连接数默认值为实例内存1/5，且最大不超过10240, 最小不低于800。例如实例规格为8000MB内存，默认最大连接数为8000/5=1600。用户可以根据需要自行调整max_connections的值。

云数据库控制台可修改的max_connections最大为10000，如需更大连接数，请提交工单申请，腾讯云会根据实例内存的使用情况审批。

但是，连接数越多，消耗系统资源也越多。如果连接数超过实际系统的负载承受能力范围，必然影响系统服务质量。

关于max_connections可以参考MySQL官方手册。 

## 3 连接云数据库的MySQL客户端的版本限制

我们建议使用CVM系统自带的MySQL客户端和lib库，连接云数据库实例。

## 4 关于慢查询的说明

1对于使用Linux云服务器的开发者，可以通过云数据库导出工具获取慢查询日志，详见：云数据库数据导出。

2对于使用Windows云服务器的开发者，暂时不能直接获取慢查询日志。如果有需要，请提交工单联系我们获取慢查询日志文件。 


## 5 云数据库的binlog保存时间说明

由于MySQL binlog会占用大量的存储空间，所云数据库只保存最近3天的binlog。另外，如果binlog数据量增加太快，服务器磁盘存储不下3天的binlog，会人工删除binlog，释放空间。 

## 6 字符集说明

云数据库与MySQL数据库一样，默认字符集编码格式是：latin1，即ISO-8859-1编码格式。

虽然云数据库支持默认字符集编码的设置，但我们还是建议您在创建表时，显式的指定表的编码，并在连接建立时指定连接的编码。

这样，您的应用将会有更好的移植性。

关于MySQL字符集的相关资源请参考MySQL官方手册。 

下面是修改云数据库字符集的方法：

(1) 执行如下语句可修改云数据库实例的默认字符集编码：
```
SET @@global.character_set_client = utf8;
SET @@global.character_set_results = utf8;
SET @@global.character_set_connection = utf8;
SET @@global.character_set_server = utf8;
```

其中@@global.character_set_server 10分钟左右将自动同步到本机文件进行持久化(另外3个变量不会同步到本机文件)，迁移或重启将保持设置后的值。

(2) 执行如下语句可修改当前连接的字符集编码：
```
SET @@session.character_set_client = utf8;
SET @@session.character_set_results = utf8;
SET @@session.character_set_connection = utf8;
```

或者
```
SET names utf8;
```

(3) 对于php程序，可通过以下函数设置当前连接的字符集编码：
```
bool mysqli::set_charset(string charset);
```
或者
```
bool mysqli_set_charset(mysqli link, string charset);
```

详细请参考MySQL官方手册。 

(4) 对于java程序，可通过如下方式设置当前连接的字符集编码：
```
jdbc:mysql://localhost:3306/dbname?useUnicode=true&characterEncoding=UTF-8
```

详细请参考MySQL官方手册。 

## 7 操作限制

(1) 请不要修改MySQL实例已有帐号的信息和权限，这个操作可能会令部分集群服务失效。

(2) 创建库和表时建议统一使用Innodb引擎，这个选择能使实例在支持高访问的能力上有更好的表现。

(3) 请不要修改、停止master-slave关系，这个操作可能会令热备失效。