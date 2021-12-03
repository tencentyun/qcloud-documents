腾讯云 VPN 连接具备高可用性，当用户 IDC 通过主备 VPN 通道上云，且主通道发生故障时，业务将自动切换到备用通道上，保证了业务的持续性、从而提高业务可靠性。本文以 IDC 与单个腾讯云 VPC 实现主备容灾为例。


## 容灾方案
![](https://main.qcloudimg.com/raw/6af07bbb57e1eaa9d59a703869796dd2.png)
用户 IDC 仅需要与单个腾讯云 VPC 实现互通，在用户 IDC 侧，用户可以部署两台 IPsec VPN 设备，分别与腾讯云私有网络型 VPN 建立 IPSec VPN 通道。VPN 网关路由表配置两条目的端一致的路由，通过优先级控制，实现主备通道效果，在发生故障时，可以实现路由自动切换。

## 前提条件
已在腾讯云侧 [创建 VPC 网络](https://console.cloud.tencent.com/vpc/vpc?rid=1)。

## 配置流程
<dx-steps>
-创建 VPN 网关
-创建对端网关
-创建 VPN 通道（主备）
-IDC 侧配置
-配置 VPN 网关路由
-配置通道健康检查
-配置 VPC 路由策略
-激活 VPN 通道
</dx-steps>

## 操作步骤

### 步骤一：[创建 VPN 网关](https://cloud.tencent.com/document/product/554/52861) 
>?本文以3.0版本的 VPN 网关为例。
>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中选择**VPN 连接** > **VPN 网关**，进入管理页。
3. 在 VPN 网关管理页面，单击**+新建**。
4. 在弹出的**新建 VPN 网关**对话框中，配置如下网关参数。
<img src="https://main.qcloudimg.com/raw/6b4bd438cf832055bcfc355896ec5382.png" width="70%"></br>
  - 网关名称：填写自定义网关名称。
  - 关联网络：选择创建好的 VPC 网络。
  - 带宽上限：依据实际需求选择带宽。
  - 计费方式：按需选择计费方式，本示例中以按量计费为例。
  其他可选不配置或者保持默认即可。
5. 完成网关参数设置后，单击**创建**启动 VPN 网关的创建。
 此时**状态**为**创建中**，等待约1～2分钟，创建成功的 VPN 网关状态为**运行中**，系统为 VPN 网关分配一个公网 IP。

### 步骤二：[创建对端网关](id:step02)

#### 在腾讯云侧创建对端网关 D。
1. 在左侧导航栏选择**VPN 连接** > **对端网关**。
2. 在**对端网关**管理页面，选择地域，单击**+新建**。
3. 填写对端网关名称，公网 IP 填写对端 IDC 侧的 VPN 网关设备的静态公网 IP ，根据需要设置标签。
<img src="https://main.qcloudimg.com/raw/6fe5acff79be8f8cf10ec79187f9f409.png" width="70%"></br>
 - 名称：填写对端网关名称。
 - 公网IP：填写 IDC 侧 VPN 网关所在的 公网 IP 地址。
4. 单击**创建**。

#### 在腾讯云侧创建对端网关 E。
重复对端网关 A 的创建步骤1 ～ 步骤4。


### 步骤三：创建 VPN 通道（主备）
VPN 网关和对端网关创建完成后，需要创建两条 VPN 网关与 IDC 侧相连的 VPN 通道，一条作为主通道，一条作为备用通道。

#### 创建主用通道 B
1. 在左侧导航栏选择**VPN 连接** > **VPN 通道**。
2. 在**VPN 通道**管理页面，选择地域，单击**+新建**。
3. 在弹出的页面中填写 VPN 通道信息，具体参数配置请参考[ 新建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。SPD 策略配置时，“对端网段”配置为`0.0.0.0/0`。
 ![](https://main.qcloudimg.com/raw/19853156932e77dc4c28fc5b4b2fad9e.png)
4. 单击**创建**。


#### 创建备用通道 C
重复主用通道 A 的创建步骤1 ～ 步骤4，其中 SPD 策略配置时，“对端网段”配置为`0.0.0.0/0`。 

### 步骤四：IDC 侧配置
完成前三步骤后，腾讯云上 VPN 网关和 VPN 通道的配置已经完成，需要继续在 IDC 侧的**本地网关**上配置另一侧的 VPN 通道信息，具体请参考 [本地网关配置](https://cloud.tencent.com/document/product/554/56361)。IDC 侧的“本地网关”即为 IDC 侧的 IPsec VPN 设备，该设备的公网 IP 记录在<a href="#step02"> 步骤二 </a>的“对端网关”中。
>!配置时，主备 VPN 通道对应的 IDC 侧 VPN 网关均需配置。
>

### 步骤五：配置 VPN 网关路由
截止至步骤四，已经将主备 VPN 通道配置成功，需要在 VPN 控制台配置 VPN 网关至 VPN 通道的路由。
1. 在左侧导航栏选择**VPN 连接** > **VPN 网关**，并在右侧 VPN 网关列表中找到步骤一创建的 VPN 网关 A，并单击其名称。
2. 在 VPN 网关 A 详情页签，单击**路由表**页签，并单击**新增路由**。
![](https://main.qcloudimg.com/raw/7a6154909b1aaa0e1a22635fe0c869f8.png)
3. 在**新建路由**页面配置 VPN 网关 A 至 VPN 通道 B 和 VPN 通道 C 的路由策略。
<img src="https://main.qcloudimg.com/raw/2b5646e3e1fc31518ed425985cec3b0a.png" width="70%"></br>
<table>
<tr>
<th width="12%">配置项</th>
<th>说明</th>
</tr>
<tr>
<td>目的端</td>
<td>填写待访问的对端网络的网段，即 IDC 侧提供对外访问的网段。</td>
</tr>
<tr>
<td>下一跳类型</td>
<td>系统自动填充**VPN 通道**。</td>
</tr>
<tr>
<td>下一跳</td>
<td>选择创建好的 VPN 通道。</td>
</tr>
<tr>
<td>权重</td>
<td><ul><li>VPN 通道 B 填写 0。</li><li>VPN 通道 C  填写100。</li></ul> <br>0 表示优先级高，100表示优先级低。</td>
</tr>
</table>
4. 单击**确定**。

### 步骤六：配置通道健康检查
VPN 网关路由配置完成后，为 VPN 通道健康检查（主备通道均需配置）。
>?当健康检查触发主备通道切换，可能会出现短暂的业务中断，请勿担心，1～2秒后主备通道切换成功后业务恢复正常。
>

#### 主用通道 B 健康检查配置
1. 在左侧导航栏选择**VPN 连接** > **VPN 通道**，并在右侧 VPN 通道列表中找到创建好的 VPN 通道，然后单击 VPN 通道名称。 
2. 在通道**基本信息**页签单击**编辑**。
<img src="https://main.qcloudimg.com/raw/cb1d19f0102c832264a7531d52e54c9f.png" width="50%">
3. 打开健康检查开关，输入**健康检查本端地址**和**健康检查对端地址**，并单击**保存**。
<img src="https://main.qcloudimg.com/raw/d4973cf03855b2b2dd85e46b0c2fa451.png" width="50%">
>?
>- 本端地址：填写腾讯云侧向 IDC 发起健康检查的访问请求 IP 地址。该 IP 地址不能为 VPC 内 IP 地址。
>- 对端地址：填写 IDC 侧用于响应腾讯云健康检查请求的 IP 地址。该 IP 地址请勿与腾讯云侧地址相同，以防 IP 冲突。
>- 当腾讯云侧发起健康检查请求，访问请求通过通道到达 IDC 后，发现有健康检查响应 IP 地址，表示通道健康正常，如果没有表示异常。
>

#### 备用通道 C 健康检查配置
重复主用通道健康检查配置步骤1 ～ 步骤3，其中健康检查连接不能与主用通道的健康检查连接相同。

### 步骤七：配置 VPC 路由策略
截止至步骤五，已经将主备 VPN 通道配置成功，需要配置 VPC 路由策略，将子网中的流量路由至 VPN 网关上，子网中的网段才能与 IDC 中的网段通信。
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击**子网**，选择对应的地域和私有网络，单击子网所关联的路由表 ID，进入详情页。
![](https://main.qcloudimg.com/raw/a1a027602e2e65914120a8ce0c3e1b51.png)
3. 单击**+新增路由策略**。
![](https://main.qcloudimg.com/raw/60984e42e4e2b0ae9b7c5d64c422fc54.png)
4. 在弹出框中，输入目的端网段，下一跳类型选择**VPN 网关**，下一跳选择刚创建的 VPN 网关，单击**创建**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/e80d882e94f5e38d537307d3ff3042d9.png)

### 步骤八：激活 VPN 通道
使用 VPC 内的云服务器 ping 对端网段中的 IP，以激活 VPN 隧道，可以 ping 通表示 VPC 和 IDC 可以正常通信。
当 VPN 路由表中探测 VPN 主用通道 B 路由不可达时，系统自动将流量切换至 VPN 通道 C，确保业务的高可用性。
