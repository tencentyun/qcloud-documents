本文介绍通过 SSH 访问主机的具体操作方法。

## 前提条件
- 独享集群为 MySQL 独享集群。
- 独享集群开放 OS 权限，详情请参见 [创建 MySQL 独享集群](https://cloud.tencent.com/document/product/1322/76526)。
- 已创建主机帐号，详情请参见 [创建主机帐号](https://cloud.tencent.com/document/product/1322/76585)。

## 背景信息
独享集群主机不支持外网访问，为保障数据库主机的安全性，仅支持同 VPC 下的服务器对主机进行访问。

## 操作步骤
1. 登录 [云数据库 MySQL 独享集群控制台](https://console.cloud.tencent.com/dbdcp)。
2. 在页面上方选择目标地域。
3. 找到目标集群，单击集群 ID，然后选择**主机列表**，或直接单击**操作**列的**管理主机**。
![](https://qcloudimg.tencent-cloud.cn/raw/eb7418889e5eee2e81f0e1bcecdd05da.png)
4. 在主机列表，找到目标主机，查看**主机帐号**以及 **IP 地址**。
![](https://qcloudimg.tencent-cloud.cn/raw/90c12f45665cac0d3ac9d76330e35c26.png)
5. 通过 SSH 命令进行连接。
```
bash ssh -p 36000 <主机帐号>@<IP地址>
```

## 主机权限
登录主机后，您拥有主机的部分权限，可执行部分操作。
