**WritableStreamDefaultWriter** 用于可写流的操作。基于 Web APIs 标准 [WritableStreamDefaultWriter](https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter) 进行设计。

 >! 不支持直接构造 `WritableStreamDefaultWriter` 对象，使用 [WritableStream.getWriter](https://cloud.tencent.com/document/product/1552/81922#getwriter) 方法得到。

## 描述
```typescript
// 使用 TransformStream 构造得到 WritableStream 对象
const { writable } = new TransformStream();

// 使用 WritableStream 对象获取 writer 
const writer = writable.getWriter();
```

## 属性
### closed 
```typescript
// writer.closed
readonly closed: Promise<void>;
```

返回 Promise 对象，如果流已关闭，Promise 状态为 `fulfilled`，如果流发生错误或写端锁已释放，Promise 状态为 `rejected`。

### ready
```typescript
// writer.ready
readonly ready: Promise<void>;
```

返回 Promise 对象，当流的内部队列的所需大小从负变为正时，该 Promise 状态为 fulfilled，表示它不再施加背压。

### desiredSize
```typescript
// writer.desiredSize
readonly desiredSize: number;
```

返回填充流的内部队列所需的大小。


## 方法
### write
```typescript
writer.write(chunk: Chunk): Promise<void>;
```

把 `chunk` 数据写入流中。

>! 不允许前一个写流操作结束前，调用 `write` 方法发起下一个写流操作。

#### 参数
<table>
  <thead>
    <tr>
      <th width="15%">参数名称</th>
      <th width="15%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>chunk</td>
      <td><a href="#Chunk">Chunk</td>
      <td>是</td>
      <td>待写入流的 chunk 数据。</li>
      </td>
    </tr>
  </tbody>
</table>

#### Chunk[](id:Chunk)
从流中读取的数据 `Chunk`，描述如下：

```typescript
type Chunk = string | ArrayBuffer | ArrayBufferView;
```

### close
```typescript
writer.close(): Promise<void>;
```

关闭当前流。

### abort
```typescript
writer.abort(reason?: string): Promise<string>;
```
终止当前流。

### releaseLock
```typescript
writer.releaseLock(): void;
```

取消与流的关联，并释放流的锁定。

## 相关参考 
- [MDN 官方文档：WritableStreamDefaultWriter](https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter)
