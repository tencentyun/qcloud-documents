## 功能简介
Token 鉴权为一种访问控制策略，通过配置鉴权规则进行访问校验，过滤不合法的访问请求。可有效防止站点资源被恶意盗刷，保护您的业务内容。

**Token 鉴权如何做到访问控制？**
客户端用户在发起请求时，其访问请求 URL 需按鉴权规则生成鉴权 URL，当且仅当鉴权 URL 中的鉴权信息（例如：时间戳）通过节点校验，即鉴权通过时，该访问请求才会被视为合法请求，节点正常响应。若校验失败，则节点拒绝该访问，直接返回403。

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，可按需配置 Token 鉴权规则。如何使用规则引擎，请参见 [规则引擎](https://cloud.tencent.com/document/product/1552/70901)。
<table>
<thead>
<tr>
<th align="left">配置项</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">鉴权方式</td>
<td align="left">目前支持4种鉴权签名计算方式，请您根据访问 URL 格式选择合适的方式。详情请参见 <a href="https://cloud.tencent.com/document/product/1552/71007#jqfs">鉴权方式</a>。</td>
</tr>
<tr>
<td align="left">密钥（主）</td>
<td align="left">鉴权方式对应的主用密码，由6-40位大小写英文字母或数字组成。</td>
</tr>
<tr>
<td align="left">密钥（备）</td>
<td align="left">鉴权方式对应的备用密码，由6-40位大小写英文字母或数字组成。</td>
</tr>
<tr>
<td align="left">鉴权参数</td>
<td align="left">鉴权参数名称，节点将校验此参数名对应的值。由1 - 100位大小写字母、数字或下划线组成。</td>
</tr>
<tr>
<td align="left">有效时长</td>
<td align="left">配置的鉴权 URL 的有效时长，单位：秒（1 - 630720000），用于判断客户端访问请求是否过期：<ul><li>若当前时间超过”timestamp + 有效时长“时间，则为过期请求，直接返回403。</li><li>若当前时间未超过”timestamp+ 有效时长“时间，则请求未过期，继续校验。</td>
</tr>
</tbody></table>



## 鉴权方式
### 方式 A
#### 鉴权 URL 格式
```js.
http://Hostname/Filename?sign=timestamp-rand-uid-md5hash
```

#### 鉴权字段说明

| 字段      | 说明                                                         |
| :-------- | :----------------------------------------------------------- |
| Hostname  | 站点加速域名。                                               |
| Filename  | 资源访问路径，鉴权时 Filename 需以`/`开头。                  |
| sign      | 自定义设置的鉴权参数名称。                                   |
| timestamp | 时间戳参数<br/>格式：十进制整型正数的 Unix 时间戳，是从 UTC 时间1970年01月01日00时00分00秒到现在的总秒数，其定义与所在时区无关。 |
| rand      | 0 - 100位随机字符串，由大小写字母与数字组成。                  |
| uid       | 用户 ID，暂未使用，默认为0。                                   |
| md5hash   | 通过 MD5 算法计算出的固定长度为32位的字符串：<li>算法：MD5（/Filename-timestamp-rand-uid-密钥）。</li><li>鉴权逻辑：若请求未过期，则节点比较此字符串值与请求 URL 中携带的 `md5hash` 值：两值相同，鉴权通过，响应请求；两值不同，鉴权失败，返回403。</li> |

### 方式 B

#### 鉴权 URL 格式

```js.
http://Hostname/timestamp/md5hash/Filename
```

#### 参数说明

| 字段      | 说明                                                         |
| :-------- | :----------------------------------------------------------- |
| Hostname  | 站点加速域名。                                                 |
| Filename  | 资源访问路径，鉴权时 Filename 需以`/`开头。                  |
| timestamp | 时间戳参数。<br/>格式：YYYYMMDDHHMM，UTC+8 时间，例如201807301000。 |
| md5hash   | 通过 MD5 算法计算出的固定长度为32位的字符串：<li>算法：MD5（密钥 + timestamp + /Filename）。</li><li>鉴权逻辑：若请求未过期，则节点比较此字符串值与请求 URL 中携带的 `md5hash` 值：两值相同，鉴权通过，响应请求；两值不同，鉴权失败，返回403。</li> |

### 方式 C

**鉴权 URL 格式**

```js.
http://Hostname/md5hash/timestamp/Filename
```

#### 参数说明

| 字段      | 说明                                                         |
| :-------- | :----------------------------------------------------------- |
| Hostname  | 站点加速域名。                                                 |
| Filename  | 资源访问路径，鉴权时 Filename 需以`/`开头。                  |
| timestamp | 时间戳参数。<br/>格式：十六进制整型正数的 Unix 时间戳，是从 UTC 时间1970年01月01日00时00分00秒到现在的总秒数，其定义与所在时区无关。 |
| md5hash   | 通过 MD5 算法计算出的固定长度为32位的字符串：<li>算法：MD5（密钥+ /Filename + timestamp ）。注：计算时，十六进制的 timestamp 需过滤掉进制数标识0x。</li><li>鉴权逻辑：若请求未过期，则节点比较此字符串值与请求 URL 中携带的 `md5hash` 值：两值相同，鉴权通过，响应请求；两值不同，鉴权失败，返回403。</li> |

### 方式 D

#### 鉴权 URL 格式

```js.
http://Hostname/Filename?sign=md5hash&t=timestamp
```

#### 参数说明

| 字段      | 说明                                                         |
| :-------- | :----------------------------------------------------------- |
| Hostname  | 站点加速域名。                                                 |
| Filename  | 资源访问路径，鉴权时 Filename 需以`/`开头。                  |
| sign      | 自定义设置的鉴权参数名称。                                     |
| t         | 自定义设置的时间戳参数名称                                   |
| timestamp | 时间戳参数。 <br/>格式：十进制整型正数的 Unix 时间戳，是从 UTC 时间1970年01月01日00时00分00秒到现在的总秒数，其定义与所在时区无关；或十六进制整型正数的 Unix 时间戳，是从 UTC 时间1970年01月01日00时00分00秒到现在的总秒数，其定义与所在时区无关。 |
| md5hash   | 通过 MD5 算法计算出的固定长度为32位的字符串：<li>算法：MD5（密钥 + /Filename + timestamp）。注：计算时，十六进制的 timestamp 需过滤掉进制数标识0x。 </li><li>鉴权逻辑：若请求未过期，则节点比较此字符串值与请求 URL 中携带的 `md5hash` 值：两值相同，鉴权通过，响应请求；两值不同，鉴权失败，返回403。</li> |

## 配置示例

假设请求 `http://www.example.com/test.jpg` 符合鉴权方式 A，则可配置如下：

![](https://qcloudimg.tencent-cloud.cn/raw/14f4c742ec824c1e4aa32e84c123d312.png)

#### 获取鉴权参数
- /Filename：`/foo.jpg`。
- imestamp：服务端生成鉴权URL的时间为2022年03月15日10:30:32（UTC+8），转换为十进制的整形数值为`1647311432`。
- rand：生成随机数为 `J0ehJ1Gegyia2nD2HstLvw`。
- uid：`0`。
- 密钥：`3C9mxSGzc8ZadmGNzE`。
- md5hash：MD5（/Filename-timestamp-rand-uid-密钥）= MD5（`/foo.jpg`-`1647311432`-`J0ehJ1Gegyia2nD2HstLvw`-`0`-`3C9mxSGzc8ZadmGNzE`）= ecce3150cbdaac83b116d937777ca77f。

#### 鉴权 URL
`http://www.example.com/foo.jpg?sign=1647311432-J0ehJ1Gegyia2nD2HstLvw-0-ecce3150cbdaac83b116d937777ca77f`。

#### 节点鉴权

当节点服务器接受到客户端通过加密 URL 发出的请求时，解析出 URL 中的 timestamp 参数，加上配置的“有效时长 - 1秒”，与当前时间比较：
<dx-steps>
-若当前时间超过”timestamp + 有效时长“时间，则为过期请求，直接返回403。
-若当前时间未超过”timestamp + 有效时长“时间，则请求未过期，继续第3步。
-节点服务器通过获取的鉴权参数计算 `md5hash` 值，与请求 URL 中携带的 `md5hash` 值做比较：两值相同，鉴权通过，响应请求；两值不同，鉴权失败，返回403。
</dx-steps>


## 注意事项
1. 鉴权通过后，节点会自动忽略 URL 中鉴权相关的参数再将其作为缓存标识（Cache key），提高缓存命中率，减少回源。
2. 鉴权通过后，若未命中节点缓存，则会继续回源，实际回源 URL 将与 鉴权 URL 格式一致，保留鉴权参数。源站可按需忽略或二次校验，或使用 [回源请求参数设置](https://cloud.tencent.com/document/product/1552/82627) 操作配置回源是忽略相关鉴权参数。
3. URL 中不能包含中文。
