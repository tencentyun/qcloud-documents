CDN 为您提供 Range 回源配置功能，Range 是 Http 请求头，用于文件指定部分的请求。如：```Range: bytes=0-999``` 就是请求该文件的前 1000 个字节。开启 Range 回源配置能够有效提高大文件分发效率，提升响应速度。
> **注意**：
> 1. 源站需要支持 Range 请求，否则会导致回源失败。
> 2. 若节点从未缓存过该资源，则首次回源获取时不会进行分片回源。
> 3. 开启 Range 回源配置后，资源在节点上分片缓存，但所有分片的缓存过期时间保持一致，按照用户指定的缓存过期规则。

## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【回源配置】，您可以看到 **Range 回源配置** 模块。
![](https://mc.qcloudimg.com/static/img/e69d4dc5e391e4b75d2aecbc9c2c042b/range.png)

### 默认配置
默认情况下，Range 回源配置为开启状态。

### 配置效果说明
假设用户甲请求资源： ```http://www.test.com/test.apk```，节点收到请求后，发现缓存的“test.apk”文件已过期，此时发起回源请求，则：
**当 Range 回源开启时**：节点回源使用 Range 请求，分片获取资源并缓存。若此时用户乙发起的也为 Range 请求，当节点上存储的分片已满足 Range 中指定的字节段，则会直接返回给用户，无需等所有分片获取完毕。 
**当 Range 回源关闭时**：节点会直接向源站获取整个资源，待完整获取资源后再返回给用户。