# setStorageSync

- 功能描述

[wx.setStorage](./setStorage.md) 的同步版本

- 参数

**string key**

本地缓存中指定的 key

**any data**

需要存储的内容。只支持原生类型、Date、及能够通过`JSON.stringify`序列化的对象。

- 示例代码

```js
wx.setStorage({
  key:"key",
  data:"value"
})
```

```js
try {
  wx.setStorageSync('key', 'value')
} catch (e) { }
```