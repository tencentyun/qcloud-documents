代表 HTTP 请求对象。 
- 可以通过 Request 构造函数来创建一个 Request 对象，用于后续的 fetch 操作。
- 也可以通过 FetchEvent 对象的 request 属性，得到一个 Request 对象。

## 语法
```typescript
class Request {
  readonly body: ReadableStream;
  readonly bodyUsed: boolean;
  readonly headers: Headers;
  readonly method: string;
  readonly url: string;
  readonly version: string
  readonly redirect: string;
  readonly maxFollow: number;
  readonly cf: IncomingRequestCfProperties;

  constructor(input: string | Request, init?: RequestInit);
  arrayBuffer(): Promise<ArrayBuffer>;
  blob(): Promise<Blob>;
  clone(copyHeaders?: boolean): Request;
  json(): Promise<object>;
  text(): Promise<string>;
  getCookies(): Cookies
  setCookies(cookies: Cookies): boolean
}

class RequestInit{
  method?: string;
  headers?: object | Array<[string, string]> | Headers;
  body?: string | Blob | ArrayBuffer | ArrayBufferView | ReadableStream;
  version?: string
  redirect?: string;
  maxFollow?: number
  copyHeaders?: boolean;
  cf?: RequestInitCfProperties
}

class RequestInitCfProperties{
  resolveOverride?: string;
  cacheEverything?: boolean;
  cacheKey?: string;
  cacheTtl?: number;
  cacheTtlByStatus?: {[key: string]: number};
}
```

## 构造方法

```typescript
let request = new Request(input [, options])
```

### 参数
- input<br>定义将要 fetch 的资源，取值有：<br>
  - 一个直接包含资源 url 的字符串。
  - 已存在的 Request 对象：拷贝传入的 Request 对象属性，并设置到返回的 Request 对象中，若 options 对象的 copyHeaders 属性为 false，则引用传入的 Request对象的 headers 属性。
- options  可选<br>一个可选对象，包含希望被设置到返回的 Request 对象中的属性选项。

