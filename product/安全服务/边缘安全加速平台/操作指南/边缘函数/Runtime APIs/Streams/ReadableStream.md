 **ReadableStream** 可读流，也称为可读端，基于 Web APIs 标准 [ReadableStream](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) 进行设计。

 >! 不支持直接构造 `ReadableStream` 对象，使用 [TransformStream](https://cloud.tencent.com/document/product/1552/81923) 构造得到。

## 描述

```typescript
// 使用 TransformStream 构造得到 ReadableStream 对象
const { readable } = new TransformStream();
```

## 属性
```typescript
// readable.locked
readonly locked: boolean;
```
标识流是否锁定。

>? 流处于锁定状态的情况有：
- 一个流最多有一个激活的 `reader`，在 `reader` 调用 `releaseLock()` 方法前，该流均处于锁定状态。 
- 流处于管道传输中，会处于锁定状态，直至管道传输结束。

## 方法
>!使用下述所有方法，要求当前流处于非锁定状态，否则会抛出异常。

### getReader
```typescript
readable.getReader(options?: ReaderOptions): ReadableStreamDefaultReader | ReadableStreamBYOBReader;
```

创建一个 `Reader`, 并锁定当前流，直至 `Reader` 调用 releaseLock() 释放锁。

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
      <td>options</td>
      <td><a href="#ReaderOptions">ReaderOptions</td>
      <td>是</td>
      <td>生成 Reader 的配置项。</li>
      </td>
    </tr>
  </tbody>
</table>

#### ReaderOptions[](id:ReaderOptions)
`ReaderOptions` 对象属性如下所示。

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">必填</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>mode</td>
			<td>string</td>
			<td>否</td>
			<td>
        <code>Reader</code> 类型，默认值为 <code>undefined</code>，取值说明如下。<br/>
        <li>
          <font color="#9ba6b7">undefined</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            创建 <a href="https://cloud.tencent.com/document/product/1552/81924">ReadableStreamDefaultReader</a> 类型的 <code>Reader</code>。
          </div>
        </li>
        <li>
          <font color="#9ba6b7">byob</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            创建 <a href="https://cloud.tencent.com/document/product/1552/81925">ReadableStreamBYOBReader</a> 类型的 <code>Reader</code>。
          </div>
        </li>
      </td>
		</tr>
	</tbody>
</table>

### pipeThrough
```typescript
readable.pipeThrough(transfromStream: TransfromStream, options?: PipeToOptions): ReadableStream; 
```

流的管道处理。将当前可读流数据传输到参数 `transfromStream` 的 writable 端，并返回 `transfromStream` 的 readable 端。

>! 在管道传输过程中，会对当前流 `writable` 端进行锁定。

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
      <td>transfromStream</td>
      <td><a href="https://cloud.tencent.com/document/product/1552/81923">TransfromStream</td>
      <td>是</td>
      <td>当前流传输到的目标对象。</td>
    </tr>
    <tr>
      <td>options</td>
      <td><a href="#PipeToOptions">PipeToOptions</td>
      <td>是</td>
      <td>流处理配置项。</td>
    </tr>
  </tbody>
</table>

#### PipeToOptions[](id:PipeToOptions)

流处理配置项如下所示：

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">必填</th>
			<th width="65%">说明</th>
	  </tr>
	</thead>
	<tbody>
		<tr>
			<td>preventClose</td>
			<td>boolean</td>
			<td>否</td>
			<td>取值 <code>true</code> 时，表示可读流的关闭，不会导致可写流关闭。</td>
		</tr>
    <tr>
			<td>preventAbort</td>
			<td>boolean</td>
			<td>否</td>
			<td>取值 <code>true</code> 时，表示可读流发生错误，不会导致可写流中止。</td>
		</tr>
    <tr>
			<td>preventCancel</td>
			<td>boolean</td>
			<td>否</td>
			<td>取值 <code>true</code> 时，表示可写流的错误，不会导致结束可读流。</td>
		</tr>
    <tr>
			<td>signal</td>
			<td><a href="https://cloud.tencent.com/document/product/1552/84091#abortsignal">AbortSignal</a></td>
			<td>否</td>
			<td>当 `signal` 被 abort 时，将会中止正在进行的传输。</td>
		</tr>
	</tbody>
</table>

### pipeTo
```typescript
readable.pipeTo(destination: WritableStream, options?: PipeToOptions): Promise<void>;
```

流的管道处理，将当前可读流传输到 `destination` 可写流。

>! 在管道传输过程中，会对当前流 `destination` 进行锁定。

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
      <td>destination</td>
      <td><a href="https://cloud.tencent.com/document/product/1552/81922">WritableStream</td>
      <td>是</td>
      <td>可写流。</td>
    </tr>
    <tr>
      <td>options</td>
      <td><a href="#PipeToOptions">PipeToOptions</td>
      <td>是</td>
      <td>流处理配置项。</td>
    </tr>
  </tbody>
</table>

### tee
```typescript
readable.tee(): [ReadableStream, ReadableStream];
```
将当前流派发出两个独立的可读流。

### cancel
```typescript
readable.cancel(reason?: string): Promise<string>;
```

结束当前流。

## 相关参考 
- [MDN 官方文档：ReadableStream](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)
- [示例函数：合并资源流式响应](https://cloud.tencent.com/document/product/1552/84085)
- [示例函数：m3u8 改写与鉴权](https://cloud.tencent.com/document/product/1552/84086)
