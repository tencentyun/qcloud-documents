# wx.getFuzzyLocation(Object object)

## 功能描述

获取当前的模糊地理位置。

## 参数

### Object object

| 属性     | 类型     | 默认值 | 必填 | 说明                                                         |
| :------- | :------- | :----- | :--- | :----------------------------------------------------------- |
| type     | string   | wgs84  | 否   | wgs84 返回 gps 坐标，gcj02 返回可用于 wx.openLocation 的坐标 |
| success  | function |        | 否   | 接口调用成功的回调函数                                       |
| fail     | function |        | 否   | 接口调用失败的回调函数                                       |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

#### object.success 回调函数

##### 参数

###### Object res

| 属性      | 类型   | 说明                                |
| :-------- | :----- | :---------------------------------- |
| latitude  | number | 纬度，范围为 -90~90，负数表示南纬   |
| longitude | number | 经度，范围为 -180~180，负数表示西经 |

## 示例代码

```js
wx.getFuzzyLocation({
 type: 'wgs84',
 success (res) {
   const latitude = res.latitude
   const longitude = res.longitude
 }
})
```