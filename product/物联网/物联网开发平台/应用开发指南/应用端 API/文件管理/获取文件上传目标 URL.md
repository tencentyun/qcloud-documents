
## 1. 接口描述

接口请求域名：`iot.cloud.tencent.com/api/exploreropen/tokenapi`。
本接口（AppGetResourceUploadURL）用于获取在小程序或 App 上上传文件的 URL。

## 2. 输入参数

| 名称             | 类型   | 必选 | 描述                                                         |
| ---------------- | ------ | ---- | ------------------------------------------------------------ |
| AccessToken      | String | 是   | 公共参数，用户通过微信号、手机或邮箱账号登录成功后，获取的访问 Token |
| RequestId        | String | 是   | 公共参数，唯一请求 ID，可自行生成，推荐使用 uuId。定位问题时，需提供该次请求的 RequestId |
| Action           | String | 是   | 公共参数，本接口取值：AppGetResourceUploadURL                |
| ProductId        | String | 是   | 产品 ID                                                      |
| UserResourceName | String | 是   | 用户要上传的文件标识名称                                     |
| FileSize         | Int    | 是   | 文件字节大小                                                 |
| ResourceVer      | String | 是   | 文件的版本                                                   |

## 3. 输出参数

| 名称         | 类型   | 描述                             |
| ------------ | ------ | -------------------------------- |
| RequestId    | String | 公共参数，唯一请求 ID，与入参相同 |
| UploadUrl    | String | 上传的 URL                       |
| ResourceName | String | 文件名称                         |

## 4. 示例

**输入示例**
<dx-codeblock>
:::  HTTP
POST https://iot.cloud.tencent.com/api/exploreropen/tokenapi HTTP/1.1
content-type: application/json
 {
   "AccessToken": "8b4a70dd16105f******************18edd4e78a3bb8ec"
   "RequestId": "1p****z1N",
   "Action": "AppGetResourceUploadURL",
   "ProductId":"22F****I7O",
   "UserResourceName":"restest", 
   "FileSize":5179,
   "ResourceVer":"0.0.1",
 }
:::
</dx-codeblock>


**输出示例:  成功**
<dx-codeblock>
:::  JSON
 {
	  "Response":
		{
		   "RequestId": "1p****z1N",
		   "UploadUrl":"https://gz-g-resource-1256872341.cos.ap-guangzhou.myqcloud.com/res%2F96666666666_BKTTNGIQOG_USER_72375312314273792_RES_restest_0.0.1?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDMUM9hdmn35rHZe72Y6UfliNo1PYQFZln%26q-sign-time%3D1620729273%3B1620732873%26q-key-time%3D1620729273%3B1620732873%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De1e31a1c14a738d1e790f92a158d4fea7f1135e7",	  	
        "ResourceName":"USER_72375312314273792_RES_restest",
     }
}
:::
</dx-codeblock>



## 5. 错误码

| 错误码                                   | 描述         |
| ---------------------------------------- | ------------ |
| InternalError                            | 内部错误     |
| InvalidParameterValue                    | 参数取值错误 |
| InvalidParameterValue.InvalidAccessToken | Token 无效    |

