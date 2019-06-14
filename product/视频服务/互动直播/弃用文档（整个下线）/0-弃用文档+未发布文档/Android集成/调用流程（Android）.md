## 一、核心模块
1. AVContext：上下文模块，它的对象代表着一个SDK的运行实例，应用程序只需要创建一个AVContext对象就可以使用SDK的所有功能。

2. AVRoom ：房间模块，提供了进入房间和退出房间的回调接口。

3. AVRoomMulti: 多人房间模块，继承了AVRoom，提供了获取房间成员列表等多人房间特性的操作接口

4. AVEndpoint: 房间成员模块，提供了请求或者取消房间成员画面的操作接口

5. AVAudioCtrl: 音频控制模块，提供了音频设备管理和对音频定制化的操作接口

6. AVVideoCtrl: 视频控制模块，提供了视频设备管理和获取视频流等操作接口

7. 视频渲染模块：将获取的视频流通过渲染模块播放到画面上。

## 二、 调用流程
下面是为了实现互动直播，调用音视频SDK的步骤和每一个步骤所用的方法主要对应的类。

在APP中用户分为主播和观众，开启视频时有不一样的调用流程：

**主播方开启视频：**

1. 创建AVContext（AVContext）

2. 启动AVContext（AVContext）

3. 进入房间（AVContext，AVRoom , AVRoomMulti）

4. 打开麦克风（AVAudioCtrl）

5. 打开摄像头，上传本端视频数据（AVVideoCtrl）

6. 获取房间内成员状态（AVRoomMulti，AVEndpoint）

7. 请求远端用户的视频数据（AVEndpoint）

8. 渲染视频画面（视频渲染模块）


**观众方开启视频：**

1. 创建AVContext（AVContext）

2. 启动AVContext（AVContext）

3. 进入房间（AVContext，AVRoom , AVRoomMulti）

4. 获取房间内成员数据（AVRoomMulti，AVEndpoint）

5. 请求远端用户的视频数据（AVEndpoint）

6. 渲染视频画面（视频渲染模块）


**关闭视频：**
1. 停止视频渲染（视频渲染模块）

2. 退出房间（AVContext）

3. 终止AVContext（AVContext）

4. 销毁AVContext（AVContext）