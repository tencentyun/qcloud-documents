# WritableStreamDefaultWriter
用于可写流的操作对象

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
- <span style="color: #0066FF">closed</span>: Promise&lt;void&gt; <br>
&emsp; Returns a Promise that fulfills if the stream becomes closed, or rejects if the stream errors or the writer's lock is released.
- <span style="color: #0066FF">ready</span>: Promise&lt;void&gt; <br>
&emsp; Returns a Promise that resolves when the desired size of the stream's internal queue transitions from non-positive to positive, signaling that it is no longer applying backpressure.
- <span style="color: #0066FF">desiredSize</span>: int<void><br>
&emsp; Returns the desired size required to fill the stream's internal queue.


### 方法
- <span style="color: #FFAA33;font-weight: bold;">write</span>(chunk: string | ArrayBuffer | ArrayBufferView):  Promise&lt;void&gt; <br>
&emsp; 将 chunk 写入到流中; <strong style="color: red"> 不允许在 前一个写操作完成前，调用 write() 方法发起下一个写操作; </strong><br>
- <span style="color: #FFAA33;font-weight: bold;">close</span>():  Promise&lt;void&gt; <br>
&emsp; 关闭当前流 <br>
- <span style="color: #FFAA33;font-weight: bold;">abort</span>(reason?: string):  Promise&lt;string&gt; <br>
&emsp; 终止当前流 <br>
- <span style="color: #FFAA33;font-weight: bold;">releaseLock</span>(): void <br>
&emsp;  取消与流的关联，并释放对流的锁定 <br>


## 参考
* [WritableStreamDefaultWriter](https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter)
