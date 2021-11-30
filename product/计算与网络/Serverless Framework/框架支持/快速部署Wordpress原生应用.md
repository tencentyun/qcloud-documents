腾讯云 Serverless 提供了基于 Serverless 架构的 WordPress 全新部署方式，通过 [Serverless Framework WordPress 组件](https://github.com/serverless-components/tencent-wordpress)，仅需几步，就可以快速部署一个 WordPress 项目。

## 架构简介
该组件主要为您创建以下资源：

| 模块 | 说明 | 
|---------|---------|
| 云函数 SCF | 负责 Serverless WordPress 的接入层实现，从而运行 WordPress。 |
| API 网关| WordPress 的对外入口，实现了 RESTful API。 |
| 文件储存 CFS  | WordPress 的 Serverless 存储仓库。 |
| <nobr>云原生数据库 TDSQL-C</nobr> <br>（可选）| 通过创建 TDSQL-C（原 CynosDB）的 MySQL 类型数据库，实现数据库按量计费，自动扩缩容。<br>您可以选择不使用默认数据库，连接自建的 MySQL 类型数据库。|
| 私有网络 VPC <br>（默认 VPC）| 内网打通云函数 SCF、CFS、TDSQL-C Serverless 之间的网络，保障网络隔离。<br>您也可以选择不使用默认VPC，连接自己指定的VPC。|

## 功能优势
- **支持使用自建数据库**
  支持直接使用您自己的 MySQL 数据库，省去冷启动问题。
  
- **降低使用成本**
  计算层使用 Serverless 资源，真正做到按量计费，弹性伸缩，极大节省成本。
  
- **部署步骤简单**
  通过 Serverless 应用控制台， 仅需几步配置，即可快速完成 WordPress 应用部署，极大降低部署门槛。

## 部署步骤
您可以通过**控制台**快速完成 Serverless WordPress 部署，步骤如下：

### 前提条件
- 已开通 [云函数 SCF 服务](https://console.cloud.tencent.com/scf)。
- 已开通 [文件存储 CFS 服务](https://console.cloud.tencent.com/cfs)。
- （可选）准备好已备案的自定义域名，您也可以通过 Serverless 备案资源包完成备案（详情请参见 [ICP 备案](https://cloud.tencent.com/document/product/1154/50706)）。

### 控制台部署
>!目前只支持北京、上海、广州三个地域。其中广州四区为默认区域。

1. 登录[ Serverless 应用控制台](https://console.cloud.tencent.com/sls?from=wpdocs), 单击**新建应用**。
2. 选择**应用模版** > **快速部署一个WordPress框架**，单击**下一步**。
![](https://main.qcloudimg.com/raw/69c8613f66c793d53afb879e5e11e4ae.png)
3. 输入应用名。您可以选择使用默认的或连接自建数据库和指定私有网络。
<dx-tabs>
::: 选择使用默认的数据库和私有网络
如果您选择使用默认的数据库和私有网络，单击**完成**即可完成应用创建。
![](https://main.qcloudimg.com/raw/63417fa4e382410b2ff6f7f7d135fbce.png)
:::
::: 选择连接自建数据库和私有网络
如果您选择连接自建数据库和私有网络，可以在高级配置勾选对应的**启用**并进行配置。您可以连接有内网 IP 的数据库，也可以连接有公网 IP 的数据库。如果选择连接内网 IP 的数据库，您需要配置私有网络，请注意您的自建数据库所在地域与应用部署地域需要相同。如果选择连接公网 IP 的数据库，您也可以不启用指定的私有网络，继续使用默认的私有网络。单击**完成**完成应用。
![](https://main.qcloudimg.com/raw/50393d473720206a8a0e515a4f253696.png)
:::
</dx-tabs>
4. 在 Serverless 应用页，单击**访问应用**，即可访问您的 WordPress 项目。
![](https://main.qcloudimg.com/raw/90d900584c4a1da68d356c1fc5adb75a.png)
您也可以单击您的应用名称，查看资源列表和部署日志。在资源列表页，您可以单机**新增**配置您的自定义域名。
![](https://main.qcloudimg.com/raw/55218c4f1a6f83f3a1e1ff58a2f15006.png)

### 版本升级
   Serverless Wordpress 应用的旧版部署架构中，存在访问速度慢的问题。为此 Serverless 应用开发团队针对此问题进行了 Serverless Wordpress 应用的优化工作，改进了部署架构，大幅提升了站点的访问速度。本指引仅适用于 Serverless Wordpress 应用旧版本的部署升级。
>? 您可通过如下方法确认您的应用是否需要升级：如您的站点可正常访问并且 Wordpress 云函数代码中仅包含一个 'scf_bootstrap' 文件，则可进行升级。
>
![](https://qcloudimg.tencent-cloud.cn/raw/e8900e455a4b37af87e0d4762933a7f2.png)
   
   
#### 前期准备 
   您已经部署了 Serverless Wordpress 应用，站点所对应的云函数前缀为 wp-server-*。

#### 操作步骤 
>! 请严格按照如下步骤升级您的站点，并使用本指引中提供的 Wordpress 源码包进行代码更新。

1. 发布函数版本和流量切换
  为了确保升级操作期间您的站点的正常访问，请首先为 wp-server-* 发布一个版本。
  ![](https://qcloudimg.tencent-cloud.cn/raw/d6e6e9427c239136198148addbe98f0b.png)
  发布版本后，将函数的默认流量配置到新版本。
  ![](https://qcloudimg.tencent-cloud.cn/raw/6e9382de942e9f68849ad2e11b6fe9cb.png)

2. 更新 $LATEST 版本的函数代码
  下载 wordpress 源码包（[source.zip](https://docs.qq.com/scenario/link.html?url=https%3A%2F%2Fserverless-template-1300862921.cos.ap-guangzhou.myqcloud.com%2Fwp-deploy-update%2Fsource.zip&pid=300000000$cSeVtSLsJmVv&cid=159036837884)），并上传更新函数代码。
>! 切勿轻易修改代码中的 handler.php 和 wp-config.php 文件，否则将导致您的站点访问异常。

![](https://qcloudimg.tencent-cloud.cn/raw/f906cb0252baea977d6461fe4a69c88c.png)

3. 更新 Php 版本（可选）
    
   此步骤为可选，Serverless Wordpress 应用站点的 Php 依赖位于函数的挂载 Layer 中，您可以选择是否升级站点的 Php Runtime 环境，升级后的 Php Runtime 版本为 php 7.4.25。在此版本中，使用了 Php Opcache 功能，在函数实例预置场景下，可进一步提高您的站点访问速度。下载 Php Runtime 源码包（php74.zip），并上传更新函数的 Layer。更新完成后，直接解绑老版本的 Layer 即可。

![](https://qcloudimg.tencent-cloud.cn/raw/475cfd1618350d3f164b5d77bdc5473a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e5e1d9a200510be895849d804eadb603.png)


4. 流量切换
完成以上步骤后，参考步骤1中的函数流量配置操作，重新将您的 wp-server-* 函数的流量切换到 $LATEST，即可完成升级。

#### 功能限制

  无论是经过升级的存量 Serverless Wrodpress 站点，还是增量站点，都**不支持原生的 Wordpress 版本升级功能。**



## 常见问题

#### 权限问题导致部署失败该如何处理？
- 主账号/子账号需确认是否有以下权限：
  - 确认角色：**SCF_QcsRole、SLS_QcsRole、CODING_QcsRole**
  - 确认权限：
    - SCF_QcsRole 须拥有 **CFSFullAccess** 权限
    - CODING_QCSRole 须拥有 **QcloudSLSFullAccess、QcloudSSLFullAccess、QcloudAccessForCODINGRole** 权限
- 子账号还需确认以下权限：
账号本身有 **SLS、SCF、CFS、CynosDB、CODING** 使用权限。

#### 绑定自定义域名后，显示报错 {"message":"There is no api match env_mapping '\/'"}？
在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service?rid=1) 修改自定义映射，如下图所示：
![](https://main.qcloudimg.com/raw/b6bbb75df052e307e8abb4e82e500c3b.png)

#### 如何通过修改 php.ini 修改上传文件大小限制？
1. 修改 layer 代码。将 etc 文件夹中的 php.ini 文件移到 etc/php.d 文件夹下，您也可以直接使用我们提供的 [压缩包](https://github.com/serverless-components/tencent-wordpress/blob/master/src/fixtures/layer/wp-layer.zip)。
重新打包上传 layer 时，注意打包层级结构，只打包父文件夹下的文件，否则会出现函数初始化失败：
![](https://main.qcloudimg.com/raw/46fcf29a9f846b84db0c0a19fe65ce35.png)
2. 按照如下修改 wp-server-xxx 函数的 bootstrap 代码：
```
#!/bin/bash
export PATH="/opt/bin:$PATH"
export LD_LIBRARY_PATH=/opt/lib/:$LD_LIBRARY_PATH
export PHP_INI_SCAN_DIR=/opt/etc/php.d
php -d extension_dir=/opt/lib/php/modules/ sl_handler.php 1>&2
```

#### 如何处理报错 "event too large"？
函数目前只支持最大**6MB**的事件上传，超过该大小文件不支持上传。
目前 API 网关 base 64转码会将用户本身代码大小扩大1.5倍左右，因此上传文件时，建议文件大小控制在**3.5MB**以内。<br/>

#### 如何修改 WordPress 根目录文件？
目前文件挂载在文件存储 CFS 上，无法直接修改，建议通过安装 File Manager 插件管理根目录文件。

