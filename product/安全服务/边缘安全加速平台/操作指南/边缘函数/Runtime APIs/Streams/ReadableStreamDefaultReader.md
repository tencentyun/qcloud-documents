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
- <span style="color: #0066FF">closed</span>: Promise&lt;void&gt; <br>
&emsp; Returns a Promise that fulfills when the stream closes, or rejects if the stream throws an error or the reader's lock is released.

### 方法
- <span style="color: #FFAA33;font-weight: bold;">read</span>(): Promise&lt;{value: Chunk, done: boolean}&gt; <br>
&emsp; 从流中读取数据; <strong style="color: red"> 不允许在 前一个读取操作完成前，调用 read() 方法发起下一个读取操作; </strong> <br>
&emsp; 返回值:<br>
  - If a chunk is available, the promise will be fulfilled with an object of the form { value: theChunk, done: false }.
  - If the stream becomes closed, the promise will be fulfilled with an object of the form { value: undefined, done: true }.
  - If the stream becomes errored, the promise will be rejected with the relevant error.
- <span style="color: #FFAA33;font-weight: bold;">cancel</span>(reason?: string): Promise&lt;string&gt; <br>
&emsp; 关闭流并结束读取操作 <br>
- <span style="color: #FFAA33;font-weight: bold;">releaseLock</span>(): void <br>
&emsp;  取消与流的关联，并释放对流的锁定 <br>


## 参考
* [ReadableStreamDefaultReader](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader)
