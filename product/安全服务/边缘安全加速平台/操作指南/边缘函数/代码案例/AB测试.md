通过cookie进行A/B测试控制。

```js
const NAME = 'ABTestCookieName';
const VALUE_A = 'VALUE_A';
const VALUE_B = 'VALUE_B';
const PATH_A = '/PATH_A';
const PATH_B = '/PATH_B';

async function handleRequest(req) {
  const url = new URL(req.url);
  // Enable Passthrough to allow direct access to control and test routes.
  if (url.pathname.startsWith(PATH_A) || url.pathname.startsWith(PATH_B)) {
    return fetch(req);
  }
  // Determine which group this requester is in.
  const cookie = req.headers.get("cookie") || '';
  if (cookie.includes(`${NAME}=${VALUE_A}`)) {
    url.pathname = PATH_A + url.pathname;
  } else if (cookie.includes(`${NAME}=${VALUE_B}`)) {
    url.pathname = PATH_B + url.pathname;
  } else {
    // If there is no cookie, this is a new client. Choose a group and set the cookie.
    const group = Math.random() < 0.5 ? VALUE_A : VALUE_B; // 50/50 split
    if (group === VALUE_A) {
      url.pathname = PATH_A + url.pathname;
    } else {
      url.pathname = PATH_B + url.pathname;
    }

    const res = await fetch(url.toString());
    res.headers.append("Set-Cookie", `${NAME}=${group}; path=/`);
    return res;
  }
  return fetch(url.toString());
}

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

```
