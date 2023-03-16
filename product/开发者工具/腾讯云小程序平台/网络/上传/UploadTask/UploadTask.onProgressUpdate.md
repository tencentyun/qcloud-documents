# UploadTask.onProgressUpdate(function callback)

- 功能描述

监听上传进度变化事件

- 参数

**function callback**

上传进度变化事件的回调函数

参数

**Object res**

| 属性                     | 类型   | 说明                                 |
| :----------------------- | :----- | :----------------------------------- |
| progress                 | number | 上传进度百分比                       |
| totalBytesSent           | number | 已经上传的数据长度，单位 Bytes       |
| totalBytesExpectedToSend | number | 预期需要上传的数据总长度，单位 Bytes |