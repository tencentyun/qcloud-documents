
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

需要用户移植适配的接口在 `ble_qiot_import.h` 中，主要包括设备信息和 BLE 协议栈两方面的移植。
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
<td align="center">ble_ota_is_enable</td>
<td align="center">获取设备是否允许升级</td>
</tr>
<tr>
<td align="center">8</td>
<td align="center">ble_ota_get_download_addr</td>
<td align="center">获取设备升级文件的存储基地址</td>
</tr>
<tr>
<td align="center">9</td>
<td align="center">ble_ota_write_flash</td>
<td align="center">存储升级文件内容到介质</td>
</tr>
<tr>
<td align="center">10</td>
<td align="center">ble_secure_bind_user_cb</td>
<td align="center">绑定请求到达后触发的用户回调</td>
</tr>
<tr>
<td align="center">11</td>
<td align="center">ble_secure_bind_user_notify</td>
<td align="center">绑定请求超时或用户取消绑定后通知用户</td>
</tr>
<tr>
<td align="center">12</td>
<td align="center">定时器接口</td>
<td align="center">定时器类接口</td>
</tr>
</tbody></table>

	1. 设备三元信息在 [物联网开发平台](https://cloud.tencent.com/product/iotexplorer) 新建产品并创建设备后通过 [查看设备信息](https://cloud.tencent.com/document/product/1081/34741#.E6.9F.A5.E7.9C.8B.E8.AE.BE.E5.A4.87.E4.BF.A1.E6.81.AF) 获取。开发者需要负责信息存储，存储介质不做限制，开发阶段可以将三元信息保存在代码中，量产阶段可以将信息存储在片上 flash、片外 flash、eeprom 等或带有文件系统的存储介质中，方便量产烧录。
	2. 不同的蓝牙协议栈获取到的 mac 地址字节序可能不同，适配该接口时可能需要进行转换。LLSync 使用大端方式存储，即 mac 地址的第0字节存储在低地址，mac 地址的第5字节存储在高地址，一般与阅读顺序相同
	3. SDK 需要存储约20字节数据到 flash 中，存储介质不做限制，存储地址由开发者划分，通过宏 `BLE_QIOT_RECORD_FLASH_ADDR` 指定；若开发者使用文件系统保存 SDK 数据，不涉及存储地址时，宏 `BLE_QIOT_RECORD_FLASH_ADDR` 可设置为 0。
	4. `ble_write_flash()` 接口只负责数据写入，擦除、读写平衡等需由开发者在合适的时机进行，例如在写入前进行擦除，写入完成后回收旧 page 等。
	5. 当使用定时广播功能时或 OTA 功能时，需要实现定时器类接口。若不使用定时器类接口可以实现为桩函数。
	6. `ble_ota_is_enable()` 接口允许用户根据当前设备状态决定是否升级版本。
	7. `ble_secure_bind_user_cb()` 和 `ble_secure_bind_user_notify()` 仅在安全绑定功能启用时需要实现。
 
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
<tr>
<td align="center">5</td>
<td align="center">ble_get_user_data_mtu_size</td>
<td align="center">获取向 UUID FFE3 写入数据的最大长度</td>
</tr>
</tbody></table>

	1. LLsync SDK 定义了若干 `BLE attribute characteristic`，LLSync SDK 初始化时会调用 `ble_services_add()` 将其加入 BLE 协议栈。具体服务可以通过 `ble_qiot_export.h` 的 `ble_get_qiot_services()` 获取。如果蓝牙协议栈不支持动态添加蓝牙服务，也可以参考 `service_info` 结构体静态蓝牙服务。对于每一个 `attribute characteristic value max length` 开发者需要保证大于等于蓝牙协议栈支持的 mtu 大小，以免造成数据丢失、指针越界等问题。
	2. LLSync 规定了广播数据的格式，开发者需要通过 BLE 协议栈将传入的数据广播出去，微信小程序依赖广播数据发现并连接设备。广播数据包含两种类型，分别是 `0x02 <Partial list of 16 bit service UUIDs>` 或 `0x03 <Complete list of 16 bit service UUIDs>` 和 `0xFF < Manufacturer Specific Data>`。
	3. 开发者可以根据实际情况选择使用 `0x02` 或 `0x03` 类型广播 UUID，UUID 中必须包含 `#define IOT_BLE_UUID_SERVICE 0xFFE0`，开发者根据需求也可以加入自己私有的 `service UUID`。
	4. `Manufacturer Specific Data` 广播类型包含 `company identifier` 在内一共为 17 字节。如果开发者需要广播设备名等其他信息，只使用广播包很可能放不下，此时可以使用广播扫描回应包携带更多广播数据。
	5. LLSync 规定了数据的最大长度为2048字节，SDK 实现了数据的分片发送，连续多次调用 `ble_send_notify` 将数据发送出去。SDK 内没有做数据重传处理，因此开发者需要保证数据的发送成功。

## 应用开发

### SDK 配置

开发者需要根据自身需求在 `ble_qiot_config.h` 中对 SDK 做简单配置后使用，具体说明如下：
1. `BLE_QIOT_RECORD_FLASH_ADDR` 是 SDK 数据的存储地址。
2. `__BYTE_ORDER__` 是设备的大小端定义。
3. SDK 支持定时广播。定义 `BLE_QIOT_BUTTON_BROADCAST` 为1，当设备在未绑定状态下开始广播时，经过 `BLE_QIOT_BUTTON_BROADCAST` 定义的时间后广播自动停止。设备处于绑定状态时不支持定时广播功能。
4. 适配 SDK 的 log 输出接口 `#define BLE_QIOT_LOG_PRINT(...) printf(__VA_ARGS__)`，根据实际情况将 printf 替换为自己的打印函数。由于部分蓝牙协议栈特殊的缓存机制，LLSync SDK 提供的 ble_qiot_log_hex() 可能无法正常工作，请将宏 `#define BLE_QIOT_USER_DEFINE_HEDUMP 0` 打开，由开发者自己实现 `ble_qiot_log_hex()` 接口。
5. `BLE_QIOT_EVENT_MAX_SIZE` 定义了设备端可以通过 notify 发送的最大数据量，开发者可以通过减小此数值来优化堆栈。经测试，`BLE_QIOT_EVENT_MAX_SIZE` 配置为128、`BLE_QIOT_EVENT_BUF_SIZE` 配置为23时，栈内存占用小于2k。
6. `BLE_QIOT_EVENT_BUF_SIZE` 配置为 `BLE_QIOT_EVENT_MAX_SIZE` 和 MTU 的最小值。
7. `BLE_QIOT_SUPPORT_OTA` 功能宏配置为1时，即可使能 OTA 功能；配置为0则关闭 OTA 功能。
8. `BLE_QIOT_USER_DEVELOPER_VERSION` 是设备版本信息，可以用作升级前的版本号比较，**务必与物联网开发平台填写保持一致**。
9. `BLE_QIOT_SUPPORT_RESUMING` 配置为1时，即可使能断点续传功能，开发者可以根据需要选择是否开启支持断点续传功能。若支持断点续传功能，则 `BLE_QIOT_OTA_INFO_FLASH_ADDR` 宏需要配置，用于存储断点续传信息。
10. `BLE_QIOT_TOTAL_PACKAGES` 表示小程序最大连续下发数据包的数量，最大值为 `0xFF`。`BLE_QIOT_PACKAGE_LENGTH` 表示单个数据包中 OTA 数据的长度，不能超过 ` ble_get_user_data_mtu_size()` - 3，其中3表示 OTA 数据包头。`BLE_QIOT_RETRY_TIMEOUT` 表示设备端收到连续两个数据包的最大间隔，超出此时间表示数据传输超时，设备会主动请求小程序进行数据重传。`BLE_QIOT_PACKAGE_INTERVAL` 表示小程序发送连续两个数据包的间隔。`BLE_QIOT_REBOOT_TIME` 表示设备 OTA 文件传输结束后小程序等待设备升级的最大时常，超出此时间没有进行版本上报认为升级失败。这些配置开发者可以自行组合，以寻求在不同的蓝牙协议栈上最佳的升级体验。
11. `BLE_QIOT_OTA_BUF_SIZE` 是 OTA 数据设备端缓冲区的大小，为了减少写 flash 的次数和提升速度，LLSync 在收到一定数量内容后才进行一次写操作，建议配置为 flash 单个 page 的大小。
12. `BLE_QIOT_REMOTE_SET_MTU` 配置为1时，即可使能腾讯连连小程序 MTU 设置功能，腾讯连连小程序将会使用 `ble_get_user_data_mtu_size()` 接口的值重新设置 `MTU`。配置为0时，腾讯连连小程序不设置 MTU，直接使用 `ble_get_user_data_mtu_size()` 接口的值作为应用层分片大小。
13. `BLE_QIOT_SECURE_BIND` 配置为1时，即可使能安全绑定功能(需要控制台同时配置设备绑定引导)，腾讯连连请求绑定时需要设备端作出确认后才可以绑定成功。

### 例程代码抽取
SDK 已经适配 `nordic 52832` 并提供例程，存储在 `samples/nrf52832` 目录下，用户可以通过脚本将指定平台的例程代码抽取出来。
```c
iot code_extract % python3 code_extract.py nrf52832
extract code for nrf52832 start, dest dir /iot/Desktop/work_code/qcloud_iot_explorer_ble/scripts/code_extract/qcloud-iot-ble-nrf52832
extract code success
```
代码抽取完成后，请参考对应的`readme.md`进行编译，参考文档一般位于生成的代码文件夹中。

### 数据模版开发
用户需要根据实际需求，对`ble_qiot_template.c`中的函数模版做具体实现，可以参考 `ref-impl` 目录下的例程进行开发。

### API 说明
在`ble_qiot_export.h`中提供了 API 函数，一般情况下用户只需要调用 API 函数即可完成应用开发。

| 序号 |             函数             |                             说明                             |
| :--: | :--------------------------: | :----------------------------------------------------------: |
|  1   |    ble_qiot_explorer_init    |                          SDK 初始化                          |
|  2   |     ble_event_get_status     |      获取数据模版最新信息，对应数据模版 `get_status` 方法      |
|  3   |  ble_event_report_property   |          上报设备最新信息，对应数据模版 `report` 方法          |
|  4   |        ble_event_post        |            上报事件，对应数据模版 `event_post` 方法            |
|  5   |  ble_qiot_advertising_start  | 开始广播，广播包内容请参见 [LLSync 协议说明](https://github.com/tencentyun/qcloud-iot-explorer-BLE-sdk-embedded/blob/master/docs/LLSync%E8%93%9D%E7%89%99%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%85%A5%E5%8D%8F%E8%AE%AE1.4.1.pdf) |
|  6   |  ble_qiot_advertising_stop   |                           停止广播                           |
|  7   |   ble_device_info_write_cb   |            UUID FFE1 数据到达后调用此接口传入数据             |
|  8   |     ble_lldata_write_cb      |            UUID FFE2 数据到达后调用此接口传入数据             |
|  9   |      ble_gap_connect_cb      |               蓝牙设备连接时调用此接口通知 SDK                |
|  10  |    ble_gap_disconnect_cb     |                   蓝牙连接端口后调用此接口                   |
|  11  |    ble_get_qiot_services     |                 获取需要加入协议栈的蓝牙服务                 |
|  12  |       ble_ota_write_cb       |            UUID FFE4 数据到达后调用此接口传入数据             |
|  13  |     ble_ota_callback_reg     |                     注册 OTA 功能回调函数                      |
|  14  |      ble_event_sync_mtu      |                 同步蓝牙 MTU 到腾讯连连小程序                  |
|  15  | ble_secure_bind_user_confirm | 安全绑定请求达到后，用户在设备端确认或拒绝绑定调用此接口通知 SDK |

## LLSync 协议

请参见 [LLSync 协议说明](https://github.com/tencentyun/qcloud-iot-explorer-BLE-sdk-embedded/blob/master/docs/LLSync%E8%93%9D%E7%89%99%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%85%A5%E5%8D%8F%E8%AE%AE1.4.1.pdf)

## SDK 使用参考

请参见 [LLSync SDK 使用参考](https://cloud.tencent.com/document/product/1081/48399)

