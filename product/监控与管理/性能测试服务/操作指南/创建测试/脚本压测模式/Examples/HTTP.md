## HTTP Get

```js
// Send a http get request
import http from 'pts/http';
import { check, sleep } from 'pts';

export default function () {
    // simple get request
    const resp1 = http.get('http://httpbin.org/get');
    console.log(resp1.body);
    // if resp1.body is a json string, resp1.json() transfer json format body to a json object
    console.log(resp1.json());
    check('status is 200', () => resp1.statusCode === 200);

    // sleep 1 second
    sleep(1);

    // get request with headers and parameters
    const resp2 = http.get('http://httpbin.org/get', {
        headers: {
            'Connection': 'keep-alive',
            'User-Agent': 'pts-engine'
        },
        query: {
            'name1': 'value1',
            'name2': 'value2',
        }
    });

    console.log(resp2.json().args.name1); // 'value1'
    check('body.args.name1 equals value1', () => resp2.json().args.name1 === 'value1');
};
```

## HTTP Post (raw)

```js
// Send a post request
import http from 'pts/http';
import {check} from 'pts';

export default function () {
    const resp = http.post('http://httpbin.org/post', {
        data: 'some data'
    }, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    console.log(resp.json().json.data); // some data
    check('body.json.data equals some data', () => resp.json().json.data === 'some data');
};
```

## HTTP Post (x-www-form-urlencoded)

```js
// Send a form urlencoded request
import http from 'pts/http';
import {check} from 'pts';

export default function () {
    const resp = http.post('http://httpbin.org/post', {
        data: 'some data'
    }, {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    });

    console.log(resp.json().headers['Content-Type']); // application/x-www-form-urlencoded
    console.log(resp.json().form.data); // some data
    check('body.form.data equals some data', () => resp.json().form.data === 'some data');
};
```

## HTTP Post (form-data)

```js
// Send a multipart request
import http from 'pts/http';
import {check} from 'pts';

const fileData = open("./sample/tmp.js")

export default function () {
    const formData = new http.FormData();
    formData.append('data', 'some data');
    formData.append('file', http.file(fileData));
    const resp = http.post('http://httpbin.org/post', formData.body(), {
        headers: {
            'Content-Type': formData.contentType()
        }
    });

    console.log(resp.json().headers['Content-Type']); // multipart/form-data; boundary=c7fced8e5c0ce8939a96691da77d13f635c389cdbcc951e8784114edb41f
    console.log(resp.json().form.data); // some data
    console.log(resp.json().files.file.length); // 801
    check('body.form.data equals some data', () => resp.json().form.data === 'some data');
};
```

## HTTP 基础鉴权

```js
// Http basic authentication
import http from 'pts/http';
import {check} from 'pts';

export default function () {
    const user = 'user';
    const passwd = 'passwd';
    const resp = http.get(`http://${user}:${passwd}@httpbin.org/basic-auth/user/passwd`);

    console.log(resp.json().authenticated); // true
    check('body.authenticated equals true', () => resp.json().authenticated === true);
}
```

## HTTP Cookie

```js
// Send a request with cookie
import http from 'pts/http';
import {check} from 'pts'

export default function () {
    const resp = http.get('http://httpbin.org/cookies', {
        headers: {
            cookie: 'k=v'
        }
    });

    console.log(resp.json().cookies.k); // v
    check('body.cookies.k equals v', () => resp.json().cookies.k === 'v');
};
```
