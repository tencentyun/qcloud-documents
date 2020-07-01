## 算法说明
**访问 URL 格式**
`http://DomainName/Filename?sign=timestamp-rand-uid-md5hash`

**算法说明**
- timestamp：十进制（UNIX 时间戳）。
- rand：随机字符串，0 - 100位随机字符串，由大小写字母与数字组成。
- uid：0
- md5hash：MD5（文件路径-timestamp-rand-uid-自定义密钥）。

**请求示例**
`http://cloud.tencent.com/test/test.jpg?sign=1582791032-im1acp76sx9sdqe601v-0-dd63f95e739ed4b47427a129d21ef4e3`

> !计算 MD5 时，若请求路径为 `http://cloud.tencent.com/test.jpg`，则计算 MD5 时路径为`/test.jpg`。

## 配置指南
### 参数说明
TypeA 所需配置如下：
![](https://main.qcloudimg.com/raw/7146ed740601d34e2676d231c4a101a4.png)
**自定义鉴权密钥**：由6 - 32位大小写字母、数字构成，密钥需要严格保密，仅用户端与服务端知晓。
**自定义鉴权参数名**：将示例中的 sign 替换为由任意1 - 100位大小写字母、数字或下划线组成的参数名，CDN 收到请求后，根据指定的签名参数取出对应的值，进行 MD5 计算，若匹配传递而来的 md5hash 值，则签名校验通过，若校验不通过则直接返回403。
**自定义有效时间**：通过请求中携带的 timestamp，加上配置的有效时间，与当前时间进行对比，判定请求是否过期，若过期则直接返回403。 

### 生效对象
配置好密钥、参数名及过期时间后，可按需指定鉴权对象，支持以下三种模式：
![](https://main.qcloudimg.com/raw/1952a0ac13633a87d4b676e52bf2eb10.png)
+ 支持指定域名下所有文件均需要鉴权校验。
+ 支持指定类型文件不做鉴权，其他均需要做鉴权校验。
+ 支持指定类型文件做鉴权校验。

## 注意事项
**缓存命中率**
开启了 TypeA 鉴权模式的域名，访问 URL 会携带鉴权参数，在 CDN 节点进行资源缓存时，会自动忽略对应的参数进行缓存，不会影响域名缓存命中率。
**回源策略**
开启了 TypeA 鉴权模式的域名，访问格式为：
`http://DomainName/Filename?sign=timestamp-rand-uid-md5hash`

鉴权通过后，未命中 CDN 节点，节点会发起回源请求，**格式与访问请求保持一致，会保留 sign 参数**，源站可按需进行忽略或二次校验。
