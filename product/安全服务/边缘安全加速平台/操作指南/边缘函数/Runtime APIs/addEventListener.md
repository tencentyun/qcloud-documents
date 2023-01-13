注册事件监听器，用于触发边缘函数脚本的执行。当前仅支持 `fetch` 请求事件，通过注册 `fetch` 事件监听器，生成 HTTP 请求事件 [FetchEvent](https://cloud.tencent.com/document/product/1552/81899) ，进而实现对 HTTP 请求的处理。

## 描述

```typescript
function addEventListener(type: string, listener: (event: FetchEvent) => void): void;
```

在一个边缘函数中，一种类型的事件，只允许注册一个事件监听器，若重复注册，只有最后注册的事件监听器有效。

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
      <td>type</td>
      <td>string</td>
      <td>是</td>
      <td>
        <p>事件类型。</p>
        <li>当前仅支持 <code>fetch</code> 请求事件。</li>
        <li>非 <code>fetch</code> 请求事件，边缘函数引擎会主动抛出 <code>Error</code> 类型的异常。</li>
      </td>
    </tr>
    <tr>
      <td>listener</td>
      <td>
        (event: <a href="https://cloud.tencent.com/document/product/1552/81899">FetchEvent</a>) => void
      </td>
      <td>是</td>
      <td>
        <p>事件监听器。用于处理事件回调。</p>
        <li>注册 <code>fetch</code> 请求事件生成 <a href="https://cloud.tencent.com/document/product/1552/81899">FetchEvent</a> 类的事件监听器。</li>
      </td>
    </tr>
  </tbody>
</table>

## 示例代码
```js
// 注册 fetch 请求事件监听器
addEventListener('fetch', (event) => {
  // 响应客户端
  event.respondWith(new Response('Hello World!'));
});
```

## 相关参考 
- [MDN 官方文档：addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [示例函数：返回 HTML 页面](https://cloud.tencent.com/document/product/1552/81941)
- [示例函数：返回 JSON](https://cloud.tencent.com/document/product/1552/81942)
