# TransformStream
代表了一对流，包括读端和写端。

## 语法
```typescript
class TransformStream {
  readonly readable: ReadableStream;
  readonly writable: WritableStream;

  constructor(transformer?: any, writableStrategy?: {highWaterMark: uint});
}
```

### 构造方法
- <span style="color: #0066FF">transfromer </span><span style="border: 3px solid #F0F8FF;border-radius: 4rem;padding:0.375rem 0.375rem;font-color: #D3D3D3;font-size: 0.7rem;">Optional</span><br>
&emsp; any, 当前实现会忽略该参数<br>
- <span style="color: #0066FF">writableStrategy </span><span style="border: 3px solid #F0F8FF;border-radius: 4rem;padding:0.375rem 0.375rem;font-color: #D3D3D3;font-size: 0.7rem;">Optional</span><br>
&emsp; 指定可写端的缓存区大小，以字节为单位，默认值为 32K, 最大值为 256K, 超过最大值则会自动调整为 256K <br>


### 属性
- <span style="color: #0066FF">readable</span>: [ReadableStream](ReadableStream.md)<br>
&emsp; 可读端
- <span style="color: #0066FF">writable</span>: [WritableStream](WritableStream.md)<br>
&emsp; 可写端

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
* [TransformStream](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream)
