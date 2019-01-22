## 增删改查Helm应用
您可以通过控制台管理Helm应用的创建、删除、修改等操作，也可以通过本地安装Helm客户端连接到集群后，通过Helm命令行进行操作。
### 前置条件
1. 已有腾讯云TKE集群，且拥有0.28核CPU，180MiB内存的资源
2. 在集群内开通Helm应用管理功能
>注：开通Helm应用管理功能上，将在集群内安装Helm tiller相关组件。

![][openHelm]

### 创建Helm应用
1. 开通Helm应用管理功能后，可以在Helm应用控制台，点击新建按钮
2. 选择需要安装的Helm Chart，选择对应的版本，点击完成
    - 选择TencentHub，可选择公开和私有两种。详情见[TencentHub Helm Chart操作指引](https://cloud.tencent.com/document/product/857/31683)
    - 可选择其他Repo（选择Helm官方或自建Helm Repo仓库）
>注：选择其他Repo，默认只填写[Chart名称:版本]时，拉取Helm官方Chart包，无须设置用户名和密码。

![][createHelm]

### 更新Helm应用

1. 前往Helm应用控制台
2. 选择需要更新的Helm应用，点击更新
3. 选择需要更新的版本(其他Repo创建的应用需要手动填写版本号)
4. 根据业务需求填写自定义参数，完成。

![][updateHelm1]


### 回滚Helm应用
1. 前往Helm应用控制台
2. 选择需要更新的Helm应用，点击应用名称进入详情页。
3. 选择版本历史 tab页，选中需要回滚的版本，点击回滚。

### 删除Helm应用
1. 前往Helm应用控制台
2. 选择需要更新的Helm应用，点击删除
![][deleteHelm]

[openHelm]:https://main.qcloudimg.com/raw/1f75726d51ff11bfacd0bbd2c6fe1762.png
[createHelm]:https://main.qcloudimg.com/raw/51521d32a640cfe601e1e7b4578cc0cb.png
[updateHelm1]:https://main.qcloudimg.com/raw/0e54964b4b1e6dd8e3863f3dcc13dcd0.png
[deleteHelm]:https://main.qcloudimg.com/raw/134a4074e91639f41017b25ff5e6bc1f.png
