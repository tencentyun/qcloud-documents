

## 操作场景

CLAA 设备广泛应用于智能楼宇、智能工业、农业和环境等场景。您只需要在腾讯物联网通信产品中进行简单的操作，并将 CLAA 通信相关信息配置到 CLAA 终端，即可在云平台中管理您的设备。本文档主要指导您如何创建 CLAA 产品。
![数据流程](https://main.qcloudimg.com/raw/80b0ef26615188d70426bd21f39e251b.png)



## 操作步骤
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，单击左侧菜单栏【产品列表】。
2. 进入产品列表页面，单击【创建新产品】。
3. 按界面提示填写相关信息。
 - 所属地区：广州。
 - 节点类型：物联网通信只能添加 CLAA 设备，CLAA 网关暂不支持添加。
 - 产品类型：选择 CLAA 产品。
 - 产品名称：为产品命名，产品名称在账号内具有唯一性。
 - AppEUI：应用 ID。
 - 数据格式：自定义或者 JSON 格式。
 - 产品描述：自定义，最多不超过500个字符。
![](https://main.qcloudimg.com/raw/417dbd272d915306760e12b7e095196a.png)
4. 信息填写完成后，单击【确定】，即可完成创建产品。
5. 创建成功后，在产品列表中，单击【管理】即可查看产品的基本信息。
6. 选择【产品列表】>【设备列表】，单击【添加新设备】。
7. 按界面提示填写相关信息。
 - 设备名称：设备名称在同一个产品下，设备名称需要保证唯一性。
 - 设备备注：选填，给设备增加备注。
 - DevEUI：设备在入网前即可获取，请找设备厂家提供，入网时设备将 DevEUI 上传，且服务器会将此 DevEUI 注册并返回一个 DevAddr，入网后 DevAddr 为设备的唯一身份标识。
 - 设备类型：支持 Class A/B/C/D/E 。
 - AppKey：设备在入网前即可获取，请找设备厂家提供，用于通讯密钥的参数加密。
 ![](https://main.qcloudimg.com/raw/26d8eef19e00e57e46a7cee79c528eb1.png)
8. 信息填写完成后，单击【保存】，即可完成添加设备。

## 后续步骤
1. 终端上电激活，上电后设备发送入网请求，服务器侧响应入网请求，下发通讯密钥参数，终端接收并解密通讯密钥，终端入网成功。
2. 单击设备列表中，入网成功之后设备的状态变为已激活，单击【管理】可查询设备详情。

通过如上配置，就可以连接在深圳地区使用腾讯铺设的 CLAA 网络。

