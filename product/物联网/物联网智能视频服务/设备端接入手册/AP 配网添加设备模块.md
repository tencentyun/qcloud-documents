

SDK 内部集成 AP 模式时数据传输功能，如果需要内部获取 Wi-Fi 信息，可以通过本模块接口获取。

## 功能介绍
设备处在 AP 模式时，设备端可以通过此模块从添加端获取所要连接 Wi-Fi 的 SSID、密码、加密方式信息。

## 流程指引
#### 总流程
注册获取 Wi-Fi 信息回调 > AP 模块初始化 > AP 模块去初始化

#### 添加流程
收到获取 Wi-Fi 信息回调 > 配网

## 接口参考
该功能模块提供以下接口：
- iv_ad_ap_init：AP 模块初始化。
- iv_ad_ap_exit：AP 模块去初始化。
- iv_ad_ap_get_wifi_info_cb：获取 Wi-Fi 信息回调。

#### iv_ap_init

**接口描述**

AP 模块初始化。进行资源申请，数据通讯准备等，需要本模块启动时调用。

```
int iv_ad_ap_init(iv_ap_init_parameters_s *pstApInitParameters); 
```

**参数说明**

参数名称 | 类型 | 描述 |输入/输出
---|---|---|---
pstApInitParameters | iv_ap_init_parameters_s * | AP 模块初始化参数 | 输入

**返回值**

返回值 | 描述 
---|---
IV_ERR_NONE | 成功
IV_ERR_* | 失败，对应相应错误码

#### iv_ad_ap_exit

**接口描述**
AP 模块去初始化。进行资源释放，退出本模块时调用。


```
int iv_ad_ap_exit(void); 
```

**参数说明**

参数名称 | 类型 | 描述 |输入/输出
---|---|---|---
无 | 无 | 无 | 无

**返回值**

返回值 | 描述 
---|---
IV_ERR_NONE | 成功
IV_ERR_* | 失败，对应相应错误码

#### iv_ad_ap_get_wifi_info_cb

**接口描述**
得到 W-iFi 信息回调，SDK 在获取到 Wi-Fi 配网信息后，回调此接口将信息传递给用户。


```
void (* iv_ad_ap_get_wifi_info_cb)(iv_ad_ap_get_wifi_info_s *pstWifiInfo); 
```

**参数说明**

参数名称 | 类型 | 描述 |输入/输出
---|---|---|---
pstWifiInfo | iv_ad_ap_get_wifi_info_s * | AP 模块获取到的 Wi-Fi 信息 | 输入

**返回值**

返回值 | 描述 
---|---
void | -

## 数据结构
改模块提供以下数据结构：
- IV_AD_AP_MAX_WIFI_SSID_LEN：最大 Wi-Fi SSID 长度。
- IV_AD_AP_MAX_WIFI_PASSWORD_LEN：最大 Wi-Fi password 长度。
- iv_ad_ap_init_parm_s：AP 模块初始化参数结构体。
- iv_ad_ap_get_wifi_info_s：获取到的 Wi-Fi 信息结构体。

#### IV_AD_AP_MAX_WIFI_SSID_LEN
**接口描述**
最大 Wi-Fi SSID 长度。


```
#define IV_AD_AP_MAX_WIFI_PASSWORD_LEN 128
```

#### IV_AP_MAX_WIFI_PASSWORD_LEN
**接口描述**
最大 Wi-Fi SSID 长度。

```
#define IV_AP_MAX_WIFI_PASSWORD_LEN 128
```

#### iv_ad_ap_init_parm_s

**接口描述**

AP 模块初始化参数结构体。


```
typedef struct iv_ad_ap_init_parm_s
{
    void (* iv_ad_ap_get_Wifi_info_cb)(iv_ad_ap_get_wifi_info_s *pstWifiInfo);
}iv_ad_ap_init_parm_s;
```

**参数说明**

成员名称 | 描述 | 取值
---|---|---
iv_ap_get_Wifi_info_cb | 获取到 Wi-Fi 信息后回调 | -

#### iv_ad_ap_get_wifi_info_s
**接口描述**
获取到的 Wi-Fi 信息结构体。


```
typedef struct iv_ad_ap_get_wifi_info_s
{
    iv_cm_wifi_enc_type_e	eEncryptType;
    char                    cSsid[IV_AD_AP_MAX_WIFI_SSID_LEN];
    char                    cPassword[IV_AD_AP_MAX_WIFI_PASSWORD_LEN];
}iv_ad_ap_get_wifi_info_s;
```

**参数说明**

成员名称 | 描述 | 取值
---|---|---
u32EncryptType  | 加密类型| iv_cm_wifi_enc_type_e
u8Ssid  | Wi-Fi SSID | -
u8Password  | Wi-Fi 密码 | -
