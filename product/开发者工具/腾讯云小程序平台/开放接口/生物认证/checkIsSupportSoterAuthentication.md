# checkIsSupportSoterAuthentication(Object object)

## 功能描述

校验本机是否支持生物认证，支持时回调success，不支持时回调fail

## 参数

### Object object

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```js
wx.checkIsSupportSoterAuthentication({
  success() {
    // 支持生物认证
   }
})
```