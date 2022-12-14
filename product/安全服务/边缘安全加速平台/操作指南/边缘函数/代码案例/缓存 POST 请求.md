

使用 Cache API 缓存 POST 请求

```js
async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

  return [...new Uint8Array(hashBuffer)].map(b => b.toString(16).padStart(2, '0')).join('');
}

async function handlePostRequest(event) {
  const request = event.request;
  const body = await request.clone().text();

  // 根据 body 计算 hash
  const hash = await sha256(body);
  const cacheUrl = new URL(request.url);

  cacheUrl.pathname = '/post' + cacheUrl.pathname + hash;

  // 构建 cacheKey
  const cacheKey = new Request(cacheUrl.toString(), {
    headers: request.headers,
    method: 'GET',
  });
  
  const cache = caches.default;
  
  // 匹配缓存
  let response = await cache.match(cacheKey);
  
  // 缓存没有命中
  if (!response) {
    response = await fetch(request);
    event.waitUntil(cache.put(cacheKey, response.clone()));
  } else {
    log(`Cache hit for: ${cacheKey.url}.`);
  }

  return response;
}

addEventListener('fetch', (event) => {
  try {
    const request = event.request;
    // 处理 POST 请求
    if (request.method.toUpperCase() === 'POST') return event.respondWith(handlePostRequest(event));
    return event.respondWith(fetch(request));
  } catch (e) {
    return event.respondWith(new Response('Error thrown ' + e.message));
  }
});


```
