为方便开发者快速接入房间管理服务，这里向您介绍房间管理服务的使用场景以及接入流程。

## 功能简介
通过客户端房间管理接口，可以简单实现对房间内成员的管理、以及对房间内成员上下麦的管理。


## 使用场景

例如在狼人杀场景中，作为主持人可以通过 EnableMic 控制其他玩家打开麦克风发言；当某位玩家已经“死亡”，不需要听房间内声音或者操作麦克风说话，则通过 ForbidUserOperation 接口禁止该玩家操作设备。


## 前提条件
- **已开通实时语音服务**：可参见 [语音服务开通指引](https://cloud.tencent.com/document/product/607/10782)。
- **已接入GME SDK**：包括核心接口和实时语音接口的接入，详情可参见 [Native SDK 快速接入](https://cloud.tencent.com/document/product/607/56374)、[Unity SDK 快速接入](https://cloud.tencent.com/document/product/607/18248)、[Unreal SDK 快速接入](https://cloud.tencent.com/document/product/607/18267)。


<dx-alert infotype="explain" title="">
此功能不支持 H5 SDK。
</dx-alert>



## 接入流程
### 类名：ITMGRoomManager

GME 房间管理功能在进房后才可调用，且只能修改房间内成员的状态。
所有接口的结果会通过 `ITMG_MAIN_EVNET_TYPE_ROOM_MANAGEMENT_OPERATOR` 回调，回调详情请参考 [回调处理](#test1)。

### 接口列表


| 类型 | 接口 | 
|---------|---------|
| 控制采集 |EnableMic、 EnableAudioCaptureDevice、EnableAudioSend | 
| 控制播放 |EnableSpeaker、 EnableAudioPlayDevice、EnableAudioRecv | 
| 设备状态获取 |GetMicState、 GetSpeakerState | 
| 敏感接口 |ForbidUserOperation | 

## 采集管理相关接口

采集管理接口包含**麦克风管理**、**音频上行管理**以及**采集硬件设备管理**。其中麦克风管理相当于音频上行管理加上采集硬件设备管理，区分出音频数据传输上下行与硬件设备的管理，是因为打开或者关闭采集设备，将会伴随整个设备（采集和播放）重启，如果此时 App 正在播放背景音乐，那么背景音乐的播放也会被中断。利用控制上下行的方式来实现开关麦克风效果，将不会中断播放设备。

### 麦克风管理

调用此接口打开或关闭房间内某用户的麦克风，调用成功后，该用户的麦克风将被关闭或打开。
EnableMic 相当于同时调用 EnableAudioSend 及 EnableAudioCaptureDevice。

#### 函数原型

<dx-codeblock>
::: Android java
public abstract int EnableMic(boolean isEnabled,String receiverID);
:::
::: iOS c++
-(QAVResult)EnableMic:(BOOL)enable Receiver:(NSString *)receiverID;
:::
</dx-codeblock>


| 参数       | 类型      | 含义                                                    |
| ---------- | --------- | ------------------------------------------------------- |
| enable     | BOOL      | YES：打开某用户麦克风，NO：关闭某用户麦克风 |
| receiverID | NSString* | 填入目标用户 OpenId                                     |


#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_MIC_OP。

### 音频上行管理

调用此接口打开或关闭房间内某用户的音频上行。调用成功后，该用户的音频上行将被关闭或打开，但不影响麦克风采集。

#### 函数原型


<dx-codeblock>
::: Android java
public abstract int EnableAudioSend(boolean isEnabled,String receiverID);
:::
::: iOS c++
-(QAVResult)EnableAudioSend:(BOOL)enable Receiver:(NSString *)receiverID;
:::
</dx-codeblock>


| 参数       | 类型      | 含义                                                |
| ---------- | --------- | --------------------------------------------------- |
| enable     | BOOL      |YES：打开某用户上行，NO：关闭某用户上行 |
| receiverID | NSString* | 填入目标用户 OpenId                                 |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_AUDIO_SEND_OP。

### 音频采集硬件设备管理

调用此接口打开或关闭房间内某用户的音频采集硬件设备。调用成功后，该用户的音频采集硬件设备将被关闭或打开，但不影响上行。

#### 函数原型

<dx-codeblock>
::: Android java
public abstract int EnableAudioCaptureDevice(boolean isEnabled,String receiverID);
:::
::: iOS c++
-(QAVResult)EnableAudioCaptureDevice:(BOOL)enabled Receiver:(NSString *)receiverID;
:::
</dx-codeblock>

| 参数       | 类型      | 含义                                                         |
| ---------- | --------- | ------------------------------------------------------------ |
| enable     | BOOL      |YES：打开某用户音频采集硬件设备，NO：关闭某用户音频采集硬件设备 |
| receiverID | NSString* | 填入目标用户 OpenId                                          |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_CAPTURE_OP。

## 播放管理相关接口

播放管理接口包含**扬声器管理**、**音频下行管理**以及**播放硬件设备管理**。其中扬声器管理相当于音频下行管理加上播放硬件设备管理。区分出音频数据传输上下行与硬件设备的管理，是因为打开或者关闭采集设备，将会伴随整个设备（采集及播放）重启，如果此时 App 正在播放背景音乐，那么背景音乐的播放也会被中断。利用控制上下行的方式来实现开关麦克风效果，不会中断播放设备。

### 扬声器管理

调用此接口打开或关闭房间内某用户的扬声器。调用成功后，该用户的扬声器将被关闭或打开，听到房间内的音频声音。
EnableSpeaker 相当于同时调用 EnableAudioRecv 及 EnableAudioPlayDevice。

#### 函数原型

<dx-codeblock>
::: Android java
public abstract int EnableSpeaker(boolean isEnabled,String receiverID);
:::
::: iOS c++
-(QAVResult)EnableSpeaker:(BOOL)enable Receiver:(NSString *)receiverID;
:::
</dx-codeblock>


| 参数       | 类型      | 含义                                                    |
| ---------- | --------- | ------------------------------------------------------- |
| enable     | BOOL      | YES ：打开某用户扬声器，NO：关闭某用户扬声器 |
| receiverID | NSString* | 填入目标用户 OpenId                                     |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_SPEAKER_OP。

### 音频下行管理

调用此接口打开或关闭房间内某用户的音频下行。调用成功后，该用户的音频下行将被关闭或打开，但不影响播放设备。

#### 函数原型

<dx-codeblock>
::: Android java
public abstract int EnableAudioRecv(boolean isEnabled,String receiverID);
:::
::: iOS c++
-(QAVResult)EnableAudioRecv:(BOOL)enabled Receiver:(NSString *)receiverID;
:::
</dx-codeblock>


| 参数       | 类型      | 含义                                                        |
| ---------- | --------- | ----------------------------------------------------------- |
| enable     | BOOL      | YES ：打开某用户音频下行，NO：关闭某用户音频下行 |
| receiverID | NSString* | 填入目标用户 OpenId                                         |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_AUDIO_REC_OP。


### 音频播放硬件设备管理

调用此接口打开或关闭房间内某用户的音频播放硬件设备。调用成功后，该用户的音频播放硬件设备将被关闭或打开，但不影响下行。

#### 函数原型

<dx-codeblock>
::: Android java
public abstract int EnableAudioPlayDevice(boolean isEnabled,String receiverID);
:::
::: iOS c++
-(QAVResult)EnableAudioPlayDevice:(BOOL)enabled Receiver:(NSString *)receiverID;
:::
</dx-codeblock>


| 参数       | 类型      | 含义                                                         |
| ---------- | --------- | ------------------------------------------------------------ |
| enable     | BOOL      |YES ：打开某用户音频播放硬件设备，NO：关闭某用户音频播放硬件设备 |
| receiverID | NSString* | 填入目标用户 OpenId                                          |

#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_PLAY_OP。

## 获取成员状态接口

### 获取某人麦克风状态

调用此接口，获取房间内某成员的麦克风状态。

#### 函数原型

<dx-codeblock>
::: Android java
public abstract int GetMicState(String receiverID);
:::
::: iOS c++
-(QAVResult)GetMicState:(NSString *)receiverID;
:::
</dx-codeblock>


| 参数       | 类型      | 含义                |
| ---------- | --------- | ------------------- |
| receiverID | NSString* | 填入目标用户 OpenId |


#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_GET_MIC_STATE。

### 获取某人扬声器状态

调用此接口，获取房间内某成员的扬声器状态。

#### 函数原型

<dx-codeblock>
::: Android java
public abstract int GetSpeakerState(String receiverID);
:::
::: iOS c++
-(QAVResult)GetSpeakerState:(NSString *)receiverID;
:::
</dx-codeblock>


#### 回调

回调参数为 ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE。


### 禁止某位成员操作麦克风及扬声器

成员进房默认为允许操作麦克风及扬声器，调用此接口可以禁止房间内的某位成员操作麦克风及扬声器，在该成员退出房间后此功能失效。

<dx-codeblock>
::: Android java
public  abstract int ForbidUserOperation(boolean isEnabled,String receiverID);
:::
::: iOS c++
-(QAVResult)ForbidUserOperation:(BOOL)enable Receiver:(NSString *)receiverID;
:::
</dx-codeblock>

| 参数       | 类型      | 含义                                                        |
| ---------- | --------- | ----------------------------------------------------------- |
| enable     | BOOL      | YES：允许某用户操作设备，NO：禁止某用户操作设备 |
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
| 7    | ITMG_ROOM_MANAGEMENT_GET_MIC_STATE     | 获取麦克风状态             |
| 8    | ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE | 获取扬声器状态             |
| 9    | ITMG_ROOM_MANAGERMENT_FOBIN_OP         | 禁止操作麦克风及扬声器事件 |

#### OperateValue

| 成员      | 含义                     |
| --------- | ------------------------ |
| boolValue |  0：关闭命令，1：打开命令 |


#### 示例代码


<dx-codeblock>
::: Android java
 public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
 if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_ROOM_MANAGEMENT_OPERATOR== type) {

            ArrayList<String> operatorArr = new ArrayList<String>();
            operatorArr.add("采集");
            operatorArr.add("播放");
            operatorArr.add("上行");
            operatorArr.add("下行");
            operatorArr.add("采集上行");
            operatorArr.add("播放下行");
            operatorArr.add("mic状态");
            operatorArr.add("spk状态");
            operatorArr.add("禁止操作mic/speak");

            String SenderID =  data.getStringExtra("SenderID");
            String ReceiverID = data.getStringExtra("ReceiverID");
            int OperateType = data.getIntExtra("OperateType",-1000);

            int Result =data.getIntExtra("Result",-1000);
            boolean OperateValue = data.getBooleanExtra("OperateValue",false);
            if (OperateType == -1000 ||Result == -1000) {
                return;
            }
            if (SenderID.equals(identifier)) {
                if (OperateType == ITMGContext.ITMG_ROOM_MANAGEMENT_GET_MIC_STATE || OperateType == ITMGContext.ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE) {
                    Toast.makeText(getActivity(), String.format("发送给id:%s 的%s操作,结果:%s", ReceiverID, operatorArr.get(OperateType), OperateValue ? "开" : "关"), Toast.LENGTH_LONG).show();
                } else  {
                    Toast.makeText(getActivity(), String.format("发送给id:%s 的%s%s操作,结果:%d", ReceiverID, operatorArr.get(OperateType), OperateValue ? "开" : "关", Result), Toast.LENGTH_LONG).show();
                }

            } else if (ReceiverID.equals(identifier)||ReceiverID.equals("ALL")) {
                if (Result == 0) {
                    switch (OperateType) {
                        case ITMGContext.ITMG_ROOM_MANAGEMENT_CAPTURE_OP:
                        {
                            if (!OperateValue) {
                                mSwitchCapture.setChecked(OperateValue);
                            } else  {
                                AlertDialog.Builder dialog = new AlertDialog.Builder (getActivity());  //创建对象
                                dialog.setTitle("是否要打开设备采集");
                                dialog.setMessage("");
                                dialog.setCancelable(false);
                                dialog.setPositiveButton("开", new DialogInterface.OnClickListener() {
                                    //设置确定按钮的点击事件
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        mSwitchCapture.setChecked(true);
                                        ITMGContext.GetInstance(getActivity()).GetAudioCtrl().EnableAudioCaptureDevice(true);
                                    }
                                });
                                dialog.setNegativeButton("关", new DialogInterface.OnClickListener() {
                                    //设置取消按钮的点击事件
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                    }
                                });
                                dialog.show();
                            }

                        }
                            break;
                        case ITMGContext.ITMG_ROOM_MANAGEMENT_PLAY_OP:
                        {
                            mSwitchPlayDevice.setChecked(OperateValue);
                        }
                            break;
                        case ITMGContext.ITMG_ROOM_MANAGEMENT_AUDIO_SEND_OP:
                        {
                            if (!OperateValue) {
                                mSwitchSend.setChecked(OperateValue);
                            } else  {
                                AlertDialog.Builder dialog = new AlertDialog.Builder (getActivity());  //创建对象
                                dialog.setTitle("是否要打开上行");
                                dialog.setMessage("");
                                dialog.setCancelable(false);
                                dialog.setPositiveButton("开", new DialogInterface.OnClickListener() {
                                    //设置确定按钮的点击事件
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        mSwitchSend.setChecked(true);
                                        ITMGContext.GetInstance(getActivity()).GetAudioCtrl().EnableAudioSend(true);
                                    }
                                });
                                dialog.setNegativeButton("关", new DialogInterface.OnClickListener() {
                                    //设置取消按钮的点击事件
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                    }
                                });
                                dialog.show();
                            }
                        }
                            break;
                        case ITMGContext.ITMG_ROOM_MANAGEMENT_AUDIO_REC_OP:
                         {
                             mSwitchRecv.setChecked(OperateValue);
                        }
                            break;
                        case ITMGContext.ITMG_ROOM_MANAGEMENT_MIC_OP:
                         {
                             if (!OperateValue) {
                                 mSwitchCapture.setChecked(OperateValue);
                                 mSwitchSend.setChecked(OperateValue);
                             }  else  {
                                 AlertDialog.Builder dialog = new AlertDialog.Builder (getActivity());  //创建对象
                                 dialog.setTitle("是否要打开采集和上行");
                                 dialog.setMessage("");
                                 dialog.setCancelable(false);
                                 dialog.setPositiveButton("开", new DialogInterface.OnClickListener() {
                                     //设置确定按钮的点击事件
                                     @Override
                                     public void onClick(DialogInterface dialog, int which) {
                                         mSwitchCapture.setChecked(true);
                                         mSwitchSend.setChecked(true);
                                         ITMGContext.GetInstance(getActivity()).GetAudioCtrl().EnableMic(true);
                                     }
                                 });
                                 dialog.setNegativeButton("关", new DialogInterface.OnClickListener() {
                                     //设置取消按钮的点击事件
                                     @Override
                                     public void onClick(DialogInterface dialog, int which) {
                                     }
                                 });
                                 dialog.show();
                             }
                          }
                            break;
                        case ITMGContext.ITMG_ROOM_MANAGEMENT_SPEAKER_OP:
                        {
                            mSwitchPlayDevice.setChecked(OperateValue);
                            mSwitchRecv.setChecked(OperateValue);
                        }
                            break;

                    }
                }
                if (OperateType == ITMGContext.ITMG_ROOM_MANAGEMENT_GET_MIC_STATE || OperateType == ITMGContext.ITMG_ROOM_MANAGEMENT_GET_SPEAKER_STATE)
                {
                    Toast.makeText(getActivity(), String.format("收到来自id:%s 的%s操作,结果:%s",SenderID,operatorArr.get(OperateType),OperateValue?"开":"关"), Toast.LENGTH_LONG).show();
                }
                else if (OperateType == ITMGContext.ITMG_ROOM_MANAGEMENT_SPEAKER_OP || OperateType == ITMGContext.ITMG_ROOM_MANAGEMENT_AUDIO_REC_OP|| OperateType == ITMGContext.ITMG_ROOM_MANAGEMENT_PLAY_OP|| OperateType == ITMGContext.ITMG_ROOM_MANAGERMENT_FOBIN_OP){
                    Toast.makeText(getActivity(), String.format("收到来自id:%s 的%s%s操作,结果:%d",SenderID,operatorArr.get(OperateType),OperateValue?"开":"关",Result), Toast.LENGTH_LONG).show();
                } else if (OperateValue == false) {
                    Toast.makeText(getActivity(), String.format("收到来自id:%s 的%s%s操作,结果:%d",SenderID,operatorArr.get(OperateType),OperateValue?"开":"关",Result), Toast.LENGTH_LONG).show();
                }
            }
 }
:::
::: iOS c++
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
:::
</dx-codeblock>

