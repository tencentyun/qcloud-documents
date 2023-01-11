基于 Web APIs 标准 [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) 进行设计。边缘函数运行时可使用 `fetch` 发起异步请求，获取远程资源。

## 描述 
```typescript
function fetch(request: string | Request, init?: RequestInit): Promise<Response>
```

### 参数

<table>
  <thead>
    <tr>
      <th width="15%">参数名称</th>
      <th width="15%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>request</td>
      <td>
        string | <br>
        <a href="https://cloud.tencent.com/document/product/1552/81902">Request</a>
      </td>
      <td>是</td>
      <td>指定将要获取的请求资源。</li>
      </td>
    </tr>
    <tr>
      <td>init</td>
      <td><a href="https://cloud.tencent.com/document/product/1552/81902#RequestInit">RequestInit</a></td>
      <td>否</td>
      <td>
        请求对象的初始化配置项。详情请参见 <a href="https://cloud.tencent.com/document/product/1552/81902#RequestInit">RequestInit</a>。
      </td>
    </tr>
  </tbody>
</table>

## CDN 回源
在边缘函数中，使用 `fetch(request)` 发起子请求时，由边缘函数直接向公网发起 HTTP 请求。但 `fetch(event.request)` 发起请求时，该请求会由 CDN Server 接管，并执行当前域名的 `EdgeOne CDN` 的配置，若不存在 CDN 缓存，则向源站重新拉取数据。

>! 当前仅支持 `fetch(event.request)` 发起的请求会执行 `EdgeOne CDN` 回源链路。即下述方式均无效：
>- **不支持**构造 Request 对象，用于 `fetch(request)` 发起执行 CDN 回源链路。
>- **不支持**传递第二个参数（请求对象的初始化配置项），用于`fetch(event.request, init)` 发起执行 CDN 回源链路。

- 参考下述示例代码

```typescript
addEventListener('fetch', async (event) => {
  // 发起请求，执行 EdgeOne CDN 回源链路
  const response = await fetch(event.request);
  event.respondWith(response);
});
```

## 重定向

`fetch` 支持 `3xx` 重定向状态码。可使用第二个参数 `init.redirect` 属性进行设置，更多重定向配置，请查看 [RequestInit](https://cloud.tencent.com/document/product/1552/81902#RequestInit)。


- 重定向规则遵从 Web APIs 标准 [fetch API](https://fetch.spec.whatwg.org/#http-redirect-fetch)，针对不同状态码有不同的跟随规则：

<table>
  <thead>
    <tr>
      <th width="30%">状态码</th>
      <th width="70%">重定向规则</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>301、302</td>
      <td><code>POST</code> 方法被转为 <code>GET</code> 方法。</td>
    </tr>
    <tr>
      <td>303</td>
      <td>除 <code>HEAD</code> / <code>GET</code> 外的所有方法都被转为 <code>GET</code> 方法。</td>
    </tr>
    <tr>
      <td>307、308</td>
      <td>保留原始方法。</td>
    </tr>
  </tbody>
</table>

>! 重定向的地址来源于响应头 `Location`，若无该响应头，则不会重定向。

- 响应头 `Location` 值可以是绝对 URL 或者相对 URL，详情参见 [RFC-3986: URI Reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.1)。

## 运行时限制
边缘函数中使用 `fetch` 发起请求，存在以下限制：
- 次数限制：边缘函数单次运行中可发起的 `fetch` 总次数为 64，超过该限制的 `fetch` 请求会请求失败，并抛出异常。
- 并发限制：边缘函数单次运行中允许发起 `fetch` 最大并发数为 8，超过该限制的 `fetch` 请求会被延迟发起，直到某个正在运行着的 `fetch` 被 resolve。

>!每一次重定向都会计入请求次数，且其优先级高于新发起的 `fetch` 请求。

## 示例代码
```js
async function handleEvent(event) {
  const response = await fetch('https://www.tencentcloud.com/');
  return response;
}

addEventListener('fetch', (event) => {
  event.respondWith(handleEvent(event));
});
```

## 相关参考 
- [MDN 官方文档：fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch)
- [示例函数：获取远程资源返回](https://cloud.tencent.com/document/product/1552/84083)
