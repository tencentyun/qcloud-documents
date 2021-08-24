## 算法说明
**访问 URL 格式**
`http://DomainName/md5hash/timestamp/FileName`

>! 访问 URL 中不能包含中文。


**算法说明**
- timestamp：十六进制（UNIX 时间戳）。
- md5hash：MD5（自定义密钥 + 文件路径 + timestamp）。

**请求示例**
`http://cloud.tencent.com/8fe9b5597c809d7ace147468c7c7eadb/5e577978/test.jpg`

> !计算 MD5 时，若请求路径为`http://cloud.tencent.com/test.jpg`，则计算 MD5 时路径为`/test.jpg`。

## 配置指南
### 参数说明
TypeC 所需配置如下：
![](https://main.qcloudimg.com/raw/d1b58cf078743dd6992b35ea846f411f.png)
**自定义鉴权密钥：**由6 - 40位大小写字母、数字构成，密钥需要严格保密，仅用户端与服务端知晓。
**自定义有效时间：**通过请求路径中 timestamp 值，加上配置的有效时间，与当前时间进行对比，判定请求是否过期，若过期则直接返回403，有效时间单位为秒，最大可设置为630720000秒。
### 生效对象
配置好密钥、参数名及过期时间后，可按需指定鉴权对象，支持以下三种模式：
![](https://main.qcloudimg.com/raw/dcf4646c2459df7b10e016b3cb4e51ae.png)
+ 支持指定域名下所有文件均需要鉴权校验。
+ 支持指定类型文件不做鉴权，其他均需要做鉴权校验。
+ 支持指定类型文件做鉴权校验。

## 注意事项
**缓存命中率**
开启了 TypeC 鉴权模式的域名，访问 URL 路径中会携带签名及时间戳，在 CDN 节点进行资源缓存时，会自动忽略鉴权路径进行缓存，不会影响域名缓存命中率。
**回源策略**
开启了 TypeC 鉴权模式的域名，访问格式为：
`http://DomainName/md5hash/timestamp/FileName`

鉴权通过后，未命中 CDN 节点，节点会发起回源请求，**回源请求会去掉路径中的 md5hash 及 timestamp 路径**，源站无需做特殊处理。
