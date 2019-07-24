用于实现人脸验证 H5 结果返回跳转第三方 URL 带唯一标识、订单号、验证结果、签名。
## 请求
**请求 URL：**`https://xxx.com/xxx?code=xxxx&orderNo=xxxx&h5faceId=xxxx&newSignature=xxxx`
**请求方法：**GET
>!
>- `xxxx.com`为合作方上送的 URL。
- 合作方根据[ 方式一：前端获取结果验证签名 ](https://cloud.tencent.com/document/product/1007/35897)或者 [方式二：服务端查询结果](https://cloud.tencent.com/document/product/1007/35898) 说明进行签名校验，确保返回结果的安全性。

## 响应
**响应参数：**

|参数	|说明	|类型	|长度（字节）|
|-|-|-|-|
|code	|人脸验证结果的返回码，0表示人脸验证成功，其他错误码标识失败。	|String	|-|
|orderNo	|订单号 ，由合作方上送，每次唯一，此信息为本次人脸验证上送的信息。|	String|	32|
|h5faceId	|本次请求返回的唯一标识，此信息为本次人脸验证上送的信息。|	String|	32|
|newSignature|	对 URL 参数 AppID、orderNo 和 SIGN ticket、code 的签名|String|	40|


详情请参见 [签名算法说明](https://cloud.tencent.com/document/product/655/31969)。	
