# choosePoi

- 功能描述

打开 POI 列表选择位置，支持模糊定位（精确到市）和精确定位混选。

- 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

**object.success 回调函数**

- 参数

**Object res**

| 属性      | 类型   | 说明                                                         |
| :-------- | :----- | :----------------------------------------------------------- |
| type      | number | 选择城市时，值为 1，选择精确位置时，值为 2                   |
| city      | number | 城市名称                                                     |
| name      | string | 位置名称                                                     |
| address   | string | 详细地址                                                     |
| latitude  | number | 纬度，浮点数，范围为-90~90，负数表示南纬。使用 gcj02 国测局坐标系（即将废弃） |
| longitude | number | 经度，浮点数，范围为-180~180，负数表示西经。使用 gcj02 国测局坐标系（即将废弃） |

## 示例

![img](https://res.wx.qq.com/op_res/lzDsNyBNifLczyLX0ms7ZpPQysgAgdhrQTGzzTQPiXkAB2HJIf1Slvl4rnN9I1q0AT3xqoGTg98jMsNexDLbbA)