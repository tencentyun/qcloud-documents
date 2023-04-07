# NFCAdapter.onDiscovered(function listener)

## 功能描述

监听 NFC Tag

## 参数

### function listener

的监听函数

#### 参数

##### Object res

| 属性     | 类型  | 说明                                                         |
| :------- | :---- | :----------------------------------------------------------- |
| techs    | Array | tech 数组，用于匹配 NFC 卡片具体可以使用什么标准（NfcA等实例）处理 |
| messages | Array | NdefMessage 数组，消息格式为 {id: ArrayBuffer, type: ArrayBuffer, payload: ArrayBuffer} |