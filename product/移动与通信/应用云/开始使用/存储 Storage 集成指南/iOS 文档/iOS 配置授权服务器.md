使用 Storage 服务时，后台需要对您的身份进行校验，校验过程是通过调用接口时携带签名实现的。因此，Storage SDK 需要提前设置临时密钥才能正常的访问数据。临时密钥有一定的有效期，过期后自动失效。由于临时密钥需要永久密钥生成，而永久密钥放在客户端中有极大的泄露风险，因此建议通过后台生成临时密钥，并下发到客户端中。

在调用 Storage 任何功能接口与前，都需要设置 [TACStorageService defaultStorage].credentailFenceQueue.delegate  ，并且实现 `QCloudCredentailFenceQueueDelegate` 协议来提供相关的权限信息。

> 可以在 [对象存储控制台](https://console.cloud.tencent.com/cos4/secret) 上面获取密钥，也就是 SecretID 与 SecretKey。

在签名接口的回调里，其实需要做的就是使用 SecretID，SecretKey （使用临时密钥服务的情况下，还有 token 和 ExpirationDate）传给 QCloudCredential 实例，然后通过该实例来生成一个签名 Creator，再调用 continueBlock 把签名 Creator 传进去即可。请参考下面的例子。


## 临时密钥使用指南

假设您已经按照 [快速搭建后台授权服务](https://cloud.tencent.com/document/product/666/17922) 搭好了授权服务器，并且服务器直接将 CAM 返回的 JSON 数据透传给客户端。（如果是其它格式的数据，那么需要自定义解析过程）。


这里假设请求临时密钥的接口是：
```
GET https://<SERVER_HOST><PATH>?<name>=<value>
Header: <header1>=<value1>
```

然后，返回的数据是一个标准的 JSON 格式：

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


那么我们需要做的是构造一个 HTTP 请求，去获取临时密钥，并对返回的数据进行解析，请参考下面的代码：

```
- (void) fenceQueue:(QCloudCredentailFenceQueue *)queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock {

  // 开始构造一个 NSURLHTTPRequest 进行网络请求
  //请求的 URL
  NSURL* URL = [NSURL URLWithString:@"https://<SERVER_HOST><PATH>?<name>=<value>"];
  NSMutableURLRequest* urlrequest = [[NSMutableURLRequest alloc] initWithURL:URL];
  //请求的方法，前面我们假设了是 GET
  [urlrequest setHTTPMethod:@"GET"];
  //如果需要设置头部 Header
  [urlrequest setValue:@"<value1>" forHTTPHeaderField:@"<header1>"];
  [[[NSURLSession sharedSession] dataTaskWithRequest:urlrequest completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
    //请求返回 200，成功
     if (((NSHTTPURLResponse*)response).statusCode == 200) {
       //将 JSON 转为 NSDictionary* 类型的对象
       NSDictionary* result = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableLeaves error:nil];

       //构造生成签名的 Creator
       QCloudCredential* crendential = [[QCloudCredential alloc] init];
       //如果是前面假设的返回的JSON格式，那么可以按照这么解析，否则需要自行从字典中找到对应的参数。
        crendential.secretID = [result valueForKeyPath:@"data.credentials.tmpSecretId"];
       crendential.secretKey = [result valueForKeyPath:@"data.credentials.tmpSecretKey"];
       crendential.experationDate = [result valueForKeyPath:@"data.expiredTime"];
       crendential.token = [result valueForKeyPath:@"data.credentials.sessionToken"];
       QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:crendential];
       continueBlock(creator, nil);
     }
  }] resume];
}
```


## 使用永久密钥进行上传（强烈不建议在线上环境使用）    

在调试时可以使用永久密钥进行上传，使用 SecretID, SecretKey生成 QCloudCredential 实例后，再生成一个 QCloudAuthentationV5Creator 实例进行调用 continueBlock 即可。建议仅仅在调试阶段使用，** 不建议线上环境使用 **。



Objective-C 代码示例：
~~~
@interface TACStorageDemoViewController () <QCloudCredentailFenceQueueDelegate>
@end

@implementation  TACStorageDemoViewController

- (void)viewDidLoad {
  [super viewDidLoad];
  //设置提供签名的对象,该对象需要实现QCloudCredentailFenceQueueDelegate 协议
  [TACStorageService defaultStorage].credentailFenceQueue.delegate = self;
}

- (void) fenceQueue:(QCloudCredentailFenceQueue *)queue requestCreatorWithContinue:(QCloudCredentailFenceQueueContinue)continueBlock
{
    QCloudCredential* crendential = [[QCloudCredential alloc] init];

    // 在调试阶段您可以通过直接设置secretID和secretKey来测试服务，但是强烈不建议在线上环境使用该方式！！！
    QCloudCredential* crendential = [[QCloudCredential alloc] init];
    crendential.secretID = <#secretID#>;
    crendential.secretKey = <#secretKey#>;
    QCloudAuthentationV5Creator* creator = [[QCloudAuthentationV5Creator alloc] initWithCredential:crendential];
    continueBlock(creator, nil);
}
@end
~~~

Swift 代码示例：
~~~
class TACStorageDemoViewController: UIViewController ,QCloudCredentailFenceQueueDelegate{
    func fenceQueue(_ queue: QCloudCredentailFenceQueue!, requestCreatorWithContinue continueBlock: QCloudCredentailFenceQueueContinue!) {
    // 在调试阶段您可以通过直接设置secretID和secretKey来测试服务，但是强烈不建议在线上环境使用该方式！！！
        let crendential = QCloudCredential.init()
        crendential.secretID = <#secretID#>
        crendential.secretKey = <#secretKey#>
        let creator = QCloudAuthentationV5Creator.init(credential: crendential)
        continueBlock(creator,nil)

    }
~~~
