
## 操作场景

当前集群开启内网访问后，容器服务 TKE 默认通过域名访问集群，您需要在访问机上配置 Host 来进行内网域名解析。如未配置对应的域名解析规则（Host），在访问机上访问对应集群（运行 kubectl get nodes）时将会报错 “no such host”，如下图所示：
![](https://main.qcloudimg.com/raw/2d03150adb99805447c57896cf5866d1.png)

在实际过程中，配置 Host 行为会增加管理访问机上 Host 的人力成本。因此，我们建议您使用腾讯云全新上线的 [私有域解析 Private DNS](https://cloud.tencent.com/document/product/1338) 服务，使用该服务简单便捷，只需要完成以下三步操作即可。




#### 收费说明

Private DNS 采用按量付费的计费方式。收费项为：私有域名数量 + 解析请求量，以自然日为单位进行结算。了解更多请参见 Private DNS [购买指南](https://cloud.tencent.com/document/product/1338/50523)。

#### 支持地域

Private DNS 目前支持的地域未完全覆盖 TKE 支持地域，具体支持地域列表请参见“私有域解析 Private DNS 限制”  [开放地域](https://cloud.tencent.com/document/product/1338/50529#.E7.A7.81.E6.9C.89.E5.9F.9F.E8.A7.A3.E6.9E.90-private-dns-.E9.99.90.E5.88.B6)。

在 Private DNS 不支持的地域使用内网访问集群功能，您仍需手动配置 Host。如需在未支持地域上使用 Private DNS 服务，请 [联系我们](https://cloud.tencent.com/act/event/connect-service)。


## 前提条件

已创建容器集群，并已开启内网访问。详情可参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。


## 操作步骤

### 开通 Private DNS

请参见官方文档开通 [Privae DNS](https://cloud.tencent.com/document/product/1338/50533)。 

### 创建私有域

1. 登录 [Private DNS](https://console.cloud.tencent.com/privatedns/domains) 控制台。
2. 单击**新建私有域**，配置以下选项（其他参数使用默认值即可），了解更多请参见 [创建私有域文档](https://cloud.tencent.com/document/product/1338/50532)。
![](https://main.qcloudimg.com/raw/2082da7f7d68f496906625372a53edd5.jpg)
 - **域名**：输入“tencent-cloud.com”（TKE 为集群访问分配的域名）。
 - **关联 VPC**：选择需要访问集群的节点网络 VPC。
3. 单击**确定**即可创建私有域。



### 配置解析记录

1. 单击上述创建的私有域名称，进入“解析记录”页面。
2. 单击**添加记录**，配置以下选项：
![](https://main.qcloudimg.com/raw/9f1c8acae204be7b08d55c7ad1ae3bc5.jpg)
   - **主机记录**：输入 TKE 集群访问的次级域名，例如 “cls-{{clsid}}.css”。
   - **记录类型**：输入 A。
   - **记录值**：输入 TKE 集群内网访问 IP。
>?**主机记录**和**记录值**可前往 **[集群管理](https://console.cloud.tencent.com/tke2/cluster?rid=1)** >**集群** > **基本信息**获取。其中**主机记录**对应**访问地址**中的域名，**记录值**对应**内网访问**中的 IP 地址，如下图所示：
![](https://main.qcloudimg.com/raw/c68ecc7c886fec6e9386e8f9d728157e.jpg)
3. 单击右侧操作栏下的**保存**以保存配置。



### 验证效果

1. 执行以下命令再次访问集群。
```sh
kubectl get nodes
```
2. 当命令执行结果显示如下图时，说明已成功访问集群并拉取 Node 列表。
![](https://main.qcloudimg.com/raw/95130bf7fa52376c21c11464b25a2741.png)
