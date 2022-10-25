若要定制压测引擎在执行压测任务时的行为（传入自定义参数值、覆盖默认配置），您可设置全局 Options，来控制诸如 TLS/HTTP/WebSocket 通信的配置参数、预处理/后处理的超时时间等。

要设置全局 Options，您可在脚本最外层定义一个 option 对象（`export const option = {...}`），再根据您的需求，在 option 对象中定义 `tlsConfig`、`http` 等字段。

参数详情可参见 PTS JavaScript API 文档：[Global Options](https://pts-js-api-1258344701.cos-website.ap-nanjing.myqcloud.com/docs/interfaces/global.Option.html)。


### HTTP 全局配置

通过 `option` 里的 `http` 字段，您可配置压测引擎作为 HTTP 客户端的相关参数，这些参数对本次压测任务的所有 HTTP 请求全局生效。

常用参数如下：
- `headers`：设置请求头。
- `basicAuth`：使用 HTTP basic auth 认证时，通过该参数传入用户名和密码。
- `disableKeepAlives`：若要禁用长连接，可将该字段设置为 true。
- `discardResponseBody`：若要丢弃服务端返回的响应包体，可将该字段设置为 true。
- `http2`：若要启用 HTTP2 协议，可将该字段设置为 true。
- `maxIdleConns`：单个 VU 的最大连接数，默认值为 100。
- `maxIdleConnsPerHost`：单个 VU 针对单个 host（地址+端口） 的最大连接数，默认值为 2。
- `maxRedirects`：重定向跳转的最大次数，默认值为 10。
- `timeout`：请求超时时间，单位为毫秒，默认值为 10 秒。


脚本示例：
```javascript
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

### WebSocket 全局配置

通过 `option` 里的 `ws` 字段，您可配置压测引擎作为 WebSocket 客户端的相关参数，这些参数对本次压测任务的所有 WebSocket 请求全局生效。

常用参数如下：
- `handshakeTimeout`：握手超时时间，单位为毫秒，默认值为 30 秒。
- `readTimeout`：读消息超时时间，单位为毫秒，默认不限制。
- `writeControlTimeout`：写控制指令超时时间，单位为毫秒，默认为 10 秒。
- `writeTimeout`：写消息超时时间，单位为毫秒，默认不限制。

示例：
```javascript
export const option = {
    ws: {
        writeTimeout: 3000,
        readTimeout: 3000,
    }
}
```

### tRPC 全局配置（腾讯内部）
```javascript
// TRPC API
import trpc from 'pts/trpc';

export const option = {
    // trpc default configs
    trpc: {
        env: "formal",
        namespace: "Production",
    }
}

const client = new trpc.Client();

export default function () {
  const res = client.invoke(
    '/trpc.wtp.demo.demo/SayHello',
    {
      msg: 'pts',
    },
    {
      env: 'test',
      serviceName: 'trpc.wtp.demo.trpc',
      metaData: {
        person_id: '123456',
      },
      serializationType: 2,
    }
  );
  console.log(JSON.stringify(res));
}
```

### TLS 全局配置
压测引擎作为客户端，在建立 TLS （Transport Layer Security/传输层安全协议）连接时，支持以下配置选项：
- `insecureSkipVerify`：是否验证服务器的证书链和主机名。若设置为 true 则不验证。默认为 false。
- `rootCAs`：在验证服务器证书时，使用的一组根证书颁发机构。 若为空，则默认使用主机的根 CA 集。
- `certificates`：在双向 TLS 认证中，客户端提供的供服务端验证的证书列表。

示例：
```javascript
export const option = {
    tlsConfig: {
        'localhost': {
            insecureSkipVerify: false,
            rootCAs: [open('tool/tls/twoway/ca.crt')],
            certificates: [{cert: open('tool/tls/twoway/client.crt'), key: open('tool/tls/twoway/client.key')}]
        }
    }
}
```

### 预处理与后处理配置
- `setupTimeoutSeconds`：预处理（setup）步骤的超时时间。默认为 60 秒。
  示例：
  ```javascript
export const option = {
    setupTimeoutSeconds: 30
}
```
- `teardownTimeoutSeconds`：后处理（teardown）步骤的超时时间。默认为 60 秒。
  示例：
  ```javascript
export const option = {
    teardownTimeoutSeconds: 30
}
```

关于脚本的预处理/后处理的详情，参见：[脚本概述](https://iwiki.woa.com/pages/viewpage.action?pageId=1440207985)。
