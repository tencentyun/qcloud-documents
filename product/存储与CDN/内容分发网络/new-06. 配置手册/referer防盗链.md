## 功能介绍

若您希望对业务资源的访问来源进行控制，CDN 为您提供了 Referer 防盗链配置功能。通过对用户HTTP Request Header 中 Referer 字段的值设置过滤策略，从而限制访问来源。

## 配置说明

登录[CDN控制台](https://console.qcloud.com/cdn)，进入 【域名管理】 页面，点击域名右侧 **管理** 按钮，进入管理页面：

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

在【访问控制】中找到 **referer防盗链** 模块：

![](https://mc.qcloudimg.com/static/img/006ecb68063d27ffc28c6becb8b038fc/referer.png)


### 默认配置

默认情况下，防盗链未启用，无黑/白名单。

### 自定义配置

#### 配置referer白名单

点击防盗链配置处**编辑**按钮，选中**referer白名单**，可进行白名单配置：

![](https://mccdn.qcloud.com/static/img/9e60a3f0366203a51c5e4a112934c692/image.png)


假设用户为域名 www.abc.com 配置了referer白名单，白名单内容如下：

> www.test.com

且未勾选**包含空referer**，则表明用户仅允许referer值为 www.test.com 的请求访问，其他请求均返回403。 

##### 白名单配置须知

- 若请求的referer字段匹配白名单设置的内容，则CDN节点正常返回请求信息；
- 若请求的referer字段不匹配白名单设置的内容，则CDN节点拒绝返回该请求信息，会直接返回状态码403；
- 当设置白名单时，CDN节点只能返回符合该白名单内字符串内容的请求；
- **当勾选包含空referer选项时，此时若请求referer字段为空或无referer字段（如浏览器请求），则CDN正常返回请求信息。**

#### 配置referer黑名单

点击防盗链配置处**编辑**按钮，选中**referer黑名单**，可进行黑名单配置：

![](https://mccdn.qcloud.com/static/img/73a145bf315304e277e5c5b4c91e15cf/image.png)

假设用户为域名 www.abc.com 配置了referer黑名单，黑名单内容如下：

> www.test.com

且未勾选**包含空referer**，则referer值为 www.test.com 的请求均返回403，其他请求情况均返回正常内容。

##### 黑名单配置须知

- 若请求的referer字段匹配黑名单内设置的内容，CDN节点拒绝返回该请求信息，直接返回403状态码
- 若请求的referer不匹配黑名单内设置的内容，则CDN节点正常返回请求信息；
- **当勾选【包含空referer】选项时，此时若请求referer字段为空或无referer字段（如浏览器请求），则CDN节点拒绝返回该请求信息，返回403状态码。**

### 注意事项

- referer黑名单、白名单二者不兼容，同一时间只能生效一种类型；
- 防盗链输入内容最多可输400条，以换行符相隔，一行输入一个。
- 防盗链支持域名/IP规则，匹配方式为前缀匹配，即假设名单为 www.abc.com，则 www.abc.com/123、www.abc.com.cn 也会匹配；假设配置名单为 127.0.0.1，则 127.0.0.1/123 也会匹配；
- 防盗链支持通配符匹配，即假设名单为 *.qq.com，则 www.qq.com、a.qq.com均会匹配。



