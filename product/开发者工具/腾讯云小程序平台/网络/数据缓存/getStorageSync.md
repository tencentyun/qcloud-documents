# getStorageSync

- 功能描述

从本地缓存中同步获取指定 key 的内容。

- 参数

**string key**

本地缓存中指定的 key

- 返回值

**any**

key对应的内容

- 示例代码

```js
wx.getStorage({
  key: 'key',
  success(res) {
    console.log(res.data)
  }
})
```

```js
try {
  var value = wx.getStorageSync('key')
  if (value) {
    // Do something with return value
  }
} catch (e) {
  // Do something when catch error
}
```