用户通过全局 Options 可控制压测引擎默认行为。
>?Options 可配置选项文档请参见 [Global Options](https://cloud.tencent.com/document/product/1484/75812)。

### 设置 HTTP 默认参数

```
import http from 'pts/http';
import { check } from 'pts';

export const option = {
    http: {
        maxRedirects: 10,
        maxIdleConns: 100,
        headers: {
            'key': 'value'
        }
    }
}
export default function () {
  // get request with headers and parameters
  const resp1 = http.get('http://httpbin.org/get', {
    headers: {
      Connection: 'keep-alive',
      'User-Agent': 'pts-engine',
    },
    query: {
      name1: 'value1',
      name2: 'value2',
    },
  });

  console.log(resp1.json().args.name1); // 'value1'
  check('status is 200', () => resp1.statusCode === 200);
  check('body.args.name1 equals value1', () => resp1.json().args.name1 === 'value1');
  check('headers.key equals value', () => resp1.json().headers.key === 'value')
}
```


