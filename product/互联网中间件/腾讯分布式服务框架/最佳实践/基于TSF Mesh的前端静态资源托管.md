## 操作场景 

该任务指导用户依托 TSF Mesh 技术以服务形式托管 Node.js 和 Nginx，最终验证 Node.js 与 Nginx 可以以服务形式注册、发现及成功调用。概要架构图如下：

![](https://main.qcloudimg.com/raw/1793a7207adf1bb9debaab11eda99ace.png)

- Nginx：前端资源托管。
- Node.js：后端服务。
- Sidecar：和服务运行在同一个 Pod 中，与 Pod 共享网络，服务感受不到 Sidecar 的存在。
	- Sidecar 代理服务向注册中心注册服务相关信息，以便其他服务发现自身。
	- Sidecar 作为 Pod 内服务的 HTTP 代理，可以自动发现其他服务。
- Consul Cluster：管理和配置 Sidecar 来执行策略并收集遥测。

## 操作步骤

### 步骤1：部署 Node.js 服务

1. 准备 Node.js 应用代码。
   可参考 [Demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/tsf%20nodejs%20demo/tsf-nodejs-demo-john.zip) 中配置文件进行构建，其它语言的 TSF Mesh 的 Demo 示例可参考 [TSF Mesh Demo](https://cloud.tencent.com/document/product/649/30436)。

2. 制作 Node.js + express 应用镜像，详细操作请参考 [制作容器镜像](https://cloud.tencent.com/document/product/649/17007)。
3. 上传到腾讯云镜像仓库，详细操作请参考 [镜像仓库](https://cloud.tencent.com/document/product/649/16695)。

4. 部署 Node.js 应用：
   1. [创建应用](https://cloud.tencent.com/document/product/649/13686#.E5.88.9B.E5.BB.BA.E5.BA.94.E7.94.A8)。应用类型选择 Mesh 应用。
   2. 在左侧导航栏选择**部署组** > **新建部署组**，创建 Node.js 的部署组。
   3. 在部署组页面，选择部署组右侧操作列的**部署应用**，选择刚刚创建的镜像，设置部署相关信息。


### 步骤2：托管前端静态资源

1. 手动在云服务器上安装 Nginx，详细操作请参考 Nginx 官网的 [安装说明](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/)。

2. 准备程序包。程序包的目录为：
   - `www` 目录：该目录名可任意，用于存放 Web 静态资源文件。
   - `start.sh` 脚本：将 www 目录下文件移动到 Nginx 站点目录下，同时启动 Nginx 服务。
   - `stop.sh` 脚本：停止 Nginx 服务。
   - `cmdline` 文件：检查 Nginx 进程是否存在的 `grep` 命令关键字。

   用户可参考 [nginx_demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/nginx_demo.zip) 了解各文件的具体作用和写法。

3. 根据 Dockerfile 生成本地镜像并上传到腾讯云镜像仓库。
4. 部署 Nginx 应用：
   1. [创建应用](https://cloud.tencent.com/document/product/649/13686#.E5.88.9B.E5.BB.BA.E5.BA.94.E7.94.A8)。应用类型选择 Mesh 应用。
   2. 在左侧导航栏选择**部署组** > **新建部署组**，创建 Node.js 的部署组。
   3. 在部署组页面，选择部署组右侧操作列的**部署应用**，选择刚刚创建的镜像，设置部署相关信息。


### 步骤3：测试 Node.js 服务和 Nginx 服务之间的调用

1. 通过外网 IP 访问测试 Node.js 应用。
   ![](https://main.qcloudimg.com/raw/294f01d232081462a244f7d8323976b2.png)

2. 通过外网 IP 访问测试前端静态资源。
   ![](https://main.qcloudimg.com/raw/92f731a6c2416ca0507a712d93785c09.png)

3. 在 Node.js 服务容器内 curl 访问 Nginx 服务。
   ```shell
   sudo docker ps   #查找容器id
   ```
   ![](https://main.qcloudimg.com/raw/21c24a732ea6f2f7577ef8b06dbf8d9d.png)

   ```shell
   sudo docker exec -it cfa4343f4a22 /bin/bash  #进入容器内部
   ```
   ![](https://main.qcloudimg.com/raw/7f8ade898b39b45a6dc94c9a48cf1871.png)

   在 Node.js 服务容器内 curl 访问 Nginx 服务成功。
   ![](https://main.qcloudimg.com/raw/aeb01fe440637c205c5533c9d371ce48.png)

  
