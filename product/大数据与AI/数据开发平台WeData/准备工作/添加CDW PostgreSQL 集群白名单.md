为了在项目中使用和访问 CDW PostgreSQL 集群，您需要将下列腾讯云 WeData 的访问 IP 地址添加到 CDW PostgreSQL 集群允许的白名单中。
```
118.89.220.0/24, 139.199.116.0/24, 140.143.68.0/24, 152.136.131.0/24, 119.81.70.150.0/24, 81.70.161.0/24, 81.70.195.0/24, 81.70.198.0/24, 120.82.156.22.0/24, 82.156.221.0/24, 82.156.23.0/24, 82.156.24.0/24, 121.82.156.27.0/24, 82.156.82.0/24, 82.156.84.0/24, 82.157.119.0/24
```
## 操作步骤
1. 查看集群用户名及数据库
登录 [云数据仓库 PostgreSQL](https://console.cloud.tencent.com/cdwpg) 控制台，在**集群列表**中选择目标集群点击**管理**。
![](https://main.qcloudimg.com/raw/d630511e1a61dbbbbf5f470986d9228e.png)
2. 选择**配置**，单击**新建白名单**。
![](https://main.qcloudimg.com/raw/7677d7a6d850524ce37bb2f56119e118.png)
3. 在弹窗中配置白名单名称、用户及数据库信息。
![](https://main.qcloudimg.com/raw/60df7783cf18ac3dbca35dd1f70a287d.png)

>? 腾讯云 WeData 使用 CDW PostgreSQL 集群默认数据库进行连通性测试，请填写默认用户名并至少对默认数据库 postgresql 开通白名单。如果还需要使用集群中的其他数据库，请同时对该数据库开通白名单。默认用户名及数据库信息查看方式：![](https://main.qcloudimg.com/raw/82517b0876c68b4f9394dc34e646b177.png)

**示例：**如果您需要在项目中绑定名为“workpace”的 CDW PostgreSQL 集群（默认集群用户名：wedata, 默认数据库名：postgres），并且使用该集群中的数据库“database1”进行数据开发。那么您需使用用户名“wedata”将默认数据库“postgres”以及“database1”开通。
 ![](https://main.qcloudimg.com/raw/fc0ba595e8fd97f9ca229ca85892c940.png)
 

 
