

本文为您介绍以 iOS 平台 Objective-C 代码进行房间管理示例演示。如果需要使用此功能，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系开发人员提供对应库文件。

## 工程配置

导入 GME SDK 后，参照下图将 ImSDK.framework 设置为 Embed&Sign。
- **XCode10：**
![](https://main.qcloudimg.com/raw/55bded873ffc3f5f7e95043c3e77aee3.png)
- **XCode11：**
![](https://main.qcloudimg.com/raw/dbb4d0fcebc2f71685969af3d9950bf1.png)

## ITMGRoomManager

GME 房间管理功能在进房后才可调用，且只能修改房间内成员的状态。
所有接口的结果会通过 `ITMG_MAIN_EVNET_TYPE_ROOM_MANAGEMENT_OPERATOR` 回调，回调详情请参考 [回调处理](#test1)。

```
@interface ITMGRoomManager :NSObject
```

## 采集管理相关接口

采集管理接口包含**麦克风管理**、**音频上行管理**以及**采集硬件设备管理**。其中麦克风管理相当于音频上行管理加上采集硬件设备管理，区分出音频数据传输上下行与硬件设备的管理，是因为打开或者关闭采集设备，将会伴随整个设备（采集和播放）重启，如果此时 App 正在播放背景音乐，那么背景音乐的播放也会被中断。利用控制上下行的方式来实现开关麦克风效果，将不会中断播放设备。

### 麦克风管理

调用此接口打开或关闭房间内某用户的麦克风，调用成功后，该用户的麦克风将被关闭或打开。
EnableMic 相当于同时调用 EnableAudioSend 及 EnableAudioCaptureDevice。

#### 函数原型
```
-(QAVResult)EnableMic:(BOOL)enable Receiver:(NSString *)receiverID;
```
| 参数       | 类型      | 含义                                                    |
| ---------- | --------- | ------------------------------------------------------- |
| enable     | BOOL      | <li> YES：打开某用户麦克风<li>NO：关闭某用户麦克风 |
| receiverID | NSString* | 填入目标用户 OpenId                                     |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_MIC_OP。

### 音频上行管理

调用此接口打开或关闭房间内某用户的音频上行。调用成功后，该用户的音频上行将被关闭或打开，但不影响麦克风采集。

#### 函数原型

```
-(QAVResult)EnableAudioSend:(BOOL)enable Receiver:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                                                |
| ---------- | --------- | --------------------------------------------------- |
| enable     | BOOL      | <li> YES：打开某用户上行<li>NO：关闭某用户上行 |
| receiverID | NSString* | 填入目标用户 OpenId                                 |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_AUDIO_SEND_OP。

### 音频采集硬件设备管理

调用此接口打开或关闭房间内某用户的音频采集硬件设备。调用成功后，该用户的音频采集硬件设备将被关闭或打开，但不影响上行。

#### 函数原型

```
-(QAVResult)EnableAudioCaptureDevice:(BOOL)enabled Receiver:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                                                         |
| ---------- | --------- | ------------------------------------------------------------ |
| enable     | BOOL      | <li>YES：打开某用户音频采集硬件设备<li>NO：关闭某用户音频采集硬件设备 |
| receiverID | NSString* | 填入目标用户 OpenId                                          |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_CAPTURE_OP。

## 播放管理相关接口

播放管理接口包含**扬声器管理**、**音频下行管理**以及**播放硬件设备管理**。其中扬声器管理相当于音频下行管理加上播放硬件设备管理。区分出音频数据传输上下行与硬件设备的管理，是因为打开或者关闭采集设备，将会伴随整个设备（采集及播放）重启，如果此时 App 正在播放背景音乐，那么背景音乐的播放也会被中断。利用控制上下行的方式来实现开关麦克风效果，不会中断播放设备。

### 扬声器管理

调用此接口打开或关闭房间内某用户的扬声器。调用成功后，该用户的扬声器将被关闭或打开，听到房间内的音频声音。
EnableSpeaker 相当于同时调用 EnableAudioRecv 及 EnableAudioPlayDevice。

#### 函数原型

```
-(QAVResult)EnableSpeaker:(BOOL)enable Receiver:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                                                    |
| ---------- | --------- | ------------------------------------------------------- |
| enable     | BOOL      | <li>YES ：打开某用户扬声器<li>NO：关闭某用户扬声器 |
| receiverID | NSString* | 填入目标用户 OpenId                                     |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_SPEAKER_OP。

### 音频下行管理

调用此接口打开或关闭房间内某用户的音频下行。调用成功后，该用户的音频下行将被关闭或打开，但不影响播放设备。

#### 函数原型

```
-(QAVResult)EnableAudioRecv:(BOOL)enabled Receiver:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                                                        |
| ---------- | --------- | ----------------------------------------------------------- |
| enable     | BOOL      | <li>YES ：打开某用户音频下行<li>NO：即关闭某用户音频下行 |
| receiverID | NSString* | 填入目标用户 OpenId                                         |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_AUDIO_REC_OP。


### 音频播放硬件设备管理

调用此接口打开或关闭房间内某用户的音频播放硬件设备。调用成功后，该用户的音频播放硬件设备将被关闭或打开，但不影响下行。

#### 函数原型

```
-(QAVResult)EnableAudioPlayDevice:(BOOL)enabled Receiver:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                                                         |
| ---------- | --------- | ------------------------------------------------------------ |
| enable     | BOOL      | <li>YES ：打开某用户音频播放硬件设备<li>NO：关闭某用户音频播放硬件设备 |
| receiverID | NSString* | 填入目标用户 OpenId                                          |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_PLAY_OP。

## 获取成员状态接口

### 获取某人麦克风状态

调用此接口，获取房间内某成员的麦克风状态。

#### 函数原型

```
-(QAVResult)GetMicState:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                |
| ---------- | --------- | ------------------- |
| receiverID | NSString* | 填入目标用户 OpenId |


#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_GET_MIC_STATE。

### 获取某人扬声器状态

调用此接口，获取房间内某成员的扬声器状态。

#### 函数原型

```
-(QAVResult)GetSpeakerState:(NSString *)receiverID;
```

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE。


## 其他接口

### 客户端移出房间接口

调用此接口可以将房间内的某位成员移出房间。

```
-(QAVResult)KickOut:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                |
| ---------- | --------- | ------------------- |
| receiverID | NSString* | 填入目标用户 OpenId |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_KICKOUT_OP。

### 禁止某位成员操作麦克风及扬声器

成员进房默认为允许操作麦克风及扬声器，调用此接口可以禁止房间内的某位成员操作麦克风及扬声器，在该成员退出房间后此功能失效。

```
-(QAVResult)ForbidUserOperation:(BOOL)enable Receiver:(NSString *)receiverID;
```

| 参数       | 类型      | 含义                                                        |
| ---------- | --------- | ----------------------------------------------------------- |
| enable     | BOOL      | <li>YES：允许某用户操作设备<li>NO：禁止某用户操作设备 |
| receiverID | NSString* | 填入目标用户 OpenId                                         |

#### 回调

回调参数为 ITMG_ROOM_MANAGERMENT_FOBIN_OP。

<span id="test1"></span>
## 回调处理

与 GME 其他回调相同，房间管理的回调也在 OnEvent 中处理，事件名称为 `ITMG_MAIN_EVNET_TYPE_ROOM_MANAGEMENT_OPERATOR`，事件会返回一个结构体，具体包含的内容如下。

#### 回调参数

| 参数         | 类型     | 含义                                                     |
| ------------ | -------- | -------------------------------------------------------- |
| SenderID     | NSString | 事件发送者 ID，如果与自己 OpenId 相同，即为本端发送的命令 |
| ReceiverID   | NSString | 事件接收者 ID，如果与自己 OpenId 相同，即为本端接收的命令 |
| OperateType  | NSNumber | 事件类型                                                 |
| Result       | NSNumber | 事件结果，0为成功                                        |
| OperateValue | NSNumber | 命令详情                                                 |

#### OperateType

| 数值 | 事件类型                               | 含义                       |
| ---- | -------------------------------------- | -------------------------- |
| 0    | ITMG_ROOM_MANAGEMENT_CAPTURE_OP        | 控制采集设备硬件回调       |
| 1    | ITMG_ROOM_MANAGEMENT_PLAY_OP           | 控制播放设备硬件回调       |
| 2    | ITMG_ROOM_MANAGEMENT_AUDIO_SEND_OP     | 控制上行回调               |
| 3    | ITMG_ROOM_MANAGEMENT_AUDIO_REC_OP      | 控制下行回调               |
| 4    | ITMG_ROOM_MANAGEMENT_MIC_OP            | 控制麦克风回调             |
| 5    | ITMG_ROOM_MANAGEMENT_PLAY_OP           | 控制扬声器回调             |
| 6    | ITMG_ROOM_MANAGEMENT_KICKOUT_OP        | 将成员移出房间事件                   |
| 7    | ITMG_ROOM_MANAGEMENT_GET_MIC_STATE     | 获取麦克风状态             |
| 8    | ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE | 获取扬声器状态             |
| 9    | ITMG_ROOM_MANAGERMENT_FOBIN_OP         | 禁止操作麦克风及扬声器事件 |

#### OperateValue

| 成员      | 含义                     |
| --------- | ------------------------ |
| boolValue | <li>0：关闭命令<li>1：打开命令 |


#### 示例代码

```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSString* log =[NSString stringWithFormat:@"OnEvent:%d,data:%@", (int)eventType, data];
    [self showLog:log];
    NSLog(@"====%@====",log);
    switch (eventType) {
		case ITMG_MAIN_EVNET_TYPE_ROOM_MANAGEMENT_OPERATOR:
        {
            NSArray *operatorArr = @[@"采集",@"播放",@"上行",@"下行",@"采集上行",@"播放下行",@"踢人",@"mic状态",@"spk状态",@"禁止操作mic/speak"];
			// _openId
            NSString *SenderID = [data objectForKey:@"SenderID"];
            NSString *ReceiverID = [data objectForKey:@"ReceiverID"];
            NSNumber *OperateType = [data objectForKey:@"OperateType"];
            NSNumber *Result = [data objectForKey:@"Result"];
            NSNumber *OperateValue = [data objectForKey:@"OperateValue"];
            
            //自己发出去的命令
            if ([SenderID isEqualToString:_openId]) {
                if (OperateType.intValue == ITMG_ROOM_MANAGEMENT_GET_MIC_STATE || OperateType.intValue == ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE) {
                          NSString *alterString = [NSString stringWithFormat:@"发送给id:%@ 的%@操作,结果:%@",ReceiverID,operatorArr[OperateType.intValue],OperateValue.boolValue?@"开":@"关"];
                                             UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"房间管理操作" message:alterString delegate:NULL cancelButtonTitle:@"OK" otherButtonTitles:nil];
                                             [alert show];
                }
                else
                {
                    NSString *alterString = [NSString stringWithFormat:@"发送给id:%@ 的%@%@操作,结果:%@",ReceiverID,OperateValue.boolValue?@"开":@"关",operatorArr[OperateType.intValue],Result];
                               UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"房间管理操作" message:alterString delegate:NULL cancelButtonTitle:@"OK" otherButtonTitles:nil];
                               [alert show];
                }
           
                
            } 
			else if([ReceiverID isEqualToString:_openId] ){ //别人发过来的命令
            	if (Result.intValue == 0) {
                	switch (OperateType.intValue) {
                        case ITMG_ROOM_MANAGEMENT_CAPTURE_OP:{
                            [_micSwitch setOn:OperateValue.boolValue animated:true];
                        }
                            break;
                        case ITMG_ROOM_MANAGEMENT_PLAY_OP:{
                            [_speakerSwitch setOn:OperateValue.boolValue animated:true];
                            }
                            break;
                        case ITMG_ROOM_MANAGEMENT_AUDIO_SEND_OP:{
                            [_sendSwitch setOn:OperateValue.boolValue animated:true];
                        }
                            break;
                        case ITMG_ROOM_MANAGEMENT_AUDIO_REC_OP:{
                            [_recvSwitch setOn:OperateValue.boolValue animated:true];
                        }
                            break;
                        case ITMG_ROOM_MANAGEMENT_MIC_OP:{
                        [_micSwitch setOn:OperateValue.boolValue animated:true];
                        [_sendSwitch setOn:OperateValue.boolValue animated:true];
                        }
                            break;
                        case ITMG_ROOM_MANAGEMENT_SPEAKER_OP:{
                        [_speakerSwitch setOn:OperateValue.boolValue animated:true];
                        [_recvSwitch setOn:OperateValue.boolValue animated:true];
                            
                        }
                            break;
                        default:
                            break;
                    }
                
                if (OperateType.intValue == ITMG_ROOM_MANAGEMENT_GET_MIC_STATE || OperateType.intValue == ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE) {
                        NSString *alterString = [NSString stringWithFormat:@"收到id:%@ 发送来的%@操作,结果:%@",SenderID,operatorArr[OperateType.intValue],OperateValue.boolValue?@"开":@"关"];
                                UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"房间管理操作" message:alterString delegate:NULL cancelButtonTitle:@"OK" otherButtonTitles:nil];
                                [alert show];
                    }
                else{
                    	NSString *alterString = [NSString stringWithFormat:@"收到id:%@ 发送来的%@%@操作,结果:%@",SenderID,OperateValue.boolValue?@"开":@"关",operatorArr[OperateType.intValue],Result];
                              UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"房间管理操作" message:alterString delegate:NULL cancelButtonTitle:@"OK" otherButtonTitles:nil];
                              [alert show];
                	}
            	}
			}
    	}
        break;
}
```
