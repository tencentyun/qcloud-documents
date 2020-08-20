![](https://main.qcloudimg.com/raw/71efa478610d0ba4ddb321221c6f21c5.png)                                      
## 步骤一：注册并实名认证

1. 打开 [腾讯云官网](https://cloud.tencent.com/)，右上角选择【免费注册】，使用任意一种注册方式注册即可。
2. 注册成功后，按照指引完成实名认证，详细认证流程请参见 [实名认证指引](https://cloud.tencent.com/doc/product/378/3629) 。   


## 步骤二：开通使用 IDaaS 服务

1. 登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，单击【开通使用】。
![](https://main.qcloudimg.com/raw/c9bf9aa61d5895b8414fbddcdf1321c5.png)
2. 设置企业信息。 
	- 门户 URL：即您企业用户访问应用程序的链接，以武汉大学为例，可以以英文名(Wuhan university)缩写 whu 命名。
	- 企业名：企业名称，中英文均可。
![](https://main.qcloudimg.com/raw/04b8fad4307c3264a6009d4e2e0b00bd.png)

 

## 步骤三：用户管理

1. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，单击左侧菜单栏【用户管理】。
2. 单击【添加用户】，有两种添加用户方法，您可以根据实际情况选择添加方法。
![](https://main.qcloudimg.com/raw/93fe9c2fbf6eb31a51995817ca103e15.png)

### 从本地表格导入用户
1. 单击【导入模板】下载，根据模版规则填写用户信息。
![](https://main.qcloudimg.com/raw/3df472afb1d63ff8e95651e1d423d7bd.png)
> !手机和邮箱不能同时为空，且唯一。所属组上下级组用“/”分割开，企业名称/部门A/组A。
>
 以武汉大学为例，用户 ID 为学号（唯一），所属组为“武汉大学/所属学部/所属院系/所属年级/所属班级”。上传成功后，组织架构会按此自动创建。
![](https://main.qcloudimg.com/raw/3912cb7e326cfe494403d7a176b56c42.png)
2. 填写完毕并保存后，单击【选择文件】，上传表格。
3. 为用户设置登录密码。
管理员可选择“自动生成密码”或“自定义密码”为用户设置密码，密码将发送至用户手机或邮箱，用户首次登录都需要重置密码。
4. 单击【提交】，将开始导入用户。
![](https://main.qcloudimg.com/raw/22812c744fd780d369931fda083b78c0.png)
若导入成功，则完成用户添加。
![](https://main.qcloudimg.com/raw/d6bc09a8ca09a7b63471a7f1823df3f2.png)
若导入失败，可单击【下载失败列表】，查看失败原因。
![](https://main.qcloudimg.com/raw/161e4707c938269e2b2a58c3c705e453.png)
   
### 在线创建用户
1. 填写用户 ID、姓名、手机等基本信息。
	- 用户 ID 仅支持数字、小写英文字母、符号 `（@._-）`，且不能以符号开头。
	- 姓名仅支持字母、数字、中文及部分符号，如 `@.-()（）《》空格`，长度64字符内。
	- 手机和邮箱不能同时为空。
	- 单次最多创建10个用户。
2. 为用户设置微信登录，登录密码。
登录密码：管理员可选择“自动生成密码”或“自定义密码”为用户设置密码，密码将发送至用户手机或邮箱，用户首次登录都需要重置密码。
以武汉大学为例，用户 ID 即为学号，姓名、手机与邮箱如实输入，手机和邮箱不能同时为空，登录方式选择自动生成密码。
![](https://main.qcloudimg.com/raw/a0591022e05bef1ff9a34d07c52a00f8.png)
3. 为用户设置用户组。
以武汉大学赵美同学为例，她是哲学学院2016级本科1班学生，武汉大学下没有任何组织架构，需要在左下角【快速创建组】，创建哲学学院-2016级本科-1班，成功后如下图。勾选并选择完成。
![](https://main.qcloudimg.com/raw/661b51dba6a9f7fe36035db02adceefe.png)   
>!组织架构也可以在添加用户前创建，但如果使用表格添加用户，**所属组**一列一定要与创建的组织架构保持一致。
>
所添加用户的手机或邮箱，收到的短信或邮件如下，用户可以在登录地址里用户ID和密码访问应用。
![](https://main.qcloudimg.com/raw/af161ff57192546660c722d1670f9a91.png)
![](https://main.qcloudimg.com/raw/f12deeaa118d4661da9862190c453f6b.png)
  

 

 

## 步骤四：应用管理

### 新建应用
管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，左侧菜单栏选择【应用管理】>【新建应用】，在本实例中，应用为腾讯云大学，即选择【库应用程序】>【腾讯云】，应用名称设置为腾讯云大学，单击【提交】。
![](https://main.qcloudimg.com/raw/5c45535c602c190cf7e63fb9d1da9566.png)

### 应用配置
1. 下载腾讯云 IDaaS 元数据文件 URL 备用。
![](https://main.qcloudimg.com/raw/ab283123cdb8d5626ac53905cba404ed.png)
2. 应用程序 SAML 配置
修改【应用程序 ACS URL】，变为您希望用户通过 IDaaS 单击【腾讯云大学】应用后跳转到的界面。
以武汉大学为例，例如要跳转到`https://cloud.tencent.com/edu`，使用转译工具转译为`https%3A%2F%2Fcloud.tencent.com%2Fedu`，则修改应用程序 ACS URL 修改为`https://cloud.tencent.com/login/saml?s_url=https%3A%2F%2Fcloud.tencent.com%2Fedu`。
![](https://main.qcloudimg.com/raw/6c338504248043f8ff084f8ebc38b738.png)

### 配置属性
1. 管理员用新窗口登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，左侧菜单栏选择【身份提供商】。
2. 单击【新建身份提供商】。**提供商名称**用户自行取名。**元数据文档**选择腾讯云 IDaaS 元数据信息处下载好的 IDaaS 元数据文件上传。单击【下一步】，确认无误后单击【完成】。
![](https://main.qcloudimg.com/raw/1db75aa54f25ad38f2239ae5f8304568.png)
以武大为例，此处创建了提供商 whu，成功后如下图所示。
![](https://main.qcloudimg.com/raw/fc599c2fed72ab03ebb7f8547035a640.png)
3. 左侧菜单栏选择【角色】>【新建角色】。
4. 选择角色载体为**身份提供商**。**身份提供商**选择上一步创建的提供商（whu），**控制台访问**勾选允许当前角色访问控制台，单击【下一步】。
![](https://main.qcloudimg.com/raw/c7b1edd9012498302d2258afceffd4f6.png)
5. 配置角色策略，为角色配置权限，单击【下一步】。
本例中即为武汉大学的学生赋予权限，只需学生可以访问腾讯云大学应用即可，此处无需勾选策略。
![](https://main.qcloudimg.com/raw/b4b0c00c1f32f2d9934ef4293542952a.png)
6. 设置角色名称，单击【完成】。身份验证后，角色创建成功。
以武大为例，此处创建角色 whu-student。
![](https://main.qcloudimg.com/raw/9dcc1ea4f62098b3cb121a377c354ad7.png)
![](https://main.qcloudimg.com/raw/342e956be7e904c2b624faa5fdbb35a7.png)
7. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，在【应用管理】>【配置属性】中，单击完善信息右侧【编辑】，在弹窗中补充信息。
![](https://main.qcloudimg.com/raw/5611e54490a0921eb365970df969b04a.png)
AccountID 为腾讯云账号 ID，输入本账号 ID 即可，可前往账号信息查看。
![](https://main.qcloudimg.com/raw/81e137ebcf88ca20a679bed398ff9c84.png)
RoleName 为第6步中创建的角色名（whu-student）。
IdPName 为第4步中创建的身份提供商名称（whu），补充完整后单击【确定】。
![](https://main.qcloudimg.com/raw/f153237f2494bfe653f50a113b1a3736.png)

### 关联用户/组
1． 单击【关联用户/组】，首先关联一个测试用户，单击【确定】，进行测试步骤。
2． 若测试通过，再关联其他用户。以武大为例，希望人文科学学部-哲学学院-2016级本科生同学可以通过 IDaaS 访问腾讯云大学，勾选人文科学学部-哲学学院下的子组2016级本科，单击【确定】。
![](https://main.qcloudimg.com/raw/fc2b7ac19914e853f374fb89897de6dd.png)
   


## 步骤五：测试

1. 打开测试用户短信或邮件中登录地址，即步骤二中设置的门户 URL：`https://whu.cloudidaas.com`。
2. 以测试用户短信或邮件中 ID、密码登录并重设密码。
3. 登录成功后进入【我的应用程序】，单击应用后可跳转到步骤四中设置的【应用程序 ACS URL】，即配置成功。
本例中，单击【腾讯云大学】可跳转到腾讯云大学网页，即配置成功，测试完毕。
![](https://main.qcloudimg.com/raw/066c4d4265b53b99bb16579539f03420.png)
4. 测试成功后，即可关联全部用户。

 

 
