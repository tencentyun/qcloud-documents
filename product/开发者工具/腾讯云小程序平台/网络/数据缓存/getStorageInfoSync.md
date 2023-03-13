# getStorageInfoSync

- 功能描述

[wx.getStorageInfo](/develop/API/datastorage/getStorageInfo.md) 的同步版本

- 返回值

**Object object**

| 属性        | 类型           | 说明                        |
| :---------- | :------------- | :-------------------------- |
| keys        | Array.<string> | 当前 storage 中所有的 key   |
| currentSize | number         | 当前占用的空间大小, 单位 KB |
| limitSize   | number         | 限制的空间大小，单位 KB     |

- 示例代码

```js
wx.getStorageInfo({
  success (res) {
    console.log(res.keys)
    console.log(res.currentSize)
    console.log(res.limitSize)
  }
})
```

```
try {
  const res = wx.getStorageInfoSync()
  console.log(res.keys)
  console.log(res.currentSize)
  console.log(res.limitSize)
} catch (e) {
  // Do something when catch error
}
```