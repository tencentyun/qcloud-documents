CCN 型 VPN 网关可以关联至云联网，实现 IDC 与云联网间的加密通信。本文介绍如何将 CCN 型 VPN 网关关联至云联网。

## 背景信息
CCN 类型的 VPN 网关可以关联至云联网，每个 CCN 型 VPN 网关可以建立多个 VPN 加密通道，每个 VPN 通道可以打通一个本地 IDC。
![](https://main.qcloudimg.com/raw/fb1ccfd3f010983a65a2bf8187a437e5.png)

将 CCN 类型的 VPN 网关关联至云联网步骤如下：
1. [创建 CCN 型 VPN 网关](#step1)：VPN 网关是云联网建立 VPN 连接的出口网关，与对端网关配合使用。
2. [ 关联云联网实例](#step2)：将创建的 CCN 型 VPN 网关与云联网实例关联。
3. [创建对端网关](#step3)：对端网关是用来记录 IDC 端的 IPsec VPN 网关公网 IP 地址的逻辑对象（IDC 端必须有固定公网 IP），需与腾讯云 VPN 网关配合使用，一个 VPN 网关可与多个对端网关建立加密的 VPN 网络通道。
4. [创建 VPN 通道](#step4)： VPN 通道支持 IPsec 加密协议，用于保护数据传输的信息安全。
5. [配置 VPN 网关路由](#step5)：VPN 通道配置成功后，需要配置 VPN 网关至对端网关的路由。
6. [IDC本地配置](#step6)：在 IDC 侧的“本地网关”上配置另一侧（腾讯云侧）的 VPN 通道信息。
7. [启用 IDC 网段](#step7)：将 SPD 策略中的对端网段加入云联网中。



## 操作步骤
### 步骤一：创建 CCN 型 VPN 网关[](id:step1)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏中选择【VPN连接】>【VPN网关】。
3. 在顶部导航栏选择【地域】，并在 “VPN 网关“页面单击【+新建】。
4. 在弹出的“新建VPN网关”窗口中，填写 VPN 网关名称（如 TomVPNGw），选择关联网络、带宽上限、计费方式，单击【创建】即可。VPN 网关创建完成后，系统随机分配公网 IP，如 `203.195.147.82`。
>?如需将 CCN 型 VPN 网关新建在指定的可用区下，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)。
>
 - 网关名称：填写 VPN 网关名称，不超过60个字符。
 - 关联网络：选择云联网。
 - 带宽上限：按需选择 VPN 网关的带宽上限。
 - 计费方式：按需选择 VPN 网关的计费方式。
   - 按流量计费：适用于带宽波动较大的场景。
   - 包年包月： 适用于带宽较稳定的场景。
    ![](https://main.qcloudimg.com/raw/a524d91fc73e82de17efe299d5a26a0e.png)
		

### 步骤二：关联云联网实例[](id:step2)
- 若您已创建云联网实例，请按如下操作关联云联网：
 1. 返回 “VPN 网关“页面，在 VPN 网关列表中，单击已创建的云联网型 VPN 网关 ID。
 2. 在“基本信息“页面，单击所属网络右侧的<img src="https://main.qcloudimg.com/raw/7b27e195bfc7f7ee82118f80c4c96b28.png" style="margin:-4px 0;"/>，在下拉列表中选择目标云联网实例，并单击【保存】即可。
![](https://main.qcloudimg.com/raw/4b201b74b503d320ebd837403990ded5.png)
- 若您未创建云联网实例，请按如下步骤关联云联网：
 1. 在左侧导航栏单击【云联网】。
 2. 在“云联网”页面上方选择【地域】，单击【+新建】。
 3. 在弹出的“新建云联网实例”窗口中进行如下操作，完成后单击【确定】。
   1. 填写云联网实例名称、描述，选择计费模式、服务质量、限速方式。
   2. 在“关联实例”下方选择【VPN 网关】，以及已创建的云联网型 VPN 网关的地域和 ID。
![](https://main.qcloudimg.com/raw/07268293996aafc70d273d785e9147f1.png)

### 步骤三：创建对端网关[](id:step3)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏选择【VPN 连接】>【对端网关】。
3. 在“对端网关”页面上方选择【地域】，并单击【+新建】。
4. 在弹出的“新建对端网关”窗口中，填写对端网关名称和 IDC 端 VPN 网关的公网 IP，并单击【创建】。
![](https://main.qcloudimg.com/raw/67a9eb50c30808ce93e9dc620c1381b9.png)

### 步骤四：创建 VPN 通道[](id:step4)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏选择【VPN 连接】>【VPN 通道】。
3. 在 “VPN 通道”页面上方选择【地域】，并单击【+新建】，进入“新建 VPN 通道”页面。
4. 输入通道名称，选择 VPN 网关类型为【云联网】，选择对端网关，并输入预共享密钥（如`123456`），单击【下一步】。
![](https://main.qcloudimg.com/raw/2cc976c50205915f0373e0ed285b92b8.png)
5. 输入 SPD 策略来限制本端哪些网段和对端哪些网段通信，单击【下一步】。
>!
>- 每个规则中的多个对端网段间相互不能重叠。
>- 同一网关下多个通道内的规则不能重叠。
>- SPD策略中的对端网段可以加入云联网中。
>
![](https://main.qcloudimg.com/raw/9cb15f0216a6941b0d3226d24bc5c893.png)
6. （可选）配置 IKE 参数，如果不需要高级配置，可直接单击【下一步】。
![](https://main.qcloudimg.com/raw/c370884071d8dd5424be80bbef1e9aec.png)
7. （可选）配置 IPsec 参数，如果不需要配置，可直接单击【完成】。
![](https://main.qcloudimg.com/raw/6c67f435c015fb6d2e03ed96dc61b7f7.png)
8. 创建成功后，返回 VPN 通道列表页，在操作栏下单击【更多】>【下载配置文件】并完成下载。
![](https://main.qcloudimg.com/raw/5470e29feb9ff64e221df07cdfde06c3.png)

### 步骤五：配置 VPN 网关路由[](id:step5)
VPN 通道配置成功后，需要配置 VPN 网关至对端网关的路由。
1. 在左侧导航栏选择【 VPN 链接】>【 VPN 网关】，并在右侧 VPN 网关列表中找到创建好的 VPN 网关，并单击其名称。 
2. 在 VPN 网关详情页签，单击【路由表】页签，然后单击【新增路由】。
![](https://main.qcloudimg.com/raw/099d7503dc5e7e2ad5e7324d7d9571f8.png)
3. 在【新建路由】页面配置 VPN 网关至对端网关的路由策略。
![](https://main.qcloudimg.com/raw/d173233ca2ee26415e352051ce024419.png)
<table>
<tr>
<th>配置项</th>
<th>说明</th>
</tr>
<tr>
<td>目的端</td>
<td>填写待访问的对端网络的网段，即对端网关中配置的 IDC 侧提供对外访问的网段。</td>
</tr>
<tr>
<td>下一跳类型</td>
<td>系统自动填充【 VPN 通道】。</td>
</tr>
<tr>
<td>下一跳</td>
<td>选择创建好的 VPN 通道。</td>
</tr>
<tr>
<td>权重</td>
<td>0 表示优先级高，100表示优先级低。</td>
</tr>
</table>
4. 单击【确定】。


### 步骤六：IDC 本地配置[](id:step6)
完成前4步后，云上 VPN 网关和 VPN 通道的配置已经完成，需要继续在 IDC 侧的“本地网关”上配置另一侧的 VPN 通道信息，具体请参考[本地网关配置](https://cloud.tencent.com/document/product/554/56361)。

### 步骤七：启用 IDC 网段[](id:step7)
>?
>+ 本步骤仅针对1.0和2.0版本的VPN网关。3.0版本的 VPN 网关，此处为【路由表】页签，如下图所示。
>+ 如果是3.0版本的CCN型 VPN 网关，且 VPN 网关已关联至云联网实例时，则下一跳到【云联网】的路由策略，系统将自动学习到并展示在路由条目中，无需手动再次配置。此外，VPN 网关中配置的路由策略也会自动同步到云联网。
>
**3.0版本的 VPN 网关【路由表】界面展示：**
![](https://main.qcloudimg.com/raw/d261071d65c453ecf21d3980d1b3a8cd.png)
**针对1.0和2.0版本的 VPN，请执行如下操作启用 IDC 网段：**
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏中选择【VPN 连接】>【VPN 网关】。
3. 在 VPN 网关列表中，单击云联网型 VPN 网关 ID。
4. 在 VPN 网关详情页面，选择【IDC 网段】页签，并启用目标网段。
![](https://main.qcloudimg.com/raw/a855442ce1c46f50382a2f779f2d89b7.png)


## 结果验证
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏中选择【云联网】。
3. 在云联网列表页中，单击 CCN 型 VPN 网关关联的云联网实例 ID。
4. 在云联网详情页面，选择【路由表】页签，若启用的网段在路由表中，且“状态”为有效，“下一跳”为 CCN 型 VPN 网关，则说明关联成功。
![](https://main.qcloudimg.com/raw/e6a6ce4b9cb4aff72b1a90fe3758d3a6.png)
