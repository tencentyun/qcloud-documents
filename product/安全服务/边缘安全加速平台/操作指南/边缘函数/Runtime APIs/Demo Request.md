**Request** 代表 HTTP 请求对象，基于标准 Request 进行了扩展，请参考 MDN 官方文档 [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request)。在边缘函数中，可通过两种方式获得 Request 对象：

- 使用 Request 构造函数创建一个 Request 对象，用于 Fetch API 的操作。
- 通过 FetchEvent 对象的 request 属性，获得当前请求的 Request 对象。



## 构造函数
```typescript
const request = new Request(input [, options])
```

### 参数

<table>
<thead>
<tr>
<th width="10%">参数名称</th>
<th width="15%">类型</th>
<th width="10%">必填</th>
<th width="65%">说明</th>
</tr>
</thead>
<tbody><tr>
<td>input</td>
<td>string | Request</td>
<td>是</td>
<td>一个直接包含资源 url 的字符串或拷贝已存在的 Request 对象，若 options 对象的 copyHeaders 属性为 false，则引用传入的 Request 对象的 headers 属性</td>
</tr>
<tr>
<td>options</td>
<td><a href="#RequestInit">RequestInit</a></td>
<td>否</td>
<td>初始化 Request 对象的属性值的选项</td>
</tr>
</tbody></table>


#### RequestInit[](id:RequestInit)

初始化 Request 对象的属性值选项。

<table>
<thead>
<tr>
<th width="15%">属性名</th>
<th width="15%">类型</th>
<th width="10%">必填</th>
<th width="10%">默认值</th>
<th width="50%">说明</th>
</tr>
</thead>
<tbody><tr>
<td>method</td>
<td>string</td>
<td>否</td>
<td>GET</td>
<td>请求方法，支持 <code>GET</code>、<code>POST</code>、……</td>
</tr>
<tr>
<td>headers</td>
<td><a href="https://cloud.tencent.com/document/product/1552/81903">Headers</a></td>
<td>否</td>
<td>-</td>
<td>请求的头部信息</td>
</tr>
<tr>
<td>body</td>
<td>string |<br> Blob | <br>ArrayBuffer | <br>ArrayBufferView | <br><a href="https://cloud.tencent.com/document/product/1552/81914">ReadableStream</a></td>
<td>否</td>
<td>-</td>
<td>请求体</td>
</tr>
<tr>
<td>redirect</td>
<td>string</td>
<td>否</td>
<td>follow</td>
<td>重定向策略，支持 <code>manual</code>、<code>error</code> 和 <code>follow</code>（自动跟随重定向）</td>
</tr>
<tr>
<td>maxFollow</td>
<td>number</td>
<td>否</td>
<td>12</td>
<td>最大可重定向次数</td>
</tr>
<tr>
<td>version</td>
<td>string</td>
<td>否</td>
<td>HTTP/1.1</td>
<td>HTTP 版本，支持 <code>HTTP/1.0</code>、<code>HTTP/1.1</code> 和 <code>HTTP/2.0</code></td>
</tr>
<tr>
<td>copyHeaders</td>
<td>boolean</td>
<td>否</td>
<td>-</td>
<td><strong>非标准选项</strong>，表示是否拷贝传入的 Request 对象的 headers 属性</td>
</tr>
<tr>
<td>cf</td>
<td><a href="#RequestInitCfProperties">RequestInitCfProperties</a></td>
<td>否</td>
<td>-</td>
<td><strong>非标准选项</strong>，用于控制边缘函数处理该请求的行为</td>
</tr>
</tbody></table>

#### RequestInitCfProperties[](id:RequestInitCfProperties)
非标准选项，用于控制边缘函数处理该请求的行为。
<table>
<thead>
<tr>
<th width="10%">参数名称</th>
<th width="15%">类型</th>
<th width="10%">必填</th>
<th width="65%">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">resolveOverride</td>
<td align="left">string</td>
<td align="left">否</td>
<td align="left">在使用 fetch(event.request) 进行 CDN 回源时，用于指定源站域名（仅支持域名，如 <code>www.qq.com</code>，不支持指定 HTTP 协议或者端口号）</td>
</tr>
<tr>
<td align="left">cacheEverything</td>
<td align="left">boolean</td>
<td align="left">否</td>
<td align="left">缓存相关，用于指定缓存响应的所有头部</td>
</tr>
<tr>
<td align="left">cacheKey</td>
<td align="left">string</td>
<td align="left">否</td>
<td align="left">缓存相关，用于指定自定义的缓存 key</td>
</tr>
<tr>
<td align="left">cacheTtl</td>
<td align="left">number</td>
<td align="left">否</td>
<td align="left">缓存相关，用于指定缓存时长(单位s)，必需大于等于0，等于0不缓存</td>
</tr>
<tr>
<td align="left">cacheTtlByStatus</td>
<td align="left">{[key: string]: number}</td>
<td align="left">否</td>
<td align="left">缓存相关，用于根据状态码指定缓存时长(单位s)，小于等于0不缓存</td>
</tr>
</tbody></table>


## 实例属性

### body
`readonly` `body：ReadableStream`
请求体，[ReadableStream](https://cloud.tencent.com/document/product/1552/81914)。

### bodyUsed
`readonly` `bodyUsed: boolean`
标识请求体是否已读取。

### headers
`readonly` `headers: Headers`
请求头部，[Headers](https://cloud.tencent.com/document/product/1552/81903)。

### method
`readonly` `method: string`
请求方法，默认值为`GET`。

### redirect
`readonly` `redirect: string`
请求被重定向后的处理方式，可取值为：follow、error、manual；默认为 manual。

### maxFollow
`readonly` `maxFollow: number`
请求最多可重定向的次数。

### url
`readonly` `url: string;`
请求的 url。

### version
`readonly` `version: string`
请求使用的 HTTP 协议版本。

### cf
`readonly` [`cf: IncomingRequestCfProperties`](#IncomingRequestCfProperties)
一个对象，其中包含了由边缘安全加速平台提供的与客户请求相关的属性。

#### IncomingRequestCfProperties[](id:IncomingRequestCfProperties)
除了标准 [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) 对象的属性外，客户端请求的 `request.cf` 对象中还包含由边缘安全加速平台提供的与请求相关的一些其他信息。包含如下信息：
<table>
<thead>
<tr>
<th width="25%">属性名</th>
<th width="25%">类型</th>
<th width="25%">说明</th>
<th width="25%">示例值</th>
</tr>
</thead>
<tbody><tr>
<td>geo</td>
<td><a href="#GeoProperties">GeoProperties</a></td>
<td>一个对象，用于描述客户请求的位置</td>
<td>-</td>
</tr>
</tbody></table>

#### GeoProperties[](id:GeoProperties)
一个对象，用于描述客户请求的位置。
<table>
<thead>
<tr>
<th width="25%">属性名</th>
<th width="25%">类型</th>
<th width="25%">说明</th>
<th width="25%">示例值</th>
</tr>
</thead>
<tbody><tr>
<td>asn</td>
<td>number</td>
<td>自治区号</td>
<td>12271</td>
</tr>
<tr>
<td>countryName</td>
<td>string</td>
<td>国家名</td>
<td>United States of America</td>
</tr>
<tr>
<td>countryCodeAlpha2</td>
<td>string</td>
<td>国家的 ISO-3611 alpha2 代码</td>
<td>US</td>
</tr>
<tr>
<td>countryCodeAlpha3</td>
<td>string</td>
<td>国家的 ISO-3611 alpha3 代码</td>
<td>USA</td>
</tr>
<tr>
<td>countryCodeNumeric</td>
<td>string</td>
<td>国家的 ISO-3611 numeric 代码</td>
<td>840</td>
</tr>
<tr>
<td>regionName</td>
<td>string</td>
<td>区域名</td>
<td>New York</td>
</tr>
<tr>
<td>regionCode</td>
<td>string</td>
<td>区域代码</td>
<td>US-NY</td>
</tr>
<tr>
<td>cityName</td>
<td>string</td>
<td>城市名</td>
<td>new york</td>
</tr>
<tr>
<td>latitude</td>
<td>number</td>
<td>经度</td>
<td>40.742802</td>
</tr>
<tr>
<td>longitude</td>
<td>number</td>
<td>纬度</td>
<td>-73.971199</td>
</tr>
</tbody></table>

## 实例方法

### arrayBuffer
`arrayBuffer(): Promise<ArrayBuffer>`
返回一个 Promise，包含一个 [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) 对象，表示整个请求体。

### blob
`blob(): Promise<Blob>`
返回一个 Promise，包含一个 [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob) 对象，表示整个请求体。

### clone
`clone(copyHeaders?: boolean): Request`
创建当前请求对象的副本，若未设置 copyHeaders 或者 copyHeaders 为 false，返回的副本 Request 对象将会引用 headers 成员。
>?标准未提供 copyHeaders 参数，添加此参数主要是出于性能的考虑，避免无意义的拷贝。

### json
`json(): Promise<object>`
返回一个 Promise，包含一个 JSON 对象，表示整个请求体。

### text
`text(): Promise<string>`
返回一个 Promise, 包含一个 string，表示整个请求体。

### getCookies
`getCookies(): Cookies`
获取 [Cookies](https://cloud.tencent.com/document/product/1552/81905) 对象，会自动解析 Cookie 头部，绑定 Cookies 对象到 Request。

### setCookies
`setCookies(values: Cookies): boolean`
设置 [Cookies](https://cloud.tencent.com/document/product/1552/81905) 对象，会忽略已有 Cookie 头部，以新设置的 Cookies 对象生成新的 Cookie 头部。

## 示例代码
```typescript
async function handleRequest() {
    const request = new Request('https://www.qq.com');
    const resA = await fetch(request);
}

addEventListener('fetch', (event) => {
  return event.respondWith(handleRequest(event));
}
```

## 相关参考
- [MDN 官方文档：Request](https://developer.mozilla.org/en-US/docs/Web/API/Request)
- [代码案列：修改请求头](https://cloud.tencent.com/document/product/1552/81938)
