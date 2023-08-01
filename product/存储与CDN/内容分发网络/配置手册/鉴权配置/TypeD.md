为保护您的站点资源不被非法站点下载盗用，您可按需选择 Type ABCD 四种鉴权方式的某一种，本文为您详细介绍 Type D 的各个参数字段和原理。

## 算法说明

-  **访问 URL 格式**
`http://DomainName/FileName?sign=md5hash&t=timestamp`

>!
>- 访问 URL 中不能包含中文。
>- 不支持带参数 URL 鉴权。
>- 有效时间最大可输入630720000s。


-  **鉴权字段说明**
<table>
<thead>
<tr>
<th>字段</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>DomainName</td>
<td>CDN 域名。</td>
</tr>
<tr>
<td>Filename</td>
<td>资源访问路径，鉴权时 Filename 需以正斜线（ <code>/</code> ）开头。</td>
</tr>
<tr>
<td>timestamp</td>
<td>服务端生成鉴权 URL 的时间，使用十进制整型正数的 Unix 时间戳，是从 UTC 时间1970年01月01日00时00分00秒到现在的总秒数，其定义与所在时区无关。</td>
</tr>
<tr>
<td>md5hash</td>
<td>通过MD5算法计算出的固定长度为32位的字符串。具体计算公式如下：md5hash = md5sum(pkeyuritimestamp) 参数之间无任何符号pkey： 自定义密钥：由6 - 40位大小写字母、数字构成，密钥需要严格保密，仅用户端与服务端知晓。uri 资源访问路径以正斜线（/）开头。</td>
</tr>
</tbody></table>
- **鉴权逻辑说明**
CDN 服务器接受到客户请求后，解析出 url 中的 timestamp 参数 + 鉴权 URL 有效时长与当前时间比较。
	1. 如果 timestamp + 鉴权 URL 有效时长小于当前时间，则服务器判定过期失效，并返回 HTTP 403错误。
	2. 如果 timestamp + 鉴权 URL 有效时长大于当前时间，则使用 MD5 算法算出 md5hash 的值，再比较计算出来的 md5hash 值与 url 中传入的 md5hash 值，如果一致则放过，不一致则返回 HTTP 403错误。

## 配置指南 

**以 Type-D 鉴权的配置为例，参数和控制台配置如下：** 

- **字段配置**
	- 鉴权密钥：dimtm5evg50ijsx2hvuwyfoiu65
	- 鉴权URL有效时长为：1s   
<img src="https://qcloudimg.tencent-cloud.cn/raw/3163e05c218e78d38b4d844137c049fa.png" width="60%">
	-    签算服务器生成鉴权 URL 的时间：2020年02月27日16:10:32（UTC+8），转换为十进制的整形数值为1582791032(timestamp)
	-    请求源站地址：`http://cloud.tencent.com/test.jpg`
- **生成过程**
	-   获取鉴权参数
<table>
<thead>
<tr>
<th>参数</th>
<th>值</th>
</tr>
</thead>
<tbody><tr>
<td>uri</td>
<td>资源访问路径为 /test.jpg</td>
</tr>
<tr>
<td>timestamp</td>
<td>1582791032</td>
</tr>
<tr>
<td>pkey</td>
<td>dimtm5evg50ijsx2hvuwyfoiu65</td>
</tr>
</tbody></table>
	- 拼接签名串：dimtm5evg50ijsx2hvuwyfoiu65/test.jpg1582791032
	- 计算签名串的 md5 值：md5hash = md5sum(pkeyuritimestamp) =md5sum(dimtm5evg50ijsx2hvuwyfoiu65/test.jpg1582791032) =900a5049aa8ac1ab144527d9c2be4cea
-   **生成鉴权 URL**
`http://cloud.tencent.com/test.jpg?sign=900a5049aa8ac1ab144527d9c2be4cea&t=1582791032`
当客户端通过加密URL进行访问时，如果CDN服务器计算出来的md5hash值与访问请求中带的md5hash值相同，都为900a5049aa8ac1ab144527d9c2be4cea，则鉴权通过，反之鉴权失败。

## 注意事项

**缓存命中率**
开启了 TypeD 鉴权模式的域名，访问 URL 会携带鉴权参数，在 CDN 节点进行资源缓存时，会自动忽略对应的参数进行缓存，不会影响域名缓存命中率。

>!
因配置后会自动忽略对应的参数，即会忽略配置的鉴权参数及时间戳参数，所以会影响鉴权范围内文件的缓存键，且此处的优先级高于**缓存配置 - 缓存键规则配置**处的缓存键规则。
例如，此处 TypeD 配置为： 鉴权参数：sigh - 时间戳参数：t - 鉴权范围：jpg，则 jpg 类型的文件会自动忽略“sign”和“t”参数，即使**缓存配置 - 缓存键规则配置**处已配置：全部文件 - 不忽略参数。

**回源策略** 
开启了 TypeD 鉴权模式的域名，访问格式为：
 `http://DomainName/FileName?sign=md5hash&t=timestamp` 

鉴权通过后，未命中 CDN 节点，节点会发起回源请求， **格式与访问请求保持一致，会保留 sign/t 参数**，源站可按需进行忽略或二次校验。
