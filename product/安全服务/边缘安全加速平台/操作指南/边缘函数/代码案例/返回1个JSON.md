### 返回1个JSON

```
addEventListener('fetch', event => {
  const data = {
    hello: 'world',
  };

  const json = JSON.stringify(data, null, 2);

  return event.respondWith(
    new Response(json, {
      headers: {
        'content-type': 'application/json;charset=UTF-8',
      },
    })
  );
});
```
