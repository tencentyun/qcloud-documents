
## TIMInit

IM SDK 初始化。

**原型：**

```c
TIM_DECL int TIMInit(uint64_t sdk_app_id, const char* json_sdk_config);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdk_app_id | uint64_t | 官网申请的 SDKAppid  |
| json_sdk_config | const char\* | SDK 配置选项 JSON 字符串，详情请参考 [SdkConfig](https://cloud.tencent.com/document/product/269/33553#sdkconfig)  |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功，其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?
- 在使用 IM SDK 进一步操作之前，需要先初始化 IM SDK。
- `json_sdk_config`可以为`NULL`或者""空字符串，在此情况下 SdkConfig 均为默认值。
- `json_sdk_config`里面的每个 JSON key 都是选填的，详情请参考 [SdkConfig](https://cloud.tencent.com/document/product/269/33553#sdkconfig)。


**示例**

```c
Json::Value json_value_init;
json_value_init[kTIMSdkConfigLogFilePath] = "D:\\";
json_value_init[kTIMSdkConfigConfigFilePath] = "D:\\";
json_value_init[kTIMSdkConfigAccountType] = "107";

uint64_t sdk_app_id = 1234567890;
if (TIM_SUCC != TIMInit(sdk_app_id, json_value_init.toStyledString().c_str())) {
    // TIMInit 接口调用错误， IM SDK 初始化失败   
}

// json_value_init.toStyledString() 得到 json_sdk_config JSON 字符串如下
{
   "sdk_config_account_type" : "107",
   "sdk_config_config_file_path" : "D:\\",
   "sdk_config_log_file_path" : "D:\\"
}
```


## TIMUninit

IM SDK 卸载。

**原型：**

```c
TIM_DECL int TIMUninit(void);
```

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功，其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?卸载 DLL 或退出进程前需此接口卸载 IM SDK，清理 IM SDK 相关资源。


**示例**

```c
if (TIM_SUCC != TIMUninit()) {
    // IM SDK 卸载失败  
}
```


## TIMGetSDKVersion

获取 IM SDK 版本号。

**原型：**

```c
TIM_DECL const char* const TIMGetSDKVersion(void);
```

**返回值**

| 类型 | 含义 |
|-----|-----|
| const char\* | 返回 IM SDK 的版本号 |

## TIMSetConfig

设置额外的用户配置。

**原型：**

```c
TIM_DECL int TIMSetConfig(const char* json_config, TIMCommCallback cb, const void* user_data);
```

**参数**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| json_config | const char\* | 其他配置选项 |
| cb | TIMCommCallback | 返回设置配置之后所有配置的回调，此回调 cb 可为空，表示不获取所有配置信息。回调函数定义请参考 [TIMCommCallback](https://cloud.tencent.com/document/product/269/33552#timcommcallback)，回调参数解析请参考 [TIMSetConfig](https://cloud.tencent.com/document/product/269/33552#timsetconfig)  |
| user_data | const void\* | 用户自定义数据，IM SDK 只负责传回给回调函数 cb，不做任何处理 |

**返回值**

| 类型 | 含义 |
|-----|-----|
| int | 返回 TIM_SUCC 表示接口调用成功（接口只有返回 TIM_SUCC，回调 cb 才会被调用），其他值表示接口调用失败。每个返回值的定义请参考 [TIMResult](https://cloud.tencent.com/document/product/269/33553#timresult)  |

>?目前支持设置的配置有代理的 IP 和端口、输出日志的级别、获取群信息/群成员信息的默认选项、是否接受消息已读回执事件等。每项配置可以单独设置、也可以一起配置，详情请参考 [SetConfig](https://cloud.tencent.com/document/product/269/33553#setconfig)。


**示例**

```c
Json::Value json_user_config;
json_user_config[kTIMUserConfigIsReadReceipt] = true;  // 开启已读回执
Json::Value json_config;
json_config[kTIMSetConfigUserConfig] = json_user_config;

if (TIM_SUCC != TIMSetConfig(json_config.toStyledString().c_str(), [](int32_t code, const char* desc, const char* json_param, const void* user_data) {
    // 回调内部
}, this)) {
    //TIMSetConfig 接口调用失败
} 

// json_config.toStyledString().c_str() 得到 json_config JSON 字符串如下
{
   "set_config_user_config" : {
      "user_config_is_read_receipt" : true
   }
}
```


