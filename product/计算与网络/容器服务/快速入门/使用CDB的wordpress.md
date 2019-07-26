## 操作场景
[单实例版 WordPress](/doc/product/457/7205) 示例中展示了如何快速创建 WordPress 服务。 通过此方式创建的 WordPress 服务，数据是写到同一个容器运行的 MySQL 数据库中。使用此配置，服务可以快速启动。但如果容器因某种原因停止，数据库和存储类的文件将会丢失。

本文档以 [原 TKE 控制台](https://console.cloud.tencent.com/tke) 为例，通过使用 [云数据库 TencentDB](https://cloud.tencent.com/product/cdb-overview)，数据将在实例/容器重新启动后继续存在，实现数据永久存储。

## 前提条件
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建集群。关于创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/9091#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4) 。
>?本文使用数据库为 [云数据库 MySQL](https://cloud.tencent.com/document/product/236/5147)。
>

## 操作步骤

### 创建 WordPress 服务
#### 创建云数据库 TencentDB
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，单击数据库实例列表上方的【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/19726071d60c533349252a5c46caca8b.png)
2. 选择购买配置，详情请见 [云数据库 MySQL](https://cloud.tencent.com/document/product/236/5147)。
>!云数据库所在地域与集群相同，否则无法连接该数据库。

3. 数据库创建成功后，可在 [MySQL-实例列表](https://console.cloud.tencent.com/cdb) 中查看。
4. 对数据库进行初始化操作，详情请参见 [初始化 MySQL 数据库](https://cloud.tencent.com/document/product/236/3128)。

#### 创建使用 TencentDB 的 WordPress 服务
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke) 。
2. 单击左侧导航栏中的【服务】，选择服务列表上方的【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/1c30a9e677e2b8d19ebbe48ed80c695d.png)
3. 设置服务的基本信息。如下图所示：
   - **服务名称**：要创建的服务的名称。服务名称由小写字母、数字和 - 组成，且由小写字母开头，小写字母或数字结尾。本文以 wordpress 为例。
   - **所在地域**：选择运行该服务集群所在的地域。
   - **运行集群**：选择服务所要运行的集群，选择运行中和集群内有可用主机的集群。
   - **服务描述**：创建服务的相关信息。该信息将显示在 **服务信息** 页面。
     >!其他选项保持为默认设置。
     >
   ![](https://main.qcloudimg.com/raw/7a34cab51e9d9d04345fb018f62cc84f.png)
4. 根据以下参数信息进行镜像配置。如下图所示：
   - **名称**：输入运行容器的名称，以 wordpress 为例。
   - **镜像**：输入 `wordpress` 。
   - **版本（Tag）**：输入 latest。
   ![](https://main.qcloudimg.com/raw/d44f322d3e4459104046e79f6f0d873c.png)
5. 单击环境变量下的【新增变量】，依次输入以下配置信息。如下图所示：
 - WORDPRESS_DB_HOST = 云数据库 MySQL 的内网 IP
 - WORDPRESS_DB_PASSWORD = 初始化时填写的密码
  ![](https://mc.qcloudimg.com/static/img/6508b3858d0bba46510a81279aad2e15/image.png)
6. 设置端口映射，将容器端口和服务端口都设置为 80 。如下图所示：
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通 30000-32768 端口，否则可能会出现容器服务无法使用问题。详情参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
>
![](https://mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)
7. 单击**创建服务**，即可完成 WordPress 服务的创建。


### 访问 WordPress 服务
可通过以下三种方式访问 WordPress 服务。

#### 通过负载均衡 IP 访问 WordPress 服务
1. 进入集群 [服务列表](https://console.cloud.tencent.com/tke/service/detail/container) 页。
2. 单击【服务信息】查看负载均衡 IP。如下图所示： 
![](https://main.qcloudimg.com/raw/fd154cfe3fd5c12e9b49a00de337f4af.png)
3. 在浏览器地址栏输入负载均衡 IP，按 “**Enter**” 即可访问服务

#### 通过域名访问 WordPress 服务
1. 进入服务信息详情页，单击服务的负载均衡 ID。如下图所示：
![](https://main.qcloudimg.com/raw/0fd61801cb68f05e7e1ffa4da25154d2.png)
2. 进入负载均衡详情页，查看域名。如下图所示：
![](https://main.qcloudimg.com/raw/cc7bf45a6044534a89c8a6d61e3b98e0.png)
3. 在浏览器地址栏输入该域名，按 “**Esc**” 即可访问服务。

#### 通过服务名称访问服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 WordPress 服务
服务创建成功，访问服务时直接进入 WordPress 服务器的配置页。如下图所示：
![](https://main.qcloudimg.com/raw/903f45d57c58541433b555d487bd2980.png)

若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。
