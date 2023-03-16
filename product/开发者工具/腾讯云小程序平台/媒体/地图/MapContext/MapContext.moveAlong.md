# MapContext.moveAlong(Object object)

>  支持度：
>
> 系统地图（仅iOS支持）：是
>
> 谷歌地图（Android、IDE支持）：否
>
> 华为地图（仅Android支持）：否
>
> 腾讯地图（Android、IDE支持）：否

## 功能描述

沿指定路径移动 `marker`，用于轨迹回放等场景。动画完成时触发回调事件，若动画进行中，对同一 `marker` 再次调用 `moveAlong` 方法，前一次的动画将被打断。

## 参数

### Object object

| 属性       | 类型     | 默认值 | 必填 | 说明                                                 |
| :--------- | :------- | :----- | :--- | :--------------------------------------------------- |
| markerId   | number   |        | 是   | 指定 marker                                          |
| path       | Array    |        | 是   | 移动路径的坐标串，坐标点格式 `{longitude, latitude}` |
| autoRotate | boolean  | true   | 否   | 根据路径方向自动改变 marker 的旋转角度               |
| duration   | number   |        | 是   | 平滑移动的时间                                       |
| success    | function |        | 否   | 接口调用成功的回调函数                               |
| fail       | function |        | 否   | 接口调用失败的回调函数                               |
| complete   | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）     |