#### RequestInit
- `method`：请求的方法，**必须是字符串类型，支持的最大长度为 4095，超出长度会被截断**。
- `headers`：请求的头部信息，详情请参见  [Headers](https://cloud.tencent.com/document/product/1552/81903)。
- `body`：请求体。
- `redirect`：重定向策略，字符串类型，支持 `manual`、`error` 和 `follow`；默认为 `follow`，即自动跟随重定向。
- `maxFollow`：最大可重定向次数，默认为 12。
- `version`：HTTP 版本，字符串类型，目前支持 `HTTP/1.0`、`HTTP/1.1` 和 `HTTP/2.0`，默认为 `HTTP/1.1`。
- `copyHeaders`：<b>非标准选项</b>，表示是否拷贝传入的 Request 对象的 headers 属性。
- `cf`: <b>非标准选项</b>，用于控制 workers 处理该请求的行为。

#### RequestInitCfProperties
一个对象，其中包含用于控制 workers 处理该请求的行为的属性：
- `resolveOverride`：在通过 `fetch(event.request)` 进行 CDN 回源时使用，用于指定源站域名(目前只支持域名，如 `www.qq.com`，不支持指定 HTTP 协议或者端口号)。
- `cacheEverything`：缓存相关，用于指定缓存响应的所有头部。
- `cacheKey`：缓存相关，用于指定自定义的缓存 key。
- `cacheTtl`: 缓存相关，用于指定缓存时长(单位s)，必需大于等于0，等于0不缓存。
- `cacheTtlByStatus`：缓存相关，用于根据状态码指定缓存时长(单位 s)，小于等于0不缓存。

### 属性
- body:  [ReadableStream](https://cloud.tencent.com/document/product/1552/81914)<br>请求体。
- bodyUsed:  `boolean`<br>标识请求体是否已读取。
- headers:  [Headers](https://cloud.tencent.com/document/product/1552/81903)<br>请求头部。
- method:  `string`<br>请求方法，缺省值为"GET"。
- redirect:  `string`<br>请求被重定向后的处理方式：follow、error、manual，默认为 manual。
- maxFollow:  `number`<br>请求最多可重定向的次数。
- url:  `string`<br>请求的 url。
- version:  `string`<br>请求使用的 HTTP 协议版本。
- cf：`IncomingRequestCfProperties`<br>一个对象，其中包含了由边缘安全加速平台提供的与客户请求相关的属性。

#### IncomingRequestCfProperties
除了标准 `Request` 对象的属性外，客户请求的 `request.cf` 对象中还包含由边缘安全加速平台提供的与请求相关的一些其他信息。目前包含如下信息：

- `geo`: 一个对象，用于描述客户请求的位置，其中包含如下数据：
  - `asn`Number<br>自治区号，例如12271。
  - `countryName`String<br>国家名，例如 `"United States of America"`。
  - `countryCodeAlpha2`String<br>国家的 ISO-3611 alpha2 代码，例如 `"US"`。
  - `countryCodeAlpha3`String<br>国家的 ISO-3611 alpha3 代码，例如 `"USA"`。
  - `countryCodeNumeric`String<br>国家的 ISO-3611 numeric 代码，例如 `"840"`。
  - `regionName`String<br>区域名，例如 `"New York"`。
  - `regionCode`String<br>区域代码，例如 `"US-NY"`。
  - `cityName`String<br>城市名，例如 `"new york"`。
  - `latitude`Number<br>经度，例如40.742802。
  - `longitude`Number<br>纬度，例如 -73.971199。

### 方法
- arrayBuffer():  Promise&lt;ArrayBuffer&gt;<br>读取整个请求体，Returns a promise that resolves with an ArrayBuffer。
- blob():  Promise&lt;Blob&gt;<br>读取整个请求体，Returns a promise that resolves with an Blob。
- clone(copyHeaders?: boolean):  Request
 - 创建当前请求对象的副本，若未设置 copyHeaders 或者 copyHeaders 为 false，返回的副本 Request 对象将会引用 headers 成员。
 - <b>标准未提供 copyHeaders 参数，添加此参数主要是出于性能的考虑，避免无意义的拷贝。</b>
- json():  Promise&lt;object&gt;<br>读取整个请求体，Returns a promise that resolves with a JSON representation of the request body。
- text():  Promise&lt;string&gt;<br>读取整个请求体，Returns a promise that resolves with a string (text) representation of the request body。
- getCookies():  [Cookies](./NonStandard/Cookies.md)<br>获取 Cookies 对象，会自动解析 Cookie 头部, 绑定 Cookies 对象到 Request。
- setCookies([Cookies](./NonStandard/Cookies.md)):  boolean<br>设置 Cookies 对象，会忽略已有 Cookie 头部，以新设置的 Cookies 对象生成新的 Cookie 头部。

## 示例
### 创建请求对象
- 创建默认的请求对象
```js
let url = 'http://www.example.com/';
let req = new Request(url);

fetch(req).then((rsp) => {
  // do something ...
});
```

- 根据已有的 Request 对象来创建
```js
addEventListener('fetch', (event) => {
  let req = new Request(event.request);
  // do something ...

  fetch(req).then((rsp) => {
    // do something ...

    // event.respondWith(...);
  });
});
```
此处 req 对象的 headers 成员，是直接引用 event.request's headers 成员。如需拷贝 headers，则需要添加 copyHeaders 选项。
```js
addEventListener('fetch', (event) => {
  let req = new Request(event.request, {copyHeaders: true});
  // do something ...

  fetch(req).then((rsp) => {
    // do something ...

    // event.respondWith(...);
  });
});
```

- 通过 `RequestInit` 对象来设置新创建的 Request 对象
```js
let url = 'http://www.example.com/';
let req = new Request(url, {
  method: 'DELETE',
  headers: {
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
  },
  body: 'id=100',
});
```
```js
addEventListener('fetch', (event) => {
  let req = new Request(event.request, {
    method: 'DELETE',
  });
  // do something ...

  fetch(req).then((rsp) => {
    // do something ...

    // event.respondWith(...);
  });
});
```

### 读取请求体
- 以文本方式读取
```js
async function handleEvent(event) {
  let data = await event.request.text();
  log('data:' + data);
}

addEventListener('fetch', (event) => {
  handleEvent(event);
});
```
- 按 JSON 解析请求体
```js
let req = new Request('http://jsonplaceholder.typicode.com/posts/2', {
  method: 'POST',
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    userId: 100,
    title: "hello",
  }),
});

req.json().then((post) => {
  log("userId:", post.userId);
  log("title:", post.title);
});
```

### Cookies 对象操作
- 获取 Cookies 对象
```js
const url = "http://qq.com";
let req = new Request(url, {
      method: "GET",
      headers: {
        "Cookie": "k1=v1; k2=v2",
      },
    });
let h = req.headers.get("Cookie");
log.info("cookie header:", h);  // k1=v1; k2=v2

let cookies = req.getCookies();
let cks = cookies.get();
// name: k1 value: v1
// name: k2 value: v2
for(let i = 0; i < cks.length; i++) {
  log.info("name:", cks[i].name, "value:", cks[i].value);
}

h = req.headers.get("Cookie");
log.info("cookie header:", h);  // k1=v1; k2=v2
```
- 设置 Cookies 对象
```js
const url = "http://qq.com";
let req = new Request(url);
let cookies = new Cookies();
cookies.set("k1", "v1");
req.setCookies(cookies);

cookies = req.getCookies();
let ck = cookies.get();
log.info("val:", ck.value);  // v1
```

## 参考
* [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request)
