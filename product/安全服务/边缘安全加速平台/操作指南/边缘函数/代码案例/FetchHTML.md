向服务发送请求，并把响应内容作为 HTML 页面返回。

```js
const url = 'https://some.doamin/and/path';

async function handleRequest() {
    const init = {
        headers: {
            'content-type': 'text/html'
        },
    };

    const response = await fetch(url, init);
    const text = await response.text();
    return new Response(text, init);
}

addEventListener('fetch', event => {
    return event.respondWith(handleRequest());
});
```
