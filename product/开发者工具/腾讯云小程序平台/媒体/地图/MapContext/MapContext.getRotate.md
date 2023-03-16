# MapContext.getRotate(Object object)

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

获取当前地图的旋转角

## 参数

### Object object

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性   | 类型   | 说明   |
| :----- | :----- | :----- |
| rotate | number | 旋转角 |