
## Step1.准备工作
## Step2.设备注册及配置参考[设备注册](/wiki/#hardware_product_intro)

## Step3.硬件SDK对接

### 3.1 初始化信息
在写第一行代码之前，有些信息是先要拿到的，这些信息将会作为参数用于初始化函数中，所以我们可以称之为初始化信息，包括如下几个：

*   **pid(product id：产品ID)** pid是在Step2.1中获取的，对于合作方而言，您旗下的一款产品可以申请一个独立的pid，QQ物联云可以为该pid分配独立的配置信息。以ipcamera为例，如果您旗下有两款产品，一款支持云台转向，而另一款是广视角卡片机，那我们推荐两款产品申请两个不同的pid。

*   **sn(serial number：序列号)** 每台设备都应该有一个唯一的序列号，序列号并不需要腾讯后台分配，所以您可以直接对接原有产品线的序列号系统，但是我们对序列号格式有严格要求：长度必须是16个字符的字母、数字或者连词符的组合，例如`ABC-0032-1234567`就是一个非常标准的序列号。 您亦可以使用我们提供的客户端工具（Step2.2所示的页面中可以下载）来生成符合要求的序列号，如下图：

[![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ipcamera_9.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ipcamera_9.png)

*   **license(sn对应的认证签名)** license用于安全校验，主要目的是保护合作方的利益，避免冒充合作方的山寨设备出现，license的产生可以借助客户端工具实现。 `注意：license的生成使用的是您在Step2.2中产生的密钥对中的私钥，文件名叫做ec_key.pem，请您不要弄混了`

[![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ipcamera_10.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ipcamera_10.png)

*   **server public key(物联云服务器认证key)** 最后一组信息是用于保护设备的，避免它被来自互联网的DNS劫持或者后台伪造等手段所攻击，所以这一项也是必选项，您可以在Step2.2提及的页面里找到这个key，如下图：

[![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/step2_n_6.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/step2_n_6.png)

### 3.2 SDK下载

参考[LinuxSDK下载](/wiki/#APIDesc_linux_sdk_download)

### 3.3 第一行代码

前三步工作完成之后，我们就可以开始写第一行代码了（您可以参照main_1.c中的示例代码）：

```
int main(int argc, char* argv[])
{
    if ( !initDevice() ) {
        return -1;
    }
    char input[100];
    while (scanf("%s", input)) {
        if ( !strcmp(input, "quit") ) {
            tx_exit_device();
            break;
        }
        sleep(1);
    }
    return 0;
}
```

这是demo的main入口函数，可以看到里面几乎什么都没有做，只是调用了initDevice()这个函数，接下来我们将逐行解读一下initDevice()。

### 3.4 init device sdk

在接下来的这段代码里，您会看到我们在3.1中辛苦准备的几个初始化参数都被用上了：

```
bool initDevice() {
    // 从文件中读取 sn
    unsigned char sn[32] = {0};
    int nSNSize = 0;
    if(!readBufferFromFile("./GUID_file.txt", sn, sizeof(sn), &nSNSize)) {
        printf("[error]get sn from file failed...\n");
        return false;
    }

    // 从文件中读取 license
    unsigned char license[256] = {0};
    int nLicenseSize = 0;
    if (!readBufferFromFile("./licence.sign.file.txt", license, sizeof(license), &nLicenseSize)) {
        printf("[error]get license from file failed...\n");
        return false;
    }

    char svrPubkey[256] = {0};
    int nPubkeySize = 0;
    if (!readBufferFromFile("./1000000004.pem", svrPubkey, sizeof(svrPubkey), &nPubkeySize))
    {
        printf("[error]get svrPubkey from file failed...\n");
        return NULL;
    }

    // 设备的基本信息
    tx_device_info info = {0};
    info.os_platform            = "Linux";

    info.device_name            = "device_demo1";
    info.device_serial_number   = sn;
    info.device_license         = license;
    info.product_version        = 101;

    info.product_id             = 1000000004;
    info.server_pub_key         = svrPubkey;

    // 设备登录、在线状态、消息等相关的事件通知
    tx_device_notify notify      = {0};
    notify.on_login_complete     = on_login_complete;
    notify.on_online_status      = on_online_status;

    // SDK初始化目录，写入配置、Log输出等信息
    tx_init_path init_path = {0};
    init_path.system_path = "./";
    init_path.system_path_capicity = 100 * 1024;
    init_path.app_path = "./";
    init_path.app_path_capicity = 1024 * 1024;
    init_path.temp_path = "./";
    init_path.temp_path_capicity = 10 * 1024; //这个参数实际没有用的，可以忽略

    // 设置log输出函数
    tx_set_log_func(log_func);

    // 初始化SDK，若初始化成功，则内部会启动一个线程去执行相关逻辑，该线程会持续运行，直到收到 exit 调用
    int ret = tx_init_device(&info, &notify, &init_path);
    if (err_null == ret) {
        printf(" >>> tx_init_device success\n");
    }
    else {
        printf(" >>> tx_init_device failed [%d]\n", ret);
        return false;
    }
    return true;
}
```

整个函数都是围绕 **tx_device_info** 这个结构体来进行，其中device_serial_number, device_license, product_id 以及 server_pub_key都可以根据 **Step3.1** 的描述来获取，而device_name和product_version则可以由您来自由指定。其中device_name最长不能超过32字节（后台系统的存储限制），product_version则是用于后续的系统升级，您可以像我们在示例代码中一样定义最初的版本号为101（也就是1.01）。

**tx_device_notify** 结构体用来承接来自SDK的事件通知，这里需要您特别注意的是`线程安全问题`，比如**on_login_complete** 和 **on_online_status** 等回调均是来自SDK内部的一个自有线程的驱动，如果您在这些函数内部实现复杂的全局变量操作，一定要考虑是否同一时刻可能存在来自您编写的模块的线程也会同样操作这些全局变量。

接下来的**tx_init_path** 结构体用于对接对设备SDK而言最重要的几个存储路径，其中 **system_path** 是最重要的一个路径，必须要保证SDK对此目录的可读写权限；**app_path**现在可以理解为是log_path，一些包含严重错误的log信息会存储到这个目录下；**temp_path**主要用于临时文件的存放，所谓的临时文件，目前还主要跟网络下载相关。该结构体的详细定义如下，其中的各个capicity字段都是用于限定目录大小所用的。

最后，示例代码调用了**tx_init_device**函数完成了初始化过程，我们来看一下这段代码的运行结果。如果设备目前还是“白纸一张”，也就是还没有被某个用户绑定过，那么期望的设备端串口输出应该是如下所示：

[![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ipcamera_12.png)](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ipcamera_12.png)

因为还没有被绑定过，所以目前为止SDK所做的工作基本就仅启动了一个内部线程，然后以一种几乎不消耗CPU的方式等待它的第一个任务——**接受绑定**。

> **为什么看不到log?** 看不到log是因为没有为log输出做定位，您可以参照demo程序中的方式调用tx_set_log_func，之后串口打印上就能看到详细的log信息了。

### 3.5 语音数据上下行

#### 3.5.1 语音数据上行

在开始语音上行之前，需要先**start service** 如下

```
//播放器回调
tx_ai_audio_player player = {0};
player.create = on_player_create;
player.destory = on_player_destroy;
player.play_res = on_player_play_url;
player.controll = on_player_control;
player.tts_push_start = on_player_tts_push_start;
player.tts_push = on_player_tts_push;
player.tts_push_end = on_player_tts_push_end;

//语音输入参数
tx_ai_audio_encode_param param = {0};
param.audio_format = ai_audio_format_pcm;
param.samples_per_sec = 16;
param.sample_bits = 16;
    tx_ai_audio_configservice_with_player_callback(&player, &param, &callback);

//全局控制参数
tx_ai_audio_callback callback = {0};
callback.on_control = on_ai_control;
callback.on_state = on_ai_state;

tx_ai_audio_service_start(&callback);
```

**tx_ai_audio_configservice_with_player_callback**设置语音输入和输出相关参数 tx_ai_audio_player 包括播放器创建、url资源播放、播放器控制、tts播放等部分， 详细说明请参考 [播放器接口说明](/wiki/#APIDesc_media_player_linux)

tx_ai_audio_encode_param 指定了语音输入格式、码率、采样率 须按照按照固定参数设置

**tx_ai_audio_service_start**开启语音服务 tx_ai_audio_callback主要负责全局控制和状态回调， 详细说明请参考 [播放器接口说明](/wiki/#APIDesc_media_player_linux)

到此为止， 已经完成了语音服务基本配置，接下去就可以往云端写入语音数据了

开启一次语音请求需要调用如下接口

```
tx_ai_audio_request_start();
```

在调用完接口后， 等待上文设置的 `on_ai_control` 回调, 其中 ctlcode = tx_ai_audio_control_code_startrecord 是表示sdk已经开始准备接受填充语音数据了

```
void on_ai_control(int ctlcode, int value) {
    printf("on_ai_control %d %d\n", ctlcode, value);
    if(ctlcode == tx_ai_audio_control_code_startrecord) {
    }
}
```

在这个时候， 就可以通过调用

```
tx_ai_audio_request_fill_data((void*)frames, frameCount * frameSize, frameCount * frameSize, 0);
```

来填充语音数据，数据类型必须按照 tx_ai_audio_configservice_with_player_callback 设置的类型写入，更多该接口说明参考头文件或[通道层接口说明](/wiki/#APIDesc_tunnel_interface) 为了先完成流程接入， 可以从pcm文件读取源数据直接填充， 流程接入完成后可以接入[唤醒词](/wiki/#APIDesc_wakeup_linux)模块

等待tx_ai_audio_control_code_endrecord事件触发 后 停止填充数据

```
void on_ai_control(int ctlcode, int value) {
    printf("on_ai_control %d %d\n", ctlcode, value);
    if(ctlcode == tx_ai_audio_control_code_endrecord) {
    }
}
```

#### 3.5.2 语音数据下行

在完成一次完整的语音上行之后， 云端会根据输入的语音内容提供相应的服务， 主要包括TTS语音和音乐

如输入:

> 今天杭州天气怎么样

输出:

> 今天天气晴, 气温...

此输出即为TTS语音 TTS语音将通过回调 `on_player_tts_push_start`、 `on_player_tts_push`、 `on_player_tts_push_end` 来播放， 你需要实现这3个回调

**on_player_tts_push_start(int pid, int sample, int channel, int pcmSample)** 收到tts参数, 包括 pid: player id， 即使用哪个播放器播放, sample: 采样率 channel, 通道数, 目前为单通道 pcmSample: pcm采样率， 目前和sample一致

**on_player_tts_push** 开始收到 pcm数据, 可直接用于播放或保存成pcm文件

**on_player_tts_push_end** tts数据接收完毕

到此为止， 简单的一次接入已经完成了
