边缘函数基于 **V8 JavaScript 引擎**设计实现的 Serverless 代码执行环境，提供了以下标准化的 Web APIs。

## JavaScript 标准内置对象

边缘函数支持所有 JavaScript 标准内置对象，详情参见 [MDN 官方文档：JavaScript Standard built-in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)。

## URL
```typescript
const urlInfo = new URL('https://www.tencentcloud.com/');
```

URL API 用于解析，构造，规范化和编码 URL，详情参见 [MDN 官方文档：URL](https://developer.mozilla.org/en-US/docs/Web/API/URL)。

## Blob
```typescript
const blob = new Blob(['hello', 'world'], { type: 'text/plain' });
```

Blob API 表示不可变、原始数据的类文件对象，详情参见 [MDN 官方文档：Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob)。

## Base64
### btoa
```typescript
function btoa(data: string | ArrayBuffer | ArrayBufferView): string;
```

执行 base64 编码，不支持 Unicode 字符串，详情参见 [MDN 官方文档：btoa](https://developer.mozilla.org/en-US/docs/Web/API/btoa)。

### atob
```typescript
function atob(data: string): string;
```

执行 base64 解码，不支持 Unicode 字符串，详情参见 [MDN 官方文档：atob](https://developer.mozilla.org/en-US/docs/Web/API/atob)。

### btoaUTF8
```typescript
function btoaUTF8(data: string): string;
```

执行 base64 编码，支持 Unicode 字符串。

### atobUTF8
```typescript
function atobUTF8(data: string): string;
```

执行 base64 解码，不支持 Unicode 字符串。

## 事件发布与订阅

### EventTarget

```typescript
const eventTarget = new EventTarget();
```

事件发布与订阅，详情参见 [MDN 官方文档：EventTarget](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)。

### Event
```typescript
const event = new Event('type name');
```

基础事件，详情参见 [MDN 官方文档：Event](https://developer.mozilla.org/en-US/docs/Web/API/Event)。

## 中止信号与控制器
### AbortSignal
```typescript
const signal = AbortSignal.abort();
```

中止信号，详情参见 [MDN 官方文档：AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)。

### AbortController
```typescript
const controller = new AbortController();
```

中止控制器，详情参见 [MDN 官方文档：AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)。
