# CameraFrameListener

> 相关文档: [camera 组件介绍](../../../component/media/camera.md)

CameraContext.onCameraFrame() 返回的监听器。

#### 方法

##### [CameraFrameListener.start(Object object)](./CameraFrameListener.md#start)

开始监听帧数据

##### [CameraFrameListener.stop()](./CameraFrameListener.md#stop)

停止监听帧数据

### start

#### CameraFrameListener.start(Object object)

开始监听帧数据

#### 参数

**Object object**

| 属性     | 类型                                                         | 默认值 | 必填 | 说明                                                         | 最低版本 |
| :------- | :----------------------------------------------------------- | :----- | :--- | :----------------------------------------------------------- | :------- |
| success  | function                                                     |        | 否   | 接口调用成功的回调函数                                       |          |
| fail     | function                                                     |        | 否   | 接口调用失败的回调函数                                       |          |
| complete | function                                                     |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |          |

### stop

#### CameraFrameListener.stop(Object object)

停止监听帧数据

#### 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |