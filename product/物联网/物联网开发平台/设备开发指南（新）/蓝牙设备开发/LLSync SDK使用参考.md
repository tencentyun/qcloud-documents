

LLSync SDK 提供 LLSync 协议接入方案，打通了 `BLE 设备-App-物联网开发平台` 或 `BLE 设备-网关设备-物联网开发平台` 的数据链路，方便用户将 BLE 设备快速接入物联网开发平台。用户可以在物联网开发平台创建产品，通过云 API 下发数据模版操作来控制 BLE 设备。

## SDK获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [LLSync SDK](https://github.com/tencentyun/qcloud-iot-explorer-BLE-sdk-embedded )。

## 软件架构

BLE 设备可以通过 LLSync 协议与移动端 App 或网关设备连接，通过 App 或网关设备接入物联网开发平台。LLSync SDK 结构框图见下图：

![LLSync结构框图](https://main.qcloudimg.com/raw/9fabb2c222ae40d6a93641b745a327bd.png)

SDK 分三层设计，从上至下分别为应用层、LLSync 核心层、HAL 移植层。
* HAL 移植层：LLSync SDK 需要适配设备硬件和 BLE 协议栈，针对不同的设备和 BLE 协议栈用户需要进行移植和适配。
* LLSync 核心组件：定义了 BLE 设备和移动端 App 或网关设备之间的通信协议，实现身份认证，数据解析等功能，用户一般无需改动即可使用。
* 应用层：LLSync SDK 提供数据模版的操作函数，用户需要根据使用场景做具体实现。

## 目录结构

```c
qcloud_iot_explorer_ble
  ├─config                            # 配置文件
  ├─docs                              # 协议文档
  ├─inc                               # 外部头文件
  ├─scripts                           # 脚本目录
  │   ├─interpret_json_dt             # json 文本转换 C 代码
  │       ├─config                    # ini 文件
  │       ├─src                       # 脚本文件
  │           ├─dt_fixed_content      # C 代码中的固定内容，无需转换生成
  └─src                               # LLSync 核心代码，用户一般无需修改
      ├─core                          # LLSync 源码
      ├─internal_inc                  # 内部头文件
      └─utils                         # 通用组件
```

## 移植指引

请参见 [LLSync SDK 接入指引](https://cloud.tencent.com/document/product/1081/48398)。



