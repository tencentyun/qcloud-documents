This document provides a simple example that walks you through how to pull a table from data subscription to Redis, and an easy [RedisDemo Download](https://main.qcloudimg.com/raw/0a3b560fad57a27440f9445039552d2b/RedisDemo.zip). We are going through the following procedure in a Centos operating system.
### Environment configuration
1. Java environment configuration 
```
yum install java-1.8.0-openjdk-devel 
```

2. Download data subscription SDK
[Click to Download](https://mc.qcloudimg.com/static/archive/2a5032c6100b9cb3316f978bb32519e5/binlogsdk-2.6.0-release.jar.zip) 

3. Download jedis-2.9.0.jar
[Click to Download](https://main.qcloudimg.com/raw/130e0f114f84e6e7eb9cc16d2fecd58c/jedis-2.9.0.zip) 


### Obtain a key
Log in to the [Tencent Cloud console](https://console.cloud.tencent.com/), and click **Cloud Products** -> **Management Tools** -> **Cloud API Key** in the navigation bar, or you can also click here to enter the [Cloud Database console](https://console.cloud.tencent.com/cam/capi).

![](https://main.qcloudimg.com/raw/c6fa15fc47536b875448f911b00ed290.png)

### Select data subscription
1. Log in to the [DTS console](https://console.cloud.tencent.com/dtsnew/migrate/page), and select **Data Subscription** on the left to go to the Data Subscription page.
2. Click the name of a TencentDB instance to be synced to launch it. Then, go back to Data Subscription, and click the data subscription you have created. For more information, please see [How to Obtain Data Subscription](https://cloud.tencent.com/document/product/571/13707).

3. Check the corresponding DTS tunnel, IP, and Port, and enter the key you previously obtained in the RedisDemo.java file.

```
 context.setSecretId("AKIDfdsfdsfsdt1331431sdfds");  Enter the secretID obtained from the cloud API
        context.setSecretKey("test111usdfsdfsddsfRkeT");  Enter the secretKey obtained from the cloud API
    // Enter the ip:port obtained through the data subscription in the data migration service
        context.setServiceIp("10.66.112.181");  Enter the IP obtained from the data subscription configuration
        context.setServicePort(7507);  Enter the PORT obtained from the data subscription configuration

        // Create a consumer
        //SubscribeClient client=new DefaultSubscribeClient(context,true);
        final DefaultSubscribeClient client = new DefaultSubscribeClient(context);

        final Jedis jedis = new Jedis("127.0.0.1", 6379);  Enter the CVM and port of your Redis

        final String targetDatabase = "test"; Enter the name of the database to be subscribed to
        final String targetTable = "alantest";  Enter the name of the table to be subscribed to, including "id" and "name" fields. (ID is the primary key)

        // Create a subscription listener
        ClusterListener listener = new ClusterListener() {
            @Override
            public void notify(List<ClusterMessage> messages) throws Exception {
		//                System.out.println("--------------------:" + messages.size());
                for(ClusterMessage m:messages){
                    DataMessage.Record record = m.getRecord();
                    //Ignore the subscription messages you are not interested in
	            if(!record.getDbName().equalsIgnoreCase(targetDatabase) || !record.getTablename().equalsIgnoreCase(targetTable)){
                        //Note: Those you are not interested in must also be acknowledged.
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

                                //Get the id value and then the primary key, find the column called "name", and assign values to Redis by inserting "key" and "name".
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


### Compiling and test
1. 
```
[root@VM_71_10_centos ~]# javac -classpath binlogsdk-2.6.0-release.jar:jedis-2.9.0.jar -encoding UTF-8 RedisDemo.java 
```

2. Once launched, the data subscription works normally if no exception occurs. Check the local file previously configured.
```
 java -XX:-UseGCOverheadLimit -Xms2g -Xmx2g -classpath .:binlogsdk-2.6.0-release.jar:jedis-2.9.0.jar RedisDemo
```

3. Insert a data record into the database and update it, you will find that the record has been successfully inserted and modified in Redis. Then, delete the Redis, and the data in it will also be deleted.

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

