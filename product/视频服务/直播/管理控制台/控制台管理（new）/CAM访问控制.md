云直播通过 CAM 访问控制进行权限管理，以便于您管理账户的云直播域名、配置和数据信息。您可以创建、管理或销毁用户（组），将不同的接口权限授予子用户（组），以实现身份管理和策略控制。

当您使用 CAM 的时候，可以将策略与一个用户或一组用户关联起来，策略能够授权或者拒绝用户使用指定资源完成指定任务。

## 基本概念

- 主账号：注册的腾讯云账号。
- 子用户：通过主账号创建，完全归属于主账号。
- 协作者：拥有主账号的身份，被添加为当前主账号的协作者，为当前主账号的子账号之一。
- 用户组：为相同职能的一类用户创建的组，可为其关联策略，便于统一批量授权管理。

详细定义和权限请参见 [CAM 用户](https://cloud.tencent.com/document/product/598/13665)。

## 操作步骤
### 步骤1：新建子用户/用户组

主账号可以创建一个或多个子用户，以为其分配特定的角色和策略。子用户有确定的身份 ID 和身份凭证，可登录控制台并完成设置，同时具有 API 访问权限。登录腾讯云控制台，进入 [访问管理](https://console.cloud.tencent.com/cam/) 页面，可新建用户，如下图所示：
![](https://main.qcloudimg.com/raw/c26d014bd50f45e8ef88abff5b271af1.png)
详细步骤请参见访问管理 [子用户](https://cloud.tencent.com/document/product/598/13674) 和 [用户组](https://cloud.tencent.com/document/product/598/14985)。

### 步骤2：为用户/用户组添加策略

用户/用户组管理和策略管理页均可完成策略添加和授权，详细请参见 [授权管理](https://cloud.tencent.com/document/product/598/10602)，简述如下：

<dx-tabs>
::: 方法一：用户/用户组添加策略
进入用户/用户组页面，选择需添加策略的用户/用户组。
- 单击左侧的 **用户**>**用户列表**，选择需添加策略的用户/用户组，单击其右侧的 **授权**，选中相应的直播策略，单击 **确定** 即可添加成功。
![](https://main.qcloudimg.com/raw/0434625d9983110ccd052e5659465150.png)
- 单击左侧的 **用户**>**用户列表** 或 **用户组**，单击需添加策略的用户/用户组名称进入详情页。单击 **关联策略**，选中相应的直播策略，单击 **确定** 即可添加成功。
![](https://main.qcloudimg.com/raw/bf79df2fa859bed9867c4df37830f748.png)
:::
::: 方法二：策略添加关联用户/用户组
单击左侧的 **策略**，选择需添加的策略，单击操作列表中的 **关联用户/组**，选中需授权的用户，单击 **确定** 即可添加成功。
![](https://main.qcloudimg.com/raw/bcecf5b50a67e67e282b9a0f7c8232bc.jpg)

:::
</dx-tabs>

#### 可添加的策略
- **添加系统预设策略**：通过左侧边栏进入策略页面，可查询当前所有的策略信息。
   - 云直播系统预设策略为 [QcloudLIVEFullAccess](https://console.cloud.tencent.com/cam/policy/detail/9545933&QcloudLIVEFullAccess&2)（全读写策略）和 [QcloudLIVEReadOnlyAccess](https://console.cloud.tencent.com/cam/policy/detail/13346800&QcloudLIVEReadOnlyAccess&2)（只读策略）。
   - 若需使用标签，需授权 [QcloudTAGFullAccess](https://console.cloud.tencent.com/cam/policy/detail/1592575&QcloudTAGFullAccess&2) （标签（TAG）全读写访问策略）。
   - 若需使用实时日志，需授权 [QcloudCamFullAccess](https://console.cloud.tencent.com/cam/policy/detail/596169&QcloudCamFullAccess&2) （用户与权限（CAM）全读写访问权限策略）。
- **添加自定义策略**：进入策略页面，单击 **新建自定义策略**，选择 **按策略生成器创建**，详细请参见 [自定义策略](https://cloud.tencent.com/document/product/598/10601)。
>? 目前云直播部分接口已支持资源级授权，具体接口可参见 [API 鉴权规则](https://cloud.tencent.com/document/product/267/58612)。

	**操作示例：**若需将 **DescribeLiveDomains 查询域名列表** 接口授权给子用户，且仅可用于指定域名，按照下述步骤配置：
	1. 新建允许访问此接口的域名级策略，进入策略生成器创建策略页面，填写各输入项：
<table>
<tr><th>配置项</th><th>是否必填</th><th>说明</th></tr>
<tr>
<td>效果</td><td>是</td><td>选择 <b>允许</b></td>
</tr><tr>
<td>服务</td><td>是</td><td>选择 <b>云直播</b></td>
</tr><tr>
<td>操作</td><td>是</td><td>选择 <b>DescribeLiveDomains 查询域名列表</b></td>
</tr><tr>
<td>资源</td><td>是</td>
<td>选择全部资源或您要授权的特定资源<ul style="margin:0"><li>授权粒度为操作级、服务级的云产品<b>不支持填写具体资源六段式，选择全部资源即可</b>。</li><li>授权粒度为资源级的云产品，可选择特定资源，资源描述方式请参见 <a href="https://cloud.tencent.com/document/product/598/10588">支持 CAM 的产品</a> 中对应产品的访问管理指南文档。云产品支持的授权粒度请参见 <a href="https://cloud.tencent.com/document/product/598/10588">支持 CAM 的产品</a> 中的授权粒度。</li></ul></td>
</tr><tr>
<td>条件</td><td>否</td>
<td>设置上述授权的生效条件，输入需授权的来源 IP，仅当请求来自指定 IP 地址范围内时才允许访问指定操作。还可添加其他条件对策略进一步约束，详细请参见 <a href="https://cloud.tencent.com/document/product/598/10608">生效条件</a>。</td>
</tr></table>
<img src="https://main.qcloudimg.com/raw/23fc298516b7ef5179e6784c14a5ffff.png">
> ! 若要支持多个服务的手段，可单击 **添加权限**，继续添加多个授权声明，对另外的服务进行授权策略配置。
	2. 单击 **下一步** 即可生成该策略。策略生成后，通过上述两种方法关联用户/用户组即可。
![](https://main.qcloudimg.com/raw/f4fe29cf6da885ca6f0ae738882a7388.png)


### 步骤3：子账号使用
使用子账号身份（主账号创建的子账号 ID 和密码），调用已授权的 API 接口（例如：“查询域名列表”等），可以获取相应的云直播信息（例如：该账号下的所有域名）。

