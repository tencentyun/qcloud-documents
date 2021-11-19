本文将以一个简单案例来说明数据订阅中拉取对应表到 Redis 的功能，并且提供简易 [RedisDemo 下载](https://main.qcloudimg.com/raw/0a3b560fad57a27440f9445039552d2b/RedisDemo.zip) 。以下操作将在 CentOS 操作系统中完成。

## 配置环境
- Java 环境配置 
```
yum install java-1.8.0-openjdk-devel 
```
- [数据订阅 SDK 下载](https://main.qcloudimg.com/raw/2aa7b213535065def5655712c8494182/binlogsdk-2.7.0-official.jar)
- [jedis-2.9.0.jar 下载](https://main.qcloudimg.com/raw/130e0f114f84e6e7eb9cc16d2fecd58c/jedis-2.9.0.zip)

## 获取密钥
登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 获取密钥。

## 选择数据订阅
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dtsnew/migrate/page)，选择左侧的**数据订阅**，进入数据订阅页面。
2. 选择需同步的 TencentDB 实例名，然后单击启动，再返回数据订阅，单击您所创建的数据订阅。 详细介绍请参考 [数据订阅](https://cloud.tencent.com/document/product/571/13707)。
3. 查看对应的 DTS 通道、IP 和 Port，然后结合之前的密钥填写到对应 RedisDemo.java 里面。
```
context.setSecretId("AKIDfdsfdsfsxxxxxsdfds"); 请填写您从云 API 获取的 secretID
        context.setSecretKey("test111usdxxxxxfRkeT"); 请填写您从云 API 获取的 secretKey
    // 在数据迁移服务里面通过数据订阅获取到对应的 IP,PORT 填写到此处
        context.setServiceIp("10.xx.xx.181"); 请填写您从数据订阅配置获取到的 IP
        context.setServicePort(7507); 请填写您从数据订阅配置获取到的 PORT

        // 创建消费者
        //SubscribeClient client=new DefaultSubscribeClient(context,true);
        final DefaultSubscribeClient client = new DefaultSubscribeClient(context);

        final Jedis jedis = new Jedis("127.0.0.1", 6379); 请填写您对应的 Redis 主机和端口

        final String targetDatabase = "test"; 填写您所要订阅的库名
        final String targetTable = "alantest"; 填写您所要订阅的表名，表有2个字段分别是 id,name（id 是做了主键）

        // 创建订阅监听者 listener
        ClusterListener listener = new ClusterListener() {
            @Override
            public void notify(List<ClusterMessage> messages) throws Exception {
		//                System.out.println("--------------------:" + messages.size());
                for(ClusterMessage m:messages){
                    DataMessage.Record record = m.getRecord();
                    //过滤不感兴趣的订阅信息
	            if(!record.getDbName().equalsIgnoreCase(targetDatabase) || !record.getTablename().equalsIgnoreCase(targetTable)){
                        //注意：对于不感兴趣的信息也必须 Ack
                        m.ackAsConsumed();
                        continue;
                    }

                    if(record.getOpt() != DataMessage.Record.Type.BEGIN && record.getOpt() != DataMessage.Record.Type.COMMIT){
                        List<DataMessage.Record.Field> fields = record.getFieldList();

                        //INSERT RECORD
                        //String pk = record.getPrimaryKeys();
			
                        if(record.getOpt() == DataMessage.Record.Type.INSERT){
			    
			    String keyid="";
			    String value="";
                            for (DataMessage.Record.Field field : fields) {

                                //先获取 id 值,需要有 primary key,然后找到名为 name 的列，赋值给 Redis 插入 key 和 name 对应的 value
				if(field.getFieldname().equalsIgnoreCase("id")){
                                    keyid=field.getValue();
               continue;
                                }
				if(field.getFieldname().equalsIgnoreCase("name")){
				    value=field.getValue();
                                  
                                }
				jedis.set(keyid, value);
                            }

                        }
```

##  编译操作与检验
1. 使用 javac 命令进行编译。
```
[root@VM_71_10_centos ~]# javac -classpath binlogsdk-2.6.0-release.jar:jedis-2.9.0.jar -encoding UTF-8 RedisDemo.java 
```
2. 执行启动，如果没有异常报错就是正常在服务了，然后查看对应之前设置的落地文件。
```
java -XX:-UseGCOverheadLimit -Xms2g -Xmx2g -classpath .:binlogsdk-2.6.0-release.jar:jedis-2.9.0.jar RedisDemo
```
3. 查看进行数据库插入和 update 操作，并从 redis 观察发现确实插入并修改成功了,最后进行 delete 操作，redis 对应的数据也被删除掉了。
```
MySQL [test]> insert into alantest values(1001,'alan1');
Query OK, 1 row affected (0.00 sec)

MySQL [test]> update alantest set name='alan2' where id=1001;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

------------------------
127.0.0.1:6379> get 1001
"alan2"

MySQL [test]> update alantest set name='alan3' where id=1001;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

------------------------
127.0.0.1:6379> get 1001
"alan3"

MySQL [test]> delete from alantest where id=1001;
Query OK, 1 row affected (0.00 sec)

-----------------------

127.0.0.1:6379> get 1001
(nil)
```
