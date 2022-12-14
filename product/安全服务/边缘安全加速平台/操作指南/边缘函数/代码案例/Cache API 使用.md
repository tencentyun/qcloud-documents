Cache API 的使用（put，match，delete）

```js
async function handleCache(event) {
  const request = event.request;
  const cacheKey = new Request("http://www.hello-world.com", request);
  const cache = caches.default;

  try {
    let response = await cache.match(cacheKey);
    
    if (!response) {
      response = await fetch(cacheKey);
      response = new Response(response.body, response);
      response.headers.append('Cache-Control', 's-maxage=300');
      event.waitUntil(cache.put(cacheKey, response.clone()));
    } else {
      console.log(`Cache hit for: ${cacheKey.url}.`);
    }
    return response;
  } catch (e) {
    console.log(`Cache expired: ${e}.`);
    const result = await cache.delete(cacheKey);
    console.log(`Cache delete: ${result}.`);

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

