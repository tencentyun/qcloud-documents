使用 Storage 服务时，后台需要对您的身份进行校验，校验过程是通过调用接口时携带签名实现的。因此，Storage SDK 需要提前设置临时密钥才能正常的访问数据。临时密钥有一定的有效期，过期后自动失效。由于临时密钥需要永久密钥生成，而永久密钥放在客户端中有极大的泄露风险，因此建议通过后台生成临时密钥，并下发到客户端中。

假设您已经按照 [快速搭建后台授权服务](https://cloud.tencent.com/document/product/666/17922) 搭好了授权服务器，服务器的请求地址如下：

```
GET https://<SERVER_HOST><PATH>?<name>=<value>
Header: <header1>=<value1>
```

我们的 SDK 会在本地临时密钥不存在或者过期的时候，自动请求您设置的服务器接口，拿到新的临时密钥。请通过 `TACStorageOptions` 设置服务器接口地址。


## SDK 设置授权服务器地址

设置方式取决于服务器返回的 JSON 数据的格式。

### 标准格式

JSON 是标准的临时密钥格式，即

```
{
    "code":0,"message":"","codeDesc":"Success",
    "data":
    {
        "credentials":
        {
            "sessionToken":"42f8151428b3960b1226f421b8f271c6242ad02c3",
            "tmpSecretId":"AKIDtd9QSGWBIDuMaYFp57tSmrhJgohLtvpT",
            "tmpSecretKey":"ZfV5PVLvFLCvPefPt76qKYXIo56tSmrg"
        },
        "expiredTime":1508400619
    }
}
```

那么，您可以以下方式设置，不需要手动解析 JSON：

```
TACApplicationOptions applicationOptions = TACApplication.options();
TACStorageOptions storageOptions = applicationOptions.sub("storage");

// 配置授权服务器接口
storageOptions.setCredentialProvider(new HttpRequest.Builder<String>()
	.scheme("https")					
	.host("<SERVER_HOST>")			
	.path("<PATH>")					
	.method("GET")
	.query("<name>", "<value>")		
	.addHeader("<header1>", "<value1>")	
	.build());
```

### 自定义格式

JSON 是自定义格式，您可以通过如下代码配置服务器接口和响应处理类，其中处理类必须继承于 `SessionCredentialProvider`:

```
TACApplicationOptions applicationOptions = TACApplication.options();
TACStorageOptions storageOptions = applicationOptions.sub("storage");

// 配置自定义的响应处理类，MySessionCredentialProvider 继承于 SessionCredentialProvider
// 在 MySessionCredentialProvider 中设置密钥获取接口
storageOptions.setCredentialProvider(new MySessionCredentialProvider(new HttpRequest.Builder<String>()
	.scheme("https")					
	.host("<SERVER_HOST>")			
	.path("<PATH>")					
	.method("GET")
	.query("<name>", "<value>")		
	.addHeader("<header1>", "<value1>")	
	.build()));
```

在响应处理类中，实现 `onRemoteCredentialReceived ` 方法，返回一个 `SessionQCloudCredentials` 实例：

```
public class MySessionCredentialProvider extends SessionCredentialProvider {
        public MySessionCredentialProvider(HttpRequest<String> httpRequest) {
            super(httpRequest);
        }

        @Override
        protected QCloudLifecycleCredentials onRemoteCredentialReceived(String jsonContent) throws QCloudClientException {
        	// 在这里处理 jsonContent，并返回一个有效的密钥实例
        	...
        	return new SessionQCloudCredentials(secretId, secretKey, sessionToken, expiredTime);
        }
    }
```

实例化 `SessionQCloudCredentials` 需要的几个参数说明如下：

* secretId: 临时密钥 secret id
* secretKey: 临时密钥 secret key
* sessionToken: 临时密钥 token
* expiredTime: 密钥过期时间

