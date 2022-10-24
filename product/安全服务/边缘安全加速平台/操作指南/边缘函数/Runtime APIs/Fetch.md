# Fetch
`fetch` API 提供了在 worker 中通过 HTTP 请求异步请求资源的能力

## 语法
```typescript
function fetch(resource: string | Request, init?: RequestInit): Promise<Response>
```

- resource<br>
&emsp;指定将要获取的资源;<br>
- init 可选<br>
&emsp;一个可选对象，包含希望被设置到此次请求中的属性选项，参考 [`RequestInit`](Request.md)

## 重定向

`fetch` 支持 3xx 重定向；包含 301、302、303、307 和 308 状态码，具体的行为可以通过 `RequestInit` 中的 `redirect` 属性设置，标准支持设置以下值：
- `manual`: 不主动跟随 3xx，由用户自行处理
- `error`: 遇到 3xx 状态码则抛出异常
- `follow`: 主动跟随 3xx; **默认行为**

根据 [fetch 标准](https://fetch.spec.whatwg.org/#http-redirect-fetch)，针对不同状态码有不同的跟随方案：

| 状态码     |               重定向方案                |
|---------|:----------------------------------:|
| 301、302 |       `POST` 方法被转为 `GET` 方法        |
| 303     | 除 `HEAD`/`GET` 外的所有方法都被转为 `GET` 方法 |
| 307、308 |               保留原始方法               |

除标准规定的 `redirect` 属性之外，还可以在 [`RequestInit`](Request.md)通过 `maxFollow` 属性配置最大可跟随次数，默认为 12；并且可以在 [`Response`](Response.md) 中通过 `redirectUrls` 获取所有重定向的 url 列表。

注意：

- 重定向的地址来源于响应中的 `Location` 头，如果未出现该头部，则不会跟随重定向
- `Location` 头部值可以是绝对 URL 或者相对 URL(参考 [RFC-3986: URI Reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.1))
- 重定向请求的 `Host` 头部：分三种情况：
  - 如果 `Location` 是相对地址，则维持原有的 `Host` 头部不变
  - 如果 `Location` 指定了主机(通过 [Absolute URI](https://www.rfc-editor.org/rfc/rfc3986#section-4.2) 或者 [network-path reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2))，且是以 IP 形式，则维持原有 `Host` 不变
  - 如果 `Location` 指定了主机，且是以域名形式，则使用 `Location` 头部值中的域名作为重定向请求的 `Host` 头部

## `fetch(event.request)` 回源

目前支持对客户请求(`event.request`)发起 `fetch` 操作进行回源。该操作会触发原CDN流程，请求CDN配置指定的源站。如果命中缓存则使用缓存。

- 注意这里 `fetch` 的传入参数使用的是原始的客户请求对象 `event.request` ，只有该用法下才是CDN回源的语义
- 如果使用的并非原始的客户请求对象，比如新创建的Request对象作为 `fetch` 参数，则为普通子请求

## 运行时限制

考虑到 worker 的性能以及安全性，目前对 `fetch` API 的调用有如下限制：

- 次数限制：worker 的单次运行过程中总共可发起的 `fetch` 操作数目，默认为 64；超过该限制值之后的所有 `fetch` 操作都会直接失败抛出异常
- 并发限制：worker 的单次运行过程中允许存在的最大未被 resolve 的 `fetch` 操作数目，默认为 8；超过该限制值之后的所有 `fetch` 操作都将被延迟发起，直到某个正在运行着的 `fetch` 被 resolve

注意：

- 每一次重定向都算一次请求，且其优先级高于新发起的 `fetch` 操作

## 示例

- 使用 IP 地址标识目标主机并发起请求

```js
fetch('https://[2001::1f0d:4120]:443/', {
    headers: {
        'Host': 'www.google.com',
    }
}).then((rsp) => {
  log(rsp.url, rsp.statusText);
});
```

- 发起 POST 请求

```js
fetch(testUrl, {
  method: 'POST',
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    id: 1,
    title: "xxxx",
  }),
});
```

- 自动跟随重定向

```js
let resp = await fetch("http://open.iciba.com/dsapi", {
    method: "GET",
    headers: {
        Host: "open.iciba.com",
    },
    maxFollow: 3,
    redirect: 'follow',
    version: 'HTTP/1.1',
});

console.log('urls used during redirection: ',
            JSON.stringify(resp.redirectUrls));
```

- 使用 HTTP/2

```js
let p1 = fetch('https://www.google.com/search?q=laputa&oq=laputa&aqs=chrome.0.69i59j69i60l6j69i65.2348j0j1&sourceid=chrome&ie=UTF-8', {
    method: 'GET',
    headers: {
        'Host': 'www.google.com',
    },
    redirect: 'manual',
    version: 'HTTP/2.0',
})
```

- `fetch(event.request)` 回源

```js
async function handleRequest(request) {
    return fetch(request});
}
```

## 参考
* [fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch)
