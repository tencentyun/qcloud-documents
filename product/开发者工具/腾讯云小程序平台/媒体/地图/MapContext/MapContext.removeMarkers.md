# MapContext.removeMarkers(Object object)

>  支持度：
>
> 系统地图（仅iOS支持）：是
>
> 谷歌地图（Android、IDE支持）：是
>
> 华为地图（仅Android支持）：是
>
> 腾讯地图（Android、IDE支持）：是

## 功能描述

移除 marker。

## 参数

### Object object

| 属性      | 类型     | 默认值 | 必填 | 说明                                             |
| :-------- | :------- | :----- | :--- | :----------------------------------------------- |
| markerIds | Array    |        | 是   | marker 的 id 集合。                              |
| success   | function |        | 否   | 接口调用成功的回调函数                           |
| fail      | function |        | 否   | 接口调用失败的回调函数                           |
| complete  | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |