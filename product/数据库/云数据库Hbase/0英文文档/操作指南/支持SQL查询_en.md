#### 1. phoenix Configuration
Before using phoenix, you need to download the [jar package of phoenix](http://hbase-10010986.cos.myqcloud.com/phoenix-4.8.1-HBase-1.1.tar.gz) we provide, and extract it to any directory of CVM after downloading:
![](https://mc.qcloudimg.com/static/img/4b4c9ca995e86e9b4ea41274d10be5e5/h1.png)
Then enter the directory bin, and add the following configuration to the configuration file hbase-site.xml

```
<property>
<name>hbase.zookeeper.quorum</name>
<value>(The connection addresses and ports provided by Tencent Cloud which can be checked on the management console.)</value>
</property>
<property>
<name> chbase.tencent.enable </name>
<value> true</value>
</property>
```

#### 2. Test Availability of phoenix
Under the directory bin, you can use shell to test the availability of phoenix, ./sqlline.py. 
![](https://mc.qcloudimg.com/static/img/c118152d54de3501f7d7de8c4b7e9c61/h2.png)
Then enter !tables.
![](https://mc.qcloudimg.com/static/img/5a1bbf8a14df481d9ed96c44d514d43c/h3.png)

#### 3. Use of Basic SQL Statements
![](https://mc.qcloudimg.com/static/img/b6b0004ade79b5d8d7a2f81a2cb31731/h4.png)
![](https://mc.qcloudimg.com/static/img/d35fd982bbbf1be6ee58fb524ecaf8a1/h5.png)
![](https://mc.qcloudimg.com/static/img/875b3745a8e21a8e75dc3dcf9993112b/h6.png)
![](https://mc.qcloudimg.com/static/img/e7250978669c40dce1d55fdb83f6b9f5/h7.png)
Please refer to the official website of phoenix http://phoenix.apache.org/language/index.html for more examples.
