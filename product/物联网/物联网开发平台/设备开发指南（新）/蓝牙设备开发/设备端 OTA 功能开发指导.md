
## 配置 OTA 功能

1. 打开您工程下的 `ble_qiot_config.h` 文件，找到 `BLE_QIOT_SUPPORT_OTA` 宏，设置为1开启 OTA 功能。
   ```
   #define BLE_QIOT_SUPPORT_OTA 1
   ```
2. 修改当前软件的版本号，内容格式不限，用户可根据自己的需求任意设置，长度在1至32字节以内，不得包含除 `a-zA-Z0-9.-_` 以外的字符，固件版本号必须与控制台保持一致，详情可参见 [固件升级](https://cloud.tencent.com/document/product/1081/40296)。
   ```
   #define BLE_QIOT_USER_DEVELOPER_VERSION "0.0.1"
   ```
3. 您可以按需要设置是否开启断点续传功能，`BLE_QIOT_SUPPORT_RESUMING` 设置为1开启断点续传功能，如使用断点续传功能请同时设置 `BLE_QIOT_OTA_INFO_FLASH_ADDR`，该地址用于在 flash 中保存断点续传信息，至少需要64字节。
   ```
   #define BLE_QIOT_SUPPORT_RESUMING 1
   #if (1 == BLE_QIOT_SUPPORT_RESUMING)
   #define BLE_QIOT_OTA_INFO_FLASH_ADDR (BLE_QIOT_RECORD_FLASH_ADDR + 0x1000)
   #endif
   ```
4. OTA 升级过程中小程序连续下发最大数据包数量，不得超过255字节，可根据实际情况修改。
   ```
   #define BLE_QIOT_TOTAL_PACKAGES 0xFF
   ```
5. 每个 OTA 数据包长度，用户可根据设备所支持的 MTU 大小进行修改，但不得超过 "mtu - 3"，适当加大该数值一定程度上提升 OTA 升级的速度。
   ```
   #define BLE_QIOT_PACKAGE_LENGTH 0x10
   ```
6. 两个数据包之间超时间隔，单位：秒，用户可根据实际情况进行修改。
   ```
   #define BLE_QIOT_RETRY_TIMEOUT  2
   ```
7. OTA 升级重启等待时间，单位：秒，在此时间内小程序将持续尝试连接设备，超时后小程序认为升级失败，如果固件较大或设备升级流程较长可适当加长重启等待时间。
   ```
   #define BLE_QIOT_REBOOT_TIME    20
   ```
8. 小程序下发两个数据包之间的时间间隔，单位：毫秒，可适当修改以提升 OTA 升级速度。
   ```
   #define BLE_QIOT_PACKAGE_INTERVAL 0x05
   ```
9. 小程序发送的 OTA 数据将暂存在这个 buffer 中，buffer 满后会写入 flash 指定地址，用户可根据设备 RAM 空间进行修改，建议与 flash 的 page 大小相等或为其整数倍。
   ```
   #define BLE_QIOT_OTA_BUF_SIZE (4096)
   ```
	 
## OTA 相关接口适配
- 查看 `qcloud_iot_explorer_ble\inc\ble_qiot_import.h` 文件，用户需要实现以下几个接口。
	1. SDK 调用该接口将版本号传给用户，用户可以按照自己的规则检查版本号是否合法、是否高于上一个版本等，通过返回值通知 SDK 是否允许 OTA 升级。
		 ```
		 uint8_t ble_ota_is_enable(const char *version);
		 ```
	2. SDK 通过此接口获取 OTA 数据在 flash 中的保存地址，用户只需提供基址，在 OTA 升级过程中 SDK 会自动在基址的基础上计算偏移。
		 ```
		 uint32_t ble_ota_get_download_addr(void);
		 ```
	3. 用户提供写入 OTA 数据的接口，存储介质不限，可以是片内 ROM 或片外 flash 等。SDK 只负责写入数据，需用户自己在适当的时间进行擦除、磨损平衡等处理。
		 ```
		 int ble_ota_write_flash(uint32_t flash_addr, const char *write_buf, uint16_t write_len);
		 ```
	 
- 查看 `qcloud_iot_explorer_ble\inc\ble_qiot_export.h` 文件，用户需要实现以下几个回调函数。

	1. 用于通知用户 OTA 升级开始。
		 ```
		 typedef void (*ble_ota_start_callback)(void);
		 ```
	2. 用于通知用户 OTA 升级结束并返回结果，例如成功、CRC 校验错误、文件错误等。用户可以根据返回结果做进一步处理，例如返回成功则重启设备，通过 boot 程序将保存在外部 flash 的 OTA  固件写入片内进行升级；返回错误则擦除已经下载的 OTA 固件等。
		 ```
		 typedef void (*ble_ota_stop_callback)(uint8_t result);
		 ```
	3. SDK 在接收完 OTA 数据并通过 CRC 校验后会调用该函数，用户可以在该函数内对固件做进一步校验，例如固件是否正确、是否为定制固件等，最终 OTA 升级的结果会通过 `ble_ota_stop_callback()` 告知用户。
		 ```
		 typedef ble_qiot_ret_status_t (*ble_ota_valid_file_callback)(uint32_t file_size, char *file_version);
		 ```
	4. 用户在自己工程代码合适的位置调用该接口，将以上回调函数注册至 SDK。
		 ```
		 void ble_ota_callback_reg(ble_ota_start_callback start_cb, ble_ota_stop_callback stop_cb,ble_ota_valid_file_callback valid_file_cb);
		 ```

## 上传固件

详情请参见 [固件升级](https://cloud.tencent.com/document/product/1081/40296)，按操作步骤上传固件。

>!因为蓝牙升级时需要腾讯连连小程序与设备保持连接，因此【升级确认】方式只有【用户确认升级】这一种。
![](https://main.qcloudimg.com/raw/eb6a5c0b52c1ffa6e2e447da924052dd.png)

## 小程序操作

1. 打开【腾讯连连】小程序，点击需要升级的设备。
2. 蓝牙连接成功后点击左上角的“省略号”。
3. 点击【固件升级】，点击【立即升级】。
4. 小程序会自动下载固件并升级，升级过程会持续若干分钟（若设备支持断点续传功能小程序会自动继续升级）。
5. 升级完成后等待设备自动重启并连接，再次查看固件版本号，可看到新版本升级成功。  
   ![](https://main.qcloudimg.com/raw/77f7ef8b33d2c2143fc96c26b5f34f36.gif)
