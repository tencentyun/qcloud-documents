## 1 版本&引擎

1)	当前只支持MMAPv1引擎，即将支持WiredTiger引擎
2)	MMAPv1引擎使用MongoDB 3.0大版本的最新版本

## 2 副本集&分片集群

### 2.1 副本集

创建MongoDB实例时有以下两种选择：

|节点配置|说明|
|:--:|:--:|
|1主1从1仲裁|包含1个Primary节点、 1个Secondary节和1个Arbiter节点|
|1主2从|包含1个Primary节点、 2个Secondary节|

每一个副本集前面都有一组proxy(MongoDB服务组件中的mongos)，连接服务的URI形如：
```
mongodb://rwuser:password@10.66.77.88:27017/admin?authMechanism=MONGODB-CR
```

如有需要，您可以在连上MongoDB服务后，在您的驱动里设置优先从Secondary读取。

### 2.2 分片集群

即将推出分片集群，敬请期待。

## 3 连接用户名

目前只能使用默认用户“rwuser”，其角色为[readWriteAnyDatabase+dbAdmin](https://docs.mongodb.org/v3.0/reference/built-in-roles/)，也就是说您可以用此用户读写任意数据库，但是不具备高危操作的权限。
即将支持用户自定义账号管理功能。


## 4 尽量避免写满磁盘

当实例磁盘被写满100%后会被禁止执行写操作，所以请根据业务发展情况及时扩容，如果出现磁盘写满封禁情况，请联系客服处理。