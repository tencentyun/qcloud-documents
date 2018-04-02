> CDN 为您提供了 IP 黑白名单配置功能，您可以根据业务需要对用户请求的源 IP 配置过滤策略，帮助您解决恶意 IP 盗刷、攻击等问题。

## 配置指引

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/1f2cb594cd614b62b589cb20a20ed362/basic-config-1.png)
单击【访问控制】，您可以看到 **IP 黑白名单配置** 模块：
![](https://mc.qcloudimg.com/static/img/e996fbd8be4168c3a8cb6bf1f4f0d403/ip-config-1.png)

默认情况下，IP 黑白名单未启用，无黑/白名单。IP 黑名单、白名单二者不兼容，同一时间只能生效一种类型，黑名单最多可输 100 条，白名单最多可输入 50 条，以换行符相隔，一行输入一个。

目前仅支持如下格式的网段：/8、/16、/24、/32，其他网段格式暂不支持。当 IP 黑名单、白名单输入内容均为空时，表示当前未开启 IP 黑白名单功能。

### 白名单配置

单击【编辑】按钮，选中 **IP 白名单**，可进行白名单配置：
![](https://mc.qcloudimg.com/static/img/a554e348cb7e797ff86071b799feae34/ip-config-2.png)

在下方输入框中输入名单并提交后，即开启了 IP 白名单功能，仅当客户源 IP 匹配列表中的 IP 或 IP 段时，访问能够正常返回所请求的内容，其他请求均直接返回 403。 
### 黑名单配置

单击【编辑】按钮，选中 **IP 黑名单**，可进行黑名单配置。
![](https://mc.qcloudimg.com/static/img/5079e665e5c945cb17719872f0afedeb/ip-config-3.png)

在下方输入框中输入名单并提交后，即开启了 IP 黑名单功能，当客户源 IP 匹配列表中的 IP 或 IP 段时，访问直接返回 403，其他访问能够正常返回所请求内容。 

## 配置案例

若域名```www.test.com``` IP 黑白名单配置如下：![](https://mc.qcloudimg.com/static/img/9ccf196039805cc26975919d51c2dc1f/ip-config-4.png)

IP 为 ```1.1.1.1``` 的用户访问资源 ```http://www.test.com/1.jpg```，匹配白名单，正常返回内容；IP 为```2.2.2.2``` 的用户访问资源 ```http://www.test.com/1.jpg```，未匹配白名单，返回 403。