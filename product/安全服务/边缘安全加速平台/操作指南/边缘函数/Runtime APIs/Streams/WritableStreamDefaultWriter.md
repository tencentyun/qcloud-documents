WritableStreamDefaultWriter 用于可写流的操作对象。

## 语法
```typescript
class WritableStreamDefaultWriter {
  readonly closed: Promise<void>;
  readonly ready: Promise<void>;
  readonly desiredSize: int;

  write(chunk: string | ArrayBuffer | ArrayBufferView): Promise<void>;
  close(): Promise<void>;
  abort(reason?: string): Promise<string>;
  releaseLock(): void;
}
```

### 属性
- closed: Promise&lt;void&gt; <br>如果流已关闭，则转为 fulfilled 状态；如果流发生错误或写端锁已释放，则转为 rejected 状态。
- ready: Promise&lt;void&gt; <br>返回一个 Promise. 当流的内部队列的所需大小从非正变为正时，该 Promise 将转为 fulfilled 状态，表示它不再施加背压。
- desiredSize: int<void><br>返回填充流的内部队列所需的大小。


### 方法
- write(chunk: string | ArrayBuffer | ArrayBufferView):  Promise&lt;void&gt; <br>将 chunk 写入到流中；**不允许在前一个写操作完成前，调用 write() 方法发起下一个写操作**。
- close():  Promise&lt;void&gt; <br>关闭当前流。
- abort(reason?: string):  Promise&lt;string&gt; <br>终止当前流。
- releaseLock(): void <br>取消与流的关联，并释放对流的锁定。

## 参考
- [WritableStreamDefaultWriter](https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter)
