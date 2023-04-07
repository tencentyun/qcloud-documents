# wx.sendSms(Object object)

## 功能描述

拉起手机发送短信界面。

## 参数

### Object object

| 属性        | 类型     | 默认值 | 必填 | 说明                                             |
| :---------- | :------- | :----- | :--- | :----------------------------------------------- |
| phoneNumber | string   |        | 否   | 预填到发送短信面板的手机号                       |
| content     | string   |        | 否   | 预填到发送短信面板的内容                         |
| success     | function |        | 否   | 接口调用成功的回调函数                           |
| fail        | function |        | 否   | 接口调用失败的回调函数                           |
| complete    | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |