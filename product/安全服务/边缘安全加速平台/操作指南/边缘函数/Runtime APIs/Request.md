**Request** 代表 HTTP 请求对象，基于 Web APIs 标准 [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) 进行设计。

>? 边缘函数中，可通过两种方式获得 `Request` 对象：
- 使用 Request 构造函数创建一个 Request 对象，用于 Fetch API 的操作。
- 使用 FetchEvent 对象 [event.request](https://cloud.tencent.com/document/product/1552/81902)，获得当前请求的 Request 对象。

## 构造函数
```typescript
const request = new Request(input: string | Request, init?: RequestInit)
```

### 参数

<table>
  <thead>
    <tr>
      <th width="10%">参数名称</th>
      <th width="20%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>input</td>
      <td>
        string | <br/>
        <a href="https://cloud.tencent.com/document/product/1552/81902">Request</a>
      </td>
      <td>是</td>
      <td>URL 字符串或 Request 对象。</td>
    </tr>
    <tr>
      <td>options</td>
      <td><a href="#RequestInit">RequestInit</a></td>
      <td>否</td>
      <td>Request 对象初始化配置项。</td>
    </tr>
  </tbody>
</table>


#### RequestInit[](id:RequestInit)

初始化 Request 对象的属性值选项。

<table>
  <thead>
    <tr>
      <th width="15%">属性名</th>
      <th width="20%">类型</th>
      <th width="10%">必填</th>
      <th width="10%">默认值</th>
      <th width="45%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>method</td>
      <td>string</td>
      <td>否</td>
      <td>GET</td>
      <td>请求方法 (<code>GET</code>、<code>POST</code> 等)。</td>
    </tr>
    <tr>
      <td>headers</td>
      <td><a href="https://cloud.tencent.com/document/product/1552/81903">Headers</a></td>
      <td>否</td>
      <td>-</td>
      <td>请求头部信息。</td>
    </tr>
    <tr>
      <td>body</td>
      <td>
        string |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob">Blob</a> | <br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer">ArrayBuffer</a> | <br>
        ArrayBufferView | <br>
        <a href="https://cloud.tencent.com/document/product/1552/81914">ReadableStream</a>
      </td>
      <td>否</td>
      <td>-</td>
      <td>请求体。</td>
    </tr>
    <tr>
      <td>redirect</td>
      <td>string</td>
      <td>否</td>
      <td>follow</td>
      <td>重定向策略，支持 <code>manual</code>、<code>error</code> 和 <code>follow</code>。</td>
    </tr>
    <tr>
      <td>maxFollow</td>
      <td>number</td>
      <td>否</td>
      <td>12</td>
      <td>最大可重定向次数。</td>
    </tr>
    <tr>
      <td>version</td>
      <td>string</td>
      <td>否</td>
      <td>HTTP/1.1</td>
      <td>HTTP 版本，支持 <code>HTTP/1.0</code>、<code>HTTP/1.1</code> 和 <code>HTTP/2.0</code>。</td>
    </tr>
    <tr>
      <td>copyHeaders</td>
      <td>boolean</td>
      <td>否</td>
      <td>-</td>
      <td><strong>非 Web APIs 标准选项</strong>，表示是否拷贝传入的 Request 对象的 headers。</td>
    </tr>
    <tr>
      <td>eo</td>
      <td><a href="#RequestInitEoProperties">RequestInitEoProperties</a></td>
      <td>否</td>
      <td>-</td>
      <td><strong>非 Web APIs 标准选项</strong>，用于控制边缘函数处理该请求的行为。</td>
    </tr>
  </tbody>
</table>

#### RequestInitEoProperties[](id:RequestInitEoProperties)
非 Web APIs 标准选项，用于控制边缘函数处理该请求的行为。

<table>
  <thead>
    <tr>
      <th width="10%">参数名称</th>
      <th width="20%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">resolveOverride</td>
      <td align="left">string</td>
      <td align="left">否</td>
      <td align="left">
        用于 <a href="https://cloud.tencent.com/document/product/1552/81897">fetch</a> 请求下覆盖原有的域名解析, 支持指定域名或者 IP 地址。更多说明如下：
        <li>IP 不允许带 scheme 以及端口号。</li>
        <li>IPv6 无需使用方括号包裹。</li>
      </td>
    </tr>
  </tbody>
</table>


## 实例属性

### body[](id:body)
```typescript
// request.body
readonly body: ReadableStream;
```
请求体，详情参见 [ReadableStream](https://cloud.tencent.com/document/product/1552/81914)。

### bodyUsed
```typescript
// request.bodyUsed
readonly bodyUsed: boolean;
```

标识请求体是否已读取。

### headers
```typescript
// request.headers
readonly headers: Headers;
```

请求头部，详情参见 [Headers](https://cloud.tencent.com/document/product/1552/81903)。

### method
```typescript
// request.method
readonly method: string;
```

请求方法，默认值为`GET`。

### redirect
```typescript
// request.redirect
readonly redirect: string;
```

请求重定向策略，可取值有：`follow`、`error`、`manual`，默认为 `manual`。

### maxFollow
```typescript
// request.maxFollow
readonly maxFollow: number;
```

请求最大重定向次数。

### url
```typescript
// request.url
readonly url: string;
```

请求 url。

### version
```typescript
// request.version
readonly version: string;
```

请求使用的 HTTP 协议版本。

### eo
```typescript
// request.version
readonly eo: IncomingRequestEoProperties;
```
边缘函数提供的与当前请求相关的一些其他信息，详情参见 [IncomingRequestEoProperties](#IncomingRequestEoProperties)。

#### IncomingRequestEoProperties[](id:IncomingRequestEoProperties)

客户端请求 [event.request](https://cloud.tencent.com/document/product/1552/81902) 对象包含 `eo` 属性，其信息如下：

<table>
  <thead>
    <tr>
      <th width="25%">属性名</th>
      <th width="15%">类型</th>
      <th width="35%">说明</th>
      <th width="25%">示例值</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>geo</td>
      <td><a href="#GeoProperties">GeoProperties</a></td>
      <td>描述客户请求的位置信息。</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

#### GeoProperties[](id:GeoProperties)
描述客户请求的位置信息。
<table>
  <thead>
    <tr>
      <th width="25%">属性名</th>
      <th width="15%">类型</th>
      <th width="35%">说明</th>
      <th width="25%">示例值</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>asn</td>
      <td>number</td>
      <td><a href="https://en.wikipedia.org/wiki/Autonomous_system_(Internet)">ASN</a></td>
      <td>132203</td>
    </tr>
    <tr>
      <td>countryName</td>
      <td>string</td>
      <td>国家名</td>
      <td>Singapore</td>
    </tr>
    <tr>
      <td>countryCodeAlpha2</td>
      <td>string</td>
      <td>国家的 <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO-3611 alpha2</a> 代码</td>
      <td>SG</td>
    </tr>
    <tr>
      <td>countryCodeAlpha3</td>
      <td>string</td>
      <td>国家的 <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3">ISO-3611 alpha3</a> 代码</td>
      <td>SGP</td>
    </tr>
    <tr>
      <td>countryCodeNumeric</td>
      <td>string</td>
      <td>国家的 <a href="https://en.wikipedia.org/wiki/ISO_3166-1_numeric">ISO-3611 numeric</a> 代码</td>
      <td>702</td>
    </tr>
    <tr>
      <td>regionName</td>
      <td>string</td>
      <td>区域名</td>
      <td>-</td>
    </tr>
    <tr>
      <td>regionCode</td>
      <td>string</td>
      <td>区域代码</td>
      <td>AA-AA</td>
    </tr>
    <tr>
      <td>cityName</td>
      <td>string</td>
      <td>城市名</td>
      <td>singapore</td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>number</td>
      <td>纬度</td>
      <td>1.29027</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>number</td>
      <td>经度</td>
      <td>103.851959</td>
    </tr>
  </tbody>
</table>

## 实例方法

>! 获取请求体方法，接收 `HTTP body` 最大字节数为 1M，超出大小会抛出 OverSize 异常。超出大小时推荐使用 [request.body](#body) 流式读取，详情参见 [ReadableStream](https://cloud.tencent.com/document/product/1552/81914)。

### arrayBuffer
```typescript
request.arrayBuffer(): Promise<ArrayBuffer>;
```
获取请求体，解析结果为 [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) 。

### blob
```typescript
request.blob(): Promise<Blob>;
```
获取请求体，解析结果为 [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob)。

### clone
```typescript
request.clone(copyHeaders?: boolean): Request;
```

创建请求对象的副本。

#### 参数

<table>
	<thead>
		<tr>
			<th width="10%">参数名称</th>
			<th width="15%">类型</th>
			<th width="10%">必填</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>copyHeaders</td>
			<td>boolean</td>
			<td>否</td>
			<td>
        开启复制请求头，默认值为 <code>false</code>，取值说明如下。<br/>
        <li>
          <font color="#9ba6b7">true</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            复制原对象的请求头。
          </div>
        </li>
        <li>
          <font color="#9ba6b7">false</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            引用原对象的请求头。
          </div>
        </li>
      </td>
		</tr>
	</tbody>
</table>

### json
```typescript
request.json(): Promise<object>;
```

获取请求体，解析结果为 `json`。

### text
```typescript
request.text(): Promise<string>;
```

获取请求体，解析结果为文本字符串。

### getCookies
```typescript
request.getCookies(): Cookies;
```

获取 `request` 头部 cookie，并自动解析为 [Cookies](https://cloud.tencent.com/document/product/1552/83932) 对象。

### setCookies
```typescript
request.setCookies(cookies: Cookies): boolean;
```

设置 `request` 头部 cookie 值。 

#### 参数

<table>
	<thead>
		<tr>
			<th width="10%">参数名称</th>
			<th width="15%">类型</th>
			<th width="10%">必填</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>cookies</td>
			<td><a href="https://cloud.tencent.com/document/product/1552/83932">Cookies</a></td>
			<td>否</td>
			<td>
        新的 Cookies 对象。
      </td>
		</tr>
	</tbody>
</table>

## 示例代码
```typescript
async function handleRequest() {
  const request = new Request('https://www.tencentcloud.com/');
  const response = await fetch(request);
  return response;
}

addEventListener('fetch', (event) => {
  event.respondWith(handleRequest());
});
```

## 相关参考
- [MDN 官方文档：Request](https://developer.mozilla.org/en-US/docs/Web/API/Request)
- [示例函数：Cache API 使用](https://cloud.tencent.com/document/product/1552/84023)
- [示例函数：基于请求区域重定向](https://cloud.tencent.com/document/product/1552/84084)
