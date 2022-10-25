ReadableStreamBYOBReader 用于对可读流的进行操作的对象。不同于 `ReadableStreamDefaultReader`，其 `read` 方法传入一个 `ArrayBufferView` 类型参数，可将数据从流读取到 view 内存中。

## 语法
```typescript
class ReadableStreamBYOBReader {
  readonly closed: Promise<void>;

  read(view: ArrayBufferView): Promise<{value: ArrayBufferView, done: boolean}>;
  cancel(reason?: string): Promise<string>;
  releaseLock(): void;
}
```

### 属性
- closed: Promise&lt;void&gt; <br>Returns a Promise that fulfills when the stream closes, or rejects if the stream throws an error or the reader's lock is released。

### 方法
- read(view: ArrayBufferView): Promise&lt;{value: ArrayBufferView, done: boolean}&gt; 
  - 从流中读取数据到 view 内存中。
  - **不允许在 前一个读取操作完成前，调用 read() 方法发起下一个读取操作**。
  -  **Note that once the promise fulfills, the original view passed to the method will be detached and no longer usable**。 
  - 返回值：
    - 如果有一个 chunk 是可用的，Promise 将转为 fulfilled 状态，包含 { value: theChunk, done: false } 格式的对象。
    - 如果流被关闭，Promise 将转为 fulfilled 状态，包含 { value: theChunk, done: true } 格式的对象。
    - 如果流出错，Promise 将转为 rejected 状态，并包含相关错误信息。
- cancel(reason?: string): Promise&lt;string&gt; <br>关闭流并结束读取操作。
- releaseLock(): void <br>取消与流的关联，并释放对流的锁定。

## 示例
```js
function assert(actual, expected, message) {
  if (arguments.length == 1)
    expected = true;

  if (actual === expected)
    return;

  if (actual !== null && expected !== null
    && typeof actual == 'object' && typeof expected == 'object'
    && actual.toString() === expected.toString())
    return;

  let errMsg = `assertion failed: goted(${actual}), expected(${expected})` + (message ? `  [${message}]` : '');
  throw Error(errMsg);
}

function ab2str(buf) {
  return String.fromCharCode.apply(null, new Uint8Array(buf));
}

(async() => {
  async function readStream(reader) {
    let buffer = new ArrayBuffer(4096);
    let offset = 0;  
    let bytesReceived = 0;

    while (offset < buffer.byteLength) {
      let {done, value} = await reader.read(new Uint8Array(buffer, offset, buffer.byteLength - offset));
      // @Note: 原 buffer 已被 detached, 需要使用返回的 buffer
      buffer = value.buffer;

      if (done) {
        break;
      }

      offset += value.byteLength;
      bytesReceived += value.byteLength;
    }

    assert(offset, 10);
    assert(bytesReceived, 10);
    console.log('data:', ab2str(new Uint8Array(buffer, 0, offset)));
  }

  let {readable, writable} = new TransformStream();
  readStream(readable.getReader({mode: 'byob'}));

  let writer = writable.getWriter();
  await writer.write('hello');
  await writer.write('world');
  await writer.close();
  log('close');
})();
```

## 参考
- [ReadableStreamBYOBReader](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamBYOBReader)
