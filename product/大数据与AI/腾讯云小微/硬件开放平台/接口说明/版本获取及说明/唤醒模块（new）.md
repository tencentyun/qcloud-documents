# 唤醒模块
## 介绍
唤醒模块是用于检测用户说的话中包含指定唤醒词的一个功能模块。唤醒模块需要持续录制声音确保设备能够及时检测到唤醒词，当用户说到唤醒词后，设备就从休眠状态被唤醒。
唤醒模块 SDK 现在支持的唤醒词有 “你好小微” 和 “小微你好”。唤醒效果受到多方面因素的影响，比如设备端麦克风阵列、降噪、回声消除效果等。目前通用的唤醒模块还无法保证极高的唤醒成功率。

唤醒模块现在使用的方式为本地检测+云端校验方式，唤醒成功后，可以断开说话或者连续说话，例如 “你好小微，今天天气怎么样？”、“你好小微今天天气怎么样？”，唤醒后，小微会等待 5 秒时间，5 秒检测不到声音就取消这次唤醒。

## 下载

目前处于内测阶段，Android 平台可以 [下载试用版](/wiki/#Hardware/hardware_download_SDK.md) 进行体验。Linux 下载请在审核通过后，[联系我们](/wiki/#Hardware/hardware_Contact_US.md)。

## 接入

唤醒模块目前由本地唤醒+云端校验组成，所以首先声音会经过本地唤醒模块的检测，本地初步唤醒后，会将这部分声音和之后一段时间的声音传到云端，由云端返回唤醒结果。

流程如下：
![](https://main.qcloudimg.com/raw/ba1b6b69d5d22b6eb5bdb92393e08345.png)
1. 本地检测唤醒（本地检测到唤醒词的一半长度即可开始云端校验）；
2. 发起云端校验类型的语音识别请求；
3. 将唤醒词的语音传到云端进行识别；
4. 云端返回校验的结果：1(唤醒失败)、2(唤醒成功并且没有连续说话)、3(指令唤醒词唤醒，例如“暂停”等。这类结果只有车机支持)、4(唤醒成功的中间结果，可能接下来还会连续说话)；
5. 客户端收到结果后，进行相应的反应。


### Android

在 AndroidDemo 中，`wakeup`为已经封装好的纯本地唤醒模块(静音检测+唤醒词检测)，本地唤醒的内部逻辑可参考`WakeupManager.java`，云端校验逻辑在`RecordDataManager.java`中。

本地唤醒后，需要将本地唤醒部分的音频数据+之后的音频数据都送到云端。所以本地唤醒模块需要记录让其检测到初步唤醒的语音数据。待会儿唤醒成功后需要拼到最前面进行校验。大致流程如下：

```
XWSDK.getInstance().request(XWCommonDef.RequestType.WAKEUP_CHECK, wakeupBuffer, wakeupContextInfo);

while(needCloudCheckWakeup){
	XWSDK.getInstance().request(XWCommonDef.RequestType.WAKEUP_CHECK, recordBuffer, wakeupContextInfo);
}
```

`request`接口会返回结果：

```
XWSDK.getInstance().setAudioRequestListener(new XWSDK.AudioRequestListener() {
    @Override
    public boolean onRequest(String voiceId, int event, XWResponseInfo rspData, byte[] extendData) {
        switch (event) {
            case XWCommonDef.XWEvent.ON_RESPONSE:
                if (rspData.wakeupFlag != WAKEUP_CHECK_RET_NOT) {
                    // 唤醒类响应
                    if (rspData.wakeupFlag == WAKEUP_CHECK_RET_FAIL) {
                        // 云端校验失败
                    } else if (rspData.wakeupFlag == WAKEUP_CHECK_RET_SUC) {
                        onWakeup();
                        // 唤醒成功，重新开启一次普通语音识别请求，并带上前300ms的数据(因为云端回来的结果经过网络有延迟，
                        // 往前面拼一点数据避免中间的语音数据丢失了)
                    } else if (rspData.wakeupFlag == WAKEUP_CHECK_RET_SUC_RSP) {
                        // 唤醒成功，收到最终结果了
                        dealRsp(voiceId, rspData, extendData);
                    } else if (rspData.wakeupFlag == WAKEUP_CHECK_RET_SUC_CONTINUE) {
                        // 如果需要 则开启动画
							...
                        // 唤醒成功。继续传语音
                        if (rspData.resources.length > 0) {
                            // 收到最终结果了
                            dealRsp(voiceId, rspData, extendData);
                        }
                    }
                }
                break;
        }
        return true;
    }
});
```

### Linux

唤醒模块目前包括静音检测和唤醒词识别，两者必须配合使用。
在接入过程中， 先使用静音检测判断未非静音数据后，传入唤醒词识别模块后检测唤醒词。

#### 静音检测

```
enum EVAD_RES
{
    EVAD_OK      = 0 ,
    EVAD_ERROR   = 1 ,

    EVAD_SPEAK   = 2 ,
    EVAD_SILENCE = 3 ,
    EVAD_UNKNOW  = 4
};

typedef void*  EVAD_HANDLE;


/*
  input param:  sample_rate  : audio sample rate : 16000 or 8000
  input param:  sil_time     : after detect a speak start ,if we detect silence longer then this time,then,we see find a speak end (unit is ms)\
                               this param set to 300 for general condition
  input param:  s_n_ration   : noise / signal,if in high noise condition set high value,default is 2.5f

  input param:  begin_confirm_window: 
  input param:  begin_confirm: the up two params used in confirm speech begin window,and confirm time length,
                               if the two param set bigger will skip some short sound ,such as cough
*/
EVAD_RES  EVAD_GetHandle(EVAD_HANDLE* ,int sample_rate,int sil_time,float s_n_ration = 2.5 ,int begin_confirm_window = 600,int begin_confirm = 450);

/*
  input param: hold_history : weather reserve prepare statics data, set true for general condition
*/
EVAD_RES  EVAD_Reset(EVAD_HANDLE handle,int hold_history =  1);


/*
   output param begin_delay_time : we find a speak begin time has some time(ms) delay, so if we find first speak frame,
                                   real speak time is early time for this time,so we must sub this delay time,that is real
                                   speak begin time.
*/
EVAD_RES  EVAD_GetBeginDelayTime(EVAD_HANDLE handle,int* begin_delay_time);

EVAD_RES  EVAD_AddData(EVAD_HANDLE handle, const char* iwdata, size_t isize);

EVAD_RES  EVAD_Release(EVAD_HANDLE* handle);

```

- **EVAD\_GetHandle** 获取句柄，设置 vad 参数，全局调用一次。参考参数：
```
EVAD_GetHandle(&m_vadInst, 16000, 500, 2.5, 300, 225)
```

- **EVAD\_Reset** 清空数据，重新一轮

- **EVAD\_GetBeginDelayTime** 由于 vad 判断开始说话会有滞后，必须从这个函数获取滞后的时间，从而把时间点进行前置

- **EVAD_AddData** 追加录音数据, 根据 返回值 判断是否已开始说话 (EVAD_SPEAK)

- **EVAD_Release** 释放句柄，全局调用一次


#### 唤醒词识别

**VoiceRecognizeEmbedInit**

初始化， 全局调用一次

```
/**
 * @brief: new the handle, read the resource and ready to recognize
 * must appear in pairs with 'VoiceRecognizeEmbedRelease'
 *
 * pResPath: the path of the resource
 * pResName: the name of the resource
 * pNameList: you needn't it if you just need wake up recognize.
 *            the person names list, separate the names by '\n'.
 *            name list is loaded from file when 'pNameList = 0', and
 *            the gram with '$name' will be ignored if the file isn't exist.
 */
VRAPI_API int VoiceRecognizeEmbedInit(VoiceRecognizeEmbedHandle *pHandle,
        const char *pResPath,
        const char *pResName,
        const char *pNameList = 0);

```


**VoiceRecognizeEmbedBegin**

开始一次语音识别

```
/**
 * @brief: ready a new recognize
 * must appear in pairs with 'VoiceRecognizeEmbedEnd'
 */
VRAPI_API int VoiceRecognizeEmbedBegin(VoiceRecognizeEmbedHandle handle);

```
**VoiceRecognizeEmbedAddData**

填充声音数据进行唤醒词检测，当返回值为1，表示已检测到完整唤醒词（“小微你好”，“你好小微”），当返回值为2，表示已检测到一半的唤醒词（“你好”，“小微”）。在云端校验模式中，在返回1或者2的时候，就可以开始云端校验，并且`VoiceRecognizeEmbedEnd`这次唤醒。

```
/**
 * @brief: add the new voice wave to recognize
 * pWavBuf: the voice wave buffer
 * nWavLength: the voice wave length
 */
/*return 0 means recognizing continue*/
/*return 1 means recognizing finished, you can get result right now before 'VoiceRecognizeEmbedEnd'*/
/*other return value means error*/
VRAPI_API int VoiceRecognizeEmbedAddData(VoiceRecognizeEmbedHandle handle, const char *pWavBuf, int nWavLength);
```

**VoiceRecognizeEmbedEnd**

结束一次语音识别，一般在收到结果或者静音以后调用。

```
/**
 * @brief: tell the recognizer the wav is end
 * must appear in pairs with 'VoiceRecognizeEmbedBegin'
 */
VRAPI_API int VoiceRecognizeEmbedEnd(VoiceRecognizeEmbedHandle handle);
```

**VoiceRecognizeEmbedGetResult**

获取结果
VoiceRecognizeResult.type == 0 即为唤醒(一般情况下不需要这样判断，部分平台拿到的 text 是乱码，可以这样判断。)

```
/**
 * @brief: get the result
 * if VoiceRecognizeEmbedAddData return 1 already, you can use this function directly
 * else you only can use it after VoiceRecognizeEmbedEnd.
 */
VRAPI_API int VoiceRecognizeEmbedGetResult(VoiceRecognizeEmbedHandle handle,
        VoiceRecognizeResult &result);

```

**VoiceRecognizeEmbedRelease**
释放句柄

```
/** 
 * @brief: release the handle
 * must appear in pairs with 'VoiceRecognizeEmbedInit'
 */
VRAPI_API void VoiceRecognizeEmbedRelease(VoiceRecognizeEmbedHandle *pHandle);
```


##### 云端校验
为了降低误唤醒，我们增加了一个云端校验的方式。在检测到半词唤醒后，可以将之前唤醒的声音，再加上之后的声音传到服务器，由服务器来判断这次是不是应该成功唤醒。

```
int ret = VoiceRecognizeEmbedAddData();
if(ret == 1 || ret == 2) {
	char voice_id[64] = {0};
	txca_request(voice_id, txca_chat_via_wakeup_check, data, length, &context);
	...
}
```
之后的流程和正常请求一样，只是请求类型为`txca_chat_via_wakeup_check`。`request`接口会返回结果：

```
typedef enum _txca_wakeup_flag {
    txca_wakeup_flag_no = 0, // 不是云端校验唤醒的结果
    txca_wakeup_flag_fail = 1, // 唤醒校验失败
    txca_wakeup_flag_suc = 2, // 成功唤醒，只说了唤醒词没有连续说话
    txca_wakeup_flag_suc_rsp = 3,// 成功唤醒并且收到了最终响应，一般是说了指令唤醒词（非车机类不支持，无需关注）
    txca_wakeup_flag_suc_continue = 4,// 成功唤醒并且还需要继续传声音，还不知道会不会连续说话
} TXCA_WAKEUP_FLAG;

bool xwei_voice_request_callback(const char* voice_id, TXCA_EVENT event, const char* state_info, const char* extend_info, unsigned int extend_info_len)
{
    if(event != txca_event_on_tts) {
        switch (event) {
	        case txca_event_on_response:
            {
		         TXCA_PARAM_RESPONSE *response   = reinterpret_cast<TXCA_PARAM_RESPONSE *>((char*)state_info);
                if(pRsp->wakeup_flag > 0) {
                		// 根据wakeup_flag的值，进行处理。
                		// 1 唤醒失败，直接忽略；2 唤醒成功，开启新的语音识别请求；3 唤醒成功并且得到了响应，交给txc_process_response；4 唤醒成功了，但还不知道待会儿变成2还是得到响应，可以先亮灯。如果响应中有资源，说明得到了响应，交给txc_process_response。
                		if(pRsp->wakeup_flag == txca_wakeup_flag_suc) {
                		
                		} else if(pRsp->wakeup_flag == txca_wakeup_flag_suc_continue) {
                			// 如果需要，则亮灯
                			
                			if(pRsp->resource_groups_size > 0) {
                				txc_process_response(voice_id, event, state_info, extend_info, extend_info_len);
                			}
                		} else if(pRsp->wakeup_flag == txca_wakeup_flag_suc_rsp) {
                			txc_process_response(voice_id, event, state_info, extend_info, extend_info_len);
                		}
                } else {
                		// 普通响应，交给控制层处理
                		txc_process_response(voice_id, event, state_info, extend_info, extend_info_len);
                }
            }
            break;
    	}	
    } 
    return true;
}

```

如果您需要知道本地是通过“你好”还是“小微”唤醒的，仍然可以使用`VoiceRecognizeEmbedGetResult`获取对应的 text。
