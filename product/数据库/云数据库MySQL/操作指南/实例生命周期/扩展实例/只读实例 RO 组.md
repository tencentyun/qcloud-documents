## 操作场景
[腾讯云 TencentDB for MySQL](https://cloud.tencent.com/product/cdb-overview) 支持用户创建一个或多个只读实例组成只读实例 RO 组，适用于用户的读写分离和一主多从应用场景，可显著提高用户数据库的读负载能力。
>!
> - 创建只读实例之前需要先创建云数据库主实例。请参考腾讯云 TencentDB for MySQL 产品文档 [购买与续费](/doc/product/236/5160) 中的步骤新建云数据库主实例。
> - 使用腾讯云 TencentDB for MySQL 之前，需要对数据库进行初始化。请参考腾讯云 TencentDB for MySQL 产品文档 [初始化 MySQL 数据库](/doc/product/236/3128) 中的步骤初始化 MySQL 数据库。

## 操作步骤
### 创建只读实例 RO 组
1. 登录 [云数据库控制台](https://console.cloud.tencent.com/cdb/ )，实例列表中，选择需要创建只读实例 RO 组的云数据库，单击【管理】，进入云数据库主实例管理界面。
![](https://main.qcloudimg.com/raw/de03b9ef53dfd65e2666238c01c2e75e.png)
2. 在管理界面中，在【相关实例】内单击【添加只读实例】，进入只读实例管理界面。
![](https://main.qcloudimg.com/raw/4cce46acd744e72c674c45202ab6b903.png)
3. 在只读实例管理界面中，单击【新建】，创建只读实例。
![](https://main.qcloudimg.com/raw/1aaf8c209fa7258e2df7d57844edda04.png)
4. 在弹出的购买页面中，选择云数据库只读实例的相应配置。核对无误后单击【立即购买】购买只读实例。
	- 指定 RO 组。

 <table>
  <tr>
    <th width="25%">指定 RO 组</th>
    <th width="75%">说明</th>
  </tr>
  <tr>
    <td>不指定（系统自动分配）</td>
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

 ![](https://main.qcloudimg.com/raw/50bdd64f0d488b1041bf0f6385604b6d.png)
 
	- 选择实例计费模式
	只读实例目前支持两种计费模式：包年包月、按量计费
 ![](https://main.qcloudimg.com/raw/111b1cd606e811c94c49d8756c47f3b0.png) 
 
	- 选择实例规格和所需的硬盘。
![](https://main.qcloudimg.com/raw/83e46e7f30ca7871fe408ce38823b664.png)
	>! 如果指定 RO 组选项配置为 **新建 RO 组**，则需要在购买界面中填写新建的 RO 组的以下基本信息。
	
  	- 设置 RO 组名称：RO 组名称不要求唯一。支持长度小于 60 的中文、英文、数字、`-`、`_`、`.` 。
 	- 延时超限剔除：是否启动剔除策略。被剔除的实例权重自动设置为 0，且新增实例状态：停服同步中。若只读实例延迟超过阈值被剔除会向用户发出警告，且实例状态为停服同步中、权重为0，当只读实例延迟时间小于阈值时会重新加入到RO组。同时，不管实例是否启用延时超限剔除功能，当只读实例故障被剔除后，待实例修复也会重新加入到RO组。
	 - 延迟阈值：为只读实例设置延迟超限阈值，超过阈值的只读实例会被剔除RO组。
	 - 最少保留实例数：组内需要保证的实例下限数，若现有只读实例数小于等于此下限且延迟时间超过阈值，现有只读实例均不被剔除。
![](https://main.qcloudimg.com/raw/c6b2ffb4a9418ddcbc8a0a763dc5977b.png)

5. 进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，找到刚才创建的实例，状态可能为如下【发货中】。

![](https://main.qcloudimg.com/raw/00dbc2d51b1f9b6bdf9da804567d95d6.png)
6. 在发货成功后状态切换成【运行中】，并且【登录】按钮有如下提示，则表示只读实例创建成功。
![](https://main.qcloudimg.com/raw/20663e141678f8fabc3899feca375d53.png)


### 配置只读实例 RO 组
在只读实例 RO 组的配置界面，可以配置只读实例 RO 组的名称、延时超限策略、延时阈值、最少保留实例、读权重等基本信息，具体的操作步骤如下。
1. 在 [云数据库控制台](https://console.cloud.tencent.com/cdb)，选择需要设置只读实例 RO 组的云数据库主实例，单击【管理】，进入云数据库主实例管理界面。
![](https://main.qcloudimg.com/raw/de03b9ef53dfd65e2666238c01c2e75e.png)
2. 在云数据库主实例管理界面，单击【只读实例】，进入只读实例 RO 组管理界面。 
![](https://main.qcloudimg.com/raw/c17438bcdd3657c082fdc620155a2640.png)
3. 在只读实例 RO 组管理页面，单击【配置】，进入只读实例 RO 组配置界面。
![](https://main.qcloudimg.com/raw/dfd48756f7dcebe5c0e472d6185842f2.png)
4. 在只读实例 RO 组配置界面，可以对只读实例 RO 组进行详细配置。
![](https://main.qcloudimg.com/raw/b57a497ea11dbdb59a02e463302f8b99.png)
	- RO 组名称：RO 组名称不要求唯一。支持长度小于 60 的中文、英文、数字、`-`、`_`、`.` 。
	- 延时超限剔除：是否启动剔除策略。被剔除的实例权重自动设置为 0，且新增实例状态：停服同步中。若只读实例延迟超过阈值被剔除会向用户发出警告。
	- 延迟阈值：为只读实例设置延迟超限阈值，超过阈值的只读实例会被剔除RO组。
	- 最少保留实例数：组内需要保证的实例下限数，若现有只读实例数小于等于此下限且延迟时间超过阈值，现有只读实例均不被剔除。
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

>?
> - RO 组内只读实例可使用不同规格，读流量权重可设置。
> - 同一 RO 组内只读实例可以支持不同到期时间和计费方式。

### 销毁和删除只读实例 RO 组
- RO 组不提供手动删除功能。
- RO 组随着组内最后一个只读实例被彻底销毁而自动删除。
- 不支持保留空 RO 组。
