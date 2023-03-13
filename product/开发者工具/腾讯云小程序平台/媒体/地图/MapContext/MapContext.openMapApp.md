# MapContext.openMapApp(Object object)

>  支持度：
>
> 系统地图（仅iOS支持）：是
>
> 谷歌地图
> - Android支持：是
> - IDE支持：否
>
> 华为地图（仅Android支持）：是
>
> 腾讯地图
> - Android支持：是
> - IDE支持：否

## 功能描述

拉起地图 APP 选择导航。

## 参数

### Object object

| 属性        | 类型     | 默认值 | 必填 | 说明                                             |
| :---------- | :------- | :----- | :--- | :----------------------------------------------- |
| longitude   | Number   |        | 是   | 目的地经度                                       |
| latitude    | Number   |        | 是   | 目的地纬度                                       |
| destination | String   |        | 是   | 目的地名称                                       |
| success     | function |        | 否   | 接口调用成功的回调函数                           |
| fail        | function |        | 否   | 接口调用失败的回调函数                           |
| complete    | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |