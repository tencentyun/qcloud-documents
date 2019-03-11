##  获取连接 IP

**获取实例 ID 和 IP 信息**	
进入腾讯云 Hbase 管理中心，可以查看实例 ID，并获取连接 Hbase 的一个或多个 IP 和端口。
![](https://mccdn.qcloud.com/static/img/14a8f475ffafe4c4cefdd84fe1737517/shili.png)

##  通过 SHELL 访问
首先 [下载](http://hbase-10010986.cos.myqcloud.com/hbase-1.1.3-bin.tar.gz) Hbase 客户端软件，然后解压到云服务器，然后修改 conf 下的 hbase-site.xml 添加如下配置项目：
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

然后执行 bin/hbase shell，可以进入Hbase命令终端：
![](https://mccdn.qcloud.com/static/img/1f97f2910f995e90c0061e8c017a3f36/image.png)
