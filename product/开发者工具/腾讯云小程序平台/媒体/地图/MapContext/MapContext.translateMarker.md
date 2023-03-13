# MapContext.translateMarker(Object object)
 
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

平移marker，iOS以及IDE支持动画效果，Android平台暂不支持。

## 参数

### Object object



| 属性           | 类型     | 默认值 | 必填 | 说明                                             | 最低版本                                                     |
| :------------- | :------- | :----- | :--- | :----------------------------------------------- | :----------------------------------------------------------- |
| markerId       | number   |        | 是   | 指定 marker                                      |                                                              |
| destination    | Object   |        | 是   | 指定 marker 移动到的目标点                       |                                                              |
| animationEnd   | function |        | 否   | 动画结束回调函数                                 |                                                              |
| success        | function |        | 否   | 接口调用成功的回调函数                           |                                                              |
| fail           | function |        | 否   | 接口调用失败的回调函数                           |                                                              |
| complete       | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |                                                              |

**destination**

| 结构属性  | 类型   | 默认值 | 必填 | 说明 |
| :-------- | :----- | :----- | :--- | ---- |
| longitude | number |        | 是   | 经度 |
| latitude  | number |        | 是   | 纬度 |