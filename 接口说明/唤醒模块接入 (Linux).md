## 简介

唤醒模块目前包括静音检测和语音识别，两者必须配合使用。 在接入过程中， 先使用静音检测判断未非静音数据后，传入语音识别模块后检测唤醒词

## 静音检测

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

**EVAD_GetHandle** 获取句柄，设置vad参数，全局调用一次 参考参数：

```
EVAD_GetHandle(&m_vadInst, 16000, 500, 2.5, 300, 225)
```

**EVAD_Reset** 清空数据，重新一轮

**EVAD_GetBeginDelayTime** 由于vad判断开始说话会有滞后，必须从这个函数获取滞后的时间，从而把时间点进行前置

**EVAD_AddData** 追加录音数据, 根据 返回值 判断是否已开始说话 (EVAD_SPEAK)

**EVAD_Release** 释放句柄，全局调用一次

## 语音识别

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

填充声音数据进行唤醒词检测，当返回值为1，表示已检测到完整唤醒词（“小微你好”，“你好小微”），当返回值为2，表示已检测到一半的唤醒词（“你好”，“小微”）。在云端校验模式中，在返回1或者2的时候，就可以开始云端校验，并且VoiceRecognizeEmbedEnd这次唤醒。

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

获取结果 VoiceRecognizeResult.type == 0 即为唤醒(一般情况下不需要这样判断，部分平台拿到的text是乱码，可以这样判断。)

```
/**
 * @brief: get the result
 * if VoiceRecognizeEmbedAddData return 1 already, you can use this function directly
 * else you only can use it after VoiceRecognizeEmbedEnd.
 */
VRAPI_API int VoiceRecognizeEmbedGetResult(VoiceRecognizeEmbedHandle handle,
        VoiceRecognizeResult &result);
```

**VoiceRecognizeEmbedRelease** 释放句柄

```
/**
 * @brief: release the handle
 * must appear in pairs with 'VoiceRecognizeEmbedInit'
 */
VRAPI_API void VoiceRecognizeEmbedRelease(VoiceRecognizeEmbedHandle *pHandle);
```

## 云端校验

为了降低误唤醒，我们增加了一个云端校验的方式。在检测到半词唤醒后，可以将之前唤醒的声音，再加上之后的声音传到服务器，由服务器来判断这次是不是应该成功唤醒。

```
int ret = VoiceRecognizeEmbedAddData();
if(ret == 1 || ret == 2) {
    tx_ai_audio_request_param param = {0};
    param.wakeup_mode = 1;// 1 表示校验唤醒词的请求；0为默认值，表示正常识别请求
    tx_ai_audio_request_start(tx_ai_audio_request_param* param);// 记得之后要把唤醒模块检测到唤醒词的那部分声音拼到前面送去识别
    ...
}
```

之后的流程和正常请求一样。如果云端检测到了唤醒词，会回调on_wakeup,否则这次请求在检测到静音后就自动结束了。在这个回调的时候，不需要单独再发起一次请求了，SDK会自动完成这部分操作，您可以在这个时候进行亮灯。

```
//AIAudio主回调
typedef struct _tx_ai_audio_callback
{
    void (*on_state)(int event, tx_ai_audio_event_info* info);                  //SDK状态回调
    void (*on_control)(int ctrlcode, int value);                                //SDK控制回调
    void (*on_rsp)(int errCode, int rsp_type, tx_ai_audio_rsp_app_info* info);  //通用请求回调
    void (*on_cc_msg_notify)(unsigned long long from, tx_ai_cc_msg* msg);
    void (*on_send_cc_msg_result)(unsigned int cookie, unsigned long long to, int err_code);
    void (*on_wakeup)();// 云端唤醒成功
} tx_ai_audio_callback;
```

如果你需要知道本地是通过“你好”还是“小微”唤醒的，仍然可以使用VoiceRecognizeEmbedGetResult获取对应的text。

如果需要关注云端校验的结果，可以监听on_state回调中tx_ai_audio_event_info的wakeup_flag字段。该字段的含义如下：
0：非云端校验结果
1：云端校验失败，说明本地误唤醒了
2：云端校验成功，并且只单独说了唤醒词
3：说了指令唤醒词（暂时不支持，无需关注）
4：云端校验成功，并且唤醒之后连续说话（“你好小微今天天气怎么样”）
