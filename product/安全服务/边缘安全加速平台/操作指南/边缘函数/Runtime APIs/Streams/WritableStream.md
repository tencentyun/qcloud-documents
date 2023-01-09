**WritableStream** 可写流，也称为可写端。基于 Web APIs 标准 [WritableStream](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream) 进行设计。

 >! 不支持直接构造 `WritableStream` 对象，使用 [TransformStream](https://cloud.tencent.com/document/product/1552/81923) 构造得到。

## 描述

```typescript
// 使用 TransformStream 构造得到 WritableStream 对象
const { writable } = new TransformStream();
```

### 属性
#### locked
```typescript
// writable.locked 
readonly locked: boolean;
```

标识流是否已锁定。

>? 流处于锁定状态的情况有：
- 一个流最多有一个激活的 `writer`，在 `writer` 调用 `releaseLock()` 方法前，该流均处于锁定状态。 
- 流处于管道传输中，会处于锁定状态，直至管道传输结束。

#### highWaterMark
```typescript
// writable.highWaterMark
readonly highWaterMark: number;
```

可写端缓冲区大小，以字节为单位，默认值为 32K, 最大值为 256K, 超过最大值则会自动调整为 256K。

## 方法 
>!使用下述所有方法，要求当前流处于非锁定状态，否则会抛出异常。

### getWriter
```typescript
writable.getWriter(): WritableStreamDefaultWriter;
```

创建一个 writer，并锁定当前流，直至 writer 调用 releaseLock() 方法释放锁。返回值参见 [WritableStreamDefaultWriter](https://cloud.tencent.com/document/product/1552/81927)。

### close
```typescript
writable.close(): Promise<void>;
```

关闭当前流。

### abort
```typescript
writable.abort(reason?: string): Promise<string>;
```
中止当前流。

## 相关参考 
- [MDN 官方文档：WritableStream](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream)
- [示例函数：合并资源流式响应](https://cloud.tencent.com/document/product/1552/84085)
- [示例函数：m3u8 改写与鉴权](https://cloud.tencent.com/document/product/1552/84086)
