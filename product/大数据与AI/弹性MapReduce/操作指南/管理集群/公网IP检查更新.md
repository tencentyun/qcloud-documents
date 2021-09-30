## 功能介绍  
EMR 控制台支持检查更新 master1 上的公网 IP，更新或添加后集群配置信息 Master 公网 IP 的同步更新，服务 WebUI 访问地址同步更新。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr) 在集群列表中单击对应的集群 ID，进入实例信息后，在**基础配置 > Master 公网 IP** 右侧支持检查更新当前 Master 公网 IP。
 ![](https://main.qcloudimg.com/raw/fe19c931476634a1f3075fede377d876.png)
2. 可将 master 上真实的外网 IP 和 EMR 中存储的外网 IP 对比，如果不一致，通过继续操作将最新的 master 公网 IP 在 EMR 相关业务数据库中更新，同步完成自动刷新当前页面。
![](https://main.qcloudimg.com/raw/1497d07e6cfb2b61ae8c3e63161e4d09.png)![](https://main.qcloudimg.com/raw/8bfa1fd235f5d07aede76d7a10a646e7.png)
