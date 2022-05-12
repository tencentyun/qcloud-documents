## 步骤1： 控制台登录访问控制授权
在创建子用户/协作者之后，即可在访问管理-[用户列表](https://console.cloud.tencent.com/cam) 页面单击**用户名**，进入用户详细信息中禁止或启用当前用户的控制台访问。
>!被禁止访问控制台的子用户/协作者，将无法登录当前账号的腾讯云控制台；协作者仍可登录其账号的腾讯云控制台，当前账号授权并不影响协作者腾讯云账号主体的使用。

## 步骤2：API 访问（编程访问）控制授权
您可以参考 [访问管理-主账号访问密钥管理](https://cloud.tencent.com/document/product/598/40488) 和 [访问管理-子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140) 文档，配置、管理 API 访问密钥。
>!您的 API 密钥代表您的账号身份和所拥有的权限，**等同于登录密码**，切勿泄露他人。


## 步骤3：授权子用户/协作者
### 内容安全产品授权
CAM 可以为子用户/协作者赋予特定内容安全服务的访问权限，配合访问方式授权管理（控制台/API 访问），实现精细化权限管理。

#### 策略授权流程
1. 通过控制台登录主账号或拥有管理员权限的子用户/协作者，进入 [访问管理-用户列表](https://console.cloud.tencent.com/cam) 页面。
2. 在用户列表页面，选择要授权的子用户/协作者，单击**授权**，弹出关联策略页面。
![](https://main.qcloudimg.com/raw/cb14a1d7e3e70778cac75d997d969fd8.png)
3. 在关联策略页面，根据需求配置子用户/协作者内容安全产品的访问权限。
>?目前支持音、视、图、文内容安全服务各个产品的读写权限配置，可配置权限为：**全读写/只读**。
>
![](https://main.qcloudimg.com/raw/836ba7c5732d8b47a84302e8fe1dba3f.png)
4. 单击**确定**，完成内容安全产品的访问权限配置。

#### 内容安全 CAM 策略说明
各个内容安全产品对应的预设策略如下表：

<table>
<thead>
<tr>
<th><strong>产品名称</strong></th>
<th><strong>预设策略</strong></th>
<th><strong>权限说明</strong></th>
</tr>
</thead>
<tbody><tr>
<td rowspan= 2>文本内容安全</td>  
<td>QcloudTMSFullAccess</td>
<td>全读写访问权限</td>
</tr>
<tr>
<td>QcloudTMSReadOnlyAccess</td>
<td>只读访问权限</td>
</tr>
<tr>
<td rowspan= 2>图片内容安全</td>
<td>QcloudIMSFullAccess</td>
<td>全读写访问权限</td>
</tr>
<tr>
<td>QcloudIMSFullAccess</td>
<td>只读访问权限</td>
</tr>
<tr>
<td rowspan= 2>音频内容安全</td>
<td>QcloudAMSFullAccess</td>
<td>全读写访问权限</td>
</tr>
<tr>
<td>QcloudAMSReadOnlyAccess</td>
<td>只读访问权限</td>
</tr>
<tr>
<td rowspan= 2>视频内容安全</td>
<td>QcloudVMFullAccess</td>
<td>全读写访问权限</td>
</tr>
<tr>
<td>QcloudVMReadOnlyAccess</td>
<td>只读访问权限</td>
</tr>
</tbody></table>


上述预设策略可用于给子用户/协作者关联相应内容安全服务不同的访问权限，将预设策略按照 [访问管理-授权管理](https://cloud.tencent.com/document/product/598/10602) 所述的步骤，分配给想要配置的用户/用户组，该用户/用户组即可根据策略授予的权限，访问或使用对应的内容安全服务。

### 注意事项
默认情况下，主账号是资源的拥有者，拥有其名下所有资源的访问权限，子用户/协作者没有任何资源的访问权限；**资源创建者不自动拥有所创建资源的访问权限**，需要资源拥有者进行授权。

策略是用于定义和描述一条或多条权限的语法规范；分为**预设策略**和**自定义策略**。
>?
>- 预设策略：用户高频使用的一些常见权限集合，如超级管理员、资源全读写权限等。操作对象范围广，操作粒度粗。预设策略为系统预设，不可被用户编辑。
>- 自定义策略：用户创建的更精细化的描述对资源管理的权限集合，允许作细粒度的权限划分，可以差异化权限管理需求。

设置用户权限共有3种方式：从策略列表中选取策略关联、复用现有用户策略和添加至组获得随组权限。
- 关于如何创建自定义策略，敬请参考 [访问管理-创建自定义策略](https://cloud.tencent.com/document/product/598/37739)。
- 关于如何为用户/用户组配置策略，敬请参考 [访问管理-授权管理](https://cloud.tencent.com/document/product/598/10602) 。

## 步骤4 CAM 授权管理配置建议
访问管理功能需要有效的配置和持续的管理才能够最大化地发挥效能。关于CAM访问管理配置的相关安全建议，敬请参见 [访问管理-安全管理策略](https://cloud.tencent.com/document/product/598/10592) 文档。
