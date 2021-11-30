## 操作场景
实例间迁移是指在腾讯云上分配的实例之前进行数据迁移，包括跨版本迁移、标准版升级为集群版等。云数据库 Redis 支持将 Redis 2.8 标准版迁移到 Redis 4.0 集群版。

## 前提条件
业务停服，停止对要迁移的实例进行写入。

## 操作步骤
1. 登录 [云数据库 Redis 控制台](https://console.cloud.tencent.com/redis)。
2. 在实例列表中，选择需要的实例，单击实例名，进入实例管理页面。
3. 单击右上角的【手动备份】，进行数据备份。
4. 等待实例完成备份，备份完成后可以在备份列表中看到备份的下载地址。
5. 在相同地域的云服务器 CVM 通过 wget 下载实例备份。
6. 通过`redis-resotre`命令将备份文件导入到新的集群版，redis-restore 导入命令参见 [使用 redis-port 工具迁移](https://cloud.tencent.com/document/product/239/36157)。
![备份图示](https://main.qcloudimg.com/raw/02e92a335201efd8a5d748bf5325df4a.png "备份图示")
    



