若您希望对业务资源的访问来源进行控制，CDN 为您提供了 referer 防盗链配置功能。通过对用户 HTTP Request Header 中 referer 字段的值设置过滤策略，从而限制访问来源。

## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【访问控制】，您可以看到 **防盗链配置** 模块。
![](https://mc.qcloudimg.com/static/img/867df9f122e72e95aa4fd64ade01472a/refer.png)

### 默认配置
默认情况下，防盗链未启用，无黑/白名单。

### 自定义配置
> **注意**：
> - referer 黑名单、白名单二者不兼容，同一时间只能生效一种类型。
> - 防盗链输入内容最多可输 400 条，以换行符相隔，一行输入一个。
> - 防盗链支持 ```域名/IP``` 规则，匹配方式为前缀匹配，即假设名单为 ```www.abc.com```，则 ```www.abc.com/123```、```www.abc.com.cn``` 也会匹配；假设配置名单为 ```127.0.0.1```，则 ```127.0.0.1/123``` 也会匹配。
> - 防盗链支持通配符匹配，即假设名单为 ```*.qq.com```，则 ```www.qq.com```、```a.qq.com``` 均会匹配。

#### 配置 referer 白名单
单击防盗链配置处【编辑】图标，选中 **referer 白名单**，可进行白名单配置。
![](https://mc.qcloudimg.com/static/img/d30c88deb641ec566362c3b837637e4a/whitelist.png)
假设用户为域名 ```www.abc.com``` 配置了 referer 白名单，白名单内容如下：
> www.test.com

且未勾选 **包含空 referer**，则表示用户仅允许 referer 值为 ```www.test.com``` 的请求访问，其他请求均返回 403。 
##### 白名单配置须知
- 若请求的 referer 字段匹配白名单设置的内容，则 CDN 节点正常返回请求信息。
- 若请求的 referer 字段不匹配白名单设置的内容，则 CDN 节点拒绝返回该请求信息，会直接返回状态码 403。
- 当设置白名单时，CDN 节点只能返回符合该白名单内字符串内容的请求。
- 当勾选 **包含空 referer** 选项时，此时若请求 referer 字段为空或无 referer 字段（如浏览器请求），则 CDN 正常返回请求信息。

#### 配置 referer 黑名单
单击防盗链配置处【编辑】图标，选中 **referer 黑名单**，可进行黑名单配置。
![](https://mc.qcloudimg.com/static/img/815bc0187a6542bc9ba156f8a3007f7d/blacklist.png)
假设用户为域名 ```www.abc.com``` 配置了 referer 黑名单，黑名单内容如下：
> www.test.com

且未勾选 **包含空 referer**，则 referer 值为 ```www.test.com``` 的请求均返回 403，其他请求情况均返回正常内容。
##### 黑名单配置须知
- 若请求的 referer 字段匹配黑名单内设置的内容，CDN 节点拒绝返回该请求信息，直接返回 403 状态码。
- 若请求的 referer 不匹配黑名单内设置的内容，则 CDN 节点正常返回请求信息。
- 当勾选 **包含空 referer** 选项时，此时若请求 referer 字段为空或无 referer 字段（如浏览器请求），则 CDN 节点拒绝返回该请求信息，返回 403 状态码。