# MapContext.includePoints(Object object)

>  支持度：
>
> 系统地图（仅iOS支持）：否
>
> 谷歌地图（Android、IDE支持）：是
>
> 华为地图（仅Android支持）：是
>
> 腾讯地图（Android、IDE支持）：是

## 功能描述

缩放视野展示所有经纬度

## 参数

### Object object

| 属性     | 类型           | 默认值 | 必填 | 说明                                                         |
| :------- | :------------- | :----- | :--- | :----------------------------------------------------------- |
| points   | Array.<Object> |        | 是   | 要显示在可视区域内的坐标点列表                               |
| padding  | Array.<number> |        | 否   | 坐标点形成的矩形边缘到地图边缘的距离，单位像素。格式为[上,右,下,左]，安卓上只能识别数组第一项，上下左右的 padding 一致。开发者工具暂不支持 padding 参数。 |
| success  | function       |        | 否   | 接口调用成功的回调函数                                       |
| fail     | function       |        | 否   | 接口调用失败的回调函数                                       |
| complete | function       |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

**points**

| 结构属性  | 类型   | 默认值 | 必填 | 说明 |
| :-------- | :----- | :----- | :--- | ---- |
| longitude | number |        | 是   | 经度 |
| latitude  | number |        | 是   | 纬度 |