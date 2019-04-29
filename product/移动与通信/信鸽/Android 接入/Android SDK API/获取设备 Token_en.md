Token is the unique identifier used by XGPush for maintaining a persistent connection with the backend. It is the only ID to identify the connection, and can only be obtained after the device is successfully registered. The token can be obtained using the following methods (the token of XGPush may change when the App is uninstalled and reinstalled).

### Using the registration API with callback
In the onSuccess(Object data, int flag) method of the registration API with XGIOperateCallback, the parameter "data" is a token. For more information, please see the examples of registration API.

### Overloading XGPushBaseReceiver
Overload the onRegisterResult (Context context, int errorCode, XGPushRegisterResult registerMessage) method of XGPushBaseReceiver, and obtain the token via the API getToken provided by the parameter registerMessage. For more information, please see "[Obtaining Registration Result](https://cloud.tencent.com/document/product/548/13951#.E8.8E.B7.E5.8F.96.E6.B3.A8.E5.86.8C.E7.BB.93.E6.9E.9C)".

### XGPushConfig.getToken(context)
After the device is registered successfully, the token is stored locally and can be obtained via the API XGPushConfig.getToken(context).

