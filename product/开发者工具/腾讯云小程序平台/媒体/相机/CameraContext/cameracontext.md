# CameraContext

CameraContext 实例，可通过 [wx.createCameraContext](./createcameracontext.md) 获取。

`cameraContext` 与页面内唯一的 `<camera>` 组件绑定，操作对应的 `<camera>` 组件。

#### 方法

##### [CameraFrameListener CameraContext.onCameraFrame(onCameraFrameCallback callback)](#oncameraframe)

获取 Camera 实时帧数据

##### [CameraContext.setZoom(Object object)](#setzoom)

设置缩放级别

##### [CameraContext.takePhoto(Object object)](#takephoto)

拍摄照片

##### [CameraContext.startRecord(Object object)](#startrecord)

开始录像

##### [CameraContext.stopRecord()](#stoprecord)

结束录像

#### 示例代码

### onCameraFrame

#### CameraFrameListener CameraContext.onCameraFrame(onCameraFrameCallback callback

获取 Camera 实时帧数据

#### 参数

**function callback**

回调函数

**参数**

**Object res**

| 属性   | 类型        | 说明                                                  |
| :----- | :---------- | :---------------------------------------------------- |
| width  | number      | 图像数据矩形的宽度                                    |
| height | number      | 图像数据矩形的高度                                    |
| data   | ArrayBuffer | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba |

#### 返回值

[CameraFrameListener](/develop/API/media/camera/CameraFrameListener.md)

注： 使用该接口需同时在 [camera](./../../../component/media/camera.md) 组件属性中指定 frame-size。

#### 示例代码

```js
const context = wx.createCameraContext()
const listener = context.onCameraFrame((frame) => {
  console.log(frame.data instanceof ArrayBuffer, frame.width, frame.height)
})
listener.start()
```

### setZoom

#### CameraContext.setZoom(Object object)

设置缩放级别

#### 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                                         |
| :------- | :------- | :----- | :--- | :----------------------------------------------------------- |
| zoom     | number   |        | 是   | 缩放级别，范围[1, maxZoom]。zoom 可取小数，精确到小数后一位。maxZoom 可在 bindinitdone 返回值中获取。 |
| success  | function |        | 否   | 接口调用成功的回调函数                                       |
| fail     | function |        | 否   | 接口调用失败的回调函数                                       |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

**object.success 回调函数**

**参数**

**Object res**

| 属性 | 类型   | 说明                                                         |
| :--- | :----- | :----------------------------------------------------------- |
| zoom | number | 实际设置的缩放级别。由于系统限制，某些机型可能无法设置成指定值，会改用最接近的可设值。 |

### startRecord

#### CameraContext.startRecord(Object object)

开始录像

#### 参数

##### Object object

属性              | 类型       | 默认值 | 必填 | 说明                      
--------------- | -------- | --- | -- | ------------------------
timeoutCallback | function |     | 否  | 超过30s或页面 `onHide` 时会结束录像
success         | function |     | 否  | 接口调用成功的回调函数             
fail            | function |     | 否  | 接口调用失败的回调函数             
complete        | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

###### object.timeoutCallback 回调函数

**参数**

**Object res**

属性            | 类型     | 说明         
------------- | ------ | -----------
tempThumbPath | string | 封面图片文件的临时路径
tempVideoPath | string | 视频的文件的临时路径 

### stopRecord

#### CameraContext.stopRecord(Object object)

结束录像

#### 参数

##### Object object

属性       | 类型       | 默认值 | 必填 | 说明                      
-------- | -------- | --- | -- | ------------------------
success  | function |     | 否  | 接口调用成功的回调函数             
fail     | function |     | 否  | 接口调用失败的回调函数             
complete | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

###### object.success 回调函数

**参数**

**Object res**

属性            | 类型     | 说明         
------------- | ------ | -----------
tempThumbPath | string | 封面图片文件的临时路径
tempVideoPath | string | 视频的文件的临时路径 

### takePhoto

#### CameraContext.takePhoto(Object object)

拍摄照片

#### 参数

##### Object object

属性       | 类型       | 默认值    | 必填 | 说明                      
-------- | -------- | ------ | -- | ------------------------
quality  | string   | normal | 否  | 成像质量                    
success  | function |        | 否  | 接口调用成功的回调函数             
fail     | function |        | 否  | 接口调用失败的回调函数             
complete | function |        | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

**object.quality 的合法值**

值      | 说明  
------ | ----
high   | 高质量 
normal | 普通质量
low    | 低质量 

###### object.success 回调函数

**参数**

**Object res**

属性            | 类型     | 说明       
------------- | ------ | ---------
tempImagePath | string | 照片文件的临时路径
