在边缘函数中，使用 `Cache API` 管理资源缓存。

```typescript
async function handleCache(event) {
  const request = event.request;
  const cacheUrl = new URL(request.url);
  const cacheKey = new Request(cacheUrl.toString(), {
    headers: request.headers,
    method: 'GET',
  });
  const cache = caches.default;

  try {
    // 获取关联的缓存 Response
    let response = await cache.match(cacheKey);

    if (!response) {
      // 缓存没有命中，回源并缓存
      response = await fetch(cacheKey);
      response = new Response(response.body, response);
      // 在响应头添加 Cahe-Control
      response.headers.append('Cache-Control', 's-maxage=300');
      event.waitUntil(cache.put(cacheKey, response.clone()));
    }
    return response;
  } catch (e) {
    const result = await cache.delete(cacheKey);

    return new Response(null, { status: parseInt(e.message) });
  }
}

addEventListener('fetch', (event) => {
  try {
    return event.respondWith(handleCache(event));
  } catch (e) {
    return event.respondWith(new Response('Error thrown ' + e.message));
  }
});
```

## 示例预览

在浏览器地址栏中输入边缘函数触发规则，即可预览到示例效果。

<img src="https://user-images.githubusercontent.com/117053395/207755578-69d6f9a8-af5a-4012-8fda-a29454cfd281.png" width=609px>

## 相关参考
- [Runtime APIs: Cache](https://cloud.tencent.com/document/product/1552/81893)
- [Runtime APIs: Fetch](https://cloud.tencent.com/document/product/1552/81897)
- [Runtime APIs: FetchEvent](https://cloud.tencent.com/document/product/1552/81899)
