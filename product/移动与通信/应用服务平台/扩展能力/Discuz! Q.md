云开发支持一键部署 [Discuz!Q](https://discuz.com/) 应用。通过云托管结合静态网站托管、共享文件存储 CFS、云数据库 CynosDB for MySQL 等各项云计算资源能力，为您提供高性能、高可靠性、可弹性扩缩容的的应用体验。

| 方案特性 | 介绍                                                                                         |
| -------- | -------------------------------------------------------------------------------------------- |
| 省钱     | 云托管没有流量可缩容到 0；存储按实际存储容量计费。无需为闲时资源买单。按量付费，无需预先支出 |
| 省心     | Serverless 无服务器化，架构弹性可自动扩缩容，无需担心网站崩溃                                |
| 更快     | 用户发帖上传的图片与附件，享受 CDN 节点就近加速分发                                          |
| 更便捷   | 自带三级域名可以快速访问，无需通过 IP 访问                                                   |


## 适用场景

- 不具备专业的运维开发人员的个人站长，无需预估业务规模，可自动扩缩容。
- 访问流量不稳定，无流量时，云托管将自动缩容到 0，减少成本。
- 对数据安全要求敏感的行业，数据独立存储在专业的云数据库 CynosDB for MySQL 中。

## 部署架构配置

| 资源                                                                                      | 架构                                                                                                                       |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [云托管](https://cloud.tencent.com/document/product/1243)                                 | 默认配置 0.25 核 0.5G 内存的容器，伸缩范围 0 - 4 个实例，遇到 CPU 负载大于 60 将会进行扩容。无流量则会缩容到 0，不产生费用 |
| [静态网站托管](https://cloud.tencent.com/document/product/1210)                           | 按照实际容量与流量付费                                                                                                     |
| [共享文件存储（Cloud File Storage，CFS）](https://cloud.tencent.com/document/product/582) | 按照实际容量付费，DAU 1000 的站点预估消耗量在 5GB 以下                                                                     |
| [云数据库 CynosDB for MySQL](https://cloud.tencent.com/document/product/1003)             | 数据库 1C1G，存储按照容量计费                                                                                              |

安装 Discuz! Q 资源配置架构图如下：
![架构图](https://main.qcloudimg.com/raw/441da6affa73b708ebafa0b7eb26efdd.png)

## 安装流程

1. 登录 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)。
2. 单击**新建环境**，新建一个**按量计费**环境，详情可参见 [开通环境](https://cloud.tencent.com/document/product/876/41391) 文档。
3. 环境创建完后，单击**环境卡片**，进入环境管理页面。
4. 单击左侧导航栏底部的 **[扩展应用](https://console.cloud.tencent.com/tcb/extensions/index)**，在更多扩展能力中，可以看到 Discuz!Q 应用。
   ![disucz入口](https://main.qcloudimg.com/raw/69482ddda7cc18bf2fbc15d559417578.png)
5. 在 Discuz!Q 应用中，单击**安装**，进入扩展安装流程。
   - 确认应用相关资源
   - 授予云开发相关资源的操作权限
   - 扩展云资源准备，声明会依赖的 2 个资源(文件存储、云数据库)
   - 扩展程序配置，请勿长期使用默认的密码，注意**修改密码**，避免管理后台被他人登录
     ![disucz安装](https://main.qcloudimg.com/raw/81bb3905d3972d4f298b9c1fbc551944.png)
6. 已安装列表里显示 Discuz!Q 应用正在安装中，安装完成后单击可进入详情页。
7. 详情页内，可以查看 Discuz!Q 的访问地址。
   ![discuz详情页](https://main.qcloudimg.com/raw/009a5504f4f2f439f53ee5ae2478be1c.png)

## 部署异常

安装过程中可能遇到一些异常，请根据异常提示查看以下解决方案进行解决。如果遇到无法解决的问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们，我们将协助您解决。
![安装异常](https://main.qcloudimg.com/raw/1e8022496f7c221a6f84fa02ddd5859e.png)

### 账户余额不足

Discuz!Q 应用创建时，会一同创建云数据库 CynosDB for MySQL。创建数据库资源会预先扣 1 个小时的费用，为了保证服务的可用，推荐先 [充值腾讯云账户](https://console.cloud.tencent.com/expense/recharge) 5 元钱。

### HTTP 访问服务 “/” 路径已经被占用

Discuz!Q 将会占用 “/” 路径，如果当前环境的 “/” 已经被占用，推荐再创建一个按量计费环境进行安装。

### CynosDB 被隔离

错误信息 `queryClusterDetail failed, err=DescribeClusters invalid response.detail.status[isolated]`，代表 CynosDB 集群被隔离，请前往[回收站](https://console.cloud.tencent.com/cynosdb/recycle)将该集群恢复或者直接删除。

### 共享文件存储 CFS 资源售罄

错误信息：”参数值错误：该地域无法提供服务“，代表 共享文件存储 CFS 该地域可用区售罄。我们将及时补货，请耐心等待。

### 部署异常后，但是资源已经创建

Discuz!Q 涉及资源较多，过程中可能产生异常。顺序为先创建 CFS、CynosDB for MySQL 资源，再开通云托管。
CFS 是按照存储量计费，没有存储数据则不产生费用。
CynosDB for MySQL 与服务器类似，是按照使用时间计费，即使没有调用也会计费。请开发者注意该项资源的计费方式。

## 常见问题

### 小程序部署

小程序的部署需要单独提审，安装完本扩展应用后，需要参考 [构建/发布 Discuz! Q 小程序与 H5 前端](https://discuz.com/docs/uniapp_hbuilderx.html#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95) 进行构建发布小程序端的代码。

### 公众号校验文件的配置

公众号等场景下需要添加业务域名时，需要将校验文件放到添加的域名根目录下。

1. 把公众号校验文件，上传到云开发的静态托管内，并且复制链接
2. [webshell](https://docs.cloudbase.net/run/webshell.html#cao-zuo-bei-jing) 登录后，将文件存放到静态资源目录 `cd /var/www/discuz/public`，既可以通过根目录访问 。
3. 从静态托管下载校验文件 `curl https://discuz-6gfk3xfudf9f84d4-1252395194.tcloudbaseapp.com/sdsk2sskd2e.txt`。

微信支付证书文件存储在 `/var/www/discuz/storage/cert/` 目录下。

### 公众号白名单 IP 配置

公众号登录开通时，需要将服务的 IP 添加到公众号的 IP 白名单中，详情请参见 [第三方登录设置](https://discuz.com/manual-admin/2.html#_2-3-%E7%AC%AC%E4%B8%89%E6%96%B9%E7%99%BB%E5%BD%95%E8%AE%BE%E7%BD%AE) 文档。

1. 在扩展应用详情页 API 和资源模块中，单击云托管的服务详情。
   ![查看云托管服务](https://main.qcloudimg.com/raw/e210b5f23304867805926e3c3a4bb07e.png)
2. 单击服务配置，查看服务的出口 NAT IP。
   ![NAT IP](https://main.qcloudimg.com/raw/e9b4724b662b52230b7ce5ca5ff270db.png)

### 如何升级到 Discuz! Q 的最新版本？

前往云托管菜单，单击 discuzq 服务，进入到版本列表页，单击流量 100% 对应的版本进行编辑并重新部署。
每次 [部署更新](https://docs.cloudbase.net/run/update-service.html#fang-shi-er-yuan-ban-ben-bian-ji-pei-zhi-bing-chong-xin-bu-shu) 都会拉取最新的 Discuz! Q 版本镜像进行安装。



### 复用已有的 CynosDB 集群

本应用会选取当前环境所处地域，并且在同一个 vpc 下，集群名为 DiscuzCynosDB 的数据库实例。如果不存在，则会创建新的集群。

如果希望复用已有 CynosDB 集群，可参考如下步骤。[CynosDB 新用户 10 元可购 1C1G 半年使用时长](https://cloud.tencent.com/act/pro/cynos-DB)

1. 查看 CynosDB 所在的私有网络，并且将集群名更改为 DiscuzCynosDB。
   ![](https://main.qcloudimg.com/raw/3549cec77f92046bada85b9ab79f05e7.png)
2. 创建一个新的按量计费环境，并且开通云托管，选择自定义配置，勾选 CynosDB 所在的私有网络，默认请勾选所有子网
   ![](https://main.qcloudimg.com/raw/eada2b2dac2ee060380da78055da1b5b.png)
3. 回到扩展应用页面安装 Discuz!Q

### 配置到其他已有 MySQL 数据库

>!该操作会发起重新安装，数据库里 dabatase 为 discuzq 的库将会**删除重建**，请安装后，再将之前的数据导入。

1. 安装 Discuz!Q 后，跳到[云托管的 webshell](https://docs.cloudbase.net/run/webshell.html#cao-zuo-bei-jing)
2. 删除 lock 锁定文件 `rm /var/lib/discuz/.clusterlock /var/lib/discuz/storage/install.lock`,以发起重装。
3. 单击[编辑配置并重新部署](https://docs.cloudbase.net/run/update-service.html#fang-shi-er-yuan-ban-ben-bian-ji-pei-zhi-bing-chong-xin-bu-shu)，更改对应的环境变量。注意需要在同一个 vpc 下，否则需要提供外网的 IP。
   ![更新环境变量](https://main.qcloudimg.com/raw/b5f9eeeee8cf2488781b4e6bc1e5abb2.png)
4. 如果需要导入原先的数据，请将 `/var/lib/discuz/config/config.php` 中的密钥字段。`'key' => 'base64:q94WREK6/c8WTTb+DeOQjmzyzQgOA5CmVpNfLQWK8kU='`，该密钥用于注册账号的密码数据加密。可使用 [nano 编辑器](https://cloud.tencent.com/developer/article/1187038)进行编辑。



## 迁移已有的 Discuz! Q 服务

>!原先如果是连接本地的 MySQL，建议将数据导出，再登录 [CynosDB for MySQL 的数据管理后台](https://dms.cloud.tencent.com/#/login?dbType=cynosdbmysql&region=ap-shanghai) 进行数据导入。在原先服务器内，更新 `config/config.php` 配置文件中的数据库连接信息，确认迁移无误后，再进行以下操作。

1. 登录到已有的服务器后，进入 Discuz! Q 应用部署的根目录，例如 `cd /www/wwwroot/discuz`
2. 打包 Discuz! Q 持久化的目录， `tar -cf public/discuz.tar.gz config storage`。如果提示没有权限，请切换为 root 角色。输入 `su` 后，填写密码后，便切换到 root 角色，再执行该命令
3. 登录云托管容器的 webshell，进入到 CFS 挂载的持久化目录 `cd /var/lib/discuz`
4. 将压缩包下载到容器内`curl http://119.29.146.208/discuz.tar.gz`（需要将 IP 替换为实际的服务器 IP 地址）
5. 解压 `tar -xvf discuz.tar.gz`，完成持久化数据的迁移。请确定数据库配置是可以连接的。

## 二开支持

云开发支持二开，[Discuz! Q](https://github.com/TencentCloudBase-Marketplace/Discuz-Q)。可通过该仓库的一键部署链接进行部署。




## 迁移到 Serverless MySQL 指引[](id:serverlessmysql)

### Serverless 形态的优点

CynosDB for MySQL 推出新的 Serverless MySQL 形态，有以下特性

1. 弹性伸缩：可配置规格范围，根据负载自动扩容，集群内可添加多个实例
2. 自动暂停：没有流量请求，最小 10 分钟自动暂停，暂停后停止计费(以往数据库按量付费是每个小时都收费)，存储仍然按实际使用量计费
3. 规格更小：最小 0.25 核，过往最低 1 核
4. 秒级计费：按秒计量，按小时结算

介绍页 https://cloud.tencent.com/document/product/1003/50853
控制台 http://console.cloud.tencent.com/cynosdb/

MySQL 数据迁移指南

1. 通过 DTS 迁移数据 https://cloud.tencent.com/document/product/571/45488
2. 原生 MySQL 导出数据文件, https://cloud.tencent.com/document/product/571/13729

### 迁移指南

Discuz! Q 当前部署采用的是按量付费的 CynosDB for MySQL 实例。是按小时收费，即使没有流量也不会自动缩容到 0，会持续收费。
当前推出新的 Serverless 形态，没有连接自动会暂停，不再计费。因此，推荐迁移到该方案。


#### 步骤1：迁移数据到 Serverless 类型的 CynosDB

1、前往 [CynosDB](https://console.cloud.tencent.com/cynosdb) 控制台，单击 Discuz! Q 创建的 DB 实例管理操作，即集群名为 DiscuzCynosDB 的实例。
![管理](https://main.qcloudimg.com/raw/7468b97f3a16294c90feaf9e9f66e456.jpg)
2、单击备份管理，进行回档操作
![管理](https://main.qcloudimg.com/raw/f6b8c62f0d97f36005b9bcd644514d66.jpg)
3、创建回档，确认创建回档，单击立即购买
![创建回档](https://main.qcloudimg.com/raw/b5d0c183a78f0f73e7197c1bbb8850b2.jpg)

- 计费模式选择 serverless
- 回档模式，选择按时间点，选择当前时间
- 私有网络选择当前实例所在的私有网络
- 算力配置可以选择从 0.25 核到 0.5 核
- 自动暂停可以设置为 10 分钟
  4、到列表页得到最新的内网地址
  ![新实例](https://main.qcloudimg.com/raw/0887318901e638a7c81cafd250e74e9c.jpg)

#### 步骤2：修改云托管的数据库配置，指向新的数据库

1. 单击云托管的菜单，单击 discuzq 服务
   ![discuzq](https://main.qcloudimg.com/raw/60ec5608e757a3436f529f028fa75b30.jpg)
2. 单击当前版本的 更多-调试 按钮
   ![调试](https://main.qcloudimg.com/raw/f705a7713733f9cba5d6beee22926d11.jpg)
3. 单击打开 webshell，进入到对应的文件夹并编辑配置文件 `cd /var/lib/discuz/config;nano config.php`,参考教程 [Nano 文本编辑器使用教程](https://cloud.tencent.com/developer/article/1187038)
   ![编辑配置文件](https://main.qcloudimg.com/raw/4dd8e89a17f853636dd05942adb3f18d.png)
4. 修改 `database` 的 `host` 配置，保存文件。
   ![修改host配置](https://main.qcloudimg.com/raw/9a8ce9974ea66aa745a6b3ca81a5579f.png)

#### 步骤3：校验是否迁移成功

1. 将 serverless 数据库设置为暂停
   ![数据库暂停](https://main.qcloudimg.com/raw/21422b519faa82a8d27ba119cc3efa0f.jpg)
2. 访问 Discuz! Q 站点，出现如下失败界面，即代表已经指向新的 DB。刷新后，访问成功。DQ 将会在下个版本适配数据库重连，不会再出现如下报错。
   ![访问DQ站点失败](https://main.qcloudimg.com/raw/341e587ca76a51862869c13a3a275219.jpg)
3. 再检查数据库集群状态，应该变更为”运行中“
4. 可以将原先的数据库删除，并前往回收站删除。

### 缩容的逻辑

1. 如果站点一直没有流量访问，云托管将于半小时内缩容到 0。
2. DQ 的应用程序会有天级、分钟级的定时任务脚本，脚本里有请求数据库。因此，数据库会在云托管缩容到 0 后 10 分钟触发暂停。

## 其他

### 程序配置信息

您可以通过以下配置参数：

- 环境 ID：选择需要部署的环境，在哪个环境下使用。
- 管理员用户名：Discuz! Q 后台管理系统的管理员用户名，默认为 admin。
- 管理员密码：Discuz! Q 后台管理系统的管理员密码，第一次安装时，会设置并加密存储在数据库内，之后变更请前往管理系统的用户管理面板重置密码，详情请参见 [用户管理](https://discuz.com/manual-admin/3.html#_3-1-%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86)。
- 数据库用户名：默认为 root，当前不可修改。
- 数据库密码：root 账号的密码，初次安装时设置后将作为初始化的密码创建 CynosDB。后续修改密码请前往 CynosDB 控制台的账号管理页面，修改密码后，请同步修改此处的密码，以保证数据库的正常使用。

### 计费

此能力使用云开发与其他腾讯云服务，可能会产生相关费用。云开发与云上其他资源分开计费，您可以在 [费用中心](https://console.cloud.tencent.com/expense/overview) 查看具体信息。

#### 云托管

[产品定价](https://cloud.tencent.com/document/product/1003/30493) 及 [使用明细](https://console.cloud.tencent.com/tcb)。
   ![云托管与静态网站托管用量查询](https://main.qcloudimg.com/raw/3135c5ef7c19be7a86156f10dc0a8749.png)

#### 静态网站托管
[产品定价](https://cloud.tencent.com/document/product/876/39095) 及 [使用明细](https://console.cloud.tencent.com/tcb)。

#### 文件存储（Cloud File Storage，CFS）

[产品定价](https://cloud.tencent.com/document/product/582/47378) 及 [使用明细](https://console.cloud.tencent.com/cfs/overview)。

![CFS用量](https://main.qcloudimg.com/raw/4022e36a8b69a450e5c36c78353c1b82.png)
	 
#### 云数据库 CynosDB for MySQL
	 
	 
[产品定价](https://cloud.tencent.com/document/product/1003/30493) 及 [使用明细](https://console.cloud.tencent.com/cynosdb)。
![数据库存储用量](https://main.qcloudimg.com/raw/d486a7bb304ea1bff2738e213ce4c9e2.png)
