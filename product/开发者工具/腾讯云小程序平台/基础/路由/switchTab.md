# switchTab

- 功能描述

跳转到 tabBar 页面，并关闭其他所有非 tabBar 页面

- 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                                         |
| :------- | :------- | :----- | :--- | :----------------------------------------------------------- |
| url      | string   |        | 是   | 需要跳转的 tabBar 页面的路径 (代码包路径)（需在 app.json 的 [tabBar](/develop/frame/dispose.md) 字段定义的页面），路径后不能带参数。 |
| success  | function |        | 否   | 接口调用成功的回调函数                                       |
| fail     | function |        | 否   | 接口调用失败的回调函数                                       |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

- 示例代码

```json
// app.json
{
  "tabBar": {
    "list": [{
      "pagePath": "index",
      "text": "首页"
    },{
      "pagePath": "other",
      "text": "其他"
    }]
  }
}
```

```
wx.switchTab({
  url: '/index'
})
```