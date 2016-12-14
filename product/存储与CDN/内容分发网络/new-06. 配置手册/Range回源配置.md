## 功能介绍
CDN 为您提供 Range 回源配置功能，开启 Range回源配置能够有效降低大文件回源率，提升响应速度。

<font color="orange">源站需要支持 Range 请求</font>

## 配置说明

登录[CDN控制台](https://console.qcloud.com/cdn)，进入 【域名管理】 页面，点击域名右侧 **管理** 按钮，进入管理页面：

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

您可以在 【回源配置】 中找到 **Range 回源配置** 配置项：

![](https://mc.qcloudimg.com/static/img/42ee9cf64caf0e5b98467709e14df0c6/range.png)

### 默认配置
默认情况下，Range 回源配置为 **开启** 状态。

### 配置效果说明

假设用户请求资源：http://www.test.com/test.apk ，节点收到请求后，发现缓存的 test.apk 文件已过期，此时发起回源请求。

**开启 Range 回源配置：**

+ 节点回源使用 Range 请求，分片获取资源
+ 若用户侧发起的也为 Range 请求，当节点上存储的分片已满足条件，则会直接返回给用户，无需等所有分片获取完毕


**关闭 Range 回源配置：**

+ 节点会直接向源站获取整个资源

**注意事项**：

+ 源站需要支持 Range 请求，否则会导致回源失败；
+ 若节点从未缓存过该资源，则首次回源获取时不会进行分片回源；
+ 开启 Range 回源配置后，资源在节点上分片缓存，但所有分片的缓存过期时间保持一致，按照用户指定的缓存过期规则。