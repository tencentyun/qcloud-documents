Streams 提供了一种高效的 API，用于在边缘函数内实现不同连接间的数据传递。

- [ReadableStream](https://cloud.tencent.com/document/product/1552/81914)
- [ReadableStreamBYOBReader](https://cloud.tencent.com/document/product/1552/81925)
- [ReadableStreamDefaultReader](https://cloud.tencent.com/document/product/1552/81924)
- [TransformStream](https://cloud.tencent.com/document/product/1552/81923)
- [WritableStream](https://cloud.tencent.com/document/product/1552/81922)
- [WritableStreamDefaultWriter](https://cloud.tencent.com/document/product/1552/81927)

**流式处理，可能会修改 HTTP 头部: Transfer-Encoding 为 chunked**。

## 示例
获取视频流的3个部分，通过流式处理，最终合并为响应流输出;
```js
async function _combineStreams(sources, destination) {
  for (const stream of sources) {
    try {
      await stream.pipeTo(destination, {
        preventClose: true
      });
    } catch (e) {
      log("excep:", e);
    }
  }

  let writer = destination.getWriter();
  writer.close();
  writer.releaseLock();
  // destination.close(); 
}

function combineStreams(streams) {
  const stream = new TransformStream();
  _combineStreams(streams, stream.writable);
  return stream.readable;
}

async function handleRequest(event) {
  const urls = [
        "https://laputa-1257579200.cos.ap-guangzhou.myqcloud.com/stream-01.mov",
        "https://laputa-1257579200.cos.ap-guangzhou.myqcloud.com/stream-02.mov",
        "https://laputa-1257579200.cos.ap-guangzhou.myqcloud.com/stream-03.mov"
  ];
  const requests = urls.map(url => fetch(url));
  const responses = await Promise.all(requests);
  const streams = responses.map(res => res.body);

  event.respondWith(new Response(combineStreams(streams), {
    headers: {
      "content-type": "video/mp4",
    }
  }));
}

addEventListener('fetch', (event) => {
  log("this is a combine demo");
  handleRequest(event);
});
```
