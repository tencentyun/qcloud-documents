## 配置场景
腾讯云 CDN 在缓存资源时，为提高存储效率会将文件进行切片存储，并且支持 Range 请求，若请求时携带 HTTP 头部`Range: bytes = 0-999`，则返回文件的前1000个字节给用户。

开启 Range 回源配置，若用户请求的部分文件已过期，CDN 会根据用户请求进行分片回源，仅拉取用户需要的部分文件进行缓存，同时返回给用户；关闭 Range 回源配置，即便用户请求的是部分文件，CDN 在回源时仍会拉取整个文件，而后进行缓存，并响应给用户其要求的部分文件。

开启 Range 回源配置能够有效提高大文件分发效率，提升响应速度，降低源站压力。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2209-31085?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


> ?开启 Range 回源配置后，资源在节点上分片缓存，但所有分片的缓存过期时间保持一致，按照用户指定的缓存过期规则。

## 配置指南
### 查看配置
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面，第四栏【回源配置】中可看到 Range 回源配置，默认情况下为关闭状态，若为 COS 源站域名，则默认为开启状态：
![](https://main.qcloudimg.com/raw/4b70cbb960c9eae8a89903ffb8ec5ec8.png)

### 修改配置
通过单击开关，可对 Range 回源配置进行开启或关闭操作，开启 Range 回源配置时，需要确认源站已经支持 Range 请求，否则可能会导致回源失败。
![](https://main.qcloudimg.com/raw/f9744888f88352bfc6c1dea6cb7ea229.png)

> !若您的加速域名服务区域为全球加速，设置的 Range 回源配置全球生效，不支持境内、境外差异化配置

## 配置示例
若域名`cloud.tencent.com`的 Range 回源配置如下：
![](https://main.qcloudimg.com/raw/07a1be72a1fa80c103ffb01f2dcb9a5d.png)
用户 A 请求资源：`http://cloud.tencent.com/test.apk`，节点收到请求后，发现缓存的`test.apk`文件已过期，此时发起回源请求，节点回源使用 Range 请求，分片获取资源并缓存。若此时用户 B 发起的也为 Range 请求，当节点上存储的分片已满足 Range 中指定的字节段，则会直接返回给用户，无需等所有分片获取完毕。

