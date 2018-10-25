##  Get Connection IP

1)	Get Instance ID and IP Information	
Enter the Tencent Cloud Hbase management center. You can view the instance ID, and get one or more IPs and ports that connect to Hbase.
![](https://mccdn.qcloud.com/static/img/14a8f475ffafe4c4cefdd84fe1737517/shili.png)

##  Access via SHELL
First [download](http://hbase-10010986.cos.myqcloud.com/hbase-1.1.3-bin.tar.gz) the Hbase client, extract to the CVM, and then modify the hbase-site.xml under conf to add the following configuration entry:
```
<configuration>
	<property>
        <name>hbase.zookeeper.quorum</name>
        <value>(The connection addresses and ports provided by Tencent Cloud which can be checked on the management console.)</value>
	</property>
	<property>
        <name> chbase.tencent.enable </name>
        <value> true</value>
	</property>
</configuration>

```


Then execute bin/hbase shell, and you can enter the Hbase command terminal:
![](https://mccdn.qcloud.com/static/img/1f97f2910f995e90c0061e8c017a3f36/image.png)







