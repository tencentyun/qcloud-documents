Token 是信鸽保持与后台长连接的唯一身份标识，是识别连接的唯一 ID，只有设备注册成功后才能获取 token，可以有以下方法获取（信鸽的 token 在应用卸载重新安装的时候有可能会变）。

### 通过带 callback 的注册接口获取
带 XGIOperateCallback 的注册接口的 onSuccess（Object data, int flag）方法中，参数 data 便是 token，具体可参考注册接口的相关示例。

### 重载 XGPushBaseReceiver
重载 XGPushBaseReceiver 的 onRegisterResult（Context context, int errorCode, XGPushRegisterResult registerMessage）方法，通过参数 registerMessage 提供的 getToken 接口获取，具体可参考 “[获取注册结果](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E7%A7%BB%E5%8A%A8%E4%B8%8E%E9%80%9A%E4%BF%A1/%E4%BF%A1%E9%B8%BD/Android%20%E6%8E%A5%E5%85%A5/Android%20SDK%20API/%E5%90%AF%E5%8A%A8%E4%B8%8E%E6%B3%A8%E5%86%8C.md#获取注册结果)” 章节。

### XGPushConfig.getToken(context)
当设备一旦注册成功后，便会将 token 存储在本地，之后可通过 XGPushConfig.getToken(context) 接口获取。
