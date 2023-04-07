# checkIsSoterEnrolledInDevice(Object object)

## 功能描述

校验设备内是否录入生物信息

## 参数

### Object object

| 属性          | 类型     | 默认值 | 必填 | 说明                                             |
| :------------ | :------- | :----- | :--- | :----------------------------------------------- |
| success       | function |        | 否   | 接口调用成功的回调函数                           |
| fail          | function |        | 否   | 接口调用失败的回调函数                           |
| complete      | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性       | 类型    | 说明           |
| :--------- | :------ | :------------- |
| isEnrolled | boolean | 是否已录入信息 |
| errMsg     | string  | 错误信息       |

## 示例代码

```js
wx.checkIsSoterEnrolledInDevice({
  success(res) {
    console.log(res.isEnrolled)
  }
})
```