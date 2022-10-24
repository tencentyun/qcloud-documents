# WritableStream
代表一个可写流对象

## 语法
```typescript
class WritableStream {
  readonly locked: boolean;
  readonly highWaterMark: uint;

  getWriter(): WritableStreamDefaultWriter;
  close(): Promise<void>;
  abort(reason?: string): Promise<string>;
}
```

### 属性
- locked: boolean<br>
&emsp; 标识流是否已锁定; <br>
  - 一个流最多有一个激活的 writer, 在 writer 调用 releaseLock() 方法之前，该流均处于锁定状态;
  - **当流处于管道传输过程中，也会处于锁定状态，直至管道传输的结束;**

- highWaterMark: uint<br>
&emsp; 流的缓冲区大小，以字节为单位

### 方法 
- getWriter(): [WritableStreamDefaultWriter](WritableStreamDefaultWriter.md) <br>
&emsp; 创建一个 Writer, 并锁定当前流，直至 Writer 调用 releaseLock() 方法释放锁; <br>
- close():  Promise&lt;void&gt; <br>
&emsp; 关闭当前流 <br>
- abort(reason?: string):  Promise&lt;string&gt; <br>
&emsp; 中止当前流 <br>

**上述所有方法的调用，要求当前流处于非锁定状态，否则会抛出异常**

## 参考
* [WritableStream](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream)
