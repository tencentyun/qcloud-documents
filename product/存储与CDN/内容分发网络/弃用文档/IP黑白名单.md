CDN 为您提供了 IP 黑白名单配置功能，您可以根据业务需要对用户请求的源 IP 配置过滤策略，帮助您解决恶意 IP 盗刷、攻击等问题。

## 配置指引
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![img](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
2. 单击【访问控制】选项卡，可以在 IP 黑白名单配置模块进行配置。默认情况下，IP 黑白名单未启用，无黑 / 白名单。
![img](https://main.qcloudimg.com/raw/0ad78b7f997c766758807eb92340efcd.png)
	- IP 黑名单、白名单二者不兼容，同一时间只能生效一种类型。黑名单最多可输100条，白名单最多可输入50条，以换行符相隔，一行输入一个。
	- 目前仅支持如下格式的网段：/8、/16、/24，其他网段格式暂不支持。当 IP 黑名单、白名单输入内容均为空时，表示当前未开启 IP 黑白名单功能。

### 白名单配置
1. 单击【编辑】，默认选中【IP 白名单】，可进行 IP 白名单配置。
   在输入框中输入名单并提交，即可开启 IP 白名单功能，仅当客户源 IP 匹配列表中的 IP 或 IP 段时，访问能够正常返回所请求的内容，其他请求均直接返回403。
![img](https://main.qcloudimg.com/raw/d96fc3efbf3e8d22492f2abef5009ec3.jpg)
2. 配置完成后，开关为开启状态，下方显示正在生效的 IP 白名单配置信息。单击【编辑】可更改配置信息。
![img](https://main.qcloudimg.com/raw/b75819f595495f27117a5f0947bc6c26.png)
3. 关闭 **IP 黑白名单**开关后，下方的配置信息失效，即 IP 黑白名单未启用。可再次手动开启。
![img](https://main.qcloudimg.com/raw/852bd47704f7a8dff83af4aa74956161.png)

### 黑名单配置

1. 单击【编辑】，选中【IP 黑名单】，可进行黑名单配置。
   在下方输入框中输入名单并提交后，即开启了 IP 黑名单功能，当客户源 IP 匹配列表中的 IP 或 IP 段时，访问直接返回403，其他访问能够正常返回所请求内容。
![img](https://main.qcloudimg.com/raw/e15849cc11a69221e281a4f8c9e15624.jpg)
2. 配置完成后，开关为开启状态，下方显示正在生效的 IP 黑名单配置信息。单击【编辑】可更改配置信息。
![img](https://main.qcloudimg.com/raw/cd2fa0e9923cb6c88a49ed95b1398af9.png)
3. 关闭 **IP 黑白名单**开关后，下方的配置信息失效，即 IP 黑白名单未启用。可再次手动开启。
![img](https://main.qcloudimg.com/raw/0e1cd5c478cddb2890736be60e8ab55e.png)

## 配置案例
若域名`www.test.com`的 IP 黑白名单配置如下：
![img](https://main.qcloudimg.com/raw/03d21c419dce2dae111333d5e8b64025.jpg)
则：
- IP 为 `1.1.1.1`的用户访问资源 `http://www.test.com/1.jpg`，匹配白名单，正常返回内容。
- IP 为`2.2.2.2` 的用户访问资源 `http://www.test.com/1.jpg`，未匹配白名单，返回403。
