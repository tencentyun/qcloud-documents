

SDK 内部集成 AP 模式时数据传输功能，如果需要内部获取 Wi-Fi 信息，可以通过本模块接口获取。

##  功能介绍

设备处在 AP 模式时，设备端可以通过此模块从添加端获取所要连接 Wi-Fi 的 SSID、密码、加密方式信息。

## 流程指引

#### 系统模块总流程

注册得到 Wi-Fi 信息回调-->AP 模块初始化-->AP 模块去初始化

#### 添加流程

收到获 Wi-Fi 信息回调-->配网
## 接口参考

该功能模块提供以下接口：

- iv_ad_ap_init：AP 模块初始化
- iv_ad_ap_exit：AP 模块去初始化
- iv_ad_ap_recv_config_info_cb：接收用户自定义配网信息回调

#### iv_ap_init

**接口描述**
AP 模块初始化。进行资源申请，数据通讯准备等，需要本模块启动时调用。

```
int iv_ad_ap_init(iv_ap_init_parameters_s *pstApInitParameters); 
```
**参数说明**

| 参数名称            | 类型                      | 描述             | 输入/输出 |
| ------------------- | ------------------------- | ---------------- | --------- |
| pstApInitParameters | iv_ap_init_parameters_s * | AP 模块初始化参数 | 输入      |

**返回值**

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应错误码 |

#### iv_ad_ap_exit

**接口描述**
AP 模块去初始化。进行资源释放，退出本模块时调用。


```
int iv_ad_ap_exit(void); 
```

**参数说明**

| 参数名称 | 类型 | 描述 | 输入/输出 |
| -------- | ---- | ---- | --------- |
| 无       | 无   | 无   | 无        |

【返回值】

| 返回值      | 描述                 |
| ----------- | -------------------- |
| IV_ERR_NONE | 成功                 |
| IV_ERR_*    | 失败，对应相应错误码 |

#### iv_ad_ap_recv_config_info_cb
**接口描述**
AP 配网接收信息回调，SDK 收到 App 传过来的用户自定义配网信息后，通过此接口将信息传递给用户。

```
void (* iv_ad_ap_recv_config_info_cb)(char *data, uint32_t length);
```

**参数说明**

| 参数名称 | 类型     | 描述                   | 输入/输出 |
| -------- | -------- | ---------------------- | --------- |
| data     | char *   | AP 模块获取到的配网信息 | 输入      |
| length   | uint32_t | 配网信息长度           | 输入      |

【返回值】

| 返回值 | 描述 |
| ------ | ---- |
| void   | -   |

##  数据结构

该模块提供以下数据结构：

- iv_ad_ap_init_parm_s：AP 模块初始化参数结构体。


#### iv_ad_ap_init_parm_s

**接口描述**
AP 模块初始化参数结构体
```
typedef struct iv_ad_ap_init_parm_s
{
    void (* iv_ad_ap_recv_config_info_cb)(char *data, uint32_t length);
}iv_ad_ap_init_parm_s;
```

**参数说明**

| 成员名称                     | 描述             | 取值 |
| ---------------------------- | ---------------- | ---- |
| iv_ad_ap_recv_config_info_cb | 接收配网信息回调 | -  |


