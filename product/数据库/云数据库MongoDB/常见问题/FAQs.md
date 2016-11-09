#### 常见问题FAQS

**Q：云数据库MongoDB是否支持外网访问**
A：暂不支持外网访问，需要购买CVM，通过内网的方式进行访问

**Q：产品售卖区域有哪些**
A：主要是广州、上海，其他地域在测试中，会陆续开放

**Q：云数据库MongoDB版是否支持动态添加Secondary节点**
A：目前暂时不支持，该功能在内测中，尽请期待

**Q：云数据库MongoDB版是否支持分片（sharding）**
A：目前暂时不支持，该功能在内测中，尽请期待

**Q：云数据库MongoDB与自建MongoDB的区别**
A：参见[云数据库MongoDB相比自建MongoDB的优势 ](http://www.qcloud.com/doc/product/240/%E4%BA%A7%E5%93%81%E4%BC%98%E5%8A%BF)

**Q：云数据库MongoDB版支持哪些语言的客户端进行连接**
A：云数据库MongoDB版针对客户端连接完全兼容MongoDB，只要是官方MongoDB版支持的客户端，云数据库全部支持。比如：C,C++,c#,java,node.js,python,php,perl等等，具体详情见官方链接，参见[https://docs.mongodb.org/ecosystem/drivers/](https://docs.mongodb.org/ecosystem/drivers/)

**Q：在shell里怎么连接腾讯云MongoDB**
A：`./mongo 10.66.136.162:27017 -u rwuser --password=******** --authenticationMechanism=MONGODB-CR --authenticationDatabase admin`
或者
`./mongo 10.66.136.162:27017/admin -u rwuser --password=********  --authenticationMechanism=MONGODB-CR`
`-u rwuser `现阶段指定用户名为 `rwuser`, 后续会推出用户管理的功能
`--authenticationMechanism=MONGODB-CR` 和 `--authenticationDatabase=admin` 是认证参数

mongo-cli版本需要在3.0.12及以上

**Q：业务程序里连接MongoDB的URI是什么样的**
A：`mongodb://rwuser:PASSWORD@IP:27017/admin?authMechanism=MONGODB-CR`
		推荐使用URI连接，参考文档：
	[https://www.qcloud.com/doc/product/240/3563](https://www.qcloud.com/doc/product/240/3563)
		[https://docs.mongodb.org/ecosystem/drivers/](https://docs.mongodb.org/ecosystem/drivers/)

**Q：我应该选用哪个版本的驱动程序**
A：尽量用高版本的，比如PHP可以选择mongo-1.6及以上

**Q：用meteor等各类框架、类库无法连接腾讯云MongoDB**
A：一般来说都是连接方式、URI拼接错误，请先检查核实

**Q：使用时如发现连接时好时坏**
A：有可能是长时间没访问，我们会踢掉空闲连接，驱动没实现自动重连，需要程序实现重连（参考经验值：重试3到5次，sleep 100ms左右）

**Q：oplog大小是多少，是否支持调整**
A：oplog为实例容量的10%，不支持调整

**Q：购买的容量是否包含oplog**
A：由于oplog存在MongoDB数据库内部，所以会占用部分用户的购买容量，默认是10%
 
**Q：腾讯云数据库MongoDB备份是周期多长，数据保留多少天**
A：目前所有实例均会每日自动备份，同时用户也可以发起手动备份。备份数据会保留5天。

**Q：腾讯云数据库MongoDB回档功能是否能回档到任意时间点**
A：由于备份数据保留5天，所以可以回档到5天内的时间点。特别说明的是回档时需要选择两次备份之间的时间点进行回档（如果您想回档的时间点后没有备份，请做一次手动备份即可选择该时间点）。另外，如果两次备份期间的数据操作导致oplog总流水超过实例容量的10%，则该两次备份之间的时间点不可回档。

**Q：备份是否支持下载**
A：暂不支持，正在内测中，敬请期待

**Q：当前开放了哪些权限**
A：当前只开放[RoleDBAdminAny和RoleReadWriteAny](https://docs.mongodb.org/v3.0/reference/built-in-roles/)两种角色的权限，暂时不开放root权限，后续会逐步放开一些权限，以及开放更多便捷实用的管理控制台功能来代替某些特殊权限的调用。

**Q：数据导入到腾讯云MongoDB实例后，占用空间比自建的MongoDB小**
A：可能原因是原始数据库长时间运行积累了大量的增删改操作，写操作时MongoDB出于性能考虑在空间分配时分配了大于实际数据的空间，删除数据后原空间没有被再次利用，综合下来导致整个数据库空间的空洞率较高，而导入数据时相当于做了一次类似磁盘整理的操作，使导入后的数据保存得相对紧凑，所以看起来数据变小了。

**Q：show dbs或者监控数据里看到数据库占用空间比实际数据大**
A：show dbs或者监控数据里的占用空间包括了oplog的数据空间，oplog默认为所选磁盘的10%
数据插入时会需要额外的空间存储BSON结构和索引，所以存储的空间比实际数据大
当前所用的MMAPv1引擎会对单条数据会分配额外的空间来存储数据，所以就会耗掉更多空间

**Q：如何使用 mongoose 连接腾讯云数据库MonogoDB**
A：[参见BBS](http://bbs.qcloud.com/thread-17852-1-1.html)

**Q：磁盘使用率达到100%会发生什么**
A：此时实例将处于封禁状态，该状态下不可写入数据，只能做读操作，尝试写入数据的连接将会被关闭。请及时关注自身业务发展和实例使用情况，当容量使用达到一定阈值时请适当扩容。

**Q：连接断开或者出现“Remote server has closed the connection”信息怎么办？**
A：需要实现一个重连机制，请参考 [实现重连](https://www.qcloud.com/doc/product/240/4980)
