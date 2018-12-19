### 1. 登录 Master 机器
您可以通过访问 [腾讯云控制台>云主机列表](https://console.cloud.tencent.com/cvm/index)，找到以 emr-master.1 开头的云主机（也就是带外网 IP 的那一台云主机）登录到 Master 节点。
>**注意：**您只能在以 emr-master.1 开头的云主机上进行此操作。

### 2. 部署信息
Presto 在 emr-master.1 节点上部署了 coordinator 进程，core 和 task 节点上部署了 worker 进程。软件安装在：
```
    cd /usr/local/service/presto
    su hadoop
```
### 3. 预置连接器使用
* Presto 服务预置了 Hive 连接器，连接 Hive 的 metastore 以读取 Hive 的表信息进行查询。
* 进入 Presto 客户端工具，并切换用户：
```
    cd /usr/local/service/presto-client
    su hadoop
```
* 执行命令查看 Hive 的表：
```
    ./presto
      --server localhost:9000
      --catalog hive
      --schema default
      --user hadoop
      --execute "show tables"
```

### 4. 更多连接器
您可以通过访问 [Presto 官方文档](https://prestodb.io/docs/current/connector.html) 获取更多连接器的设置方法。
