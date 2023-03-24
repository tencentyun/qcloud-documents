# wx.chooseContact(Object object)

## 功能描述

拉起手机通讯录，选择联系人。

## 参数

### Object object

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object object

| 属性            | 类型   | 说明                                                         |
| :-------------- | :----- | :----------------------------------------------------------- |
| phoneNumber     | string | 手机号                                                       |
| displayName     | string | 联系人姓名                                                   |
| phoneNumberList | string | 选定联系人的所有手机号（部分 Android 系统只能选联系人而不能选特定手机号） |