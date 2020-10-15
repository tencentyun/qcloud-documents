
本文为您介绍如何将 LLSync SDK 移植到目标硬件平台。LLSync SDK 采用模块化设计，分离 LLSync 核心组件与硬件抽象层，在进行跨平台移植时，一般只需要用户对硬件抽象层进行适配即可。

## SDK 获取

SDK 使用 Github 托管，可访问 Github 下载最新版本设备端 [LLSync SDK](https://github.com/tencentyun/qcloud-iot-explorer-BLE-sdk-embedded)。

## 接入指引

一般情况下，各平台接入 LLSync SDK 可以分为以下2个步骤。

### 数据模版代码生成

1. 用户需要在物联网开发平台创建设备并定义数据模版，详情请参见 [物联网开发平台产品开发手册](https://cloud.tencent.com/document/product/1081/34738)。
2. 将定义完成的数据模版拷贝到本地，通过 LLSync SDK 提供的代码生成脚本生成对应的 C 代码
   ```c
   iot$ python3 interpret_dt_ble.py ../example.json 
   reading json file start
   reading json file end
   generate header file start
   generate header file end
   generate source file start
   generate source file end
   ```
3. 拷贝生成的`ble_qiot_template.c`和`ble_qiot_template.h`到`date_template`文件夹。

### 硬件抽象层移植

需要用户移植适配的接口在`ble_qiot_import.h`中，主要包括设备信息和 BLE 协议栈两方面的移植。

- **设备信息接口适配**
<table>
<thead>
<tr>
<th align="center">序号</th>
<th align="center">函数</th>
<th align="center">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="center">1</td>
<td align="center">ble_get_product_id</td>
<td align="center">获取设备三元信息之产品 ID</td>
</tr>
<tr>
<td align="center">2</td>
<td align="center">ble_get_device_name</td>
<td align="center">获取设备三元信息之设备名称</td>
</tr>
<tr>
<td align="center">3</td>
<td align="center">ble_get_psk</td>
<td align="center">获取设备三元信息之设备密钥</td>
</tr>
<tr>
<td align="center">4</td>
<td align="center">ble_get_mac</td>
<td align="center">获取设备蓝牙 MAC 地址</td>
</tr>
<tr>
<td align="center">5</td>
<td align="center">ble_write_flash</td>
<td align="center">SDK 需要存储内部信息到设备存储介质</td>
</tr>
<tr>
<td align="center">6</td>
<td align="center">ble_read_flash</td>
<td align="center">SDK 需要从设备存储介质读取存储的信息</td>
</tr>
<tr>
<td align="center">7</td>
<td align="center">log 接口</td>
<td align="center">在<code>ble_qiot_configh</code>中适配 log 接口</td>
</tr>
<tr>
<td align="center">8</td>
<td align="center">定时器接口</td>
<td align="center">定时器类接口</td>
</tr>
</tbody></table>

 >?设备三元信息在物联网开发平台创建设备后获取，用户需要自行存储到设备。
 >
- **BLE 协议栈适配**
<table>
<thead>
<tr>
<th align="center">序号</th>
<th align="center">函数</th>
<th align="center">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="center">1</td>
<td align="center">ble_advertising_start</td>
<td align="center">开始广播接口</td>
</tr>
<tr>
<td align="center">2</td>
<td align="center">ble_advertising_stop</td>
<td align="center">停止广播接口</td>
</tr>
<tr>
<td align="center">3</td>
<td align="center">ble_send_indication</td>
<td align="center">向 UUID FFE3 写入通知/指示</td>
</tr>
<tr>
<td align="center">4</td>
<td align="center">ble_services_add</td>
<td align="center">添加 LLSync 服务到 BLE 协议栈</td>
</tr>
</tbody></table>

## 应用开发

- **SDK配置**
用户需要根据自身需求在 `ble_qiot_config.h` 中对 SDK 做简单配置后使用，具体操作步骤如下：
 1. SDK 需要存储内部数据到设备内，存储地址在`ble_qiot_config.h` 中使用 `BLE_QIOT_RECORD_FLASH_ADDR` 定义，请用户根据实际情况修改。
 2. 用户需要明确定义设备大小端，在 `ble_qio_config.h` 中定义 `__BYTE_ORDER__`。
 3. SDK 支持两种广播模式，可以选择默认开启广播或按键开始广播。
   - 定义 `BLE_QIOT_BUTTON_BROADCAST` 为1时，当设备未绑定时需要按键才开始广播（需要用户在按键动作中添加广播功能），设备绑定时开机默认广播。
   - 定义 `BLE_QIOT_BUTTON_BROADCAST` 为0时，设备开机默认广播。

- **例程代码抽取**
SDK 已经适配 `nordic 52832` 并提供例程，存储在 `samples/nrf52832` 目录下，用户可以通过脚本将指定平台的例程代码抽取出来。
```c
iot code_extract % python3 code_extract.py nrf52832
extract code for nrf52832 start, dest dir /iot/Desktop/work_code/qcloud_iot_explorer_ble/scripts/code_extract/qcloud-iot-ble-nrf52832
extract code success
```
代码抽取完成后，请参考对应的`readme.md`进行编译，参考文档一般位于生成的代码文件夹中。

- **数据模版开发**
用户需要根据实际需求，对`ble_qiot_template.c`中的函数模版做具体实现，可以参考`ref-impl`目录下的例程进行开发。

- **API说明**
在`ble_qiot_export.h`中提供了 API 函数，一般情况下用户只需要调用 API 函数即可完成应用开发。
<table>
<thead>
<tr>
<th align="center">序号</th>
<th align="center">函数</th>
<th align="center">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="center">1</td>
<td align="center">ble_qiot_explorer_init</td>
<td align="center">SDK 初始化</td>
</tr>
<tr>
<td align="center">2</td>
<td align="center">ble_event_get_status</td>
<td align="center">获取数据模版最新信息，对应数据模版<code>get_status</code>方法</td>
</tr>
<tr>
<td align="center">3</td>
<td align="center">ble_event_report_property</td>
<td align="center">上报设备最新信息，对应数据模版<code>report</code>方法</td>
</tr>
<tr>
<td align="center">4</td>
<td align="center">ble_event_post</td>
<td align="center">上报事件，对应数据模版<code>event_post</code>方法</td>
</tr>
<tr>
<td align="center">5</td>
<td align="center">ble_qiot_advertising_start</td>
<td align="center">开始广播，广播包内容请参考 <a href="https://main.qcloudimg.com/raw/28854b0c56ed0cfd2e06904550d90243.pdf" target="_blank">LLSync 协议说明</a></td>
</tr>
<tr>
<td align="center">6</td>
<td align="center">ble_qiot_advertising_stop</td>
<td align="center">停止广播</td>
</tr>
<tr>
<td align="center">7</td>
<td align="center">ble_device_info_write_cb</td>
<td align="center">UUID FFE1 数据到达后调用此接口传入数据</td>
</tr>
<tr>
<td align="center">8</td>
<td align="center">ble_lldata_write_cb</td>
<td align="center">UUID FFE2 数据到达后调用此接口传入数据</td>
</tr>
<tr>
<td align="center">9</td>
<td align="center">ble_gap_disconnect_cb</td>
<td align="center">蓝牙连接端口后调用此接口</td>
</tr>
</tbody></table>

## LLSync 协议

请参考 [LLSync 协议说明](https://main.qcloudimg.com/raw/28854b0c56ed0cfd2e06904550d90243.pdf)

## SDK使用参考

请参考 [LLSync SDK 使用参考](https://cloud.tencent.com/document/product/1081/48399)

