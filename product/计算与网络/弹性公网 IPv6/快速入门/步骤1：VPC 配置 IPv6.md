本教程将帮助您搭建一个具有 IPv6 CIDR 的私有网络（VPC）。
## 操作须知
1. 在开始使用腾讯云产品前，您需要先 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。
2. 目前弹性公网 IPv6 处于内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/c28sebss8v)。
3. 目前支持 IPv6 的地域为北京、上海、广州、上海金融云、深圳金融云，请在这些地域部署 IPv6 服务。
4. IPv6 地址为 GUA 地址，每个 VPC 分配1个`/56`的 IPv6 CIDR，每个子网分配1个`/64`的 IPv6 CIDR，每个弹性网卡分配1个 IPv6 地址。
5. 主网卡、辅助网卡均支持申请 IPv6 地址。想要了解更多云服务器和弹性网卡的关系，请参见 [弹性网卡](https://cloud.tencent.com/document/product/576) 产品文档。

## 操作步骤
>?如下步骤1 - 步骤5中的目标云服务器均指需配置 IPv6 的云服务器。
>
### 步骤1：VPC 分配 IPv6 CIDR
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在目标云服务器所属 VPC 所在行的操作栏下，单击【编辑 CIDR】。
3. 在弹框中的 IPv6 CIDR 单击【获取】并确认操作，系统将为 VPC 分配一个`/56`的 IPv6 地址段，您可以在列表里看到 IPv6 地址段的详细信息。
![](https://main.qcloudimg.com/raw/06cc0c14dc28e511492d5f1b5cb01f32.png)

### 步骤2：为子网分配 IPv6 CIDR
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【子网】，进入管理页面。
3. 在目标云服务器所属子网所在行的操作栏下，单击【获取 IPv6 CIDR】并确认操作，系统将从 VPC 的`/56` IPv6 CIDR 分配一个`/64`的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/d3d8fcaa9c336dac11485d5f7ed95a92.png)

### 步骤3：弹性网卡获取 IPv6 地址
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性网卡】，在列表页中单击目标云服务器所绑定的弹性网卡 ID，进入详情页。
3. 选择【IPv6 地址管理】标签页，单击【分配 IP】。
![](https://main.qcloudimg.com/raw/3988ff4d36229c8ce99a9276875204a9.png)
4. 在弹窗中单击【确定】即可。
![](https://main.qcloudimg.com/raw/737f2b30db0766ebf09ce99f2bdc4e01.png)
5. 系统将会为弹性网卡分配一个 IPv6 地址，如下图所示。
![](https://main.qcloudimg.com/raw/309e8e9d70b69ddb4c70a0ead71f7862.png)

### 步骤4：为弹性网卡的 IPv6 地址开通公网（可选）
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性公网 IPv6】。
3. 选择需要开通 IPv6 公网的地域，如“华南地区（广州）”，单击【申请】，进入管理页面。
4. 勾选已绑定目标云服务器的 IPv6 地址、设置目标带宽上限	，单击【提交】即可。
>?
>- 弹性网卡申请了 IPv6 地址后，默认关闭了公网访问能力，可通过弹性公网 IPv6 [管理 IPv6 公网](https://cloud.tencent.com/document/product/1142/38141) 能力。
>- 当运营商类型为 BGP 时，弹性公网 IPv6 地址即为弹性网卡获取到的 IPv6 地址，所以请确保弹性网卡已经获取到 IPv6 地址。
>- 单次操作可支持最多100个 IPv6 地址同时开通公网，如果超过100个 IPv6 地址需要开通公网，请分多次操作。
>
![](https://main.qcloudimg.com/raw/f66f01c4b1a0791f956663188e2b702b.png)

### 步骤5：配置 IPv6 的安全组规则
>?出入方向的安全组规则支持配置来源为单个 IPv6 地址或者 IPv6 CIDR，其中`::/0`代表所有的 IPv6 源地址。
>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【安全】>【安全组】，在列表页中单击目标云服务器绑定的安全组 ID，进入详情页。
3. 选择【入站规则】并单击【添加规则】，添加 IPv6 的入方向安全组规则，单击【完成】即可。
![](https://main.qcloudimg.com/raw/73ff04af93a1f13eef92d4f74ac30fc2.png)
4. 选择【出站规则】并单击【添加规则】，添加 IPv6 的出方向安全组规则，单击【完成】即可。
![](https://main.qcloudimg.com/raw/c0d255728fa6b48292f425c5ffb6559f.png)
