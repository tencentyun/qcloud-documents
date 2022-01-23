## 容灾方案
![](https://qcloudimg.tencent-cloud.cn/raw/d1ed92e5968c7fb9f35a84ed3063a40e.png)
用户 IDC 仅需要与单个腾讯云 VPC 实现互通，在用户 IDC 侧，用户可以部署两台 IPsec VPN 设备，分别与腾讯云私有网络型 VPN 建立 IPSec VPN 通道，VPN 网关路由表配置两条目的端一致的路由，通过优先级控制，实现主备通道效果；在发生故障时，可以实现路由自动切换。

## 前提条件
已腾讯云侧已创建 VPC 网络。

## 配置流程
<dx-steps>
-创建 VPN 网关
-创建 VPB 对端网关
-创建 VPN 通道（主备）
-IDC 侧本地配置
-配置 VPN 网关路由
-配置 VPN 通道健康检查
-配置 VPC 路由策略
</dx-steps>


### [步骤一：创建 VPN 网关](https://cloud.tencent.com/document/product/554/52861) 
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 网关**，进入管理页。
3. 在 VPN 网关管理页面，单击**+新建**。
4. 在弹出的**新建 VPN 网关**对话框中，配置如下网关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/1dc440a01b581da4cc17810140e5cae8.png)
  - 网关名称：填写自定义网关名称。
  - 关联网络：选择创建好的 VPC 网络。
  - 带宽上限：依据实际需求选择带宽。
  - 计费方式：按需选择计费方式，本示例中以按量计费为例。
  其他可选不配置或者保持默认即可。
5. 完成网关参数设置后，单击**创建**启动 VPN 网关的创建。
 此时**状态**为**创建中**，等待约1～2分钟，创建成功的 VPN 网关状态为**运行中**，系统为 VPN 网关分配一个公网 IP。
 
### 步骤二：创建对端网关[](id:step02)

