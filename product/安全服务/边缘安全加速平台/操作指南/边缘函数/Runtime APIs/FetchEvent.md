**FetchEvent** 代表任何传入的 HTTP 请求事件，边缘函数通过注册 `fetch` 事件监听器实现对 HTTP 请求的处理。

## 描述
在边缘函数中，使用 [addEventListener](https://cloud.tencent.com/document/product/1552/81928) 注册 `fetch` 事件监听器，生成 HTTP 请求事件 [FetchEvent](https://cloud.tencent.com/document/product/1552/81899) ，进而实现对 HTTP 请求的处理。

>! 不支持直接构造 `FetchEvent` 对象，使用 `addEventListener` 注册 `fetch` 事件获取 `event` 对象。

```typescript
// event 为 FetchEvent 对象
addEventListener('fetch', (event) => {
  event.respondWith(new Response('hello world!'))；
});
```

## 属性

### clientId

```typescript
// event.clientId
readonly clientId: string;
```

边缘函数为每一个请求分配的 id 标识。

### request
```typescript
// event.request
readonly request: Request;
```
客户端发起的 HTTP 请求对象，详情参见 [Request](https://cloud.tencent.com/document/product/1552/81902)。

## 方法
### respondWith

```typescript
event.respondWith(response: Response | Promise<Response>): void;
```

边缘函数接管客户端的请求，并使用该方法，返回自定义响应内容。 

>! 事件监听器 `addEventListener` 的 `fetch` 事件回调中，需要调用接口 `event.respondWith()` 响应客户端，若未调用该接口，边缘函数会将当前请求转发回源站。

#### 参数
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
      <td>response</td>
      <td>
        <a href="https://cloud.tencent.com/document/product/1552/81917">Response</a> | 
        Promise&lt;<a href="https://cloud.tencent.com/document/product/1552/81917">Response</a>&gt;
      </td>
      <td>是</td>
      <td>
        客户端 HTTP 请求的响应。
      </td>
    </tr>
  </tbody>
</table>

### waitUntil
```typescript
event.waitUntil(task: Promise<any>): void;
``` 
用于通知边缘函数等待 `Promise` 完成，可延长事件处理的生命周期。

#### 参数
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
      <td>task</td>
      <td>
        Promise&lt;<a href="https://cloud.tencent.com/document/product/1552/81917">Response</a>&gt;
      </td>
      <td>是</td>
      <td>
        等待完成的 Promise 任务。 
      </td>
    </tr>
  </tbody>
</table>

### passThroughOnException
```typescript
event.passThroughOnException(): void;
```

用于防止运行时响应异常信息。当函数代码抛出未处理的异常时，边缘函数会将此请求转发回源站，进而增强服务的可用性.

## 示例代码
- 未调用接口 `event.respondWith`，边缘函数将当前请求转发回源站。

```typescript
function handleRequest(request) {
  return new Response('Edge Functions, Hello World!');
}

addEventListener('fetch', event => {
  const request = event.request;
  // 请求 url 包含字符串 /ignore/ ，边缘函数会将当前请求转发回源站。
  if (request.url.indexOf('/ignore/') !== -1) {
    // 未调用接口 event.respondWith
    return;
  }

  // 在边缘函数中，自定义内容响应客户端
  event.respondWith(handleRequest(request));
});
```

- 当函数代码抛出未处理的异常时，边缘函数会将此请求转发回源站。

```typescript
addEventListener('fetch', event => {
  // 当函数代码抛出未处理的异常时，边缘函数会将此请求转发回源站 
  event.passThroughOnException();
  throw new Error('Throw error');
});
```

## 相关参考 
- [MDN 官方文档：FetchEvent](https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent)
- [示例函数：返回 HTML 页面](https://cloud.tencent.com/document/product/1552/81941)
- [示例函数：Cache API 使用](https://cloud.tencent.com/document/product/1552/84023)
