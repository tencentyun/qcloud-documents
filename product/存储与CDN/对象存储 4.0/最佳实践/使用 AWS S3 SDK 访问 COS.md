## 使用 AWS S3 SDK 访问 COS

COS 提供了S3 兼容的 API，因此当您的数据从 S3 迁移到 COS 之后，只需要做简单的修改，就可以让你原来的客户端应用轻松兼容 COS 服务。本文主要介绍不同平台的 S3 SDK 的适配步骤。在添加适配步骤之后，您就可以使用 S3 SDK 的接口来访问 COS 上的文件了。

### 准备工作

1. 您已经注册了腾讯云账号，并且从 [腾讯云控制台](https://console.cloud.tencent.com/cam/capi) 上面获取密钥 SecretID 与 SecretKey。
2. 您已经有一个集成了 S3 SDK，并能正常工作的客户端应用。


### Android

下面以 `AWS Android SDK` 2.14.2 版本为例，介绍如何使用访问 COS 服务。

#### 初始化实例时设置 临时密钥提供者 和 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

```
AmazonS3Client s3 = new AmazonS3Client(new AWSCredentialsProvider() {
    @Override
    public AWSCredentials getCredentials() {
    	 // 这里后台请求 STS 得到临时密钥信息
        return new BasicSessionCredentials(
        		"<TempSecretID>", "<TempSecretKey>", "<STSSessionToken>"
        );
    }

    @Override
    public void refresh() {
        //
    }
});

s3.setEndpoint("cos.ap-guangzhou.myqcloud.com"); 
```


### iOS

下面以 `AWS iOS SDK` 2.10.2 版本为例，介绍如何使用访问 COS 服务。

#### 1. 实现 AWSCredentialsProvider 协议

```
-(AWSTask<AWSCredentials *> *)credentials{
	// 这里后台请求 STS 得到临时密钥信息
    AWSCredentials *credential = [[AWSCredentials alloc]initWithAccessKey:@"<TempSecretID>" secretKey:@"<TempSecretKey>" sessionKey:@"<STSSessionToken>" expiration:[NSDate dateWithTimeIntervalSince1970:1565770577]];
    
    return [AWSTask taskWithResult:credential];
    
}

- (void)invalidateCachedTemporaryCredentials{
    
}
```

#### 2. 提供 临时密钥提供者 和 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

```
NSURL* bucketURL = [NSURL URLWithString:@"http://cos.ap-guangzhou.myqcloud.com"];
    
AWSEndpoint* endpoint = [[AWSEndpoint alloc] initWithRegion:AWSRegionUnknown service:AWSServiceS3 URL:bucketURL];
AWSServiceConfiguration* configuration = [[AWSServiceConfiguration alloc] 
	initWithRegion:AWSRegionUSEast2 endpoint:endpoint 
	credentialsProvider:[MyCredentialProvider new]]; // MyCredentialProvider 实现了 AWSCredentialsProvider 协议
   
[[AWSServiceManager defaultServiceManager] setDefaultServiceConfiguration:configuration];
```

### JavaScript

下面以 `AWS JS SDK` 2.509.0 版本为例，介绍如何使用访问 COS 服务。

#### 初始化实例时设置 腾讯云密钥 和 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

```
var AWS = require('aws-sdk');

AWS.config.update({
    accessKeyId: "<腾讯云的 Secret ID>",
    secretAccessKey: "<腾讯云的 Secret Key>",
    region: "ap-guangzhou",
    endpoint: 'https://cos.{region}.myqcloud.com',
});

s3 = new AWS.S3({apiVersion: '2006-03-01'});
```

### Java

下面以 `AWS Java SDK` 1.11.609 版本为例，介绍如何使用 AWS JAVA SDK 访问 COS 服务。

#### 1. 修改 AWS 配置和证书文件

AWS SDK 的默认配置文件通常在用户目录下，可以参考 [配置和证书文件](https://docs.aws.amazon.com/zh_cn/cli/latest/userguide/cli-configure-files.html)。

在配置文件（以 Linux 为例，文件位置是 `~/.aws/config`） 中添加以下配置：
  
```
[default]  
s3 =  
addressing_style = virtual 
```
 
在证书文件（以 Linux 为例，文件位置是 `~/.aws/credentials`）中配置腾讯云的密钥：  

```
[default]  
aws_access_key_id = [腾讯云的 Secret ID]  
aws_secret_access_key = [腾讯云的 Secret Key] 
```

#### 2.代码中设置 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

```
AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
    .withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration(
    		"http://cos.ap-guangzhou.myqcloud.com", 
    		"ap-guangzhou"))
    .build();
```

### Python

下面以 `AWS Python SDK` 1.9.205 版本为例，介绍如何访问 COS 服务。

#### 1. 修改 AWS 配置和证书文件

AWS SDK 的默认配置文件通常在用户目录下，可以参考 [配置和证书文件](https://docs.aws.amazon.com/zh_cn/cli/latest/userguide/cli-configure-files.html)。

在配置文件（以 Linux 为例，文件位置是 `~/.aws/config`） 中添加以下配置：
  
```
[default]  
s3 =  
addressing_style = virtual 
```
 
在证书文件（以 Linux 为例，文件位置是 `~/.aws/credentials`）中配置腾讯云的密钥：  

```
[default]  
aws_access_key_id = [腾讯云的 Secret ID]  
aws_secret_access_key = [腾讯云的 Secret Key] 
```

#### 2.代码中设置 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

```
client = boto3.client('s3', endpoint_url='"https://cos.ap-guangzhou.myqcloud.com"')
```

### PHP

下面以 `AWS PHP SDK` 3.109.3 版本为例，介绍如何使用访问 COS 服务。

#### 1. 修改 AWS 配置和证书文件

AWS SDK 的默认配置文件通常在用户目录下，可以参考 [配置和证书文件](https://docs.aws.amazon.com/zh_cn/cli/latest/userguide/cli-configure-files.html)。

在配置文件（以 Linux 为例，文件位置是 `~/.aws/config`） 中添加以下配置：
  
```
[default]  
s3 =  
addressing_style = virtual 
```
 
在证书文件（以 Linux 为例，文件位置是 `~/.aws/credentials`）中配置腾讯云的密钥：  

```
[default]  
aws_access_key_id = [腾讯云的 Secret ID]  
aws_secret_access_key = [腾讯云的 Secret Key] 
```

#### 2.代码中设置 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

```
$S3Client = new S3Client([
  'region'          => 'ap-guangzhou',
  'version'         => '2006-03-01',
  'endpoint'        => 'https://cos.ap-guangzhou.myqcloud.com'
]);
```


### .NET

下面以 `AWS .NET SDK` 3.3.104.12 版本为例，介绍如何使用访问 COS 服务。

#### 初始化实例时设置 腾讯云密钥 和 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

```
string sAccessKeyId = "<腾讯云的 Secret ID>";
string sAccessKeySecret = "<腾讯云的 Secret Key>";
string region = "ap-guangzhou";
  
var config = new AmazonS3Config() { ServiceURL = "https://cos." + region + ".myqcloud.com" };
var client = new AmazonS3Client(sAccessKeyId, sAccessKeySecret, config);
```

### Go

下面以 `AWS Go SDK` 1.21.9 版本为例，介绍如何使用访问 COS 服务。

#### 1. 根据密钥创建session

以 Bucket 所在地域是 `ap-guangzhou` 为例：

``` golang
func newSession() (*session.Session, error) {
	creds := credentials.NewStaticCredentials("<腾讯云的 Secret ID>", "<腾讯云的 Secret Key>", "")
	region := "ap-guangzhou"
	endpoint := "http://cos.ap-guangzhou.myqcloud.com"
	config := &aws.Config{
		Region:           aws.String(region),
		Endpoint:         &endpoint,
		S3ForcePathStyle: aws.Bool(true),
		Credentials:      creds,
		// DisableSSL:       &disableSSL,
	}
	return session.NewSession(config)
}
```

#### 2. 根据session创建server发起请求

``` golang
sess, _ := newSession()
service := s3.New(sess)

// 以上传文件为例
fp, _ := os.Open("s3_test.go")
defer fp.Close()

ctx, cancel := context.WithTimeout(context.Background(), time.Duration(30)*time.Second)
defer cancel()

service.PutObjectWithContext(ctx, &s3.PutObjectInput{
	Bucket: aws.String("alangz-1250000000"),
	Key:    aws.String("test/s3_test.go"),
	Body:   fp,
})
```


### C++

下面以 `AWS C++ SDK` 1.7.68 版本为例，介绍如何使用访问 COS 服务。

#### 1. 修改 AWS 配置和证书文件

AWS SDK 的默认配置文件通常在用户目录下，可以参考 [配置和证书文件](https://docs.aws.amazon.com/zh_cn/cli/latest/userguide/cli-configure-files.html)。

在配置文件（以 Linux 为例，文件位置是 `~/.aws/config`） 中添加以下配置：
  
```
[default]  
s3 =  
addressing_style = virtual 
```
 
在证书文件（以 Linux 为例，文件位置是 `~/.aws/credentials`）中配置腾讯云的密钥：  

```
[default]  
aws_access_key_id = [腾讯云的 Secret ID]  
aws_secret_access_key = [腾讯云的 Secret Key] 
```

#### 2.代码中设置 Endpoint

以 Bucket 所在地域是 `ap-guangzhou` 为例：

``` cpp
Aws::Client::ClientConfiguration awsCC;
awsCC.scheme = Aws::Http::Scheme::HTTP;
awsCC.region = "ap-guangzhou";
awsCC.endpointOverride = "cos.ap-guangzhou.myqcloud.com"; 
Aws::S3::S3Client s3_client(awsCC);
```