#### 1 在腾讯云侧创建对端网关 A。
1. 在左侧导航栏选择 **VPN 连接** > **对端网关**。
2. 在“对端网关”管理页面，选择地域，单击**+新建**。
3. 填写对端网关名称，公网 IP 填写对端 IDC 侧的 VPN 网关设备的静态公网 IP ，根据需要设置标签。
![](https://qcloudimg.tencent-cloud.cn/raw/f0f4656b85297341553f46baec05bf49.png)
 - 名称：填写对端网关名称。
 - 公网IP：填写 IDC 侧 VPN 网关所在的 公网 IP 地址。
4. 单击**创建**。

#### 2 在腾讯云侧创建对端网关 B。
重复对端网关 A 的创建步骤1～步骤4。

### 步骤三：创建 VPN 通道（主备）[](id:step3)
VPN 网关和对端网关创建完成后，需要创建两条 VPN 网关与 IDC 侧相连的 VPN 通道，一条作为主通道，一条作为备用通道。

#### 1 创建主用通道 A
1. 在左侧导航栏选择 **VPN 连接** > **VPN 通道**。
2. 在“VPN 通道”管理页面，选择地域，单击**+新建**。
3. 在弹出的页面中填写 VPN 通道信息，具体参数配置请参考[ 新建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。
![](https://qcloudimg.tencent-cloud.cn/raw/02b26432501c9760e3e5bd9e64db7eee.png)
SPD策略配置时，“对端网段”配置为对端网关 D 的公网网段。
4. 单击**创建**。

#### 2 创建备用通道 B
重复主用通道 A 的创建步骤1～步骤4，其中 SPD 策略配置时，“对端网段”，请配置为对端网关 E 的公网网段。

### 步骤四：IDC 侧配置[](id:step4)
完成前三步骤后，腾讯云上 VPN 网关和 VPN 通道的配置已经完成，需要继续在 IDC 侧的“本地网关”上配置另一侧的 VPN 通道信息，具体请参考 [本地网关配置](https://cloud.tencent.com/document/product/554/56361)。IDC 侧的“本地网关”即为 IDC 侧的 IPsec VPN 设备，该设备的公网 IP 记录在<a href="#step02"> 步骤二 </a>的“对端网关”中。
>!配置时，主备 VPN 通道对应的 IDC 侧 VPN 网关均需配置。
>

### 步骤五 配置 VPN 网关路由[](id:step5)
截止至步骤四，已经将主备 VPN 通道配置成功，需要在 VPN 控制台配置 VPN 网关至 VPN 通道的路由。
1. 在左侧导航栏选择 **VPN 连接** > **VPN 网关**，并在右侧 VPN 网关列表中找到步骤一创建的 VPN 网关 A，并单击其名称。 
2. 在 VPN 网关 A 详情页签，单击**路由表**页签，并单击**新增路由**。
![](https://qcloudimg.tencent-cloud.cn/raw/2e713ef2f839cdd6b7c5c1a9c36e6654.png)
3. 在**新建路由**页面配置 VPN 网关 A 至 VPN 通道 B 和 VPN 通道 C 的路由策略。
![](https://qcloudimg.tencent-cloud.cn/raw/81f5e710b5d4b7ced56bad36dadab647.png)
<table>
<tr>
<th>配置项</th>
<th>说明</th>
</tr>
<tr>
<td>目的端</td>
<td>填写待访问的对端网络的网段，即 IDC侧提供对外访问的网段。</td>
</tr>
<tr>
<td>下一跳类型</td>
<td>系统自动填充<b> VPN 通道</b>。</td>
</tr>
<tr>
<td>下一跳</td>
<td>选择创建好的 VPN 通道。</td>
</tr>
<tr>
<td>权重</td>
<td><ul><li>VPN 通道 B 填写 0。</li><li>VPN 通道 C  填写 100。</li></ul> <br>0 表示优先级高，100表示优先级低。</td>
</tr>
</table>
4. 单击**确定**。

### 步骤六：配置通道健康检查[](id:step6)
VPN 网关路由配置完成后，为 VPN 通道健康检查（主备通道均需配置）。

#### 主用通道 B 健康检查配置
1. 在左侧导航栏选择 **VPN 连接** > **VPN 通道**，并在右侧 VPN 通道列表中找到创建好的 VPN 通道，然后单击 VPN 通道名称。 
2. 在通道**基本信息**页签单击**编辑**。
![](https://qcloudimg.tencent-cloud.cn/raw/955d7b3013112ec130080f5b2ed90613.png)
3. 打开健康检查开关，输入**健康检查本端地址**和**健康检查对端地址**，并单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/29c8cc58e1fd547e2415b90c1950a721.png)
>?
>- 本端地址：填写腾讯云侧向 IDC 发起健康检查的访问请求 IP 地址。该 IP 地址不能为 VPC 内 IP 地址。
>- 对端地址：填写 IDC 侧用于响应腾讯云健康检查请求的 IP 地址。该 IP 地址请勿与腾讯云侧地址相同，以防 IP 冲突。
  当腾讯云侧发起健康检查请求，访问请求通过通道到达 IDC 后，发现有健康检查响应IP地址，表示通道健康正常；如果没有表示异常。

#### 备用通道 C 健康检查
重复主用通道健康检查配置步骤1～步骤3，其中健康检查连接不能与主用通道的健康检查连接相同。


### 步骤七：配置 VPC 路由策略[](id:step7)
截止至步骤 5，已经将主备 VPN 通道配置成功，需要配置 VPC 路由策略，将子网中的流量路由至 VPN 网关上，子网中的网段才能与 IDC 中的网段通信。
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击**子网**，选择对应的地域和私有网络，单击子网所关联的路由表 ID，进入详情页。
![](https://qcloudimg.tencent-cloud.cn/raw/99ea9fd4c6ec6c573211e2cd6e6560fa.png)
3. 单击**+新增路由策略**。
![](https://main.qcloudimg.com/raw/60984e42e4e2b0ae9b7c5d64c422fc54.png)
4. 在弹出框中，输入目的端网段，下一跳类型选择 **VPN 网关**，下一跳选择刚创建的 VPN 网关，单击**创建**即可。
![](https://main.qcloudimg.com/raw/9ace02a3b05f91279707615edb312ae2.png)


### 步骤八：激活 VPN 通道[](id:step8)
使用 VPC 内的云服务器 ping 对端网段中的 IP，以激活 VPN 隧道，可以 ping 通表示 VPC 和 IDC 可以正常通信。
当 VPN 路由表中探测 VPN 主用通道 B 路由不可达时，系统自动将流量切换至 VPN 通道 C，确保业务的高可用性。
