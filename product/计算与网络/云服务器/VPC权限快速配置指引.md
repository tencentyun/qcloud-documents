
本文提供三种授权方式供您参考，其中：
- **方式1**：采用预设策略进行授权，授予用户 QcloudVPCReadOnlyAccess-私有网络 VPC 只读访问权限。
- **方式2**：采用预设策略进行授权，授予用户 QcloudVPCFullAccess-私有网络 VPC 全读写访问权限。
主账号默认拥有以上预设策略，您可单击策略名称以查看策略详情。
- **方式3**：若方式1及方式2所授予的“预设策略”不符合您的需求，则可以通过新建“自定义策略”对本次涉及到的接口进行授权，配置方式请参见 [方式3：新建自定义策略](#type3)。如需了解更多自定义策略信息，则请参考 [创建自定义策略](https://cloud.tencent.com/document/product/598/37739)。

## 操作步骤

### 方式1： 授予用户私有网络 VPC 只读访问权限
1. 登录访问管理控制台，选择左侧导航栏的【[策略](https://console.cloud.tencent.com/cam/policy)】。
2. 选择列表上方的【预设策略】，在右上角的搜索框内输入 `QcloudVPCReadOnlyAccess` 后，单击 <img src="https://main.qcloudimg.com/raw/bc0a065148f0e50a739e17f4f238ae37.png" style="margin:-3px 0px"> 进行搜索。
3. 单击 `QcloudVPCReadOnlyAccess` 所在行右侧的【关联用户/组】。如下图所示：
![](https://main.qcloudimg.com/raw/4e92e7a1f1266b7e9d5901a3bd3205ad.png)
4. 在弹出的“关联用户/用户组”窗口中，勾选需添加的用户，并单击【确定】即可完成授权。

### 方式2： 授予用户私有网络 VPC 全读写访问权限
1. 登录访问管理控制台，选择左侧导航栏的【[策略](https://console.cloud.tencent.com/cam/policy)】。
2. 选择列表上方的【预设策略】，在右上角的搜索框内输入 `QcloudVPCFullAccess` 后，单击 <img src="https://main.qcloudimg.com/raw/bc0a065148f0e50a739e17f4f238ae37.png" style="margin:-3px 0px"> 进行搜索。
3. 单击 `QcloudVPCFullAccess` 所在行右侧的【关联用户/组】。如下图所示：
![](https://main.qcloudimg.com/raw/3785b599b78659f23da6e8ec66d66007.png)
4. 在弹出的“关联用户/用户组”窗口中，勾选需添加的用户，并单击【确定】即可完成授权。

### 方式3：新建自定义策略[](id:type3)
>?如方式1及方式2的预设策略不符合您的实际需求，则可参考本步骤，通过新建自定义策略的方式对本次涉及到的 DescribeSubnetEx 接口进行授权。如需了解更多自定义策略信息，则请参考 [创建自定义策略](https://cloud.tencent.com/document/product/598/37739)。


1. 登录访问管理控制台，选择左侧导航栏的【[策略](https://console.cloud.tencent.com/cam/policy)】。
2. 在“策略”页面中，单击【新建自定义策略】：
 1. 在“选择创建策略方式”窗口中，单击【按策略语法创建】。
 2. 在“选择策略模板”步骤中，选择“空白模板”，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/f173f35fae6e87849ba72f00941156ea.png)
 3. 在“编辑策略”步骤中，根据以下提示填写相关信息。
	   - **策略名称**：自定义策略名称，推荐使用 `DescribeSubnetEx`。
	   - **策略内容**：输入以下内容。
<pre style="color:white">
{
            "version": "2.0",
            "statement": [
              {
                "effect": "allow",
                "action": [
                  "vpc:DescribeSubnetEx"
                ],
                "resource": [
                  "*"
                ]
              }
            ]
}
</pre>
 4. 单击【完成】即可完成新建。	 
3. 在“策略”页面，选择刚创建的 `DescribeSubnetEx` 策略所在行右侧的【关联用户/组】。如下图所示：
![](https://main.qcloudimg.com/raw/7eeba36965c3986475b3805da4eb455e.png)
4. 在弹出的“关联用户/用户组”窗口中，勾选需添加的用户，并单击【确定】即可完成授权。
