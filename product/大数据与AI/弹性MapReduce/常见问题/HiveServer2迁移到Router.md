### HiveServer2 迁移到 Router 的方法是什么？

1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在【集群列表】中选择对应的集群单击【ID/名称】进入集群详情页，在集群详情页中选择【集群资源】>【资源管理】，进入资源管理页面，单击【扩容】进入集群扩容页面。
![](https://main.qcloudimg.com/raw/6cc0dfec6655ecbac907b8448248705c.png)
在集群扩容页面中，选择扩容【节点类型】为【Router】，【扩容服务】为【Hive-2.3.5】，其他选项可根据需要自行选择。
![](https://main.qcloudimg.com/raw/b105f0c241eefb212930538b13cc1c3b.png)
2. 登录 router 节点，修改`hive-site.xml`配置文件。
![](https://main.qcloudimg.com/raw/83b77aecc5ee3f8fcdcc811e359f6234.png)
3. 关闭 master 上的 hive 服务。
在【集群服务】中选择 hive 组件的【操作】>【角色管理】，将 master 节点上的所有 hive 进程暂停，重启 Router 节点上的 hive 进程。
![](https://main.qcloudimg.com/raw/e84a86cd2db03fb635040d450e0d8a3c.png)
4. 测试。
在 router 上测试 hiveserver2。如果能正确连接并查询到已有的表，则说明迁移成功。
![](https://main.qcloudimg.com/raw/0bb6d0a7c08abaf483b14d5e931b3a34.png)
5. Hue 更改配置文件以至于代理到 Router 的 Hive 组件。
```
vim /usr/local/service/knox/conf/topologies/emr.xml 修改 HIVE 和 HIVEUI。
<service>
    <role>HIVE</role>
    <url>http://Router-ip:7003</url>
    <param>
        <name>replayBufferSize</name>
        <value>8</value>
    </param>
</service>
<service>
    <role>HIVEUI</role>
    <url>http://Router-ip:7003</url>
</service>
```
命令行执行重启 knox。
```
su hadoop 
/usr/local/service/knox/bin/gateway.sh stop ; /usr/local/service/knox/bin/gateway.sh start
```
