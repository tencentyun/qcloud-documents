# openLocation

- 功能描述

使用内置地图查看位置

- 参数

**Object object**

| 属性      | 类型     | 默认值 | 必填 | 说明                                                        |
| :-------- | :------- | :----- | :--- | :---------------------------------------------------------- |
| type      | string   | tencent| 否   | 腾讯地图tencent，谷歌地图google，仅IDE支持   |
| latitude  | number   |        | 是   | 纬度，范围为-90~90，负数表示南纬。使用 gcj02 国测局坐标系   |
| longitude | number   |        | 是   | 经度，范围为-180~180，负数表示西经。使用 gcj02 国测局坐标系 |
| scale     | number   | 18     | 否   | 缩放比例，范围5~18                                          |
| name      | string   |        | 否   | 位置名                                                      |
| address   | string   |        | 否   | 地址的详细说明                                              |
| success   | function |        | 否   | 接口调用成功的回调函数                                      |
| fail      | function |        | 否   | 接口调用失败的回调函数                                      |
| complete  | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）            |

- 示例代码

```js
wx.getLocation({
 type: 'gcj02', //返回可以用于 wx.openLocation 的经纬度
 success (res) {
   const latitude = res.latitude
   const longitude = res.longitude
   wx.openLocation({
     latitude,
     longitude,
     scale: 18
   })
 }
})
```