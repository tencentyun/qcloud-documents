VPC 间防火墙高级模式下，用户可以对路由进行自定义配置，实现个性化引流和防护的方案。本文将从如下几个步骤指引您如何创建防火墙和配置引流路由。

## 准备工作
### 防火墙名词概念
#### 防火墙实例
用于承载防火墙功能的虚拟化实例，与 CVM 类似，可前往 [云防火墙控制台](https://console.cloud.tencent.com/cfw/switch/vpc/vpc?tab=instance) 查看。
#### 防火墙引流 VPC
由防火墙在云联网创建的专用 VPC，用于将用户网络流量通过防火墙引流 VPC 牵引至防火墙实例，从而实现防护效果，请勿删改。一般命名为“防火墙专用 VPC_请勿删改”。可以前往 [云联网实例详情控制台](https://console.cloud.tencent.com/vpc/ccn) 查看。
>?防火墙会在每个地域分别创建不同的 VPC 用于对应地域流量的引流。
>
![](https://qcloudimg.tencent-cloud.cn/raw/d8064b75c356c5815e67d7ddbf200a0b.png)

#### 防火墙路由表
防火墙自动创建的路由表，用于分配流量，请勿手动修改。一般命名为“防火墙VPC专用路由表_请勿删改”。
>!每个地域会创建一张用于防火墙的路由表。
>
![](https://qcloudimg.tencent-cloud.cn/raw/5721c3764972821c6db1ad7fde1506de.png)


### 工作模式
VPC 间防火墙和所有业务 VPC 在同一个云联网中，通过建立一个防火墙专用 VPC 网段来将用户 VPC 互访的流量牵引至防火墙。
![](https://qcloudimg.tencent-cloud.cn/raw/20045df62ab191caf5ac4028815d6544.png)

## 步骤1：创建高级模式实例[](id:step1)
参考 [VPC 间防火墙开关-新建防火墙实例](https://cloud.tencent.com/document/product/1132/46930#.E6.96.B0.E5.BB.BA.E9.98.B2.E7.81.AB.E5.A2.99.E5.AE.9E.E4.BE.8B)，创建目标实例，其中模式选择**高级模式**。

## 步骤2：配置引流路由
当前操作目的是将用户需要防护的业务 VPC 通过防火墙网关引流至防火墙实例。

1. 前往 [创建高级模式实例](#step1) 时选择的云联网实例的控制台，查看高级模式关联的云联网实例详情。
2. 确认防火墙引流 VPC 和相关路由表已经创建，若未创建请等待实例创建完成或 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
3. 查看默认路由表页面，确定需要接入的业务 VPC 及防火墙引流 VPC。
>?本文以北京业务 VPC：VPC-A；重庆业务 VPC：VPC-B；北京地域防火墙引流 VPC：VPC-BJFW 举例来演示如何接入。
>
![](https://qcloudimg.tencent-cloud.cn/raw/531b51b6f93e3ca9c6e37ab46669f3f0.png)
4. 前往**私有网络** > **[路由表](https://console.cloud.tencent.com/vpc/route?rid=1)** 页面，选择需要接入的防火墙引流 VPC，可以看到包含“防火墙 VPC 专用路由表_请勿删改”和“default”在内的路由表。选择“default”路由表编辑路由策略。
![](https://qcloudimg.tencent-cloud.cn/raw/cb8e6feaccba52a170b4da8a805cee77.png)
5. 单击**新增路由策略**，将业务 VPC 下一跳引流至防火墙。
![](https://qcloudimg.tencent-cloud.cn/raw/652b9224a864dd6f66d15802681062e7.png)
目的端输入业务 VPC 的 CIDR，下一跳类型选择**高可用虚拟 IP**，下一跳选择**防火墙网关 ID**，备注可以自由填写。
![](https://qcloudimg.tencent-cloud.cn/raw/f7192421f2ee288d52bd037f1af30c15.png)
防火墙网关 ID 可以前往实例详情中查看。
![](https://qcloudimg.tencent-cloud.cn/raw/fdafe93b9c032402ad106e33c7a85f63.png)
>?若有提示“指定 CIDR 形成 ECMP”时，需要先在默认路由表中停用相关业务路由。
>
6. 将新增路由发布到云联网，详情请参见 [管理路由策略](https://cloud.tencent.com/document/product/215/53587#.E5.8F.91.E5.B8.83.2F.E6.92.A4.E9.94.80.E8.B7.AF.E7.94.B1.E7.AD.96.E7.95.A5.E5.88.B0.E4.BA.91.E8.81.94.E7.BD.91.3Ca-id.3D.22revoke.22.3E.3C.2Fa.3E)。发布后可以在对应云联网中的默认路由表看到指定路由策略。
>?因新路由策略与原路由策略冲突，原路由条目会失效，可以忽略。
>
![](https://qcloudimg.tencent-cloud.cn/raw/b38dfb8d4a4e102e86f0c72340798297.png)

## 步骤3：建立业务 VPC 互访路由表
当前操作目的是为了将防火墙网络和用户的业务网络打通，实现网络互访。
1. 在 [云联网页面](https://console.cloud.tencent.com/vpc/ccn)，分别为每个引流至防火墙的业务 VPC 建立路由表。
![](https://qcloudimg.tencent-cloud.cn/raw/162f8b628d419b6a16ceecc0958d82a9.png)
2. 调整路由接收策略。在各个 VPC 的专属路由表中的**路由接收策略**中单击**添加网络实例**，将路由表自身所属 VPC 实例和互通 VPC 实例添加至路由表中。
>!添加网络实例务必分为两个步骤，先添加自身 VPC 实例和不经过防火墙防护的 VPC 实例；再添加防火墙引流专用 VPC 实例。
>
例如：假设 VPC-C 是不需要接入防火墙实例的业务 VPC，则在 VPC-A 的路由表中应先添加 VPC-A，VPC-C 两个实例，添加成功后，重复上述操作再添加 VPC-BJFW 一个实例。
![](https://qcloudimg.tencent-cloud.cn/raw/ac48d7119efb4b56e434d10cf08851eb.png)
3. 检查各个 VPC 的专属路由表中路由条目是否符合预期。
4. 绑定网络实例。各个 VPC 的专属路由表的**绑定实例**单击**绑定网络实例**，将各个 VPC 专属路由表绑定至其对应的 VPC 实例，操作完成后网络会引流至防火墙。
>!请务必确认路由无误后再绑定路由表，绑定后会立即生效。
>

## 步骤4：验证防火墙是否正常工作
1. 参考 [日志审计](https://cloud.tencent.com/document/product/1132/45858#.E6.9F.A5.E7.9C.8B.E6.B5.81.E9.87.8F.E6.97.A5.E5.BF.97) 查看是否有流量日志。
2. 参考 [日志审计](https://cloud.tencent.com/document/product/1132/45858#.E6.9F.A5.E7.9C.8B.E5.85.A5.E4.BE.B5.E9.98.B2.E5.BE.A1.E6.97.A5.E5.BF.97) 查看入侵防御是否正常。
>!高级模式下的入侵防御模式跟随主模式，无法单独调节。
>
3. 配置内网间规则，检查是否正常命中。

至此防火墙已正常工作，如果您的网络结构较为复杂或涉及专线场景，请  [提交工单](https://console.cloud.tencent.com/workorder/category)  咨询详细路由配置方案；如果您有更多疑问也欢迎  [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
