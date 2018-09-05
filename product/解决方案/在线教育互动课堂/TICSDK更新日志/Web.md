# TICSDK更新日志

## [1.3.0] - 2018-09-05
### 优化
1. TICSDK支持cos大账号模式。

### 变更

1. 接口名变更
    | 原接口名 | 新接口名 | 描述
    | -------- | --------- | ------ |
    | uploadFile | addFile和addImgFile | 原来的上传PPT接口改为addFile（上传PPT），addImgFile（上传图片） | 
    | sendC2CTextMessage<br/>sendGroupTextMessage | sendTextMessage | sendC2CTextMessage，sendGroupTextMessage接口合并为一个 |
    | sendC2CCustomMessage<br/>sendGroupCustomMessage | sendCustomTextMessage | sendC2CCustomMessage，sendGroupCustomMessage合并为一个 |


## [1.2.0] - 2018-08-08
### 优化
1. 支持设置im用户昵称和头像。
2. 封装im事件回调对齐WebIm。
3. TICSDK支持纯音频推流。
4. 修复白板若干bug。

## [1.1.0] - 2018-07-13
### 优化
1. 修复白板若干 bug，完善白板 SDK 体验

## [1.0.0] - 2018-06-13
### 新增
1.0.0 版本发布，包含以下功能：

1. 账号登录；
2. 创建、加入、退出课堂；
3. 在线课堂线上音视频互动；
4. 数字白板功能；
5. 课堂 IM 消息互动。


# BoardSDK更新日志

> 如果1.x需要升级到2.x，请先与腾讯云侧联系。

## [2.2.0] 2018-09-05
1. 提供公共 COS 账户，无需客户自行申请配置 COS 账号。
2. 解决上传文件名带特殊字符的问题。

## [2.1.0] 2018-08-02
1. 修复白板candraw的Bug。
2. 背景图片的加载优化。

## [2.0.0] 2018-07-20
1. 调整白板事件回调监听方式。
2. 调整白板初始化。

## [1.2.7] 2018-07-15
1. 新增清空文件涂鸦功能。
2. 修复获取白板历史数据和Im消息不同步的bug。

## [1.2.0] - 2018-06-11
1. 修复白板SDK若干bug。