 **ReadableStreamDefaultReader** 用于可读流操作，基于 Web APIs 标准 [ReadableStreamDefaultReader](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader) 进行设计。

 >! 不支持直接构造 `ReadableStreamDefaultReader` 对象，使用 [ReadableStream.getReader](https://cloud.tencent.com/document/product/1552/81914#getreader) 方法得到。

## 描述

```typescript
// 使用 TransformStream 构造得到 ReadableStream 对象
const { readable } = new TransformStream();

// 使用 ReadableStream 对象获取 reader
const reader = readable.getReader();
```

## 属性
### closed 
```typescript
// reader.closed
readonly closed: Promise<void>;
```

返回 Promise 对象，如果流已关闭，Promise 状态为 `fulfilled`，如果流发生错误或读端锁已释放，Promise 状态为 `rejected`。

## 方法
### read
```typescript
reader.read(): Promise<{value: Chunk, done: boolean}>;
```

从流中读取数据。

>! 不允许前一个流读取操作结束前，调用 `read` 方法发起下一个流读取操作。

#### 返回值
`reader.read` 返回 Promise 包含读取的数据（[Chunk](#Chunk)）与读取状态，说明如下：

- 如果有一个 chunk 可用，Promise 为 `fulfilled` 状态，包含 `{ value: theChunk, done: false }` 格式的对象。
- 如果流被关闭，Promise 为 `fulfilled` 状态，包含 `{ value: undefined, done: true }` 格式的对象。
- 如果流出错，Promise 为 `rejected` 状态，并包含相关错误信息。

#### Chunk[](id:Chunk)
从流中读取的数据 `Chunk`，描述如下：

```typescript
type Chunk = string | ArrayBuffer | ArrayBufferView;
```

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
- [MDN 官方文档：ReadableStreamDefaultReader](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader)
