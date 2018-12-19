# 获取设备推送 token


注册成功后，会返回设备 token，token 用于标识设备唯一性，同时也是 Messaging 服务维持与后台连接的唯一身份标识。在 Android SDK 中，您可以在接入 Messaging 服务时，通过重写注册的 `TACMessagingReceiver` 子类的 `onRegisterResult()` 方法来获取 token。

```

public class MyReceiver extends TACMessagingReceiver {

    // 启动 Messaging 服务后，会自动向 Messaging 后台注册，注册完成后会回调此接口。
    @Override
    public void onRegisterResult(Context context, int errorCode, TACMessagingToken tacMessagingToken) {

        if (tacMessagingToken != null) {
            String token = tacMessagingToken.getTokenString(); // 获取推送 token
        }
    }
    
    ...
}


```
> 接入 Messaging 服务请参考 [这里](https://cloud.tencent.com/document/product/666/14323)


