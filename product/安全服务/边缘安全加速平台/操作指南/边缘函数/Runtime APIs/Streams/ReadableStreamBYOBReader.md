 **ReadableStreamBYOBReader** 用于可读流操作，基于 Web APIs 标准 [ReadableStreamBYOBReader](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamBYOBReader) 进行设计。`BYOB`（bring your own buffer），表示允许从流读取数据到缓冲区，从而最大限度的减少副本。

 >! 不支持直接构造 `ReadableStreamBYOBReader` 对象，使用 [ReadableStream.getReader](https://cloud.tencent.com/document/product/1552/81914#getreader) 方法得到。

## 描述 
```typescript
// 使用 TransformStream 构造得到 ReadableStream 对象
const { readable } = new TransformStream();

// 使用 ReadableStream 对象获取 reader
const reader = readable.getReader({
  mode: 'byob',
});
```

## 属性

```typescript
// readable.locked
readonly locked: boolean;
```

返回 Promise 对象，如果流已关闭，Promise 状态为 `fulfilled`，如果流发生错误或读端锁已释放，Promise 状态为 `rejected`。

## 方法
### read
```typescript
reader.read(bufferView: ArrayBufferView): Promise<{value: ArrayBufferView, done: boolean}>;
```

从流中读取数据到缓冲区 `bufferView`。

>! 不允许前一个流读取操作结束前，调用 `read` 方法发起下一个流读取操作。

#### 返回值
`reader.read` 返回 Promise 包含读取的数据与读取状态，说明如下：

- 如果有一个 chunk 是可用的，Promise 为 `fulfilled` 状态，包含 `{ value: theChunk, done: false }` 格式的对象。
- 如果流被关闭，Promise 将转为 `fulfilled` 状态，包含 `{ value: theChunk, done: true }` 格式的对象。
- 如果流出错，Promise 为 `rejected` 状态，并包含相关错误信息。

### cancel
```typescript
reader.cancel(reason?: string): Promise<string>;
```
关闭流并结束读取操作。

### releaseLock
```typescript
reader.releaseLock(): void;
```

取消与流的关联，并释放流的锁定。


## 相关参考 
- [MDN 官方文档：ReadableStreamBYOBReader](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamBYOBReader)
