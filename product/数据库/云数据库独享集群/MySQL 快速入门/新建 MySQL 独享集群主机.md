MySQL 独享集群创建后，您需要在独享集群内新建主机，才能在主机上分配实例并使用独享集群的各项功能。

## 前提条件
[创建 MySQL 独享集群](https://cloud.tencent.com/document/product/1322/76526)。

## 操作步骤
1. 登录 [云数据库 MySQL 独享集群控制台](https://console.cloud.tencent.com/dbdcp)。
2. 在页面上方选择目标地域。
3. 找到目标集群，单击集群 ID，然后选择**主机列表**，或直接单击**操作**列的**管理主机**。
![](https://qcloudimg.tencent-cloud.cn/raw/eb7418889e5eee2e81f0e1bcecdd05da.png)
4. 在主机列表页，单击**新建**。
5. 在跳转的 MySQL 独享集群主机购买页，完成以下参数设置。
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>独享集群</td>
<td>默认为上述步骤3的目标集群，可通过下拉键更换集群。</td></tr>
<tr>
<td>地域</td>
<td>主机所在的地域。默认为所选集群所在地域。</td></tr>
<tr>
<td>可用区</td>
<td>主机所在可用区。建议将主机分布在不同可用区提高可用性。</td></tr>
<tr>
<td>网络</td>
<td>主机所属网络，您也可 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=1">新建私有网络</a> 或 <a href="https://console.cloud.tencent.com/vpc/subnet?rid=1">新建子网</a>。</td></tr>
<tr>
<td>设备</td>
<td>主机的设备机型。</td></tr>
<tr>
<td>存储空间</td>
<td>主机规格对应的存储空间。支持选择 SSD 云硬盘和增强型 SSD 云硬盘。</td></tr>
<tr>
<td>主机名称</td>
<td>立即命名或创建后命名。实例名称仅支持数字，英文大小写字母、中文以及特殊字符_-./()[]（），且长度不能超过60，批量购买实例时，会在自定义实例名称的尾部添加数字序号。</td></tr>
<tr>
<td>数量</td>
<td>购买主机的数量。</td></tr>
<tr>
<td>自动续费</td>
<td>账户余额足够时，到期后自动按月续费。</td></tr>
<tr>
<td>服务条款</td>
<td><a href="https://cloud.tencent.com/document/product/1322/52362">独享集群服务条款</a>。</td></tr>
<tr>
<td>购买时长</td>
<td>主机购买时长。</td></tr>
</tbody></table>
6. 单击**立即购买**，并完成支付。

## 后续步骤
MySQL 独享集群主机创建完成后，您需要创建和分配实例。详情请参见 [分配实例](https://cloud.tencent.com/document/product/1322/76528)。
