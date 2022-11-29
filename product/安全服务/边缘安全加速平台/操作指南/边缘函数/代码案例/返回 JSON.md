直接在边缘函数中返回 JSON 数据。
```js
const data = {
    hello: 'world',
};

async function handleRequest() {
    const json = JSON.stringify(data, null, 2);
    return new Response(json, {
        headers: {
            'content-type': 'application/json;charset=UTF-8',
        },
    });
}

addEventListener('fetch', event => {
    return event.respondWith(handleRequest());
});
```
