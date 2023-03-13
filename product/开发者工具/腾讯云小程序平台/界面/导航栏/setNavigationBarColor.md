# setNavigationBarColor

- 功能描述

设置页面导航条颜色

- 参数

**Object object**

| 属性            | 类型     | 默认值 | 必填 | 说明                                                         |
| :-------------- | :------- | :----- | :--- | :----------------------------------------------------------- |
| frontColor      | string   |        | 是   | 前景颜色值，包括按钮、标题、状态栏的颜色，仅支持 #ffffff 和 #000000 |
| backgroundColor | string   |        | 是   | 背景颜色值，有效值为十六进制颜色                             |
| animation       | Object   |        | 否   | 动画效果                                                     |
| success         | function |        | 否   | 接口调用成功的回调函数                                       |
| fail            | function |        | 否   | 接口调用失败的回调函数                                       |
| complete        | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

**object.animation 的结构**

| 属性       | 类型   | 默认值   | 必填 | 说明                  |
| ---------- | ------ | -------- | ---- | --------------------- |
| duration   | number | 0        | 否   | 动画变化时间，单位 ms |
| timingFunc | string | 'linear' | 否   | 动画变化方式          |

**object.animation.timingFunc 的合法值**

| 值          | 说明                       |
| ----------- | -------------------------- |
| 'linear'    | 动画从头到尾的速度是相同的 |
| 'easeIn'    | 动画以低速开始             |
| 'easeOut'   | 动画以低速结束             |
| 'easeInOut' | 动画以低速开始和结束       |

- 示例代码

```javascript
wx.setNavigationBarColor({
  frontColor: '#ffffff',
  backgroundColor: '#ff0000',
  animation: {
    duration: 400,
    timingFunc: 'easeIn'
  }
})
```