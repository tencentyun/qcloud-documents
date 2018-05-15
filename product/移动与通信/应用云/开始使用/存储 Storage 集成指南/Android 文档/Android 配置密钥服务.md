Storage SDK 需要一个有效的密钥提供者，这样后台才能正确地识别您的身份。所以在调用 SDK 任何功能接口前，**请先通过 `TACStorageOptions` 设置密钥提供者**。

下面的示例代码假设您配置的服务器请求地址是:

```
GET https://<SERVER_HOST><PATH>?<name>=<value>
Header: <header1>=<value1>
```

设置方式取决于请求响应体的 JSON 结构。

### 1.（推荐）使用服务器 SDK 返回的标准 JSON 结构

通过 `TACStorageOptions` 配置密钥获取接口：

```
TACApplicationOptions applicationOptions = TACApplication.options();
TACStorageOptions storageOptions = applicationOptions.sub("storage");

// 配置密钥获取接口
storageOptions.setCredentialProvider(new HttpRequest.Builder<String>()
	.scheme("https")					
	.host("<SERVER_HOST>")			
	.path("<PATH>")					
	.method("GET")
	.query("<name>", "<value>")		
	.addHeader("<header1>", "<value1>")	
	.build());
```

### 2. 自定义 JSON 结构

通过 `TACStorageOptions` 配置密钥获取接口和 响应处理类，其中处理类必须继承于 `SessionCredentialProvider`:

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

在自定义的响应处理类中，实现 `onRemoteCredentialReceived ` 方法，返回一个 `SessionQCloudCredentials` 实例：

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

