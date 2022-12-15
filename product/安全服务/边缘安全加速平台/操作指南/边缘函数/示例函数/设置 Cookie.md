根据给定的 Cookie 名称，获取 Cookie 的值。

```js
const COOKIE_KEY = 'name'

async function handleParse(event) {
  const request = event.request;
  const cookies = new Cookies(request.headers.get('cookie') || '');
  // 获取指定 name 的 Cookie 对象
  const cookie = cookies.get(COOKIE_KEY);
 
  if (cookie !== null) {
    return new Response(`Cookie name: ${COOKIE_KEY} value: ${cookie.value}`);
  }

  // 返回 null, 表示无对应 Cookie 对象
  return new Response('No cookie with name: ' + COOKIE_KEY);
}
  
addEventListener('fetch', (event) => {
  try {
    return event.respondWith(handleParse(event));
  } catch (e) {
    return event.respondWith(new Response('Error thrown ' + e.message));
  }
});

```

![image-20221214204900780](/Users/tomtomyang/Library/Containers/com.tencent.WeWorkMac/Data/Documents/Profiles/D711BAD185CCD117B3EAFB62BF1FABB4/Caches/Files/2022-12/31d6a097f33d11df7c0ce87ef73dc288/assets/image-20221214204900780.png)
