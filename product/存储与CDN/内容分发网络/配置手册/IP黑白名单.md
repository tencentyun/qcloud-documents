CDN 为您提供了 IP 黑白名单配置功能，您可以根据业务需要对用户请求的源 IP 配置过滤策略，帮助您解决恶意 IP 盗刷、攻击等问题。

## 配置指引
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧目录中，单击【域名管理】，进入管理页面。
2. 在列表中，找到您需要编辑的域名所在行，单击操作栏中【管理】。
![img](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
3. 单击【访问控制】选项卡，可以在IP 黑白名单配置模块进行配置。默认情况下，IP 黑白名单未启用，无黑 / 白名单。
![img](https://main.qcloudimg.com/raw/67233e90db977ef23f981ced126f14e1.png)
	- IP 黑名单、白名单二者不兼容，同一时间只能生效一种类型。黑名单最多可输100条，白名单最多可输入50条，以换行符相隔，一行输入一个。
	- 目前仅支持如下格式的网段：/8、/16、/24、/32，其他网段格式暂不支持。当 IP 黑名单、白名单输入内容均为空时，表示当前未开启 IP 黑白名单功能。

### 白名单配置
1. 单击开启 **IP 黑白名单**，默认选中【IP 白名单】，可进行 IP 白名单配置。
   在输入框中输入名单并提交，即可开启 IP 白名单功能，仅当客户源 IP 匹配列表中的 IP 或 IP 段时，访问能够正常返回所请求的内容，其他请求均直接返回403。
![img](https://main.qcloudimg.com/raw/7a3c457c4448a8c10aedd6feb399af05.png)
2. 配置完成后，开关为开启状态，下方显示正在生效的 IP 白名单配置信息。单击【编辑】可更改配置信息。
![img](https://main.qcloudimg.com/raw/31c725a85d339d28f117a9e60a1b644d.png)
3. 关闭 **IP 黑白名单**开关后，下方的配置信息失效，即 IP 黑白名单未启用。可再次手动开启。
![img](https://main.qcloudimg.com/raw/690f14a3823b4e09897b792a4a7c91f0.png)

### 黑名单配置

1. 单击开启 **IP 黑白名单**，选中【IP 黑名单】，可进行黑名单配置。
   在下方输入框中输入名单并提交后，即开启了 IP 黑名单功能，当客户源 IP 匹配列表中的 IP 或 IP 段时，访问直接返回403，其他访问能够正常返回所请求内容。
![img](https://main.qcloudimg.com/raw/5df321c78a59f19125634230dee84a42.png)
2. 配置完成后，开关为开启状态，下方显示正在生效的 IP 黑名单配置信息。单击【编辑】可更改配置信息。
![img](https://main.qcloudimg.com/raw/bb9068501bd29d7f16309c738f1c537d.png)
3. 关闭 **IP 黑白名单**开关后，下方的配置信息失效，即 IP 黑白名单未启用。可再次手动开启。
![img](https://main.qcloudimg.com/raw/d1f877a9f0675838e5a14852fea2f6a9.png)

## 配置案例
若域名`www.test.com`的 IP 黑白名单配置如下：
![img](https://main.qcloudimg.com/raw/36f95d220f4bb2804f7bdd3b6e5d9424.png)
则：
- IP 为 `1.1.1.1`的用户访问资源 `http://www.test.com/1.jpg`，匹配白名单，正常返回内容。
- IP 为`2.2.2.2` 的用户访问资源 `http://www.test.com/1.jpg`，未匹配白名单，返回403。
