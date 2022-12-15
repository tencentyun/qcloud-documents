在边缘函数中，使用 `Cache API` 缓存 POST 请求。

```typescript
function uint8ArrayToHex(arr) {
  return Array.prototype.map.call(arr, (x) => (('0' + x.toString(16)).slice(-2))).join('');
}

// sha256 签名摘要
async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

  return uint8ArrayToHex(new Uint8Array(hashBuffer));
}

async function handleRequest(event) {
  const request = event.request;
  const body = await request.clone().text();

  // 根据 request body 计算 hash
  const hash = await sha256(body);
  const cacheUrl = new URL(request.url);

  cacheUrl.pathname = '/post' + cacheUrl.pathname + hash;

  // 构建 cacheKey
  const cacheKey = new Request(cacheUrl.toString(), {
    headers: request.headers,
    method: 'GET',
  });

  const cache = caches.default;

  // 获取关联的缓存 Response
  let response = await cache.match(cacheKey);

  if (!response) {
    // 缓存没有命中，回源并使用缓存
    response = await fetch(request);
    event.waitUntil(cache.put(cacheKey, response.clone()));
  }

  return response;
}

addEventListener('fetch', (event) => {
  try {
    const request = event.request;
    // 处理 POST 请求
    if (request.method.toUpperCase() === 'POST') {
      return event.respondWith(handleRequest(event));
    }
    // 非post 请求
    return event.respondWith(fetch(request));
  } catch (e) {
    return event.respondWith(new Response('Error thrown ' + e.message));
  }
});
```


## 示例预览

在浏览器地址栏中输入边缘函数触发规则，即可预览到示例效果。

<img src="https://user-images.githubusercontent.com/117053395/207755071-06ec4067-8071-42d7-b871-d74c67d67caf.png" width=609px>

## 相关参考
- [Runtime APIs: Fetch](https://cloud.tencent.com/document/product/1552/81897)
- [Runtime APIs: Cache](https://cloud.tencent.com/document/product/1552/81893)
