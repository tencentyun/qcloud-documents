**Response** 代表 HTTP 响应，基于 Web APIs 标准 [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) 进行设计。

>? 边缘函数中，可通过两种方式获得 `Response` 对象：
- 使用 `Response` 构造函数创建一个 Response 对象，用于 [event.respondWith](https://cloud.tencent.com/document/product/1552/81899#respondwith) 响应。
- 使用 <a href="https://cloud.tencent.com/document/product/1552/81897">fetch</a> 获取请求响应 Response 对象。

## 构造函数
```typescript
const response = new Response(body?: string | ArrayBuffer | Blob | ReadableStream | null | undefined, init?: ResponseInit);
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
      <td>body</td>
      <td>
        string | <br/>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer">ArrayBuffer</a> | <br/>
        <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob">Blob</a> | <br/>
        <a href="https://cloud.tencent.com/document/product/1552/81914">ReadableStream</a> | <br/>
        null | <br/>
        undefined
      </td>
      <td>是</td>
      <td><code>Response</code> 对象的 body 内容。</td>
    </tr>
    <tr>
      <td>init</td>
      <td><a href="#ResponseInit">ResponseInit</a></td>
      <td>否</td>
      <td><code>Response</code> 对象的初始化配置项。</td>
    </tr>
  </tbody>
</table>

#### ResponseInit[](id:ResponseInit)

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
      <td align="left">status</td>
      <td align="left">number</td>
      <td align="left">否</td>
      <td align="left">响应的状态码。</td>
    </tr>
    <tr>
      <td align="left">statusText</td>
      <td align="left">string</td>
      <td align="left">否</td>
      <td align="left">响应的状态消息，最大长度为 4095，超出长度会被截断。</td>
    </tr>
    <tr>
      <td align="left">headers</td>
      <td align="left"><a href="https://cloud.tencent.com/document/product/1552/81903">Headers</a></td>
      <td align="left">否</td>
      <td align="left">响应的头部信息。</td>
    </tr>
  </tbody>
</table>

## 属性
### body[](id:body)
```typescript
// response.body
readonly body: ReadableStream;
```
响应体，详情参见 [ReadableStream](https://cloud.tencent.com/document/product/1552/81914)。

### bodyUsed
```typescript
// response.bodyUsed
readonly bodyUsed: boolean;
```

标识响应体是否已读取。

### headers
```typescript
// response.headers
readonly headers: Headers;
```

响应头部，详情参见 [Headers](https://cloud.tencent.com/document/product/1552/81903)。

### ok
```typescript
// response.ok
readonly ok: boolean;
```

标识响应是否成功（状态码在 200-299 范围内）。

### status
```typescript
// resposne.status
readonly status: number;
```
响应状态代码。

### statusText
```typescript
// resposne.statusText
readonly statusText: string;
```

响应的状态消息。

### url
```typescript
// response.url
readonly url: string;
```
响应的 url。

### redirected
```typescript
// response.redirected
readonly redirected: boolean;
```

标识响应是否为重定向的结果。

### redirectUrls
```typescript
// response.redirectUrls
readonly redirectUrls: Array<String>
```

所有重定向 URL。

## 方法

>! 获取响应体方法，接收 `HTTP body` 最大字节数为 1M，超出大小会抛出 OverSize 异常。超出大小时推荐使用 [response.body](#body) 流式读取，详情参见 [ReadableStream](https://cloud.tencent.com/document/product/1552/81914)。


### arrayBuffer
```typescript
request.arrayBuffer(): Promise<ArrayBuffer>;
```
获取响应体，解析结果为 [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) 。

### blob
```typescript
request.blob(): Promise<Blob>;
```
获取响应体，解析结果为 [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob)。

### clone
```typescript
request.clone(copyHeaders?: boolean): Request;
```

创建响应对象的副本。

#### 参数

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
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
        开启复制响应头，默认值为 <code>false</code>，取值说明如下。<br/>
        <li>
          <font color="#9ba6b7">true</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            复制原对象的响应头。
          </div>
        </li>
        <li>
          <font color="#9ba6b7">false</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            引用原对象的响应头。
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

获取响应体，解析结果为 `json`。

### text
```typescript
request.text(): Promise<string>;
```

获取响应体，解析结果为文本字符串。

### getCookies
```typescript
request.getCookies(): Cookies;
```

获取 `response` 头部 cookie，并自动解析为 [Cookies](https://cloud.tencent.com/document/product/1552/83932) 对象。

### setCookies
```typescript
request.setCookies(cookies: Cookies): boolean;
```

设置 `response` 头部 cookie 值。 

## 示例代码
```typescript
addEventListener('fetch', (event) => {
  const response =  new Response('hello world');
  event.respondWith(response);
});
```

## 相关参考 
- [MDN 官方文档：Response](https://developer.mozilla.org/en-US/docs/Web/API/Response)
- [示例函数：返回 HTML 页面](https://cloud.tencent.com/document/product/1552/81941)
- [示例函数：修改响应头](https://cloud.tencent.com/document/product/1552/81937)
- [示例函数：AB测试](https://cloud.tencent.com/document/product/1552/81934)
