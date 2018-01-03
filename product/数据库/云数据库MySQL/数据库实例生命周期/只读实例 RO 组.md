## 简介
[腾讯云 CDB for MySQL](https://cloud.tencent.com/product/cdb-overview) 支持用户创建一个或多个只读实例组成只读实例 RO 组，适用于用户的读写分离和一主多从应用场景，可显著提高用户数据库的读负载能力。
>**注意：**
> - 创建只读实例之前需要先创建云数据库主实例。请参考腾讯云 CDB for MySQL 产品文档 [购买与续费](/doc/product/236/5160) 中的步骤新建云数据库主实例。
> - 使用腾讯云 CBD for MySQL 之前，需要对数据库进行初始化。请参考腾讯云 CDB for MySQL 产品文档 [初始化 MySQL 数据库](/doc/product/236/3128) 中的步骤初始化 MySQL 数据库。

## 操作说明
### 1. 创建只读实例
1.1 在 [关系型数据库](https://console.cloud.tencent.com/cdb) 页面中，选择需要创建只读实例 RO 组的云数据库，单击【管理】，进入云数据库主实例管理界面。
![](//mc.qcloudimg.com/static/img/09c0db073e75d30c287de0f10ffed935/image.png)
1.2 在管理界面中，点击【添加只读实例】，进入只读实例管理界面。
![](//mc.qcloudimg.com/static/img/ac1a151fe0079fac79b2901a5f9283bc/image.png)
1.3 在只读实例管理界面中，单击【新建】，创建只读实例。
![](//mc.qcloudimg.com/static/img/fa84be50d87cd09d0c7f25f16b31ffca/image.png)
1.4 在弹出的购买页面中，选择云数据库只读实例的相应配置。核对无误后单击【立即购买】购买只读实例。
- 指定 RO 组。

 <table>
  <tr>
    <th width="25%">指定 RO 组</th>
    <th width="75%">说明</th>
  </tr>
  <tr>
    <td>不指定（系统分配）</td>
    <td>若一次购买多个实例，将为每个实例分配一个独立的 RO 组。权重分配方式默认为系统自动分配。</td>
  </tr>
  <tr>
    <td>新建 RO 组</td>
    <td>新建一个 RO 组，若一次购买多个实例，将都分配至这个 RO 组。权重分配方式默认为系统自动分配。</td>
  </tr>
  <tr>
    <td>指定 RO 组</td>
    <td>指定一个 RO 组，若一次购买多个实例，将都分配至这个 RO 组。权重分配方式与 RO 组设置相同：如果 RO 组设置为系统自动分配，则根据购买规格自动添加 RO 组；如果为自定义分配，则默认权重为零。<b>由于同一 RO 组内网地址相同，因此若是 VPC 网络将共享同一个安全组设置。若指定 RO 组，则在购买时无法再自定义安全组。</b></td>
  </tr>
</table>

 ![](//mc.qcloudimg.com/static/img/5db6834345e4087bff22e6c0715eb033/image.png)
 
- 选择实例规格和所需的硬盘。
![](//mc.qcloudimg.com/static/img/ab288476b0ad541d6064d7ef42209836/image.png)
如果指定 RO 组选项配置为 **新建 RO 组**，则需要在购买界面中填写新建的 RO 组的以下基本信息。
- 设置 RO 组名称：RO 组名称不要求唯一。支持长度小于 60 的中文、英文、数字、`-`、`_`、`.` 。
- <span id="rid-of-delay">延时超限剔除：是否启动剔除策略。被剔除的实例权重自动设置为 0，且新增实例状态：停服同步中。只读实例延迟超过阀值被剔除会向用户发出警告。同时，不管实例是否设置延时超限剔除，当只读实例故障，都会在保证最少保留实例数的基础上，剔除、修复实例，并在数据确认完整后，重新加入到RO组。</span>
- 延迟阀值：为只读实例设置延迟超限阀值，超过阀值可设置剔除。此项必须设置。无论是否启用剔除策略，延迟超限都会告警。
- 最少保留实例数：组内需要保证的实例下限。若现有只读实例数低于此下限则超限不再自动设置权重为 0。此项必须设置，且最小为 0。
![](//mc.qcloudimg.com/static/img/06cf1b511761c3fb35fd08a504af3750/image.png)

1.5 进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，找到刚才创建的实例类型为 **只读实例** 的实例，则表示只读实例创建成功。
![](//mc.qcloudimg.com/static/img/c43acd917b990016bb418220ee5e18e3/image.png)

### 2. 配置只读实例 RO 组
在只读实例 RO 组的配置界面，可以配置只读实例 RO 组的名称、延时超限策略、延时阈值、最少保留实例、读权重等基本信息，具体的操作步骤如下。
2.1 在 [云数据库控制台](https://console.cloud.tencent.com/cdb)，选择需要设置只读实例 RO 组的云数据库主实例，单击【管理】，进入云数据库主实例管理界面。
![](//mc.qcloudimg.com/static/img/a4c91d09c83f1e9d6738610ba4d81933/image.png)
2.2 在云数据库主实例管理界面，单击【只读实例】，进入只读实例 RO 组管理界面。 
![](//mc.qcloudimg.com/static/img/edfc8913abe2154244edbb36d01b6fe0/image.png)
2.3 在只读实例 RO 组管理页面，单击【配置】，进入只读实例 RO 组配置界面。
![](//mc.qcloudimg.com/static/img/96c1ece808557044fa9f788bf0a36d04/image.png)
2.4 在只读实例 RO 组配置界面，可以对只读实例 RO 组进行详细配置。
![](//mc.qcloudimg.com/static/img/2857c2fd73a6750e32c10667cd0f1f76/image.png)
- RO 组名称：RO 组名称不要求唯一。支持长度小于 60 的中文、英文、数字、`-`、`_`、`.` 。
- 实例延时超限剔除：是否启动剔除策略。被剔除的实例权重自动设置为 0，且新增实例状态：停服同步中。只读实例延迟超过阀值被剔除会给用户提供警告。
- 延迟阀值：为只读实例设置延迟超限阀值，超过阀值可设置剔除。此项必须设置。无论是否启用剔除策略，延迟超限都会告警。
- 最少保留实例数：组内需要保证的实例下限。若现有只读实例数低于此下限则超限不再自动设置权重为 0。此项必须设置，且最小为 0。
- 读权重分配：RO 组支持系统自动分配权重和自定义权重两种权重设置方式。权重输入范围为 0-100，且必须是整数。系统自动设置实例的读权重值列表：
<table>
  <tr>
    <th>配置类型</th>
    <th>数据库类型</th>
    <th>实例规格</th>
    <th>权重</th>
  </tr>
  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 1000MB</td>
		<td>1</td>
  </tr>
  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 2000MB</td>
		<td>1</td>
  </tr>
  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 4000MB</td>
		<td>2</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 8000MB</td>
		<td>2</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 12000MB</td>
		<td>4</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 16000MB</td>
		<td>4</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 24000MB</td>
		<td>8</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 32000MB</td>
		<td>8</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 48000MB</td>
		<td>10</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 64000MB</td>
		<td>12</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 96000MB</td>
		<td>14</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 128000MB</td>
		<td>16</td>
  </tr>
	  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 244000MB</td>
		<td>26</td>
  </tr>  <tr>
    <td>高 IO 版</td>
    <td>MySQL 实例</td>
		<td>内存 488000MB</td>
		<td>50</td>
  </tr>
</table>
- 重新负载均衡：
	- 关闭重新负载均衡时，修改权重时仅对新增负载生效，不改变原长连接所访问的只读实例，不会引起数据库闪断。
	- 开启重新负载均衡时，数据库会有秒级闪断来断开所有连接，新增连接将按照设置的权重均衡负载。

> **说明：**
> - RO 组内只读实例可使用不同规格，读流量权重可设置。
> - 同一 RO 组内只读实例可以支持不同到期时间和计费方式。

### 3. 销毁和删除只读实例 RO 组
- RO 组不提供手动删除功能。
- RO 组随着组内最后一个只读实例被彻底销毁而自动删除。
- 不支持保留空 RO 组。
