## 功能介绍

回源 HOST 是指 CDN 节点在回源过程中，在源站访问的站点域名。

**注意事项：**

+ 源站与回源 HOST：源站配置的 IP/域名能够指引 CDN 节点回源时找到对应的源站服务器，服务器上可能存在若干 WEB 站点，回源 HOST 指明了资源所在的站点。


## 配置说明

登录[CDN控制台](https://console.qcloud.com/cdn)，进入 【域名管理】 页面，点击域名右侧 **管理** 按钮，进入管理页面：

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

在 【基本配置】中找到 **回源配置** 模块，配置回源host：

![](https://mc.qcloudimg.com/static/img/5440c6887c5120a103601f52167113dd/image.png)



### 默认配置

默认情况下，子域名的回源 HOST 为所配置的加速域名，泛域名回源 HOST 为访问域名：

![](https://mc.qcloudimg.com/static/img/df14797663acbdf2924702a4f49c0142/image.png)

+ 若您接入的加速域名为 www.test.com，则此节点对此域名下资源发起回源请求时，Request HTTP Header中host字段的值为 www.test.com；
+ 若您接入的加速域名为泛域名，如 \*.test.com，若访问域名为 abc.test.com，则回源 HOST 为 abc.test.com。


### 自定义配置

您可以根据自身业务情况配置自定义回源HOST。

![](https://mc.qcloudimg.com/static/img/e6e934df080a16422d56f35bab8b312e/image.png)


### 注意事项

- 目前仅支持接入方式为**自有源**的域名配置回源HOST；
- 请保证您配置的回源HOST域名能够支持访问，否则会导致回源失败的情况，影响您的业务。