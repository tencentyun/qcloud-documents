TransformStream 代表了一对流，包括读端和写端。

## 语法
```typescript
class TransformStream {
  readonly readable: ReadableStream;
  readonly writable: WritableStream;

  constructor(transformer?: any, writableStrategy?: {highWaterMark: uint});
}
```

### 构造方法
- transfromer  可选<br>any，当前实现会忽略该参数。
- writableStrategy  可选<br>指定可写端的缓存区大小，以字节为单位，默认值为 32K，最大值为 256K，超过最大值则会自动调整为 256K。

### 属性
- readable: [ReadableStream](https://cloud.tencent.com/document/product/1552/81909)<br>可读端。
- writable: [WritableStream](https://cloud.tencent.com/document/product/1552/81922)<br>可写端。

## 示例
```js
addEventListener('fetch', (event) => {
  log("tfs begin");
  let req = event.request;

  log("req.method:", req.method);
  log("req.url:", req.url);

  req.text().then((text) => {
    log("req.body:", text);
  });

  let { readable, writable } = new TransformStream();

  // respond with ReadableStream
  let rsp = new Response(readable);
  event.respondWith(rsp);

  (async () => {
    try {
      // here will make Transfer-Encoding to be chunked!
      let writer = writable.getWriter();
      await writer.write("The first line.\n");
      await writer.write("The second line.\n");
      log("writer close");
      await writer.close();
      writer.releaseLock();
    } catch (e) {
      log.error("writable got excep='" + e + "'");
    }
  })();
});
```

## 参考
- [TransformStream](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream)
