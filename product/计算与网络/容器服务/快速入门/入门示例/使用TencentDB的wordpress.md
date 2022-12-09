## 操作场景
[单实例版 WordPress](/doc/product/457/7205) 示例中展示了如何快速创建 WordPress 服务。通过此方式创建的 WordPress 服务特点如下：
- 数据是写到同一个容器运行的 MySQL 数据库中。
- 服务可快速启动。
- 容器因某种原因停止，数据库和存储类的文件将会丢失。

而使用 MySQL 数据库可实现数据永久存储，数据库会在实例/容器重新启动后继续存在。本文档旨在介绍如何通过 [云数据库 TencentDB](https://cloud.tencent.com/product/cdb-overview) 设置 MySQL 数据库，以及如何创建使用 TencentDB 的 WordPress 服务。

## 前提条件
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建集群。关于创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。
>?本文使用数据库为 [云数据库 MySQL](https://cloud.tencent.com/document/product/236/5147)。
>

## 操作步骤

### 创建 WordPress 服务
#### 创建云数据库 TencentDB
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，单击数据库实例列表上方的**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/19726071d60c533349252a5c46caca8b.png)
2. 选择购买配置，详情请见 [云数据库 MySQL](https://cloud.tencent.com/document/product/236/5147)。
>!云数据库所在地域与集群相同，否则无法连接该数据库。
>
3. 数据库创建成功后，可在 [MySQL-实例列表](https://console.cloud.tencent.com/cdb) 中查看。
4. 对数据库进行初始化操作，详情请参见 [初始化 MySQL 数据库](https://cloud.tencent.com/document/product/236/3128)。

#### 创建使用 TencentDB 的 WordPress 服务
1. 登录腾讯云容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，选择需创建服务的集群 ID，进入集群的工作负载 “Deployment” 页面并单击**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/19997a6644943a2c6ec1587404eb8ca0.png)
3. 在“新建Workload” 页面，根据以下信息，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/0cfabf9ae002a49ce1b5e78ef4919fcf.png)
 - **工作负载名**：要创建的工作负载的名称，本文中以 wordpress 为例。
 - **描述**：填写工作负载的相关信息。
 -  **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **wordpress**。
 -  **命名空间**：根据实际需求进行选择。
 -  **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。
4. 参考以下信息设置“实例内容器”。如下图所示：
![](https://main.qcloudimg.com/raw/0b8fe37f0ab6432dabc090d12ed9c5e5.png)
主要参数信息如下，其余选项保持默认设置：
  - **名称**：输入自定义容器名称，本文以 test 为例。
  - **镜像**：输入 `wordpress`。
  - **镜像版本（Tag）**：输入 latest。
  - **镜像拉取策略**：提供以下3种策略，请按需选择，本文以不进行设置使用默认策略为例。
若不设置镜像拉取策略，当镜像版本为空或 latest 时，使用 Always 策略，否则使用 IfNotPresent 策略。
      - **Always**：总是从远程拉取该镜像。
      - **IfNotPresent**：默认使用本地镜像，若本地无该镜像则远程拉取该镜像。
      - **Never**：只使用本地镜像，若本地没有该镜像将报异常。
 - **环境变量**：依次输入以下配置信息：
WORDPRESS_DB_HOST = 云数据库 MySQL 的内网 IP
WORDPRESS_DB_PASSWORD = 初始化时填写的密码
5. 根据以下提示，设置服务的实例数量。如下图所示：
![](https://main.qcloudimg.com/raw/08f24d05d98670d6c2566d688388941f.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容](https://cloud.tencent.com/document/product/457/14209)。
6. 根据以下提示，进行工作负载的访问设置。如下图所示：
![](https://main.qcloudimg.com/raw/865b5b9de1f922ac2fc46cd3f7d8e334.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“提供公网访问”。
 - **负载均衡器**：根据实际需求进行选择。
  - **端口映射**：选择 TCP 协议，将容器端口和服务端口都设置为80。
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题。详情参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
>
7. 单击**创建Workload**，完成 WordPress 服务的创建。


### 访问 WordPress 服务
可通过以下两种方式访问 WordPress 服务。

#### 通过负载均衡 IP 访问 WordPress 服务
1. 单击左侧导航栏中 **[集群](https://console.cloud.tencent.com/tke2/cluster)**，进入“集群管理”页面。
2. 单击 WordPress 服务所在的集群 ID，选择**服务** > **Service**。
3. 进入服务管理页面，复制 WordPress 服务的负载均衡 IP，如下图所示：
![](https://main.qcloudimg.com/raw/e832352b82c6aa9ed7c030ae30fc0c28.png)
4. 在浏览器地址栏输入负载均衡 IP，按 **Enter** 即可访问服务。

#### 通过服务名称访问服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 WordPress 服务
服务创建成功，访问服务时直接进入 WordPress 服务器的配置页。如下图所示：
![](https://main.qcloudimg.com/raw/903f45d57c58541433b555d487bd2980.png)

### 更多 WordPress 设置
若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。
