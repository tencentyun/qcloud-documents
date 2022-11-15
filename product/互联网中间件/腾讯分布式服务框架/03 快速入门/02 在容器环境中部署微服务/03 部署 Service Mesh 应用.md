## 操作场景

Mesh 应用支持 Go/Python/C++ 等不同编程语言，通过 Service Mesh 技术接入 TSF，无需修改代码，支持全套 TSF 服务治理能力。如果您想了解如何实现微服务应用的相关功能，请参见 [Mesh 应用开发](#building)。

为了帮助您快速体验如何在 TSF 中部署微服务应用，TSF 提供了一组 Mesh 应用 Demo，包含 user、shop 和 promotion 三个应用。本文以一个示例介绍如何在容器环境中部署 Service Mesh 应用，并实现简单的服务调用。



## 前提条件

已参见 [快速创建一个容器集群](https://cloud.tencent.com/document/product/649/55505) 创建好一个容器集群并导入云主机。


[](id:building)
## 操作步骤

[](id:step1)
### 步骤1：新建应用

1. 在左侧导航栏，单击**应用管理**，进入应用列表页。
2. 在应用列表上方单击**新建应用**。
3. 设置应用信息，单击**提交**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/8944525b1b3eec0a85630d055dc4e31d.png)
   - **应用名**：填写 **user**。
   - **部署方式**：选择 **容器部署**。
   - **业务类型**：选择 **业务应用**。
   - **开发语言**：选择 **其他语言**。
   - **开发框架**：选择 **其他框架**。
   - **应用类型**：选择 **Mesh应用**。
   - **服务配置：**选择使用 **使用本地Spec.yaml**。
   - **标签**：用于分类管理资源，可不选。详情参见 [标签](https://cloud.tencent.com/document/product/649/53869)。
   - **数据集**：选择“无”。用户可以通过数据集管理配置不同的子账号和协作者使用不同资源的权限，详情参阅 [数据集管理](https://cloud.tencent.com/document/product/649/38326)。
   - **备注**：选填，可留空。
4. 在弹出的弹窗中单击**确认**，前往上传镜像并部署应用。
   ![](https://main.qcloudimg.com/raw/761b87560d72e3a9e4b00a0d3b05a3b3.png)



[](id:step2)
### 步骤2：上传镜像

#### 前提条件

- [安装 docker](https://www.docker.com/products/docker-desktop)。
- 使用 `sudo` 允许系统管理员让普通用户执行 `docker` 命令。
- [下载并解压 Demo](https://main.qcloudimg.com/raw/b4a0a86d3eb11bcee368b3eccf6e3052/tsf_python_docker_demo-1225.tar.gz)（包含 user、shop 和 promotion 三个应用）。



#### 1. 初始化镜像仓库

首次使用 [镜像仓库](https://console.cloud.tencent.com/tsf/image) 时，需要进行初始化操作，设置登录镜像仓库的登录密码。
![](https://main.qcloudimg.com/raw/464e16a2db8c976784a226aa031b1c56.png)

TSF 会针对每个容器应用创建一个名为 `tsf_<账号ID>/<应用名>` 的镜像仓库。
![](https://qcloudimg.tencent-cloud.cn/raw/44244ad9524cc86d0ac97c21c0f666d4.png)

#### 2. 制作镜像

1. 解压下载的 Demo 程序包，进入`demo-mesh-user/`目录，在 dockerfile 文件所在目录下，执行如下命令制作镜像。
   ```dockerfile
   docker build . -t ccr.ccs.tencentyun.com/tsf_<主账号 ID>/<应用名>:[tag]
   ```
   其中`<主账号 ID>`对应用户腾讯云的**主账号 ID**（注意不是当前登录账号 ID，主账号 ID 可以在腾讯云控制台账号信息页面获取。），`<应用名>`表示控制台上刚刚创建的应用名。`[tag]`为镜像的 tag，用户可自定义。
   参见示例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/d83e710fe3a81515fdc0c26a8911e9a8.png)
2. 命令执行完成后，执行`docker image ls`命令查看创建的镜像。
![](https://qcloudimg.tencent-cloud.cn/raw/5b1ac6663dfe313457f08505ca41d20f.png)
   可查看到该镜像 tag 和 ImageId，这两个参数将用于推送镜像到镜像仓库。
更多关于制作镜像相关的操作请参见 [制作容器镜像](https://cloud.tencent.com/document/product/649/17007)。

#### 3. 推送镜像到镜像仓库

1. 在[应用列表](https://console.cloud.tencent.com/tsf/app)中，单击在 [步骤1. 新建应用](#step1) 中创建的应用“ID/应用名”，进入部署组页面。
2. 选择**镜像**标签页，单击**上传程序包/镜像**，可以获得登录镜像仓库、拉取镜像和推送镜像到仓库的命令。
  ![](https://qcloudimg.tencent-cloud.cn/raw/57416809cf15c4220511e4567e2aac61.png)
3. 复制**使用指引**中登录腾讯云 docker registry 的命令并执行。
   ```
   sudo docker login --username=<账号 ID>  ccr.ccs.tencentyun.com
   ```
   >?用户需要输入两次密码，首次为 sudo 密码，第二次为镜像仓库登录密码。
   命令行工具显示 `Login Succeeded` 即表示登录成功。
4. 登录成功后，复制**使用指引**中给镜像打tag的命令并执行。
   ```
   sudo docker tag [ImageId] ccr.ccs.tencentyun.com/tsf_<账号ID>/<应用名>:[tag]
   ```
   其中 [ImageId] 和 [tag] 是在制作镜像时获取。
   >?若此时需要输入密码，请输入sudo 密码。
5. 复制**使用指引**中推送镜像到仓库的命令并执行，其中 [tag] 和步骤4相同。
   ```
   sudo docker push ccr.ccs.tencentyun.com/tsf_<账号ID>/<应用名>:[tag] 
   ```
   运行结果如下：
![](https://qcloudimg.tencent-cloud.cn/raw/b01b6df9550819ffd2f19c48bddb98b7.png)
6. 推送镜像成功后，在控制台刷新镜像列表页面，可以看到上传镜像仓库中的镜像。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a636cdb35ca67866e2c23c8c472af44c.png)

### 步骤3：部署应用

1. 在应用列表中，单击在 [步骤1. 新建应用](#step1) 中创建的应用的 “ID”。
2. 在部署组页面，单击**新建部署组**，设置部署组相关信息。
   - **组名**：填写 **user**。
   - **集群**：选择提前创建好的集群。
   - **命名空间**：选择集群关联的默认命名空间。
   - **日志配置项**：用于采集应用的业务日志数据，此处可选择**无**。关于日志配置项的使用说明可参见 [日志配置项](https://cloud.tencent.com/document/product/649/13697)。
   - **日志投递**：用于日志转储，此处可选择**无**。关于日志投递的详情说明可参见 [日志投递](https://cloud.tencent.com/document/product/649/43510)。
   - **标签**：用于分类管理资源，可不选。详情参见 [标签](https://cloud.tencent.com/document/product/649/53869)。
   - **备注**：选填，可留空。
3. 单击**保存&下一步**，进入部署应用页面。
4. 设置部署相关信息。
![](https://qcloudimg.tencent-cloud.cn/raw/b016247838c8b956b2fc6d5e5bb07457.png)
   ![](https://qcloudimg.tencent-cloud.cn/raw/963d9d8478d55def1f45fd7734c7d44f.png)
   - **选择镜像**：选择 [步骤2：上传镜像](#step2) 中推送到镜像仓库的镜像版本。
   - **启动参数**（选填）：设置 Java 应用的启动参数。
   - 环境变量（选填）：此处可不填写。
   - **资源配置**：应用容器的 CPU 和内存限制使用默认值即可，实例数设置为1。
   - **访问配置**： 
     - 网络访问方式决定了部署组内应用的网络属性，不同访问方式的应用可以提供不同网络能力。此处设置为**主机端口访问**。
     - 端口映射中选择 TCP 协议，容器端口和服务端口设置为8089。
5. 单击**提交**，完成应用部署。应用部署成功后，部署组中**运行中/预期服务实例数**的数值发生变化。
![](https://qcloudimg.tencent-cloud.cn/raw/053bc414c5377dc57a49e65289c78408.png)
6. 在服务治理页面，选择地域和应用关联的命名空间后，可以看到服务实例显示在线状态，表示服务注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/87d60f78b7713b575199832468bea86c.png)
7. 在服务列表页单击服务的“ID”，进入服务详情页，单击**接口列表**标签页，可以查看上报的 API 定义。



### 步骤4：验证服务调用

使用同样的步骤部署应用 Demo 中的 shop 和 promotion 应用。user、shop、promotion 三个服务的接口间调用关系如下：
![](https://main.qcloudimg.com/raw/4b4cfb3f587dcca35f975db0c924542a.png)

对应的服务名和应用监听端口为：user （8089），shop （8090），promotion （8091）。

#### 1. 触发 user 服务调用 shop 和 promotion 服务 
1. 在 [部署组](https://console.cloud.tencent.com/tsf/group) 列表页面，单击 user 部署组的“ID”，进入服务实例列表页面。
2. 在页面上方选择“基本信息”页签，在**服务访问**模块获取**主机端口（NodePort）**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f676f66378ef9f888f23de6ebb9e6500.png)
3. 在集群 [云主机](https://console.cloud.tencent.com/tsf/cluster-detai) 列表页面，获取集群中任一云主机的 IP。
![](https://qcloudimg.tencent-cloud.cn/raw/81c3f5e7c1dd47596c6c168d4cea0cc7.png)
4. 单击云主机操作栏的**登录**按钮，输入登录密码，登录云服务器。
5. 执行 curl 命令调用 user 服务，其中`<云主机 IP> `和 `<NodePort> `为上述步骤获取的主机端口（NodePort）和云主机 IP。
   ```
   curl <云主机 IP>:<NodePort>/api/v6/user/account/query
   ```
   调用结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/9222eb6578d2cc6a262fe744d0507f28.png)

   

#### 2. 在 TSF 控制台查看服务依赖拓扑图

1. 在 [服务治理](https://console.cloud.tencent.com/tsf/service) 页面，选择创建集群和命名空间后，可以看到 user、shop 和 promotion 服务的运行状况。服务状态为**在线**或**单点在线**，表示服务被代理注册成功。如果服务提供者的请求量大于0，请求成功率为100%，表示服务提供者被服务消费者请求成功。
![](https://qcloudimg.tencent-cloud.cn/raw/ea108ded4d9249876374d817a99b2ad8.png)
2. 在服务治理页面，单击 shop 服务的“ID”，进入服务详情页面，可以看到三个服务的依赖关系。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d1c6821c4658746c527ea469d01f1c8a.png)

   
