基于 Web APIs 标准 [TextEncoder](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder/TextEncoder)、[TextDecoder](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/TextDecoder) 进行设计，实现了编码器与解码器。

## TextEncoder
编码器，接受码点流作为输入，并输出 `UTF-8` 字节流。请参考 MDN 官方文档 [TextEncoder](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder/TextEncoder)。 

### 构造函数

```typescript
// TextEncoder 构造函数，不接受任何参数。
const encoder = new TextEncoder();
```

### 属性
```typescript
// encoder.encoding
readonly encoding: string;
```

编码器的编码类型，当前值仅为 `UTF-8`。

### 方法
#### encode 
```typescript
encoder.encode(input?: string | undefined): Uint8Array
```
接受码点流作为输入，并输出 `UTF-8` 字节流。

>! **input 最大长度为 300M**，超出长度会抛出异常。

- `encoder.encode` 参数

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
      <td>input</td>
      <td>string | undefined</td>
      <td>否</td>
      <td>编码器输入值。</li>
      </td>
    </tr>
  </tbody>
</table>

#### encodeInto 
```typescript
encoder.encodeInto(input: string, destination: Uint8Array): EncodeIntoResult;
```
接受码点流作为输入，输出 `UTF-8` 字节流，并写入到参数 `destination` 字节数组中。

- 参数

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
      <td>input</td>
      <td>string</td>
      <td>是</td>
      <td>编码器输入值。</td>
    </tr>
    <tr>
      <td>destination</td>
      <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array">Uint8Array</a></td>
      <td>是</td>
      <td>编码器输出值。</td>
    </tr>
  </tbody>
</table>


- 返回值 `EncodeIntoResult`

<table>
  <thead>
    <tr>
      <th width="15%">属性名</th>
      <th width="15%">类型</th>
      <th width="70%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>read</td>
      <td>number</td>
      <td>已转换为 UTF-8 的 UTF-16 单元数。</td>
    </tr>
    <tr>
      <td>written</td>
      <td>number</td>
      <td>目标 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array">Uint8Array</a> 中修改的字节数。</td>
    </tr>
  </tbody>
</table>

## TextDecoder
解码器。将字节流作为输入，并提供码点流作为输出。请参考 MDN 官方文档 [TextDecoder](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/TextDecoder)。

### 构造方法

```typescript
const decoder = new TextDecoder(label?: string | undefined, options?: DecoderOptions | undefined): TextEncoder;
```

### 参数

>! 参数 [label](https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings) ，下述的值暂不支持：
>- iso-8859-16。
>- hz-gb-2312。
>- csiso2022kr，iso-2022-kr。

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
      <td>label</td>
      <td>string | <br/> undefined</td>
      <td>否</td>
      <td>
        解码器类型，默认值为 <code>UTF-8</code>。可选的 <code>label</code> 值参考 <a href="https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings">MDN 官方文档</a>
      </td>
    </tr>
    <tr>
      <td>options</td>
      <td><a href="#MatchOptions">DecoderOptions</a> | <br/> undefined</td>
      <td>否</td>
      <td>解码器配置项</td>
    </tr>
  </tbody>
</table>

#### DecoderOptions[](id:MatchOptions)
解码器配置项如下所示。

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">默认值</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>fatal</td>
			<td>boolean</td>
			<td>false</td>
			<td>标识解码失败时是否抛出异常</td>
		</tr>
    <tr>
			<td>ignoreBOM</td>
			<td>boolean</td>
			<td>false</td>
			<td>标识是否忽略 <a href="https://www.w3.org/International/questions/qa-byte-order-mark">byte-order marker</a></td>
		</tr>
	</tbody>
</table>

### 属性
#### encoding
```typescript
// decoder.encoding
readonly encoding: string;
```
解码器类型。

#### fatal
```typescript
// decoder.fatal
readonly fatal: boolean;
```

当解码失败，标识是否抛出异常。

#### ignoreBOM
```typescript
// decoder.ignoreBOM
readonly ignoreBOM: boolean;
```
标识是否忽略 [byte-order marker](https://www.w3.org/International/questions/qa-byte-order-mark)。

### 方法
#### decode

```typescript
const result = decoder.decode(buffer?: ArrayBuffer | ArrayBufferView | undefined, options?: DecodeOptions | undefined): string;
```
>! 参数 `buffer` 最大长度为 100M，超出长度会抛出异常。
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
      <td>buffer</td>
      <td>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer">ArrayBuffer</a> | <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer">ArrayBufferView</a> | undefined
      </td>
      <td>否</td>
      <td>
        待解码的字节流。<br>
        <li><code>buffer</code> 最大长度为 100M，超出长度会抛出异。</li>
      </td>
    </tr>
    <tr>
      <td>options</td>
      <td>
        <a href="#DecodeOptions">DecodeOptions</a>
      </td>
      <td>否</td>
      <td>执行解码配置项。</td>
    </tr>
  </tbody>
</table>

#### DecodeOptions[](id:DecodeOptions)
执行解码配置项如下所示。

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">默认值</th>
			<th width="65%">说明</th>
	  </tr>
	</thead>
	<tbody>
		<tr>
			<td>stream</td>
			<td>boolean</td>
			<td>false</td>
			<td>
        设置流式解码，默认为 false ，取值说明如下。<br/>
        <li>
          <font color="#9ba6b7">true</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            表示以 <code>chunk</code> 的方式处理数据，即流式解码。
          </div>
        </li>
        <li>
          <font color="#9ba6b7">false</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            表示 <code>chunk</code> 已结束或未使用 <code>chunk</code> 处理数据，即非流式解码。
          </div>
        </li>
      </td>
		</tr>
	</tbody>
</table>

## 示例代码
```typescript
function handleEvent(event) {
  // 编码器
  const encoder = new TextEncoder();
  const encodeText = encoder.encode('hello world');
  
  // 解码器
  const decoder = new TextDecoder();
  const decodeText = decoder.decode(encodeText);

  // 客户端响应内容
  const response = new Response(JSON.stringify({
    encodeText: encodeText.toString(),
    decodeText,
  }));

  return response;
}

addEventListener('fetch', (event) => {
  event.respondWith(handleEvent(event));
});
```

## 相关参考 
- [MDN 官方文档：TextEncoder](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder)
- [MDN 官方文档：TextDecoder](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)
- [MDN 官方文档：Encoding Label](https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings)
- [示例函数：防篡改校验](https://cloud.tencent.com/document/product/1552/84081)
