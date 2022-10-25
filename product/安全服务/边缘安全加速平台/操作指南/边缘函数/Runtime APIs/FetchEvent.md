FetchEvent 代表任何传入的 HTTP 请求事件，边缘函数通过注册 "fetch" 事件的监听器实现对 HTTP 请求的处理。

## 语法
```typescript
class FetchEvent {
  readonly clientId: string;
  readonly request: Request;
  respondWith(resp: Response | Promise<Response>): void;
  waitUntil(p: Promise<any>): void;
}
```

### 属性
- clientID:  string<br>Workers 引擎内部为每一个请求分配的 id 标识，方便 Workers 内部的日志记录。
- request:   [Request](https://cloud.tencent.com/document/product/1552/81902)<br>客户端发送过来的 HTTP 请求。

### 方法
- respondWith(resp: [Response](https://cloud.tencent.com/document/product/1552/81901) | Promise<[Response](https://cloud.tencent.com/document/product/1552/81901)>)  void<br>回复响应给客户端。</br>
- waitUntil(p: Promise<any>):  void<br>waitUntil 方法用于通知 Workers 引擎等待 promise 的完成，延长了事件处理的生命周期。</br>

## 示例
```js
addEventListener('fetch', (event) => {
  event.respondWith(new Response('hello workers!'))
})
```
- 使用 waitUntil 方法异步上报统计数据
```js
async function report(req) {
  let headers = req.headers;
  headers.set('ClientURL', req.url);

  // do something ...

  return fetch('http://www.example.report.com/', {
    method: 'POST',
    headers: headers,
  });
}

addEventListener('fetch', (event) => {
  event.waitUntil(report(event.request));
  event.respondWith(Response('hello workers!'))
});
```
- 使用 waitUntil 方法异步缓存数据
```js
async function getCache(req) {
  // do something ...
  req.headers.set('Origin-Url', req.url);

  return fetch('http://www.example.cache.com/', {
    method: 'GET',
    headers: req.headers,
  });
}

async function setCache(req, rsp) {
  let headers = req.headers;
  headers.set('rsp-status', rsp.status);
  headers.set('rsp-statusText', rsp.statusText);
  // do something ...

  return fetch('http://www.example.cache.com/', {
    method: 'PUT',
    headers: headers,
    body: rsp.body,
  });
}

async function handleEvent(event) {
  let rsp = await getCache(event.request);
  if (rsp) {
    let status = rsp.headers.get('rsp-status');
    let statusText = rsp.headers.get('rsp-statusText');
    rsp.headers.delete('rsp-status');
    rsp.headers.delete('rsp-statusText');
    event.respondWith(rsp, {
      status: status,
      statusText: statusText,
    });
    return;
  }

  rsp = await fetch(event.request);
  let clone = rsp.clone();
  event.waitUntil(setCache(event.request, clone));
  event.respondWith(rsp);
}

addEventListener('fetch', (event) => {
  handleEvent(event);
});
```

## 参考
- [FetchEvent](https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent)
