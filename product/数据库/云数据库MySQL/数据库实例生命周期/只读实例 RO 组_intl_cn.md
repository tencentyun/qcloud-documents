[腾讯云 CDB for MySQL](https://cloud.tencent.com/product/cdb-overview) 支持用户创建一个或多个只读实例组成只读实例 RO 组，以支持用户的读写分离和一主多从应用场景，可显著提高用户数据库的读负载能力。

## 1. 创建主实例
创建只读实例之前需要先创建云数据库主实例。如果已经创建云数据库主实例并初始化，请跳转至步骤 3 创建只读实例。
1.1 登录腾讯云 [管理控制台](https://console.cloud.tencent.com/)，将鼠标移至导航条中的【云产品】>【基础产品】>【数据库】单击【关系型数据库】，进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，单击【新建】按钮，进入云数据库 MySQL 购买界面。
![](//mc.qcloudimg.com/static/img/30ad113b94de202c67769b08128523dd/image.png)
1.2 在弹出的购买页面中，选择云数据库主实例的相应配置。       
- 选择所需的计费模式，支持包年包月和按量计费两种模式。（按量计费购买前需要实名认证，详见 <a href="https://cloud.tencent.com/document/product/378/3629" target="_blank">实名认证指引</a>）
- 选择地域和可用区。地域说明请参见 <a href="https://cloud.tencent.com/document/product/236/8458" target="_blank">地域和可用区</a>。
- 选择网络环境，支持基础网络和私有网络。基础网络和私有网络的区别请参见 <a href="https://cloud.tencent.com/document/product/213/5227" target="_blank">网络环境</a>。
- 选择实例规格和所需的硬盘。
- 选择数据复制方式。关于数据库实例复制方式的区别可参见 <a href="https://cloud.tencent.com/document/product/236/7913" target="_blank">数据库实例复制</a>。
- 选择数据库实例所属的项目，缺省设置为默认项目。
- 选择购买数量和时长，核对无误后单击【立即购买】。
- 费用详情请参见 <a href="https://cloud.tencent.com/document/product/236/5158" target="_blank">费用总览</a>。
![](//mc.qcloudimg.com/static/img/e1401535799aeb1204707da530d37f89/image.png)
> **注意：**
> 目前只读实例仅支持高IO版4000MB内存、100GB容量及以上规格的主实例。

## 2.  初始化主实例
通过此步骤对已经购买的 MySQL 数据库执行初始化操作。
2.1 在 [腾讯云控制台](https://console.cloud.tencent.com/) 的左上角，单击【云产品】菜单下的【关系型数据库】，进入数据库产品页面。
![](//mc.qcloudimg.com/static/img/511cad3621447b36d204b87bf83bb09f/image.png)
2.2 在关系型数据库页面中，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中要操作的状态为“**未初始化**” 的 MySQL 数据库实例。
![](//mc.qcloudimg.com/static/img/2256d49a17e08e5243f95c1804097c6c/image.png)
2.3 单击【初始化】对要操作的 MySQL 实例执行初始化。
![](//mc.qcloudimg.com/static/img/d7de05d1e3cea427c391072eebecba94/image.png)
2.4 配置初始化相关参数，然后单击【确定】开始初始化。初始化操作会重启实例，大概耗时 50 秒，请耐心等待。
- **支持的字符集：**选择 MySQL 数据库支持的字符集。
- **表名大小写敏感：**表名是否大小写敏感，默认为是。
- **自定义端口：**数据库的访问端口，默认为 3306。
- **root 账户密码：**新创建的 MySQL 数据库的用户名默认为 root，此处用来设置此 root 账户的密码。
- **确认密码：**再次输入密码。

![](//mc.qcloudimg.com/static/img/a1b69801dc18d284ef8b0f3ea777265b/image.png)
2.5 目标 MySQL 主实例的状态变为“**运行中**”，说明已初始化成功。
![](//mc.qcloudimg.com/static/img/5bc58fa06377190a29ef23d3784b9006/image.png)

## 3. 创建只读实例
3.1 在关系型数据库页面中，选择之前初始化成功的云数据库，单击【管理】，进入云数据库主实例管理界面。
![](//mc.qcloudimg.com/static/img/850a55d5b5c51a854f3b038276fce9c0/image.png)
3.2 在管理界面中，点击【添加只读实例】，进入只读实例管理界面。
![](//mc.qcloudimg.com/static/img/5b1c2de58ef8a0fbbec30a322340f27f/image.png)
3.3 在只读实例管理界面中，单击【新建】，创建只读实例。
![](//mc.qcloudimg.com/static/img/a3356a9115f34ac68ed5b538c27adf86/image.png) 
3.4 在弹出的购买页面中，选择云数据库只读实例的相应配置。核对无误后单击【立即购买】购买只读实例。
- 指定RO组。
<table>
  <tr>
    <th width="25%">指定 RO 组</th>
    <th width="75%">说明</th>
  </tr>
  <tr>
    <td>不指定（系统分配）</td>
    <td>若一次购买多个实例，将为每个实例分配一个独立的RO组。权重分配方式默认为系统自动分配。</td>
  </tr>
  <tr>
    <td>新建 RO 组</td>
    <td>新建一个 RO 组，若一次购买多个实例，将都分配至这个 RO 组。权重分配方式默认为系统自动分配。</td>
  </tr>
	  <tr>
    <td>指定 RO 组</td>
    <td>指定一个 RO 组，若一次购买多个实例，将都分配至这个 RO 组。权重分配方式与 RO 组设置相同：如果 RO 组设置为系统自动分配，则根据购买规格自动添加 RO 组；如果为自定义分配，则默认权重为零。</td>
  </tr>
</table>
- 选择实例规格和所需的硬盘。
![](//mc.qcloudimg.com/static/img/e12c53af50e5da4717971c835f6b7c52/image.png)
如果指定 RO 组选项配置为“**新建 RO 组**”，则需要在购买界面中填写新建的 RO 组的基本信息。
- 设置 RO 组名称：RO 名称不要求唯一。支持长度小于60的中文/英文/数字/"-"/"_"/"." 。
- 延时超限剔除：是否启动剔除策略。被剔除的实例权重自动设置为0，且新增实例状态：停服同步中。只读实例延迟超过阀值被剔除会向用户发出警告。
- 延迟阀值：为只读实例设置延迟超限阀值，超过阀值可设置剔除。此项必须设置。无论是否启用剔除策略，延迟超限都会告警。
- 最少保留实例数：组内需要保证的实例下限。若现有只读实例数低于此下限则超限不再自动设置权重为0。此项必须设置，且最小为0。

![](//mc.qcloudimg.com/static/img/3afb117591392e4e7e1d69a10b7976c2/image.png)
3.5 进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，找到刚才创建的实例类型为“**只读实例**”的实例，则表示只读实例创建成功。
![](//mc.qcloudimg.com/static/img/c9785571ba892afe730f45a9ed7dd48c/image.png)

## 4. 配置只读实例 RO 组
4.1 在 [云数据库控制台](https://console.cloud.tencent.com/cdb)，选择需要设置只读实例 RO 组的云数据库主实例，单击【管理】，进入云数据库主实例管理界面。
![](//mc.qcloudimg.com/static/img/6617bf48cdc9a3de82342543e05ee03f/image.png)
4.2 在云数据库主实例管理界面，单击【只读实例】，进入只读实例 RO 组管理界面。 
![](//mc.qcloudimg.com/static/img/83730fa97348eb5a11beaaf7ec4c8f5b/image.png)
4.3 在只读实例 RO 组管理页面，单击【配置】，进入只读实例 RO 组配置界面。
![](//mc.qcloudimg.com/static/img/d5e477a253afd98f251857f3bae398f5/image.png)
4.4 在只读实例 RO 组配置界面，可以对只读实例 RO 组进行详细配置。
![](//mc.qcloudimg.com/static/img/2f87d2f6a5b0e1ccd6c65ea16ae37bf3/image.png)
- RO 组名称：RO 名称不要求唯一。支持长度小于60的中文/英文/数字/"-"/"_"/"."。 
- 实例延时超限剔除：是否启动剔除策略。被剔除的实例权重自动设置为0，且新增实例状态：停服同步中。只读实例延迟超过阀值被剔除会给用户提供警告。
- 延迟阀值：为只读实例设置延迟超限阀值，超过阀值可设置剔除。此项必须设置。无论是否启用剔除策略，延迟超限都会告警。
- 最少保留实例数：组内需要保证的实例下限。若现有只读实例数低于此下限则超限不再自动设置权重为0。此项必须设置，且最小为0。
- 读权重分配：RO组支持系统自动分配权重和自定义权重两种权重设置方式。权重输入范围为0-100，且必须是整数。
系统自动设置实例的读权重值列表：

| 配置类型	| 数据库类型	| 实例规格	| 权重 |
|-------------|------------------|-----------------|-----------------|
| 高IO版	| MySQL实例	| 内存1000MB	| 1 |
| 高IO版	| MySQL实例	| 内存2000MB |	1 |
| 高IO版	| MySQL实例	| 内存4000MB	| 2 |
| 高IO版	| MySQL实例	| 内存8000MB	| 2 |
| 高IO版	| MySQL实例	| 内存12000MB	| 4 |
| 高IO版	| MySQL实例	| 内存16000MB	| 4 |
| 高IO版	| MySQL实例	| 内存24000MB	| 8 |
| 高IO版	| MySQL实例	| 内存32000MB	| 8 |
| 高IO版	| MySQL实例	| 内存48000MB	| 10 |
| 高IO版	| MySQL实例	| 内存64000MB	| 12 |
| 高IO版	| MySQL实例	| 内存96000MB	| 14 |
| 高IO版	| MySQL实例	| 内存128000MB	| 16 |
| 高IO版	| MySQL实例	| 内存244000MB	| 26 | 
| 高IO版	| MySQL实例	| 内存488000MB	| 50 |
- 重新负载均衡：如果关闭重新均衡负载，修改权重时仅对新增负载生效，不改变原长连接所访问的只读实例，不会引起数据库闪断。


> **说明：**
> - RO 组内只读实例可使用不同规格，读流量权重可设置。
> - 同一 RO 组内只读实例可以支持不同到期时间和计费方式。

## 5. RO 组的销毁和删除
- RO 组不提供删除功能。
- RO 组随着组内最后一个只读实例被彻底销毁而删除。
- 暂时不支持保留空RO组。
