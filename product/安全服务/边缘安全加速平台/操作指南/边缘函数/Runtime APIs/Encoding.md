## TextEncoder
编码器。接受码点流作为输入，并提供 UTF-8 字节流作为输出。

### 语法

```typescript
class TextEncoder {
  readonly encoding: string;

  constructor(): TextEncoder;
  encode(input?: string | undefined): Uint8Array;
  encodeInto(input: string, destination: Uint8Array): {read: number, written: number};
}
```

### 构造方法

```js
let encoder = new TextEncoder();
log(encoder.encoding);
```

### 属性
- encoding:  string<br>编码器的编码类型，当前只会返回 "utf-8"。

### 方法
- encode(input?: string | undefined):  Uint8Array
  - 接受码点流作为输入，并提供 UTF-8 字节流作为输出。
  - **input 最大长度为 300M**，超出长度会抛出异常。
- encodeInto(input: string, destination: Uint8Array):  {read: number, written: number}
 - 接受码点流作为输入，输出的 UTF-8 字节流写入到 destination 字节数组中。
 - 返回值为包含如下成员的对象：
    - read：已转换为 UTF-8 的 UTF-16 单元数。
    - written：目标 Uint8Array 中修改的字节数。

## TextDecoder
解码器。将字节流作为输入，并提供码点流作为输出。

### 语法
```typescript
class TextDecoder {
  readonly encoding: string;
  readonly fatal: boolean;
  readonly ignoreBOM: boolean;

  constructor(utfLabel?: string | undefined, options?: {fatal: boolean, ignoreBOM: boolean} | undefined): TextEncoder;
  decode(buffer?: ArrayBuffer | ArrayBufferView | undefined, options?: {stream: boolean} | undefined): string;
}
```

### 构造方法
- utfLabel 可选<br>可选参数，指定解码器类型，默认值为 "utf-8". 合法的 label 值可参考 [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings)。
>!如下 label 值暂不支持：
>- iso-8859-16。
>- hz-gb-2312。
>- csiso2022kr，iso-2022-kr。
- options 可选<br>可选对象，包含如下选项：<br>
  - fatal：标识解码失败时是否抛出异常，默认值为 false。
  - ignoreBOM：标识是否忽略 byte-order marker，默认值为 false。


### 属性
- encoding:  string<br>解码器类型。
- fatal:  boolean<br>当解码失败，标识是否抛出异常。
- ignoreBOM:  boolean<br>标识是否忽略 byte-order marker。

### 方法
- decode(buffer?: ArrayBuffer | ArrayBufferView | undefined, options?: {stream: boolean} | undefined):  string<br>对输入的字节流进行解码，参数说明如下:<br>
  - buffer：可选参数，表示待解码的字节流，若没有数据需要解码，则填入 undefined；**buffer 最大长度为 100M**，超出长度会抛出异常。<br>
  - options: 可选对象，用于流式解码，默认为非流式。<br>如果以 chunk 的方式处理数据，则设置为 true，但如果 chunk 已结束或数据未使用 chunk，则设置为 false。 默认值为 flase。

## 示例
#### 基本使用
```js
let encoder = new TextEncoder();
log(encoder.encode("hello"));

const u8Arr = new Uint8Array(8);
let ret = encoder.encodeInto("hello", u8Arr);
log(ret);
log(u8Arr.slice(0, ret.written));

let decoder = new TextDecoder();
log(decoder.decode(u8Arr.slice(0, ret.written)));
```
#### 流式解码
```js
let encoder = new TextEncoder();
const u8Arr = encoder.encode("你好");

let decoder = new TextDecoder(undefined, {fatal: true, ignoreBOM: true});
log(decoder.decode(u8Arr.slice(0, 4), { stream: true}));
log(decoder.decode(u8Arr.slice(4, 6), { stream: false}));
```

## 参考
* [TextEncoder](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder)
* [TextDecoder](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)
* [Label](https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings)
