如果您 VPC 中部署的云服务需要共享给其他地域下的 VPC 访问，您可以使用私有连接和云联网服务。

## 背景信息
VPC 是您独有的云上私有网络，不同 VPC 之间默认完全隔离。您可以通过私有连接（Private Link）服务，实现腾讯云 VPC 与同地域其他 VPC 上安全稳定的访问连接，简化网络架构，避免公网访问服务带来的潜在安全风险。如果您需要跨地域提供VPC服务共享，那么可以结合云联网打通跨地域 VPC 通信，然后再共同使用私有连接服务使用方 VPC 的终端节点实现对服务提供方 VPC 中服务的访问。

使用私有连接 Private Link 建立连接，您需要创建终端节点服务和终端节点。在创建终端节点服务之前，您需要创建一个内网4层负载均衡实例，并创建监听器关联已经部署业务的云服务器实例，之后在创建终端节点服务时关联该负载均衡实例，此时终端节点服务将作为服务提供方的业务访问入口，供服务使用方创建的终端节点来申请连接，连接建立成功后，服务使用方即可访问服务提供方部署的业务服务。

## 场景示例
本文以下图业务场景为例。某公司业务部署在成都地域 VPC2 中，现需要将该业务用共享给同地域下其他 VPC1 网络及重庆地域下的 VPC3  网络中的客户端访问，为避免公网访问带来的潜在安全风险，使用腾讯云私有连接以及云联网来实现该通信方案。
![](https://main.qcloudimg.com/raw/9adb36d1b01e0245aee8003419854bb1.png)
>?本文假设三个 VPC 为同账号下 VPC，如果是跨账号，私有连接和云联网的连接请求方发起连接后，均需要得到服务方的同意才可连通；私有连接需要服务使用方提前将账号告知服务提供方来添加白名单，服务提供方需要将负载均衡的 VPORT 告知服务使用方，其余操作无异。

## 前提条件
+ 您已注册腾讯云账号，并已创建服务提供方 VPC2 和服务使用方 VPC1，以及跨地域服务使用方 VPC3。
+ 您已提交私有连接 [内测申请](https://cloud.tencent.com/apply/p/5i6ii4g3lgk)。
+ 在服务提供方 VPC2 中已创建内网4层 CLB 实例，并在 CLB 后端云服务器实例中部署相关服务资源，请确保后端云服务器实例可以正常处理负载均衡转发的请求，具体请参加 [负载均衡快速入门](https://cloud.tencent.com/document/product/214/8975)。
+ 为保证服务使用方能够正常访问腾讯云公共业务，例如 MySQL，**请确保服务提供方 VPC2 中负载均衡后端云服务器关联的安全组已放通11.163.0.0/16地址段**，如下图所示。   
	<img src="https://main.qcloudimg.com/raw/0462ab7efa311e9fb253e147628e2f7a.png" width="80%" />

## 操作步骤

### 步骤1：服务提供方创建终端节点服务
>?本例中服务提供方 VPC2 中已创建4层内网 CLB，CLB 后端云服务器实例已部署相关业务服务，且云服务器实例安全组已放通11.163.0.0/16网段。
>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=16)。
2. 在左侧导航栏单击【私有连接】>【终端节点服务】。
3. 单击【新建】，在弹出的新建终端节点服务界面，配置相关参数。
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
<td>指定终端节点服务是否自动接受终端节点发起的连接请求，默认为否。本例为同账号 VPC 连接，无论此处选择是否，均自动接受，因此保持默认即可。
</td>
</tr>
</table>
4. 完成参数设置后，单击【确定】完成终端节点服务的创建。

### 步骤2：服务使用方创建终端节点
1. 单击左侧导航栏单击【终端节点】。
2. 单击【新建】，在弹出的新建终端节点界面，配置相关参数。
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
<td>选择需要访问的 VPC 的所属账户，【我的账户】说明是同账户 VPC 的访问，【其他账户】说明是跨账户 VPC 的访问，本例选择【我的账户】。</td>
</tr>
<tr>
<td>选择服务</td>
<td>输入终端节点服务的 ID 后单击【验证】，只有验证通过的服务才可建立连接。</td>
</tr>
</table>
<img src="https://main.qcloudimg.com/raw/8a7c0a80da4686295ca7571794767b35.png" width="50%" />
3. 完成参数配置后，单击【确定】，当前终端节点的连接状态为【待接受】。
   <img src="https://main.qcloudimg.com/raw/81154a54e227c00995da4e770619e5b2.png" width="80%" />


### 步骤3：创建云联网并关联跨地域 VPC
1. 登录 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn)。
2. 单击【新建】创建云联网实例，关联跨地域 VPC1 和 VPC3，单击【确定】，即可实现 VPC1 和 VPC3 的互联。
![](https://main.qcloudimg.com/raw/17e03652899379f8a1b143d8839791b5.png)
>?更多详细内容，请参见 [云联网快速入门](https://cloud.tencent.com/document/product/877/18763)。
>

### 步骤4：服务使用方发起访问请求进行连接验证
- 验证成都地域服务使用方 VPC1 访问 VPC2：
 1. 登录服务使用方 VPC1 下的某台 CVM，通过 VIP+VPORT 访问服务提供方的后端服务。
 2. 本例使用 telnet 验证连通性，执行 telnet *VIP VPORT*。
     >?如果服务器没有安装 telnet，请先执行 `yum install telnet` 安装 telnet。
     >
	获取终端节点VIP：
 <img src="https://main.qcloudimg.com/raw/d21dc32174c18fc67e4f549c44b86086.png" width="70%" /><br>
   获取CLB的VPORT：
 <img src="https://main.qcloudimg.com/raw/922dc796b2d687354a355ab6fe845437.png" width="70%" /><br>
  返回如下信息，表示访问成功：
<img src="https://main.qcloudimg.com/raw/8f9817596cf774d69605ab30bfaed49e.png" width="50%" /><br>
- 验证重庆地域下 VPC3 通过成都地域服务使用方 VPC1 中的终端节点访问服务提供方 VPC2：
 1.  登录 VPC3 下的某台 CVM，通过 VIP+VPORT 访问服务提供方的后端服务。该 VIP 为 VPC1 中终端节点获取的 VIP，本例中为172.16.2.16，VPORT 为 VPC2 中 CLB 的监听端口，本例为1044。
 2.  依然使用 telnet 验证连通性，执行 telnet *VIP VPORT*。
     >?如果服务器没有安装 telnet，请先执行 `yum install telnet` 安装 telnet。
     >
	返回信息如下，表示访问成功：<br>
	<img src="https://main.qcloudimg.com/raw/2504940fd846c6cb3a37a8fd2b8812ec.png" width="50%" />
