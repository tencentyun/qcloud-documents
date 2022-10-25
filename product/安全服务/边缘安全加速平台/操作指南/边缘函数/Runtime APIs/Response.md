# Response
代表 HTTP 响应对象
1) 可以通过 Response 构造函数来创建一个 Response 对象，用于后续 FetchEvent.respondWith 方法对请求的回复;
2) 也可以通过 fetch 操作，得到子请求的响应对象 Response;

## 语法
```typescript
class Response {
  readonly body: ReadableStream;
  readonly bodyUsed: boolean;
  readonly headers: Headers;
  readonly ok: boolean;
  readonly status: number;
  readonly statusText: string;
  readonly url: string;
  readonly redirected: boolean;
  readonly redirectUrls: Array<String>

  constructor(body?: null | undefined | string | ArrayBuffer | Blob | ReadableStream, options?: ResponseInit);
  arrayBuffer(): Promise<ArrayBuffer>;
  blob(): Promise<Blob>;
  clone(copyHeaders?: boolean): Response;
  json(): Promise<object>;
  text(): Promise<string>;
  getCookies(): Cookies
  setCookies(cookies: Cookies): boolean
}

class ResponseInit {
  status?: number;
  statusText?: string;
  headers?: object | Array<[string, string]> | Headers;
}
```

### 构造方法
- body  可选<br>
&emsp;可选参数，用于定义 Response 对象的 body 成员<br>
- options  可选<br>
&emsp;可选参数，包含希望被设置到返回的 Response 对象中的属性选项。可用的选项如下：<br>
  - status: 响应的状态码;
  - statusText: 响应的状态码相关联的状态信息, **必须是字符串类型，支持的最大长度为 4095，超出长度会被截断**;
  - headers: 响应的头部信息, 参考 [Headers](Headers.md);

### 属性
- body:  [ReadableStream](Streams/ReadableStream.md)<br>
&emsp;响应体
- bodyUsed:  `boolean`<br>
&emsp;标识响应体是否已读取
- headers:  [Headers](Headers.md)<br>
&emsp;响应头部
- ok:  `boolean`<br>
&emsp;标识响应是否成功(状态码在 200-299 范围内)
- status:  `number`<br>
&emsp;响应的状态代码
- statusText:  `string`<br>
&emsp;响应的状态消息
- url:  `string`<br>
&emsp;响应的 url
- redirected:  `boolean`<br>
  &emsp;标识该响应是否是重定向的结果
- redirectUrls:  `Array<string>`<br>
  &emsp;重定向过程中使用的所有 URL

### 方法
- arrayBuffer():  Promise&lt;ArrayBuffer&gt;<br>
&emsp;读取整个响应体，Returns a promise that resolves with an ArrayBuffer.
- blob():  Promise&lt;Blob&gt;<br>
&emsp;读取整个响应体，Returns a promise that resolves with an Blob.
- clone(copyHeaders?: boolean):  Request<br>
&emsp;创建当前响应对象的副本，若未设置copyHeaders或者copyHeaders为false, 返回的副本Response对象将会引用headers成员.<br>
&emsp;<b>标准未提供copyHeaders参数, 添加此参数主要是出于性能的考虑，避免无意义的拷贝;</b><br>
- json():  Promise&lt;object&gt;<br>
&emsp;读取整个响应体，Returns a promise that resolves with a JSON representation of the response body.
- text():  Promise&lt;string&gt;<br>
&emsp;读取整个响应体，Returns a promise that resolves with a string (text) representation of the response body.
- getCookies():  [Cookies](./NonStandard/Cookies.md)<br>
&emsp;获取 Cookies 对象. 会自动解析 Set-Cookie 头部, 绑定 Cookies 对象到 Response.
- setCookies([Cookies](./NonStandard/Cookies.md)):  boolean<br>
&emsp;设置 Cookies 对象. 会忽略已有 Set-Cookie 头部, 以新设置的 Cookies 对象生成新的 Set-Cookie 头部.

## 示例

### 创建 Response 对象
* 创建默认的 Response 对象<br>

```js
addEventListener('fetch', (event) => {
  let rsp = new Response();
  event.respondWith(rsp);
});
```

* 创建带有 body 数据的 Response 对象<br>

```js
addEventListener('fetch', (event) => {
  let rsp = new Response("hello world!");
  event.respondWith(rsp);
});
```

* 通过 options 对象来设置新创建的 Response 对象<br>

```js
addEventListener('fetch', (event) => {
  let rsp = new Response("<h1>hello world!</h1>", {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
    },
  });
  event.respondWith(rsp);
});
```

### 读取响应体
* 以文本形式读取<br>

```js
fetch('http://www.example.com/').then((rsp) => {
  rsp.text().then((data) => {
    log(data);
  });
});
```

* 按 json 解析响应体<br>

```js
async function handleEvent(event) {
  let req = new Request('http://jsonplaceholder.typicode.com/posts/2', {
    headers: {
      "User-Agent": "curl/7.71.1",
      "Accept": "*/*",
    },
  });

  let resp = await fetch(req);
  let post = await resp.json();
  log("post.userId:", post.userId);
  log("post.id:", post.id);
  log("post.title:", post.title);
  log("post.body:'" + post.body + "'");

  event.respondWith(Response(post.body + "\n", {
    headers: {
      id: post.id,
      userId: post.userId,
      title: "'" + post.title + "'",
    },
  }));
}

addEventListener('fetch', (event) => {
  handleEvent(event);
});
```

### Cookies 对象操作
* 获取 Cookies 对象<br>

```js
let rsp = new Response("hello workers!", {
  status: 200,
  headers: {
    "Set-Cookie": "k1=v1; Domain=qq.com; Path=/; HttpOnly",
  },
});
let h = rsp.headers.get("Set-Cookie");
log.info("setcookie header:", h);  // k1=v1; Domain=qq.com; Path=/; HttpOnly

let cookies = rsp.getCookies();
let ck = cookies.get();
log.info("val:", ck.value, "domain:", ck.domain, "path:", ck.path, "httponly:", ck.httponly);  // val: v1 domain: qq.com path: / httponly: true

h = rsp.headers.get("Set-Cookie");
log.info("setcookie header:", h);  // k1=v1; Domain=qq.com; Path=/; HttpOnly
```

* 设置 Cookies 对象<br>

```js
let rsp = new Response();
let cookies = new Cookies();
cookies.set("k1", "v1");
rsp.setCookies(cookies);

cookies = rsp.getCookies();
let ck = cookies.get();
log.info("val:", ck.value);  // v1
```

## 参考
* [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response)