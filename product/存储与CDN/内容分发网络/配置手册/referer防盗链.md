若您希望对业务资源的访问来源进行控制，CDN 为您提供了 referer 防盗链配置功能。通过对用户 HTTP Request Header 中 referer 字段的值设置访问控制策略，从而限制访问来源，避免恶意用户盗刷。
## 配置指引

1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![img](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
2. 单击【访问控制】选项卡，可在防盗链配置模块进行配置。默认情况下，防盗链未启用，无黑 / 白名单。
![img](https://main.qcloudimg.com/raw/56110bcf45df710945235bb7c08e5d29.png)
	referer 黑名单、白名单二者不兼容，同一时间只能生效一种类型，防盗链输入内容最多可输400条，以换行符相隔，一行输入一个。
	
>!
> - 防盗链支持域名 / IP 规则，匹配方式为前缀匹配（仅支持路径情况下，域名的前缀匹配不支持），即假设配置名单为 `www.abc.com`，则 `www.abc.com/123`匹配，`www.abc.com.cn`不匹配。假设配置名单为127.0.0.1，则127.0.0.1/123也会匹配。
> - 防盗链支持通配符匹配，即假设名单为`*.qq.com`，则`www.qq.com`、`a.qq.com`均会匹配。

### referer 白名单
1. 单击开启**防盗链**，默认选中【referer 白名单】，可进行 referer 白名单配置。
   假设用户为域名`www.test.com`配置了 referer 白名单，白名单内容如下：`www.abc.com`，且**未勾选**“包含空 referer”，则表示用户仅允许 referer 值为`www.abc.com`的请求访问，其他请求均返回403。
   ![img](https://main.qcloudimg.com/raw/6f3a737f65e449f523e1675eaedaf0cc.png)
>?
>- 若请求的 referer 字段匹配白名单设置的内容，则 CDN 节点正常返回请求信息。
>- 若请求的 referer 字段不匹配白名单设置的内容，则 CDN 节点拒绝返回该请求信息，会直接返回状态码403。
>- 当设置白名单时，CDN 节点只能返回符合该白名单内字符串内容的请求。
>- 当**勾选**“包含空 referer” 选项时，此时若请求 referer 字段为空或无 referer 字段（如浏览器请求），则 CDN 正常返回请求信息。
2. 配置完成后，开关为开启状态，下方显示正在生效的 referer 白名单配置信息。点击【编辑】可更改配置信息。
![img](https://main.qcloudimg.com/raw/dff4308fc9d07f231263eafe7c7aafc9.png)
3. 关闭**防盗链**开关后，下方的配置信息失效，即防盗链未启用。可再次手动开启。
![img](https://main.qcloudimg.com/raw/192b17814016f3148fc83f17e3bfae05.png)

### referer 黑名单
1. 单击开启**防盗链**，选中【referer 黑名单】，可进行 referer 黑名单配置。
   假设用户为域名`www.abc.com`配置了 referer 黑名单，黑名单内容如下：`www.test.com`，且**未勾选**“包含空 referer”，则 referer 值为 `www.test.com` 的请求均返回403，其他请求情况均返回正常内容。
![img](https://main.qcloudimg.com/raw/9f524d173fe917c7523a59fbef8f4b51.png)
>?
>- 若请求的 referer 字段匹配黑名单内设置的内容，CDN 节点拒绝返回该请求信息，直接返回403状态码。
>- 若请求的 referer 不匹配黑名单内设置的内容，则 CDN 节点正常返回请求信息。
>- 当**勾选**“包含空 referer” 选项时，此时若请求 referer 字段为空或无 referer 字段（如浏览器请求），则 CDN 节点拒绝返回该请求信息，返回403状态码。
2. 配置完成后，开关为开启状态，下方显示正在生效的referer 黑名单配置信息。点击【编辑】可更改配置信息。
![img](https://main.qcloudimg.com/raw/4c7f6a01c0d2f2984bcd3c5a9c0c2f0d.png)
3. 关闭**防盗链**开关后，下方的配置信息失效，即防盗链未启用。可再次手动开启。
![img](https://main.qcloudimg.com/raw/2796c0a0b56f69e6b56a0ae73db54956.png)

## 配置案例
若域名 referer 配置如下：
![img](https://main.qcloudimg.com/raw/4252af2551ec2d32db072d00011bba41.png)
- 用户请求 URL 为`http://www.test.com/1.jpg?version=1.1`的资源，通过浏览器访问，请求 referer 为空，此时正常返回内容。
- 用户请求 URL 为`http://www.test.com/1.jpg?version=1.1`的资源，请求 referer 为 `www.abcd.com`，此时未在白名单中，因此直接返回403。
