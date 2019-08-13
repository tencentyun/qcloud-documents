本文档旨在帮助大家了解如何快速创建一个容器集群内的 Nginx 服务。Nginx 是一个异步框架的 Web 服务器，也可以用作反向代理，负载平衡器 和 HTTP 缓存。



>!在创建 Nginx 服务之前，您必须拥有一个已经创建好的容器集群。有关如何创建集群的详细信息，参见 [集群](https://cloud.tencent.com/document/product/649/13684)。



## 创建 Nginx 应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 单击左侧导航栏 **应用管理**。
3. 在应用列表上方单击【新建应用】。
4. 设置应用信息后，单击【提交】按钮。
   - 部署方式：选择容器部署
   - 应用类型：选择普通应用
5. 单击【提交】。

![](https://main.qcloudimg.com/raw/59db1f1fe2cdd324e3dc2e14d6bd2366/createapp.png)

## 推送 Nginx 镜像到镜像仓库

首次使用镜像仓库需要进行初始化镜像仓库，参考 [镜像仓库](https://cloud.tencent.com/document/product/649/16695)。

1. 在应用列表中单击目标应用 **ID/应用名** 进入应用详情页。
2. 单击【镜像】标签页。
3. 单击【使用指引】按钮，弹出使用镜像的相关命令。
4. 在开发机上，通过 `docker pull nginx` 获取最新的 nginx 官方镜像。使用 `docker tag` 命令给镜像打 tag，然后执行 `docker push` 命令将镜像推送到镜像仓库。
5. 刷新镜像标签页，在镜像版本列表中显示出镜像信息。

![](https://main.qcloudimg.com/raw/e31ba244e74f6ee7d351b3c967b8dd22/imageInfo.png)



## 创建部署组

1. 在应用的详情页中单击【部署组】标签页。
2. 单击【新建部署组】按钮，在弹框中填写部署组相关信息，可参考下方截图填写。注意网络访问方式选择【公网】，端口映射中两个端口号都填写 80。
   ![](https://main.qcloudimg.com/raw/31f7816456e45c8176660f54af922817/creategroup.png)
3. 单击【提交】按钮。



## 部署应用

1. 单击部署组列表右侧的【部署应用】按钮。
2. 在部署应用的弹框中填写镜像等信息，参考下图填写。
   ![](https://main.qcloudimg.com/raw/90ace29375b5ef3b6ca02022e05283ea/deploy.png)
3. 单击【提交】按钮。



## 验证

1. 部署成功后，部署组的状态变为运行中。
   ![](https://main.qcloudimg.com/raw/e6153a8ffcfdad0cab9cebe6d112ceb1.png)
2. 复制负载均衡 IP，在浏览器地址栏粘贴后，显示 Nginx 欢迎页面。
   ![](https://main.qcloudimg.com/raw/3ff519319e5dc4d3b3cc3d6668281a45.png)
