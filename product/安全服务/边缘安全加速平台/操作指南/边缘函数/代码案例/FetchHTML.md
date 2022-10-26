向服务发送请求，并把响应内容作为 JSON 数据返回。
```js
/**
 * Example someHost at URL is set up to respond with HTML
 * Replace URL with the host you wish to send requests to
 */
const someHost = 'https://www.examples.com';
const url = someHost + '/static/html';

/**
 * gatherResponse awaits and returns a response body as a string.
 * Use await gatherResponse(..) in an async function to get the response body
 * @param {Response} response
 */
async function gatherResponse(response) {
  const { headers } = response;
  const contentType = headers.get('content-type') || '';
  if (contentType.includes('application/json')) {
    return JSON.stringify(await response.json());
  } else if (contentType.includes('application/text')) {
    return response.text();
  } else if (contentType.includes('text/html')) {
    return response.text();
  } else {
    return response.text();
  }
}

async function handleRequest() {
  const init = {
    headers: {
      'content-type': 'text/html;charset=UTF-8',
    },
  };
  const response = await fetch(url, init);
  const results = await gatherResponse(response);
  return new Response(results, init);
}

addEventListener('fetch', event => {
  return event.respondWith(handleRequest());
});
```
