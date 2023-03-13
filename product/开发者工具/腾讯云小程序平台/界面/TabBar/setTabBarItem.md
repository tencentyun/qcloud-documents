# setTabBarItem

- 功能描述

动态设置 tabBar 某一项的内容。

- 参数

**Object object**

| 属性             | 类型     | 默认值 | 必填 | 说明                                                         |
| :--------------- | :------- | :----- | :--- | :----------------------------------------------------------- |
| index            | number   |        | 是   | tabBar 的哪一项，从左边算起                                  |
| text             | string   |        | 否   | tab 上的按钮文字                                             |
| iconPath         | string   |        | 否   | 图片路径，icon 大小限制为 40kb，建议尺寸为 81px * 81px，当 postion 为 top 时，此参数无效 |
| selectedIconPath | string   |        | 否   | 选中时的图片路径，icon 大小限制为 40kb，建议尺寸为 81px * 81px ，当 postion 为 top 时，此参数无效 |
| success          | function |        | 否   | 接口调用成功的回调函数                                       |
| fail             | function |        | 否   | 接口调用失败的回调函数                                       |
| complete         | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

- 示例代码

```js
wx.setTabBarItem({
  index: 0,
  text: 'text',
  iconPath: '/path/to/iconPath',
  selectedIconPath: '/path/to/selectedIconPath'
})
```