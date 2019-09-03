> ?
>- CDN 为您提供 Range 回源配置功能，Range 是 HTTP 请求头，用于文件指定部分的请求。如：`Range: bytes = 0-999`就是请求该文件的前1000个字节。开启 Range 回源配置能够有效提高大文件分发效率，提升响应速度。
>- 源站需要支持 Range 请求，否则会导致回源失败。
>-  开启 Range 回源配置后，资源在节点上分片缓存，但所有分片的缓存过期时间保持一致，按照用户指定的缓存过期规则。

## 配置指引
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![img](https://main.qcloudimg.com/raw/99e0c24b4530c30b9abe27325bb1b317.png)
2. 单击【回源配置】，您可以看到 **Range 回源配置**模块，默认情况下，Range 回源配置为开启状态。
 ![img](https://main.qcloudimg.com/raw/7653b9061b29fea611ae396df373c2cc.png)

## 配置案例
- 若域名`www.test.com`， Range 回源配置如下：
![img](https://main.qcloudimg.com/raw/d08305ba88dd4afc1cca6091b12d9528.png)
用户 A 请求资源：`http://www.test.com/test.apk`，节点收到请求后，发现缓存的`test.apk`文件已过期，此时发起回源请求，节点回源使用 Range 请求，分片获取资源并缓存。若此时用户乙发起的也为 Range 请求，当节点上存储的分片已满足 Range 中指定的字节段，则会直接返回给用户，无需等所有分片获取完毕。
- 若域名 `www.test.com` ，Range 回源配置如下：
![img](https://main.qcloudimg.com/raw/2e0aee010a727ec375927482e114a210.png)
  用户 A 请求资源：`http://www.test.com/test.apk`，节点收到请求后，发现缓存的`test.apk`文件已过期，此时发起回源请求，节点会直接向源站获取整个资源，待完整获取资源后再返回给用户。
