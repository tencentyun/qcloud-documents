您需要先创建 MySQL 独享集群，才能使用独享集群内的各项功能。
>?MySQL 独享集群目前内测中，您可通过 [内测申请](https://cloud.tencent.com/apply/p/xugaubtwg9h) 申请开通。

## 背景信息
关于独享集群的更多介绍，请参见 [产品概述](https://cloud.tencent.com/document/product/1322/52306)。

## 操作步骤
1. 登录 [云数据库 MySQL 独享集群控制台](https://console.cloud.tencent.com/dbdcp)。
2. 在页面上方选择目标地域。
3. 单击地域下方的**新建**，跳转至集群资源创建页面。
![](https://qcloudimg.tencent-cloud.cn/raw/905de5877f742539ba63d0dedd5ba959.png)
4. 在集群资源创建页，设置以下参数，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/68b67a01889e2093ae2808a5d72593c1.png)
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>地域</td>
<td>当前支持地域为北京、成都、广州、上海、上海金融，如已在上述步骤2中选择了目标地域，此项会默认同目标地域。</td></tr>
<tr>
<td>数据库类型</td>
<td>选择数据库类型为 MySQL。</td></tr>
<tr>
<td>CPU 超配比</td>
<td>独享集群的 CPU 超配比。即所有实例的 CPU 资源之和可以是实际 CPU 资源的2倍，可较大化使用。CPU 资源默认为100%，最高支持调整为200%。</td></tr>
<tr>
<td>内存限额</td>
<td>独享集群中每台主机的内存最大使用率限额。可设置范围：50% - 90%。</td></tr>
<tr>
<td>资源分配策略</td>
<td>紧凑分配：更充分的资源利用率，优先从创建时间较早且已分配资源较多的主机中分配资源。<br>均衡分配：更稳定的系统表现，优先从未分配资源或已分配资源较少的主机中分配资源。</td></tr>
<tr>
<td>主机 OS 访问</td>
<td>选择启用或关闭 OS 权限，启用后，可以登录主机进行上传、下载等操作，可创建和管理主机账号。需注意，此项仅支持在创建独享集群时设置，创建后在控制台无法修改。</td></tr>
<tr>
<td>私有网络</td>
<td>设置独享集群的私有网络 VPC，如需重新创建新的 VPC，您可 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=1">新建私有网络</a>。</td></tr>
<tr>
<td>集群名</td>
<td>立即命名或创建后命名。名称仅支持数字，英文大小写字母、中文以及特殊字符_-./()[]（），且长度不能超过60。</td></tr>
</tbody></table>

## 后续操作
独享集群创建完成后，您需要添加主机，分配实例。具体操作，请参见 [新建 MySQL 独享集群主机](https://cloud.tencent.com/document/product/1322/76527) 和 [分配实例](https://cloud.tencent.com/document/product/1322/76528)。

