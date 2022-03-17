认证结束后，认证结果页会回调启动 H5 人脸核身入参中指定的回调 url 地址。并带有 code、orderNo、h5faceId、newSignature 参数。

如果您只需要获取核身结果，您可以根据我们刷脸完成后的回调 url 请求中的参数中的 code 判断是否核身通过，code 0 表示人脸核身成功，其他错误码表示失败。如果您需要拉取人脸核身的视频和图片用于存证等其他需要，请参看查询核身结果。（您可以在收到完成刷脸的回调后，再来我们的服务器获取到刷脸视频和照片）


**请求 URL**：`https://xxx.com/xxx?code=xxxx&orderNo=xxxx&h5faceId=xxxx&newSignature=xxxx`
>! xxx.com 为启动 H5 人脸核身入参中指定的回调 url 地址。
>
**请求方法**：GET
**参数**：

|参数|	说明	|类型|	长度（字节）|
|---|---|---|--|
|code	|人脸核身结果的返回码，0 表示人脸核身成功，其他错误码标识失败。|	String	|-|
|orderNo	|订单号 ，由合作方上送，每次唯一，此信息为本次人脸核身上送的信息。	|String	|32|
|h5faceId	|本次请求返回的唯一标识，此信息为本次人脸核身上送的信息。|	String	|32|
|newSignature	|对 URL 参数 App ID、orderNo 和 SIGN ticket、code 的签名。详细签名验证步骤见下面说明步骤	|String|	40|
