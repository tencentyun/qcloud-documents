注册事件监听器。

## 描述
在一个 workers 脚本中，一种类型的事件，只允许注册对应的一个事件监听器，重复注册的话，只有最后注册的事件监听器有效。
```typescript
function addEventListener(type: string, listener: (ev: FetchEvent) => void): void;
```


### 参数
- type: string<br>事件类型，当前仅支持 `fetch`事件; 对于非 `fetch` 事件，Workers 引擎会主动抛出 Error 类型的异常。
- listener: (ev: [FetchEvent](https://cloud.tencent.com/document/product/1552/81899)) => void<br>事件监听器，用于处理接收到的请求事件。

## 示例
```js
addEventListener('fetch', (event) => {
  event.respondWith(new Response("Hello World!"));
});
```

## 参考
- [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
