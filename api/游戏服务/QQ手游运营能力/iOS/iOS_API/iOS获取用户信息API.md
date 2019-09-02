

## 功能描述
开发者可以通过调用 API 获取 用户的个人信息。

获取用户信息分为两个步骤：
1. 发送获取用户信息的请求
```
// _tencentOAuth为TencentOAuth类的实例
[_tencentOAuth getUserInfo])
```
2. 实现协议 TencentSessionDelegate 的获取到用户信息后的回调方法

```
//可以通过response获取数据的返回结果
- (void)getUserInfoResponse:(APIResponse*) response;
```

## 方法原型

```
/**
 * 获取用户个人信息
 * \return 处理结果，YES表示API调用成功，NO表示API调用失败，登录态失败，重新登录
 */
- (BOOL)getUserInfo;

```

## 实际示例

```
- (void)getUserInfoResponse:(APIResponse*) response {
if (URLREQUEST_SUCCEED == response.retCode 
&& kOpenSDKErrorSuccess == response.detailRetCode) {
NSMutableString *str = [NSMutableString stringWithFormat:@""];
    for (id key in response.jsonResponse) {
[str appendString: [NSString stringWithFormat: 
@"%@:%@\n", key, [response.jsonResponse objectForKey:key]]];
    }
UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"操作成功"
message: [NSString stringWithFormat:@"%@",str];
    delegate:self cancelButtonTitle:@"我知道啦" otherButtonTitles: nil];
[alert show];
} else {
NSString *errMsg = [NSString stringWithFormat:@"errorMsg:%@\n%@",
response.errorMsg, [response.jsonResponse objectForKey:@"msg"]];
UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"操作失败"
message:errMsg
delegate:self
cancelButtonTitle:@"我知道啦"
otherButtonTitles: nil];
[alert show];
}
}
```
