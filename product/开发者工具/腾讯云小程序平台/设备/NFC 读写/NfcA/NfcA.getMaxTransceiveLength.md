# NfcA.getMaxTransceiveLength(Object object)

> **微信 iOS 版**：不支持
>
> **微信 Android 版**：支持

## 功能描述

获取最大传输长度

## 参数

### Object object

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性   | 类型   | 说明         |
| :----- | :----- | :----------- |
| length | number | 最大传输长度 |

## 错误

| 错误码 | 错误信息                        | 说明                                 |
| :----- | :------------------------------ | :----------------------------------- |
| 13000  | 设备不支持NFC                   |                                      |
| 13001  | 系统 NFC 开关未打开             |                                      |
| 13010  | 未知错误                        |                                      |
| 13019  | user is not authorized          | 用户未授权                           |
| 13011  | invalid parameter               | 参数无效                             |
| 13012  | parse NdefMessage failed        | 将参数解析为 NdefMessage 失败        |
| 13021  | NFC discovery already started   | 已经开始 NFC 扫描                    |
| 13018  | NFC discovery has not started   | 尝试在未开始 NFC 扫描时停止 NFC 扫描 |
| 13022  | Tech already connected          | 标签已经连接                         |
| 13023  | Tech has not connected          | 尝试在未连接标签时断开连接           |
| 13013  | NFC tag has not been discovered | 未扫描到 NFC 标签                    |
| 13014  | invalid tech                    | 无效的标签技术                       |
| 13015  | unavailable tech                | 从标签上获取对应技术失败             |
| 13024  | function not support            | 当前标签技术不支持该功能             |
| 13017  | system internal error           | 相关读写操作失败                     |
| 13016  | connect fail                    | 连接失败                             |