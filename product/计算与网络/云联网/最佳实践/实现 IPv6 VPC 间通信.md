云联网可以关联 IPv6 地址的 VPC，支持 IPv6 VPC 之间通信、IPv4 VPC 和 IPv6 VPC 通信、IPv4/Pv6 VPC 和 IDC 间的通信。本文将介绍如何使用云联网实例，以实现同账号下的广州和北京地域的 IPv6 VPC 互通。

## 背景信息

创建云联网实例时，您可以根据实际选择月预付费或月95后付费模式，详情请参见 [计费总览](https://cloud.tencent.com/document/product/877/18676)，两种模式对应的操作不同，具体如下图所示：
![](https://main.qcloudimg.com/raw/52b2edef58c332cb5aee06f20c061c2f.png)

您还可以使用将云联网实例管理跨账号的 IPv4/Pv6 VPC 实例，详情请参见 [关联跨账号 VPC](https://cloud.tencent.com/document/product/877/19890)。本文以同账号下的广州和北京地域的 IPv6 VPC 互通，为您介绍相关操作。

## 使用限制

- 云联网课绑定 IPv6 VPC 功能灰度中，请联系腾讯云商务经理申请。
- 云联网可绑定 IPv6 VPC 功能仅支持北京、广州地域。

## 前提条件

已在广州和北京地域下分别创建 VPC 和子网并分配 IPv6 CIDR ，确保二者网段不重叠，且在子网内分别创建云服务器并分配 IPv6 地址。详情请参见 [快速搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/37946)。

<span id="1"></span>

## 步骤一：创建云联网实例

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) ，在左侧导航栏中，单击【云联网】。
2. 在云联网实例列表上方，单击【+新建】。
3. 在“新建云联网实例”对话框中配置以下信息，单击【确定】。
   ![](https://main.qcloudimg.com/raw/1fb0eda559741723f6574f2a4d43ed60.png)
	 **字段说明如下**：
 <table>
 <thead>
 <tr>
  <th >字段</th>
  <th >子字段</th>
  <th >说明</th>
 </tr>
  </thead>
 <tr>
  <td>名称</td>
   <td >-</td>
  <td >云联网实例的名称。</td>
 </tr>
 <tr >
  <td rowspan=2  >计费模式</td>
  <td >预付费</td>
  <td>单价较月95约低20%，适合带宽稳定的成熟业务。</td>
 </tr>
 <tr >
  <td >月95后付费</td>
  <td>按当月实际使用带宽95削峰计费，适合带宽波动较大业务。</td>
 </tr>
 <tr>
  <td rowspan=3 >服务质量</td>
  <td >白金</td>
  <td>适用于通信质量最敏感的关键业务，金牌次之，主要包括支付，游戏加速等。</td>
 </tr>
 <tr>
  <td  >金</td>
  <td >适用于重要数据业务数据传输业务，如企业商务数据传递、ERP 等。</td>
 </tr>
 <tr >
  <td>银</td>
  <td >银牌适用成本敏感，抖动不敏感，安全性高的业务。</td>
 </tr>
 <tr>
  <td rowspan=2>限速方式</td>
  <td >地域出口限速</td>
  <td >某地域去往其它地域的总体出带宽限速。</td>
 </tr>
 <tr>
  <td>地域间限速</td>
  <td >两地域之间的出入带宽限速。预付费模式下仅支持地域间限速。</td>
 </tr>
 <tr>
  <td>关联实例</td>
  <td  >-</td>
  <td >可关联私有网络、专线网关、黑石私有网络、VPN
  网关等实例，本示例中选择关联广州地域的 IPv6 VPC。</td>
 </tr>
</table>

<span id="2"></span>

## 步骤二：关联网络实例

将北京地域的 IPv6 VPC 关联至云联网，具体步骤如下：

1. 在 [云联网列表](https://console.cloud.tencent.com/vpc/ccn) 中，单击目标云联网实例 ID。
2. 在“关联实例”页面，单击【新增实例】。 
3. 在“关联实例”对话框中，选择广州地域的 IPv6 VPC 实例进行关联。
![](https://main.qcloudimg.com/raw/ed593d8eb3529df916dfef1507f41dae.png)
4. 单击【确定】，将所选网络实例加入云联网。

>?如还需关联其他网络实例，可单击【新增实例】继续关联。
>
<span id="3"></span>

## 步骤三：检查路由表

查看云联网关联的 IPv6 VPC 中各子网的路由策略是否生效。若所关联的网络实例网段有冲突，则会产生失效路由。

1. 在 [云联网列表](https://console.cloud.tencent.com/vpc/ccn) 中，单击目标云联网实例 ID。
2. 在云联网实例详情页，单击【路由表】标签页。
3. 查看该云联网路由表是否存在状态为**失效**的路由策略。若存在，则根据 [路由限制](https://cloud.tencent.com/document/product/877/18679#.E8.B7.AF.E7.94.B1.E9.99.90.E5.88.B6) 中的路由冲突原则，修改路由表并启用路由，详情请参见 [启用路由](https://cloud.tencent.com/document/product/877/18750)。
   >? IPv6 VPC 子网的路由策略中，目的端同时存在主 IPv4 地址和扩展 IPv6 地址。

## 步骤四：配置带宽

- **购买两端地域带宽（仅月预付费云联网实例适用）**
  若您创建的月预付费云联网实例，未购买带宽时，所有地域间10Kbps以下带宽可以免费通信。而实际业务中需要更高带宽，则需按通信地域购买。
    1. 在 [云联网列表](https://console.cloud.tencent.com/vpc/ccn) 中，单击目标云联网实例 ID。
    2. 在云联网实例详情页，单击【带宽管理】标签页。
    3. 在“带宽管理”标签页，单击【购买带宽】。
    3. 在“购买带宽”对话框中，选择广州和上海地域，并设置带宽上限和购买时长，单击【确定】。
![](https://main.qcloudimg.com/raw/ff6256d91cc96bcf7a4566ed558889ff.png)

- **设置跨地域带宽限制（仅月95后付费云联网实例适用）**
  若您创建的月95后付费云联网实例，可以按需配置跨地域带宽上限，有以下两种方式：
  > ?默认带宽上限为 1Gbps，如需更大默认带宽，请提 [工单申请](https://console.cloud.tencent.com/workorder/category)。
  > 
	- **设置地域间带宽限速**
  单击【调整带宽】，在弹框中选择需要限速的两个地域，填写地域间的带宽上限，如需添加多条请单击【添加】继续，完成添加后单击【确定】。
	![image-20200717162724864](/Users/luoyang/Library/Application Support/typora-user-images/image-20200717162724864.png)
	- **设置地域出口带宽限速**
   单击【调整带宽限速】，在弹框中勾选需要限速的地域，填写地域出口的带宽上限，单击【确定】即可。
   ![image-20200717162546138](/Users/luoyang/Library/Application Support/typora-user-images/image-20200717162546138.png)

>?云联网实例间通信可能会产生费用，详情请参见 [计费总览](https://cloud.tencent.com/document/product/877/18676)。

## 结果验证

登录广州地域的云服务器，向北京地域的云服务器执行 `ping <IPv6 地址>` 命令，若出现以下结果说明网络连接成功。
![image-20200717172951136](/Users/luoyang/Library/Application Support/typora-user-images/image-20200717172951136.png)



## 更多信息

您可以按照以下内容进行更多云联网操作：

- 实例管理
  - [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)
  - [关联网络实例](https://cloud.tencent.com/document/product/877/18747)
  - [删除云联网实例](https://cloud.tencent.com/document/product/877/18748)
  - [解除网络实例关联](https://cloud.tencent.com/document/product/877/18757)
  - [添加 IDC 网段](https://cloud.tencent.com/document/product/877/19036)
  - [解关联跨账号 VPC](https://cloud.tencent.com/document/product/877/19891)
  - [关联跨账号 VPC](https://cloud.tencent.com/document/product/877/19890)
- 路由管理
  - [查看路由信息](https://cloud.tencent.com/document/product/877/18756)
  - [查看已关联 VPC 的路由表](https://cloud.tencent.com/document/product/877/18754)
  - [启用路由](https://cloud.tencent.com/document/product/877/18750)
  - [停用路由](https://cloud.tencent.com/document/product/877/18746)
- 监控与告警
  - [查看监控信息](https://cloud.tencent.com/document/product/877/18755)
  - [查看出带宽上限](https://cloud.tencent.com/document/product/877/18753)
  - [调整出带宽上限](https://cloud.tencent.com/document/product/877/18759)
  - [设置跨地域互联告警](https://cloud.tencent.com/document/product/877/18758)
