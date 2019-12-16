# Release Notes - iOS & macOS

## 2019.11.18

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.7.7734 | 4.5.111 | 2.3.6 |
| **macOS** | 6.7.7734 | 4.5.111 | 2.3.6 |


## 2019.10.30

- 增加接口init:(int)sdkAppId disableModule:(TICDisableModule)disableModule callback:(TICCallback)callback可屏蔽内部TRTC模块

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.7.7734 | 4.5.111 | 2.3.5 |
| **macOS** | 6.7.7734 | 4.5.111 | 2.3.5 |

## 2019.09.25

- 进房参数TICClassroomOption增加compatSaas字段，兼容SaaS方案
- sendGroupTextMessage/sendGroupCustomMessage/sendGroupMessage删除groupId参数

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.6.7460 | 4.5.45 | 2.3.4 |
| **macOS** | 6.6.7460 | 4.5.45 | 2.3.4 |

## 2019.09.11

离线录制上报增加设备ID字段

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.6.7460 | 4.4.900 | 2.3.3 |
| **macOS** | 6.6.7460 | 4.4.900 | 2.3.3 |

## 2019.08.19

新增大房间方案支持
- TICClassroomOption增加classScene和roleType
- createClassroom接口增加参数classScene

| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.6.7460 | 4.4.900 | 2.3.3 |
| **macOS** | 6.6.7460 | 4.4.900 | 2.3.3 |

## 2019.08.07


| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.5.7272 | 4.4.716 | 2.3.2 |
| **macOS** | 6.5.7272 | 4.4.716 | 2.3.2 |

## 2019.08.05


| | TRTC版本 | TIM版本 | TEduBoard版本 |
| :-: | :-: | :-: | :-: |
| **iOS** | 6.5.7272 | 4.4.716 | 2.3.1 |
| **macOS** | 6.5.7272 | 4.4.716 | 2.3.1 |


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
