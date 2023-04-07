# getStorage

- 功能描述

从本地缓存中异步获取指定 key 的内容。

- 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| :------- | :------- | :----- | :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| key      | string   |        | 是   | 本地缓存中指定的 key                                         |                                                              |
| success  | function |        | 否   | 接口调用成功的回调函数                                       |                                                              |
| fail     | function |        | 否   | 接口调用失败的回调函数                                       |                                                              |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |                                                              |

**object.success 回调函数**

- 参数

**Object res**

| 属性 | 类型 | 说明          |
| :--- | :--- | :------------ |
| data | any  | key对应的内容 |

- 示例代码

```js
wx.getStorage({
  key: 'key',
  success (res) {
    console.log(res.data)
  }
})
```

```
try {
  const value = wx.getStorageSync('key')
  if (value) {
    // Do something with return value
  }
} catch (e) {
  // Do something when catch error
}
```

