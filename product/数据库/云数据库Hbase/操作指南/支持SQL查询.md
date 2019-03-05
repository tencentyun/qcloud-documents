#### 1.phoenix配置
需要使用phoenix需要先下载我们提供的[phoenix的jar包](http://hbase-10010986.cos.myqcloud.com/phoenix-4.8.1-HBase-1.1.tar.gz)，下载后解压到CVM的任意一个目录下:
![](https://mc.qcloudimg.com/static/img/4b4c9ca995e86e9b4ea41274d10be5e5/h1.png)
然后进入bin目录下，在配置文件hbase-site.xml中添加如下配置

```
<property>
<name>hbase.zookeeper.quorum</name>
<value>(腾讯云提供的连接地址和端口，管理控制台可查)</value>
</property>
<property>
<name> chbase.tencent.enable </name>
<value> true</value>
</property>
```

#### 2.测试phoenix的可用性
在bin目录下可以使用shell来测试phoenix的可用性，./sqlline.py 
![](https://mc.qcloudimg.com/static/img/c118152d54de3501f7d7de8c4b7e9c61/h2.png)
再输入!tables
![](https://mc.qcloudimg.com/static/img/5a1bbf8a14df481d9ed96c44d514d43c/h3.png)

#### 3.基本SQL语句的使用
![](https://mc.qcloudimg.com/static/img/b6b0004ade79b5d8d7a2f81a2cb31731/h4.png)
![](https://mc.qcloudimg.com/static/img/d35fd982bbbf1be6ee58fb524ecaf8a1/h5.png)
![](https://mc.qcloudimg.com/static/img/875b3745a8e21a8e75dc3dcf9993112b/h6.png)
![](https://mc.qcloudimg.com/static/img/e7250978669c40dce1d55fdb83f6b9f5/h7.png)
更多的范例详见phoenix官网http://phoenix.apache.org/language/index.html