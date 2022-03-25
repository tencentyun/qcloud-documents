## 功能简介
支持自定义变更/增加/删除 HTTP 响应头（从节点响应客户端用户时的 HTTP 响应头），不会影响节点缓存。若您需要实现跨域访问，可使用此功能。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。
>

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) ，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，单击![](https://qcloudimg.tencent-cloud.cn/raw/fe4d4900f8ad69d506adc49bdb70fa32.png)可按需配置修改 HTTP 响应头规则。
>!目前仅支持匹配条件为全部（任意请求） 或 Host 时配置修改 HTTP 请求头操作。
>
参数说明：
<table>
<thead>
<tr>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>变更</td>
<td>变更指定头部参数的取值为设置后的值<br>注意：<ul><li>若指定头部不存在，则会增加该头部</li><li>若头部已存在（即使有多个重复的头部），则会覆盖原有头部且唯一（合并多个重复的头部为1个头部）</td>
</tr>
<tr>
<td>增加</td>
<td>增加指定的头部<br>注意：<br>若头部已存在（即使有多个重复的头部），则会覆盖原有头部且唯一（合并多个重复的头部为1个头部）</td>
</tr>
<tr>
<td>删除</td>
<td>删除指定的头部</td>
</tr>
</tbody></table>

## 注意事项
- 头部参数格式要求如下：
  - 参数名：1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成。
  - 参数值：1 - 1000个字符，不支持中文。
- 一个修改 HTTP 请求头操作中，可添加多条不同类型操作，最多30条，执行顺序为从上至下。
- 部分标准头部不支持修改，清单如下：
```
Date
Expires
Content-Type
Content-Encoding
Content-Length
Transfer-Encoding
Cache-Control
If-Modified-Since
Last-Modified
Connection
Content-Range
ETag
Accept-Ranges
Age
Authentication-Info
Proxy-Authenticate
Retry-After
Set-Cookie
Vary
WWW-Authenticate
Content-Location
Content-MD5
Content-Range
Meter
Allow
Error
```
