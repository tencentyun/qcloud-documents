## 算法说明
**访问 URL 格式**
`http://DomainName/timestamp/md5hash/FileName`

**算法说明**
- timestamp：时间戳，格式为 YYYYMMDDHHMM。
- md5hash：MD5（自定义密钥 + timestamp + 文件路径）。

**请求示例**
`http://cloud.tencent.com/202003032017/b91bad39a0f9c885ddebd6b6164de3c4/test.jpg`

> !计算 MD5 时，若请求路径为`http://cloud.tencent.com/test.jpg`，则计算 MD5 时路径为`/test.jpg`。

## 配置指南

### 参数说明
TypeB 所需配置如下：
![](https://main.qcloudimg.com/raw/b4d9e34b14987c604bba666b04a78a18.png)
**自定义鉴权密钥：**由6 - 32位大小写字母、数字构成，密钥需要严格保密，仅用户端与服务端知晓。
**自定义有效时间：**通过请求路径中 timestamp 值，加上配置的有效时间，与当前时间进行对比，判定请求是否过期，若过期则直接返回403。 

### 生效对象
配置好密钥、参数名及过期时间后，可按需指定鉴权对象，支持以下三种模式：
![](https://main.qcloudimg.com/raw/1952a0ac13633a87d4b676e52bf2eb10.png)
- 支持指定域名下所有文件均需要鉴权校验。
- 支持指定类型文件不做鉴权，其他均需要做鉴权校验。
- 支持指定类型文件做鉴权校验。

## 注意事项
**缓存命中率**
开启了 TypeB 鉴权模式的域名，访问 URL 路径中会携带签名及时间戳，在 CDN 节点进行资源缓存时，会自动忽略路径中的字段进行缓存，不会影响域名缓存命中率。
**回源策略**
开启了 TypeB 鉴权模式的域名，访问格式为：
`http://DomainName/timestamp/md5hash/FileName`

鉴权通过后，若未命中 CDN 节点，节点会发起回源请求，**回源请求会去掉路径中的 md5hash 及 timestamp**，源站无需做特殊处理。

