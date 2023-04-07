# removeStorageSync

- 功能描述

[wx.removeStorage](./removeStorage.md) 的同步版本

- 参数

**string key**

本地缓存中指定的 key

- 示例代码

```js
wx.removeStorage({
  key: 'key',
  success (res) {
    console.log(res)
  }
})
```

```
try {
  wx.removeStorageSync('key')
} catch (e) {
  // Do something when catch error
}
```