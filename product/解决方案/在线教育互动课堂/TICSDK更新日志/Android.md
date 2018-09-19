## boardsdk [1.5.1] - 2018-09-11
### 优化
1. 优化文件存储模块。

## ticsdk [1.5.0] - 2018-09-03
### 优化
1. 接口优化。

### 删除
1. 移除初始化接口中的 accountType 参数。

### 接口变更
1. TICClassroomOption 中 setEnableCamera() 变更为 autoCamera()，setEnableMic 变更为 autoMic()；
2. TICManager 中合并和精简了如 send###MessageIM 消息系列发送接口；
3. IClassroomIMListener 合并和精简了消息回调接口，由 Constants 中的 MSG_TYPE_C2C 和 MSG_TYPE_GROUP 区分消息类型；
4. TICManager 中新增了 destroyClassroom 接口。

## boardsdk [1.5.0] - 2018-09-03
### 新增
1. 增加 COS 大账号模式；

### 优化
1. 增加白板背景资源预缓存逻辑和清理逻辑；
2. 接口优化；
3. 优化激光点功能。

### 删除
1. 移除初始化接口中的 accountType 信息。

## ticsdk [1.2.2] - 2018-08-15
### 新增
1. 将 COS 相关逻辑迁移至白板 SDK 内，并移除 TICManager 的 setCosConfig 接口。

## boardsdk [1.2.10] - 2018-08-15
### 新增
1. 增加 COS 相关业务逻辑，WhiteboardManager 增加 setCosConfig 接口；
2. WhiteboardView 支持设置宽高比例；
3. WhiteboardView 支持缩放和拖动；
4. 内置 HTTP 下载，用户不再需实现 WhiteboardEventListener 中的 uploadImage 和 downloadImage 接口。

### 优化
1. 优化手绘涂鸦的圆滑性，减少涂鸦的“折线”现象。

### 修复
1. 修复已知 ANR 问题和 crash 问题。

## ticsdk [1.2.1] - 2018-07-24
### 新增
1. 新增 IM 原始类型消息回调；
2. 新增 IM 原始类型消息发送接口。

## boardsdk [1.2.8] - 2018-07-24
### 修复
1. 修复若干已知问题。

### 优化
1. 优化日志模块。

## ticsdk [1.1.1] - 2018-07-11
### 优化
1. 默认使用实时音视频线路优化版本。

## boardsdk [1.2.6.4] - 2018-07-11
### 修复
1. 修复若干已知问题。

### 优化
1. 优化中途进课堂体验。

## ticsdk [1.0.1] - 2018-06-29
### 新增
1. 新增成员加入课堂和退出课堂事件回调；
2. 修复若干已知问题。

## boardsdk [1.2.5.6] - 2018-06-29
### 修复
1. 修复若干绘制异常问题。

### 优化
1. 优化白板绘制，降低 CPU 占用。

## ticsdk [1.0.0] - 2018-06-13
### 新增
1.0.0 版本发布，包含以下功能：

1. 账号登录；
2. 创建、加入、退出课堂；
3. 在线课堂线上音视频互动；
4. 数字白板功能；
5. 课堂 IM 消息互动。
