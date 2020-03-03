### HiveServer2 迁移到 Router 的方法是什么？
1. 登录 EMR 控制台，在左侧菜单栏选择【云硬件管理】，然后单击【新增router节点】进入新增 Router 节点页面，选择安装【hive 2.1.1】组件。
![](https://main.qcloudimg.com/raw/d6f24f0d76260c53e9e5fbffadc98f9e.png)
2. 登录 router 节点，修改`hive-site.xml`配置文件。
 ![](https://main.qcloudimg.com/raw/0a9fdf9401f68f799db530bee95d34c0.png)
3. 关闭 master 上的 hive 服务。
在组件管理 hive 角色管理页面将 master 节点上的所有 hive 进程暂停，重启 Router 节点上的 hive 进程。
![](https://main.qcloudimg.com/raw/964453733f4ef2af326fd7890380f1a0.png)
4. 测试。
在 router 上测试 hiveserver2。如果能正确连接并查询到已有的表，则说明迁移成功。
![](https://main.qcloudimg.com/raw/3ffae19871f972bef3ccd8796deb2e27.png)
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
