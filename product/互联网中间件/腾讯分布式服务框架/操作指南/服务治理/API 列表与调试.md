## 操作场景
API 列表显示服务对外暴露的 API 列表。API 调试提供用户在线调试 API 的能力。
您可以在 TSF 控制台中，通过 API 列表查看 API 的详细信息，并进行 API 在线调试。

## 前提条件
要使用 API 列表和调试功能，需要先将服务的 API 注册到注册中心，具体请参考开发手册 [API 注册](https://cloud.tencent.com/document/product/649/30604)。

## 操作步骤
### API 列表
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)，在左侧导航栏中，选择【[服务治理](https://console.cloud.tencent.com/tsf/service)】。
2. 单击服务名称，进入服务详情页。
3. 在服务详情页，单击顶部的【API列表】，会显示服务对外提供的 API。
![](https://main.qcloudimg.com/raw/328d3f8bdcae038d27aac23a5f33eacd.png)
4. 单击 API 名称进入详情页，可以查看到 API 的详细信息。
API 详情按照【应用名/版本号】划分显示了 API 的详细信息，包括：路径、方法、描述、入参、出参。其中 Models 表示参数中的复杂类型。
![](https://main.qcloudimg.com/raw/a3c7492e80d624202a0d20d7ba6f1207.jpg)

### API 调试

1. 在 API 详情页，单击【调试】，进入API 调试页面。
![](https://main.qcloudimg.com/raw/9fd5e16766a052ff35ecd5ed065596ab.png)
2. 填写调用 API 的默认参数，单击【发送请求】。
![](https://main.qcloudimg.com/raw/46ab294adb80f8787aaa0aadec277373.png)
3. 右侧会展示调用 API 的返回结果。
![](https://main.qcloudimg.com/raw/e44f9f0de84c20b4af2606e87933125b.png)
