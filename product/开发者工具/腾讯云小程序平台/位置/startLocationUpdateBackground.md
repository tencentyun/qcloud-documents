# startLocationUpdateBackground

- 功能描述

开启小程序进入前后台时均接收位置消息，需引导用户开启'授权'。授权以后，小程序在运行中或进入后台均可接受位置消息变化。

- 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                                         |
| :------- | :------- | :----- | :--- | :----------------------------------------------------------- |
| type     | string   | gcj02  | 否   | wgs84 返回 gps 坐标，gcj02 返回可用于 wx.openLocation 的坐标 |
| success  | function |        | 否   | 接口调用成功的回调函数                                       |
| fail     | function |        | 否   | 接口调用失败的回调函数                                       |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

