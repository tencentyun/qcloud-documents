通过 cookie 进行 A/B 测试控制。
```js
const NAME = 'ABTestCookieName';
const VALUE_A = 'VALUE_A';
const VALUE_B = 'VALUE_B';
const PATH_A = '/PATH_A';
const PATH_B = '/PATH_B';

async function handleRequest(request) {
    const urlObject = new URL(request.url);

    if (urlObject.pathname.startsWith(PATH_A) || urlObject.pathname.startsWith(PATH_B)) {
        return fetch(request);
    }

    const cookies = new Cookies(request.headers.get('cookie'));
    const cookie = cookies.get(NAME);
    const cookieValue = cookie && cookie.value;

    if (cookieValue === VALUE_A) {
        urlObject.pathname = PATH_A + urlObject.pathname;
        return fetch(urlObject.toString());
    }
    
    if (cookieValue === VALUE_B) {
        urlObject.pathname = PATH_B + urlObject.pathname;
        return fetch(urlObject.toString());
    }

    const type = Math.random() < 0.5 ? VALUE_A : VALUE_B;
    const path = type === VALUE_A ? PATH_A : PATH_B;
    urlObject.pathname = path + urlObject.pathname;

    const response = await fetch(urlObject.toString());
    response.headers.append('Set-Cookie', `${NAME}=${type}; path=/`);
    return response;
}

addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request));
});
```
