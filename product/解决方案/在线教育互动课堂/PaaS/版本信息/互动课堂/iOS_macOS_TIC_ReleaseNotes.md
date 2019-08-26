# Release Notes - iOS & macOS

## 2019.07.18

新增功能
- iOS/macOS增加事件上报

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.5.7272 | 4.4.627 | 2.3.0 |
| **macOS** | 6.5.7272 | 4.4.627 | 2.3.0 |

## 2019.06.25

macOS
- macOS Demo重构

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.5.7272 | 4.4.479 | 2.2.1 |
| **macOS** | 4.0.0 | 4.4.479 | 2.2.1 |



## 2019.06.21

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.5.7272 | 4.4.479 | 2.2.1 |
| **macOS** | 4.0.0 | 4.3.145 | 2.2.1 |

## 2019.06.20
修复bug
- 修复多次发送课后录制对时信息的问题
增加接口
- 增加课后录制对时信息接口`sendOfflineRecordInfo`
- 进房参数`TICClassroomOption`增加白板初始化参数`boardInitParam`和白板回调`boardDelegate`

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.5.7272 | 4.4.479 | 2.2.0 |
| **macOS** | 4.0.0 | 4.3.145 | 2.2.0 |

## 2019.06.05

修复bug
- 修复被踢下线再次登陆没有回调问题
- 修复iOS退后台录制对时信息发送多次问题
- 替换iOS/macOS IMSDK版本为4.3.145

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 1.0.235 | 4.3.145 | 2.1.0 |
| **macOS** | 4.0.0 | 4.3.145 | 2.1.0 |

## 2019.05.29

修复bug
- onNewMessage过滤录制信息

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 1.0.235 | 4.2.52 | 2.1.0 |
| **macOS** | 4.0.0 | 4.3.112 | 2.1.0 |

## 2019.05.22

新增功能
- 增加`onTICUserAudioAvailable`回调
- 增加`onTICSendOfflineRecordInfo`回调
- 增加离线录制功能
- 增加`sendGroupMessage`方法
- TRTC退房时，TIC全量回调视频、音频以及辅流状态

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 1.0.235 | 4.2.52 | 2.0.0.4 |
| **macOS** | 4.0.0 | 4.3.112 | 2.0.0.4 |

## 2019.05.17

- iOS替换TRTC版本1.0.235
- iOS删除onUserExit回调代码
