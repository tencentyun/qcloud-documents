## 业务咨询
请参考其他友商的相关内容
阿里：https://imwukong.com/#faq/0
网易：http://dev.netease.im/docs?doc=faq

## 客户端集成
### Android保活
### 去除imsdk原有的crash上报
云通信SDK默认使用bugly做crash上报，如果App已经集成了Crash上报，则可以不使用该功能，通过调用接口禁用掉，并可以去除相应的jar包或framework
iOS
```
[[TIMManager sharedInstance] disableCrashReport];
```
Android
```
TIMManager.getInstance().disableCrashReport();
```

### iOS/Android重连机制

### Android混淆

### 票据自动化验证？？？

### 多终端切换-最近联系人、消息存储

### 多APP消息互通

### Android Jar包说明

## DEMO

## 消息

### 消息长度限制

### 自定义字段

### 消息、图片、语音、视频的保存时间

### 唯一消息标识



## 用户资料

## 关系链
### 好友验证问题？？？

## 群组

## 帐号

## REST API

## 第三方回调

### 第三方回调中获取图片、语音、视频