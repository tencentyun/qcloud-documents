This document provides a simple example that walks you through how to pull a table from data subscription to a local file, and an easy [LocalDemo Download](https://main.qcloudimg.com/raw/f145138da95d16063a3219f030f24625/LocalDemo.zip). We are going through the following procedure in a Centos operating system.
### Environment configuration
1. Java environment configuration
```
 yum install Java-1.8.0-openjdk-devel 
```

2. Download data subscription SDK
[Click to Download](https://mc.qcloudimg.com/static/archive/2a5032c6100b9cb3316f978bb32519e5/binlogsdk-2.6.0-release.jar.zip) 

### Obtain a key
Log in to the [Tencent Cloud console](https://console.cloud.tencent.com/), and click **Cloud Products** -> **Management Tools** -> **Cloud API Key** in the navigation bar, or you can also click here to enter the [Cloud Database console](https://console.cloud.tencent.com/cam/capi).

![](https://main.qcloudimg.com/raw/c6fa15fc47536b875448f911b00ed290.png)

### Select data subscription
1. Log in to the [DTS console](https://console.cloud.tencent.com/dtsnew/migrate/page), and select **Data Subscription** on the left to go to the Data Subscription page.
2. Click the name of a TencentDB instance to be synced to launch it. Then, go back to Data Subscription, and click the data subscription you have created. For more information, please see [How to Obtain Data Subscription](https://cloud.tencent.com/document/product/571/13707).
3. Check the corresponding DTS tunnel, IP, and port, and enter the key you previously obtained in the LocalDemo.java file.
```
  // Enter the key obtained from the cloud API
        context.setSecretId("AKIDfdsfdsfsdt1331431sdfds");  Enter the secretID obtained from the cloud API
        context.setSecretKey("test111usdfsdfsddsfRkeT");  Enter
        the secretKey obtained from the cloud API
	// Enter the ip:port obtained through the data subscription in the data migration service
        context.setServiceIp("10.66.112.181");  Enter the IP obtained from the data subscription configuration
        context.setServicePort(7507);
        Enter the PORT obtained from the data subscription configuration
        final DefaultSubscribeClient client = new DefaultSubscribeClient(context);
	// Enter the names of both database and table to be synced, and modify the name of the file where they are stored
        final String targetDatabase = "test"; Enter the name of the database to be subscribed to
        final String targetTable = "alantest"; Enter the name of the table to be subscribed to

        final String fileName = "test.alan.txt"; Enter the name of the local file where the data is stored
        
          client.addClusterListener(listener);
	// Enter the configuration information of dts-channel obtained from the configuration option subscribed to through the data migration
	client.askForGUID("dts-channel-e4FQxtYV3It4test"); Enter the name of the channel "dts" obtained from the data subscription
        client.start();
```


### Compiling and test
1. 
```
[root@VM_71_10_centos ~]# javac -classpath binlogsdk-2.6.0-release.jar -encoding UTF-8 LocalDemo.java
```

2. Once launched, the data subscription works normally if no exception occurs. Check the local file previously configured.
```
java -XX:-UseGCOverheadLimit -Xms2g -Xmx2g -classpath .:binlogsdk-2.6.0-release.jar LocalDemo
```
3. Check the "test.alan.txt" file we configured previously, you can see that the data has been pulled into it.

```
[root@VM_71_10_centos ~]# cat test.alan.txt  

checkpoint:144251@3@357589@317713
record_id:000001000000000004D9110000000000000001
record_encoding:utf8
fields_enc:latin1,utf8
gtid:4f21864b-3bed-11e8-a44c-5cb901896188:1562
source_category:full_recorded
source_type:mysql
table_name:alantest
record_type:INSERT
db:test
timestamp:1523356039
primary:

Field name: id
Field type: 3
Field length: 2
Field value: 26
Field name: name
Field type: 253
Field length: 4
Field value: alan

```


