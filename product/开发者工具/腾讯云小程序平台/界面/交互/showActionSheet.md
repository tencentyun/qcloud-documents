# showActionSheet

- 功能描述

显示操作菜单

- 参数

**Object object**

| 属性      | 类型           | 默认值  | 必填 | 说明                                             | 最低版本                                                     |
| :-------- | :------------- | :------ | :--- | :----------------------------------------------- | :----------------------------------------------------------- |
| itemList  | Array.&lt;string&gt; |         | 是   | 按钮的文字数组，数组长度最大为 6                 |                                                              |
| itemColor | string         | #000000 | 否   | 按钮的文字颜色                                   |                                                              |
| success   | function       |         | 否   | 接口调用成功的回调函数                           |                                                              |
| fail      | function       |         | 否   | 接口调用失败的回调函数                           |                                                              |
| complete  | function       |         | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |                                                              |

**object.success 回调函数**

- 参数

**Object res**

| 属性     | 类型   | 说明                                        |
| :------- | :----- | :------------------------------------------ |
| tapIndex | number | 用户点击的按钮序号，从上到下的顺序，从0开始 |

- 示例代码

```js
wx.showActionSheet({
  itemList: ['A', 'B', 'C'],
  success (res) {
    console.log(res.tapIndex)
  },
  fail (res) {
    console.log(res.errMsg)
  }
})
```
