##  获取连接IP

1)	申请资格
[点击](https://www.qcloud.com/product/HBase.html)进入产品介绍页申请测试资格

2)	获取实例ID和IP信息	
进入腾讯云Hbase管理中心，可以查看实例ID，并获取连接Hbase的一个或多个IP和端口：
![](https://mccdn.qcloud.com/static/img/14a8f475ffafe4c4cefdd84fe1737517/shili.png)

##  通过SHELL访问
首先[下载](http://hbase-10010986.cos.myqcloud.com/hbase-1.1.3-bin.tar.gz)Hbase客户端软件，然后解压到云主机，然后修改conf下的hbase-site.xml添加如下配置项目：
```
<configuration>
	<property>
        <name>hbase.zookeeper.quorum</name>
        <value>(腾讯云提供的连接地址和端口，管理控制台可查)</value>
	</property>
	<property>
        <name> chbase.tencent.enable </name>
        <value> true</value>
	</property>
</configuration>

```


然后执行bin/hbase shell，可以进入Hbase命令终端：
![](https://mccdn.qcloud.com/static/img/1f97f2910f995e90c0061e8c017a3f36/image.png)






