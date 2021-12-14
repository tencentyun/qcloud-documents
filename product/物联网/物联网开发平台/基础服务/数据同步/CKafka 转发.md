## 操作场景

开发者基于物联网开发平台完成设备接入与管理，往往需要实时接收设备上报的数据与上下线状态便于闭环开发某个行业的垂直解决方案。平台提供了 CKafka 转发能力，满足需要通过消息队列订阅设备上报数据与状态的场景。

## 操作步骤
1. 登录 [物联网开发平台](https://console.cloud.tencent.com/iotexplorer) ，选择项目列表。
2. 进入项目列表页面，单击左侧菜单【数据同步】，您可单击【HTTPS】与【Ckafka】进行页面切换，这里我们单击【Ckafka】。
![](https://main.qcloudimg.com/raw/7d2b3708c540736e780e3ed20ef46550.jpg)
3. 进入CKafka 配置页面，您可设置某个产品所有设备上报消息与上下线状态转发至 CKafka，单击设备列表中的【设置】，在未授权的情形下需先进行授权操作，授权成功后进行配置消息队列 CKafka 参数，单击同意授权后，再次单击【设置】，单击【创建实例】进行创建消息服务CKafka，单击【创建Topic】创建Topic。
![](https://main.qcloudimg.com/raw/90243074b1f34b88d3fb63f33549b932.jpg)
4. 选择创建好的实例 和Topic ，并单击【保存】，会弹出提示，保存并开启后，平台会立即向当前所选 CKafka 实例的主题推送消息。
![](https://main.qcloudimg.com/raw/4b968138aed96b4a9b5254397136814f.jpg)
5. 保存成功后，跳转到列表页，可开启该产品的【生效状态】，【生效状态】打开后平台将对该产品下所有设备上报的消息转发到指定 CKafka 实例中。
![](https://main.qcloudimg.com/raw/edd6ab57a69d4d03356094bf7a51d24d.jpg)
6. 如何使用 CKafka 订阅消费消息，请参考 [消息队列 CKafka](https://cloud.tencent.com/document/product/597)。

## 示例


- **设备上报消息格式**

```plaintext
{
	"MsgType": "Publish",
	"Event": "",
	"Topic": "$thing/up/property/F4N****0AN/dev1",
	"Seq": 32726,
	"PayloadLen": 250,
	"ProductId": "F4N****0AN",
	"DeviceName": "dev1",
	"Payload": "eyJtZXRob2QiOiJyZXBvcnRfaW5mbyIsICJjbGllbnRUb2tlbiI6IkY0TkE3NFYwQU4tMCIsICJwYXJhbXMiOnsibW9kdWxlX2hhcmRpbmZvIjoiRVNQODI2NiIsIm1vZHVsZV9zb2Z0aW5mbyI6IlYxLjAiLCJmd192ZXIiOiIzLjEuMCIsImltZWkiOiIxMS0yMi0zMy00NCIsImxhdCI6IjIyLjU0NjAxNSIsImxvbiI6IjExMy45NDExMjUiLCAiZGV2aWNlX2xhYmVsIjp7ImFwcGVuZF9pbmZvIjoieW91ciBzZWxmIGRlZmluZSBpbmZvIn19fQ==",
	"Time": "2020-06-08 20:03:41",
	"Reason": ""
}
```

>?Payload 是经过 base64 编码后的数据，开发者在使用之前需进行 base64 解码。

- **设备下线消息格式**

```plaintext
{
	"MsgType": "StatusChange",
	"Event": "Offline",
	"Topic": "",
	"Seq": 13895,
	"PayloadLen": 0,
	"ProductId": "F4N****0AN",
	"DeviceName": "dev1",
	"Payload": null,
	"Time": "2020-06-08 20:03:47",
	"Reason": "REASON_DEVICE_DISCONNECT"
}
```


- **设备上线消息格式**

```plaintext
{
	"MsgType": "StatusChange",
	"Event": "Online",
	"Topic": "",
	"Seq": 13870,
	"PayloadLen": 0,
	"ProductId": "F4N****0AN",
	"DeviceName": "dev1",
	"Payload": null,
	"Time": "2020-06-08 20:03:41",
	"Reason": ""
}
```


