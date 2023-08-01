为保护您的站点资源不被非法站点下载盗用，您可按需选择 Type ABCD 四种鉴权方式的某一种，本文为您详细介绍 Type B 的各个参数字段和原理。

## 算法说明

- **访问 URL 格式**
`http://DomainName/timestamp/md5hash/FileName`

>!
>- 访问 URL 中不能包含中文。
>- 不支持带参数 URL 鉴权。
>- 有效时间最大可输入630720000s。


- **鉴权字段说明**

|字段|说明|
|--|--|
|DomainName|CDN 域名。|
|Filename|资源访问路径，鉴权时Filename需以正斜线（ `/` ）开头。|
|timestamp|签算服务器生成鉴权 URL 的时间，与有效时间共同控制鉴权 URL 的失效时间，格式为：YYYYMMDDHHMM（时间点取自签算服务器的 UTC+8 时间），如：201807301000。|
|md5hash|通过 MD 5算法计算出的固定长度为32位的字符串。具体计算公式如下：<br>• md5hash = md5sum(pkeytimestampuri) 参数之间无任何符号 <br>• pkey：自定义密钥：由6 - 40位大小写字母、数字构成，密钥需要严格保密，仅客户端与服务端知晓。 <br>• uri 资源访问路径以正斜线（/）开头。<br>• timestamp：取值为上述中的timestamp。|

- **鉴权逻辑说明**
CDN 服务器接受到客户请求后，解析出 url 中的 timestamp 参数 + 鉴权 URL 有效时长与当前时间比较。
	1. 如果 timestamp + 鉴权 URL 有效时长小于当前时间，则服务器判定过期失效，并返回 HTTP 403错误。
	2. 如果 timestamp + 鉴权 URL 有效时长大于当前时间，则使用 MD5 算法算出 md5hash 的值，再比较计算出来的 md5hash 值与 url 中传入的 md5hash 值，如果一致则放过，不一致则返回 HTTP 403错误。

## 配置指南 

**以 Type-B 鉴权的配置为例，参数和控制台配置如下：**

- **字段配置**
	- 鉴权密钥：dimtm5evg50ijsx2hvuwyfoiu65
	- 鉴权URL有效时长为：1s   
	<img src="https://qcloudimg.tencent-cloud.cn/raw/fd8a39902be99d134143d4fb85ac5e89.png" width="60%">
	-  签算服务器生成鉴权URL的时间：2020年02月27日16:10:32（UTC+8）
	-  请求源站地址：`http://cloud.tencent.com/test.jpg`
- **生成过程**
	-  获取鉴权参数
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
<td>202002271610</td>
</tr>
<tr>
<td>pkey</td>
<td>dimtm5evg50ijsx2hvuwyfoiu65</td>
</tr>
</tbody></table>
	- 拼接签名串：dimtm5evg50ijsx2hvuwyfoiu65202002271610/test.jpg
	- 计算签名串的 md5 值：md5hash = md5sum(pkeytimestampuri) =md5sum(dimtm5evg50ijsx2hvuwyfoiu65202002271610/test.jpg) = 2e03a07cfa55a47768226d3e5ea82a8d
- **生成鉴权 URL**
`http://cloud.tencent.com/202002271610/2e03a07cfa55a47768226d3e5ea82a8d/test.jpg`
当客户端通过加密 URL 进行访问时，如果 CDN 服务器计算出来的 md5hash 值与访问请求中带的 md5hash 值相同，都为 2e03a07cfa55a47768226d3e5ea82a8d，则鉴权通过，反之鉴权失败。
## 注意事项 

**缓存命中率**

开启了 TypeB 鉴权模式的域名，访问 URL 路径中会携带签名及时间戳，在 CDN 节点进行资源缓存时，会自动忽略路径中的字段进行缓存，不会影响域名缓存命中率。

**回源策略**

开启了 TypeB 鉴权模式的域名，访问格式为：
 `http://DomainName/timestamp/md5hash/FileName` 

鉴权通过后，若未命中 CDN 节点，节点会发起回源请求，**回源请求会去掉路径中的 md5hash 及 timestamp**，源站无需做特殊处理。
