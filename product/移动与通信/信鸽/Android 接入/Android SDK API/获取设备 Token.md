Token 是信鸽保持与后台长连接的唯一身份标识，是识别连接的唯一 ID，只有设备注册成功后才能获取 token，可以有以下方法获取（信鸽的 token 在应用卸载重新安装的时候有可能会变）。

### 通过带 callback 的注册接口获取
带 XGIOperateCallback 的注册接口的 onSuccess（Object data, int flag）方法中，参数 data 便是 token，具体可参考注册接口的相关示例。

### 重载 XGPushBaseReceiver
重载 XGPushBaseReceiver 的 onRegisterResult（Context context, int errorCode, XGPushRegisterResult registerMessage）方法，通过参数 registerMessage 提供的 getToken 接口获取，具体可参考 “[获取注册结果](https://cloud.tencent.com/document/product/548/13951#.E8.8E.B7.E5.8F.96.E6.B3.A8.E5.86.8C.E7.BB.93.E6.9E.9C)” 章节。

### XGPushConfig.getToken(context)
当设备一旦注册成功后，便会将 token 存储在本地，之后可通过 XGPushConfig.getToken(context) 接口获取。
