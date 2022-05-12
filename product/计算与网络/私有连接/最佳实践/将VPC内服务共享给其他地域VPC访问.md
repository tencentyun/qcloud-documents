如果您 VPC 中部署的云服务需要共享给其他地域下的 VPC 访问，您可以使用私有连接和云联网服务。

## 背景信息
VPC 是您独有的云上私有网络，不同 VPC 之间默认完全隔离。您可以通过私有连接（Private Link）服务，实现腾讯云 VPC 与同地域其他 VPC 上安全稳定的访问连接，简化网络架构，避免公网访问服务带来的潜在安全风险。如果您需要跨地域提供VPC服务共享，那么可以结合云联网打通跨地域 VPC 通信，然后再共同使用私有连接服务使用方 VPC 的终端节点实现对服务提供方 VPC 中服务的访问。

使用私有连接 Private Link，您需要创建终端节点服务和终端节点。在创建终端节点服务之前，您需要创建一个内网4层负载均衡实例，并创建监听器关联已经部署业务的云服务器实例，之后在创建终端节点服务时关联该负载均衡实例，此时终端节点服务将作为服务提供方的业务访问入口，供服务使用方创建的终端节点来申请连接，连接建立成功后，服务使用方即可访问服务提供方部署的业务服务。

## 场景示例
本文以下图业务场景为例。某公司业务部署在成都地域 VPC2 中，现需要将该业务用共享给同地域下其他 VPC1 网络及重庆地域下的 VPC3  网络中的客户端访问，为避免公网访问带来的潜在安全风险，使用腾讯云私有连接以及云联网来实现该通信方案。
![](https://main.qcloudimg.com/raw/9adb36d1b01e0245aee8003419854bb1.png)
>?本文假设三个 VPC 为同账号下 VPC。
>

## 前提条件
+ 您已提交私有连接 [内测申请](https://cloud.tencent.com/apply/p/5i6ii4g3lgk)。
+ 已创建服务提供方 VPC2 和服务使用方 VPC1，以及跨地域服务使用方 VPC3。
+ 在服务提供方 VPC2 中已创建内网4层 CLB 实例，并在 CLB 后端云服务器实例中部署相关服务资源，请确保后端云服务器实例可以正常处理负载均衡转发的请求，具体请参加 [负载均衡快速入门](https://cloud.tencent.com/document/product/214/8975)。
+ **请确保服务提供方 VPC2 中负载均衡后端云服务器关联的安全组已放通11.163.0.0/16地址段**，如下图所示。   
	<img src="https://main.qcloudimg.com/raw/0462ab7efa311e9fb253e147628e2f7a.png" width="80%" />

## 操作步骤
[](id:step1)
### 步骤1：服务提供方创建终端节点服务
>?本例中服务提供方 VPC2 中已创建4层内网 CLB，CLB 后端云服务器实例已部署相关业务服务，且云服务器实例安全组已放通11.163.0.0/16网段。
>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=16)。
2. 在左侧导航栏单击**私有连接** > **终端节点服务**。
3. 单击**新建**，在弹出的新建终端节点服务界面，配置相关参数。
    <img src="https://main.qcloudimg.com/raw/ca3c8b893bdd15975b85a23d78db9805.png" width="50%" /></br>
<table>
<tr>
<th width="12%">参数名称</th>
<th>描述</th>
</tr>
<tr>
<td>服务名称</td>
<td>自定义终端节点服务的名称。</td>
</tr>
<tr>
<td>所在地域</td>
<td>终端节点服务所在地域。</td>
</tr>
<tr>
<td>所属网络</td>
<td>选择所属 VPC，本例选择 VPC2。</td>
</tr>
<tr>
<td>负载均衡</td>
<td>选择 VPC 下已创建的负载均衡，本例选择 VPC2 中已创建好的 CLB 实例。</td>
</tr>
<tr>
<td>自动接受</td>
<td>指定终端节点服务<b>是</b>、<b>否</b>自动接受终端节点发起的连接请求，本例选择<b>是</b>：<ul><li>当选择<b>是</b>自动接受时，终端节点服务默认接受所有连接的终端节点的请求，终端节点创建成功后，状态即为<b>可用</b>。<li>当选择<b>否</b>不接受自动连接时，终端节点连接状态将为<b>待接受</b>，需要终端节点服务手动执行<b>接受连接</b>才能将状态从<b>待接受</b>变为<b>可用</b>。
</td>
</tr>
</table>
4. 完成参数设置后，单击<b>确定</b>完成终端节点服务的创建。

### 步骤2：服务使用方创建终端节点
>! 本例为同账号VPC间访问，故无需在终端节点服务中添加服务使用方的白名单账号；如果是跨账号VPC间访问，则需要服务使用方提前将UIN账号告知服务提供方，由服务提供方的终端节点服务先添加白名单，再执行本步骤，详情请参见 [跨账号 VPC 间服务共享](https://cloud.tencent.com/document/product/1451/57394)。
>
1. 单击左侧导航栏单击**终端节点**。
2. 单击**新建**，在弹出的新建终端节点界面，配置相关参数。
    <img src="https://main.qcloudimg.com/raw/24cb315ff0ef57647686e498d0ab2e31.png" width="50%" /><br>
<table>
<tr>
<th width="12%">参数名称</th>
<th>描述</th>
</tr>
<tr>
<td>名称</td>
<td>自定义终端节点的名称。</td>
</tr>
<tr>
<td>所属地域</td>
<td>终端节点所在地域。</td>
</tr>
<tr>
<td>所属网络</td>
<td>选择终端节点所在的 VPC，本例选择 VPC1。</td>
</tr>
<tr>
<td>所属子网</td>
<td>选择终端节点所在的子网。</td>
</tr>
<tr>
<td>IP 地址</td>
<td>终端节点的 IP 地址。可以指定 IP 地址，IP 地址为 VPC1 内的内网 IP，也可以选择自动分配 IP。</td>
</tr>
<tr>
<td>对端账户类型</td>
<td>选择待连接的终端节点服务所属账户，本例选择<b>我的账户</b>：<ul><li>同账号VPC间访问，选择<b>我的账户</b></li><li>跨账号VPC间访问，选择<b>其他账户</b></td>
</tr>
<tr>
<td>选择服务</td>
<td>输入终端节点服务的 ID 后单击<b>验证</b>，只有验证通过的服务才可建立连接。</td>
</tr>
</table>
3. 完成参数配置后，单击<b>确定</b>，由于本例 [步骤1](#step1) 中终端节点服务设置的是自动接受连接，即终端节点服务默认接受所有连接的终端节点的连接请求，故终端节点创建成功后，状态即为**可用**。
   ![](https://main.qcloudimg.com/raw/ea6a0b7da06b0e71daf19817a4cf0faa.png)


### 步骤3：创建云联网打通 VPC3 和 VPC1 网络
1. 登录 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn)。
2. 单击**新建**创建云联网实例，关联跨地域 VPC1 和 VPC3，单击**确定**，即可实现 VPC1 和 VPC3 的互联。
![](https://main.qcloudimg.com/raw/17e03652899379f8a1b143d8839791b5.png)
>?更多详细内容，请参见 [云联网快速入门](https://cloud.tencent.com/document/product/877/18763)。
>

### 步骤4：服务使用方发起访问请求进行连接验证
- 验证成都地域服务使用方 VPC1 访问 VPC2：
 1. 登录服务使用方 VPC1 下的某台 CVM，通过 VIP + VPORT 访问服务提供方的后端服务。
 2. 本例使用 telnet 验证连通性，执行 telnet *VIP VPORT*。
>?如果服务器没有安装 telnet，请先执行 `yum install telnet` 安装 telnet。
>
	获取终端节点 VIP：
 <img src="https://main.qcloudimg.com/raw/d21dc32174c18fc67e4f549c44b86086.png" width="70%" /><br>
   获取 CLB 的 VPORT：
 <img src="https://main.qcloudimg.com/raw/922dc796b2d687354a355ab6fe845437.png" width="70%" /><br>
  返回如下信息，表示访问成功：
<img src="https://main.qcloudimg.com/raw/8f9817596cf774d69605ab30bfaed49e.png" width="50%" /><br>
- 验证重庆地域下 VPC3 通过成都地域服务使用方 VPC1 中的终端节点访问服务提供方 VPC2：
 1.  登录 VPC3 下的某台 CVM，通过 VIP + VPORT 访问服务提供方的后端服务。该 VIP 为 VPC1 中终端节点获取的 VIP，本例中为172.16.2.16，VPORT 为 VPC2 中 CLB 的监听端口，本例为1044。
 2.  依然使用 telnet 验证连通性，执行 telnet *VIP VPORT*。
>?如果服务器没有安装 telnet，请先执行 `yum install telnet` 安装 telnet。
>
	返回信息如下，表示访问成功：<br>
	<img src="https://main.qcloudimg.com/raw/2504940fd846c6cb3a37a8fd2b8812ec.png" width="50%" />
