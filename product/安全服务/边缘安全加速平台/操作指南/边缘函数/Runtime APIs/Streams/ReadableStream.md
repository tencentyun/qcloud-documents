# ReadableStream
代表一个可读流对象

## 语法
```typescript
class ReadableStream {
  readonly locked: boolean;

  getReader(options?: {mode?: string}): ReadableStreamDefaultReader | ReadableStreamBYOBReader;
  pipeThrough(transfromStream: TransfromStream, options?: PipeToOptions): ReadableStream; 
  pipeTo(destination: WritableStream, options?: PipeToOptions): Promise<void>;
  tee(): [ReadableStream, ReadableStream];
  cancel(reason?: string): Promise<string>;
}

interface PipeToOptions {
  preventClose?: boolean;
  preventAbort?: boolean;
  preventCancel?: boolean;
  signal?: AbortSignal;
}
```

### 属性
- locked: boolean<br>
&emsp; 标识流是否已锁定; 
  - 一个流最多有一个激活的 reader, 在reader 调用 releaseLock() 方法之前，该流均处于锁定状态;
  - **当流处于管道传输过程中，也会处于锁定状态，直至结束管道传输;**

### 方法
- getReader(options?: {mode?: string}):  [ReadableStreamDefaultReader](ReadableStreamDefaultReader.md) | [ReadableStreamBYOBReader](ReadableStreamBYOBReader.md) <br>
&emsp; 创建一个 Reader, 并锁定当前流，直至 Reader 调用 releaseLock() 释放锁; <br>
&emsp; options 参数用于指定 Reader 类型，取值有：<br>
  - "byob": 表示创建 [ReadableStreamBYOBReader](ReadableStreamBYOBReader.md) 类型的 Reader;
  - undefined: 未指定时，默认创建 [ReadableStreamDefaultReader](ReadableStreamDefaultReader.md) 类型的 Reader;
- pipeThrough(transfromStream: TransfromStream, options?: PipeToOptions):  ReadableStream<br>
&emsp; 流的链式处理，将当前可读流的数据传输到 transfromStream 的 writable 端，并返回 transfromStream 的 readable 端;<br>
&emsp; **在整个管道传输过程中，会对当前流 && writable 端进行锁定** <br>
&emsp; options 参数说明: <br>
  - preventClose: boolean, true 表示可读流的关闭，不会导致对可写流的 close() 方法的调用;
  - preventAbort: boolean, true 表示可读流的错误，不会导致对可写流的 abort() 方法的调用;
  - preventCancel: boolean, true 表示可写流的错误，不会导致对可读流的 cancel() 方法的调用;
  - signal: AbortSignal, 当 signal 被 abort 时，将会中止正在进行的传输操作;
- pipeTo(destination: WritableStream, options?: PipeToOptions):  Promise&lt;void&gt; <br>
&emsp; 流的链式处理，将当前可读流的数据传输到 destination 可写流; <br>
&emsp; **在管道传输过程中，会对当前流 && destination 进行锁定** <br>
&emsp; 返回值：一个 Promise， 处理成功时为 fulfilled 状态，发生错误时为 rejected 状态<br>
- tee():  [ReadableStream, ReadableStream] <br>
&emsp; 将当前流派发出两个独立的可读流； <br>
- cancel(reason?: string):  Promise&lt;string&gt; <br>
&emsp; 结束当前流 <br>

**上述所有方法的调用，要求当前流处于非锁定状态，否则会抛出异常**


## 参考
* [ReadableStream](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)
