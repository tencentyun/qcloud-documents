## 创建NFS服务

### 教程目的
本教程介绍一种利用容器自建NFS服务来共享cbs云盘的方法。

### NFS简介
NFS是Network File System的简写,即网络文件系统。NFS允许一个系统在网络上与他人共享目录和文件。通过使用NFS，用户和程序可以像访问本地文件一样访问远端系统上的文件。

### 容器服务创建NFS服务说明

步骤：

- 第一步：选择镜像
![Alt text](https://mc.qcloudimg.com/static/img/95fa43aef0712a1c798ac2c762d1d43d/%7BFA88D589-64B7-4F27-90F2-1E8A86485DA6%7D.png)
按照上图创建服务，选择 ccr.ccs.tencentyun.com/library/nfs-server tag为latest 的公有镜像

- 第二步：在容器配置中添加数据盘
![Alt text](https://mc.qcloudimg.com/static/img/728edfe98f53421d0b621c4f2a290649/%7BE25FD03D-CEAC-406E-8582-913897778175%7D.png)

- 第三步：在容器配置中设置挂载路径
![Alt text](https://mc.qcloudimg.com/static/img/728edfe98f53421d0b621c4f2a290649/%7BE25FD03D-CEAC-406E-8582-913897778175%7D.png)
请务必按照上图所示将云盘挂载到/exports中

- 第四步：在容器配置中添加端口映射
![Alt text](https://mc.qcloudimg.com/static/img/728edfe98f53421d0b621c4f2a290649/%7BE25FD03D-CEAC-406E-8582-913897778175%7D.png)
如图，设置访问方式为集群内访问，并添加111,2049,20048三个端口映射。

- 第五步：完成创建容器

注意：在使用该方法创建的NFS盘服务时，请在挂载时指定挂载路径为 服务集群IP:/exports，如图所示。
