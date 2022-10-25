# ReadableStreamDefaultReader
用于对可读流的进行操作的对象

## 语法
```typescript
type Chunk = string | ArrayBuffer | ArrayBufferView;

class ReadableStreamDefaultReader {
  readonly closed: Promise<void>;

  read(): Promise<{value: Chunk, done: boolean}>;
  cancel(reason?: string): Promise<string>;
  releaseLock(): void;
}
```

### 属性
- closed: Promise&lt;void&gt; <br>
&emsp; Returns a Promise that fulfills when the stream closes, or rejects if the stream throws an error or the reader's lock is released.

### 方法
- read(): Promise&lt;{value: Chunk, done: boolean}&gt; <br>
&emsp; 从流中读取数据; **不允许在 前一个读取操作完成前，调用 read() 方法发起下一个读取操作;** <br>
&emsp; 返回值:<br>
  - 如果有一个 chunk 是可用的，Promise 将转为 fulfilled 状态，包含 { value: theChunk, done: false } 格式的对象。
  - 如果流被关闭，Promise 将转为 fulfilled 状态，包含 { value: undefined, done: true } 格式的对象。
  - 如果流出错，Promise 将转为 rejected 状态，并包含相关错误信息。
- cancel(reason?: string): Promise&lt;string&gt; <br>
&emsp; 关闭流并结束读取操作 <br>
- releaseLock(): void <br>
&emsp;  取消与流的关联，并释放对流的锁定 <br>


## 参考
* [ReadableStreamDefaultReader](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader)
