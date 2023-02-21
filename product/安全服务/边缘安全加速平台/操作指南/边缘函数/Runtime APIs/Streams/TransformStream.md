**TransformStream** 由一对流组成，一个可读流，称为可读端，一个可写流，称为可写端。基于 Web APIs 标准 [TransformStream](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream) 进行设计。

## 构造函数
```typescript
const { readable, writable } = new TransformStream(transformer?: any, writableStrategy?: WritableStrategy);
```

### 参数 

<table>
  <thead>
    <tr>
      <th width="10%">参数名称</th>
      <th width="20%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>transformer</td>
      <td>any</td>
      <td>否</td>
      <td><strong>暂不支持，传值不生效，自动忽略该参数。</strong></td>
    </tr>
    <tr>
      <td>writableStrategy</td>
      <td><a href="#WritableStrategy">WritableStrategy</a></td>
      <td>否</td>
      <td>可写端策略配置。</td>
    </tr>
  </tbody>
</table>

#### WritableStrategy[](id:WritableStrategy)

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
			<td>highWaterMark</td>
			<td>number</td>
			<td>是</td>
			<td>
        可写端缓冲区大小，以字节为单位，默认值为 32K, 最大值为 256K, 超过最大值则会自动调整为 256K。
      </td>
		</tr>
	</tbody>
</table>

## 属性
### readable
```typescript
readonly readable: ReadableStream;
```

可读端，详情参见 [ReadableStream](https://cloud.tencent.com/document/product/1552/81914)。

### writable
```typescript
readonly writable: WritableStream;
```

可写端，详情参见 [WritableStream](https://cloud.tencent.com/document/product/1552/81922)。

## 示例代码
```typescript
async function handleEvent(event) {
  // 生成可读端与可写端
  const { readable, writable } = new TransformStream();
  // 获取远程资源 
  const response = await fetch('https://www.tencentcloud.com/');
  // 流式响应客户端 
  response.body.pipeTo(writable);

  return new Response(readable, response);
}

addEventListener('fetch', (event) => {
  event.respondWith(handleEvent(event));
});
```

## 相关参考 
- [MDN 官方文档：TransformStream](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream)
- [示例函数：合并资源流式响应](https://cloud.tencent.com/document/product/1552/84085)
- [示例函数：m3u8 改写与鉴权](https://cloud.tencent.com/document/product/1552/84086)
