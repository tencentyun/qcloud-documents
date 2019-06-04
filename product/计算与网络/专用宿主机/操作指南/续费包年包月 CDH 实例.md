您可以通过控制台或者 API 对包年包月的专用宿主机实例进行续费。

## 通过 CDH 控制台续费包年包月 CDH 实例
1. 登录 [专用宿主机控制台](https://console.cloud.tencent.com/cvm/cdh)。
2. 选择相应的地域，勾选需要修改续费的专用宿主机实例，单击【续费】。
![列表页续费](https://main.qcloudimg.com/raw/197e0fe5044ff9798e8c8eeaa2d67b1e.png)
3. 在续费弹窗中，选择需要续费的时间，单击【确定】。
![列表页续费弹窗](https://main.qcloudimg.com/raw/ce69bc227b4c27a4beb1cc5c3c232134.png)
4. 进行支付后则完成了对 CDH 实例的续费操作。

## 通过续费管理页续费包年包月 CDH 实例
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com)。
2. 进入【费用中心】>【续费管理】页面，产品类别选择专用宿主机，选择相应的地域，勾选需要修改续费的专用宿主机实例，单击【续费】。
![续费管理页](https://main.qcloudimg.com/raw/614e5d734c1107ebb3404da1a9e9807f.png)
3. 在续费弹窗中，选择需要续费的时间，单击【确认】。
![续费管理页弹窗](https://main.qcloudimg.com/raw/d56ef02f5615e83bfe9c7982ffdcbf1e.png)
4. 进行支付后则完成了对 CDH 实例的续费操作。

### 续费管理页设置自动续费包年包月 CDH 实例
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com)。
2. 进入【费用中心】>【续费管理】页面，产品类别选择专用宿主机，选择相应的地域，勾选需要修改续费的专用宿主机实例，单击【设为自动续费】。
3.在自动续费弹窗中，单击【确认】，账户余额充足的情况下，系统将在到期当日为您进行自动续费。
![自动续费](	https://main.qcloudimg.com/raw/fa9b94b28ba9c026a736ee26b8f14916.png)

## 使用 API 续费包年包月 CDH 实例
使用 ModifyHostsAttribute 接口将专用宿主机实例设置为自动续费，具体用法详见[修改 CDH 实例的属性 API](https://cloud.tencent.com/document/api/213/16475)。