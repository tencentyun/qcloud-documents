### 1. 功能介绍

腾讯云智营解析SDK MSDKDns的主要功能是为了有效的避免由于运营商传统LocalDns解析导致的无法访问最佳接入点的方案。原理为使用Http加密协议替代传统的DNS协议，整个过程不使用域名，大大减少劫持的可能性。

您可以通过以下方式获取智营解析 iOS SDK：

[从 Github 访问 >>](https://github.com/tencentyun/httpdns-ios-sdk)

注意：
如果客户端的业务是与host绑定的，比如是绑定了host的http服务或者是cdn的服务，那么在用HTTPDNS返回的IP替换掉URL中的域名以后，还需要指定下Http头的Host字段。
以curl为例，假设你要访问www.qq.com，通过HTTPDNS解析出来的IP为192.168.0.111，那么通过这个方式来调用即可：`curl -H "Host:www.qq.com" http://192.168.0.111/aaa.txt`

名词解释：
DNS_KEY，DNS_ID，开通使用httpdns时，会分配对应业务的ID和KEY，ID和KEY是与产品绑定的，不能修改，通过接口使用httpdns时，需要提供ID与KEY，具体参照接口调用手册

### 2. 安装包结构
压缩文件中包含demo工程，其中包含：

- MSDKDns.framework：适用“Build Setting->C++ Language Dialect”配置为GNU++98，“Build Setting->C++ Standard Library”为“libstdc++(GNU C++ standard library)”的工程。
- MSDKDns_C11.framework：适用于该两项配置分别为“GNU++11”和“libc++(LLVM C++ standard library with C++11 support)”的工程。

### 3. 接入步骤

#### 3.1 引入依赖库
**已接入MSDK的应用**：MSDKDns依赖MSDK2.14.0i及其以上版本，接入MSDKDns之前必须接入MSDKFoundation.framework、MSDK.framework；

**未接入MSDK的应用**：在接入MSDKDns之前必须引入以下依赖库
1. Demo中的BeaconAPI_Base.framework
2. 系统公共库：
	-	libz.tdb
	- libsqlite3.tdb
	-	libstdc++.tdb
	- libstdc++.6.0.9.tdb
	- libc++.tdb
	- Foundation.framework
	- CoreTelephony.framework
	- SystemConfiguration.framework
	-	CoreGraphics.framework
	- Security.framework

并在`application:didFinishLaunchingWithOptions:`加入注册灯塔代码
```
//已正常接入MSDK的游戏无需关注以下代码，未接入MSDK的外部APP调用以下代码注册灯塔
//******************************
NSString *plistPath = [[NSBundle mainBundle] pathForResource:@"Info" ofType:@"plist"];
NSDictionary *dic = [NSDictionary dictionaryWithContentsOfFile:plistPath];
NSString *appid = dic[@"COOPERATOR_APPID"];
[BeaconBaseInterface setAppKey:appid];
[BeaconBaseInterface enableAnalytics:@"" gatewayIP:nil];
//******************************
```
注意：需要在Other linker flag里加入`-ObjC`标志。

#### 3.2 引入MSDKDns

#### 3.3 配置文件
在`info.plist`中配置允许http声明，具体配置如下：

| Key | Type | Value |
|---------|---------|---------|
| IS_COOPERATOR| Boolean| 外部应用填“YES”|
| COOPERATOR_APPID| String| 注册后由系统或管理员分配提供|
| TIME_OUT| Number| 请求httpdns超时设定时间，单位：ms，建议设置1000ms|
| DNS_ID| String| 注册后由系统或管理员分配提供|
| DNS_KEY| String| 注册后由系统或管理员分配提供|
| Debug| Boolean| 日志开关配置，YES为打开MSDKDns日志，No为关闭MSDKDns日志，建议在接入测试阶段打开日志，以便排查问题，上线后可以关闭
| IS_TEST| Boolean| 测试开关配置，当选择YES，即是指使用官方提供的demo进行测试，无需申请ID与KEY，如需正式接入，需要注册申请ID与KEY，当您的项目有了自己的ID与KEY后，此选项设置为空

### 4. API及使用示例

#### 4.1 获取IP: WGGetHostByName
引入头文件，调用WGGetHostByName接口会返回IP数组：
```
/**
 *  @param domain 域名
 *  @return 查询到的IP数组，返回长度为2的数组，其中第一个值为解析到的ipv4地址；第二个值为解析到的ipv6地址，如不存在，则为0
 *  注意：超时（1s）或者未查询到返回空数组
 */
std::vector<unsigned char*> WGGetHostByName(unsigned char* domain);
```

接口调用示例：
```
std::vector<unsigned char*> ipsVector = MSDKDns::GetInstance()->WGGetHostByName((unsigned char *)"www.qq.com");
if (ipsVector.size() > 1){
    NSString* ipv4 = [NSString stringWithUTF8String:(const char*)result[0]];
    NSString* ipv6 = [NSString stringWithUTF8String:(const char*)result[1]];
    if (![ipv6 isEqualToString:@"0"]) {
        //使用建议：当ipv6地址存在时，优先使用ipv6地址
        //TODO 使用ipv6地址进行连接，注意格式，ipv6需加方框号[ ]进行处理，例如：http://[64:ff9b::b6fe:7475]/
    } else {
       //使用ipv4地址进行连接
    }
}
```
>注意：
>使用ipv6地址进行连接时，注意格式，ipv6需加方框号[ ]进行处理，例如：`http://[64:ff9b::b6fe:7475]/*******`
>使用建议：
>1、ipv6为0，直接使用ipv4地址连接
>2、ipv6地址不为0，优先使用ipv6连接，如果ipv6连接失败，再使用ipv4地址进行连接，注：返回给业务的地址格式为："dns=ipv4,ipv6"，如果没有ipv6地址，返回为0，例如:dns=192.168.1.1,0

#### 4.2 控制台日志: WGOpenMSDKDnsLog

游戏可以通过开关控制是否打印MSDKDns相关的Log，注意和MSDKLog区分。
```
/**
 *
 *  @param enabled true:打开 false:关闭
 */
void WGOpenMSDKDnsLog(bool enabled);
```

接口调用示例：
```
MSDKDns::GetInstance()->WGOpenMSDKDnsLog(true);
```

### 5. 注意事项

1. 如发现编译时报错: "string file not found"，将调用WGGetHostByName接口的.m文件，后缀名改为.mm即可。

2. 异常情况下，httpdns可能会解析失败：
表现形式为：WGGetHostByName接口返回为空
解决方案：业务再次请求一次WGGetHostByName即可，或者走业务原本的解析逻辑。

3. 针对iOS 9以上版本，请关闭 ATS（Application Transport Secure）特性。即在info.plist中添加如下配置项：
```
<key>NSAppTransportSecurity</key>
<dict>
	    <key>NSAllowsArbitraryLoads</key>
	    <true/>
</dict>
```

### 6. 线下咨询
如有其他问题可按以下方式联系咨询：
QQ：584258402 2202081228
邮箱：porsche@tencent.com
