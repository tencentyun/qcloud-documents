### 1. Feature Overview

Tencent Cloud MSDKDns is mainly used to effectively avoid inaccessibility to the best access point caused by ISP's traditional resolution through LocalDNS. It is designed to replace traditional DNS protocol with HTTP encryption protocol, and the domain name is not used across the entire resolution process, therefore greatly lowering the possibility of hijacking.

Acquire MSDKDns for iOS SDK in the following way:

[Acquire the latest SDK version from Github >>](https://github.com/tencentyun/httpdns-ios-sdk)
[Click to download iOS SDK >>](https://mc.qcloudimg.com/static/archive/9381e78fd2f0c26f3532b67a7579ff59/httpdns-ios-sdk-master.zip)

Note:
If the business on the client is bound with host, for example, HTTP service bound with host or CDN service, you still need to specify the Host field of HTTP header after replacing the domain name in URL with the returned IP from HttpDNS.
Take curl for example. If you want to visit www.qq.com, and the IP resolved through HttpDNS is 192.168.0.111, then you can call the API using `curl -H "Host:www.qq.com" http://192.168.0.111/aaa.txt`.

Glossary:
DNS_KEY, DNS_ID: When you activate HttpDNS, ID and KEY are assigned to the corresponding business. Both ID and KEY are bound with the product and cannot be modified. They are required when you use HttpDNS via API. For more information, please see API calling guide.

### 2. Composition of Installation Package
The compressed file has a demo project, which contains:

- MSDKDns.framework: Used for the project, whose "Build Setting->C++ Language Dialect" is GNU++98 and "Build Setting->C++ Standard Library" is "libstdc++(GNU C++ standard library)".
- MSDKDns_C11.framework: Used for the project, whose "Build Setting->C++ Language Dialect" is GNU++11 and "Build Setting->C++ Standard Library" is "libc++(LLVM C++ standard library with C++11 support)".

### 3. Connection Procedure

### 3.1. Introduce Dependent Libraries
**App already connected to MSDK**: Since MSDKDns relies on MSDK2.14.0i and above, connection to MSDKFoundation.framework and MSDK.framework must be completed before connecting to MSDKDns;

**App not connected to MSDK**: The following dependent libraries must be introduced before connecting to MSDKDns
1. BeaconAPI_Base.framework of Demo
2. Common system libraries:
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

Add the code for registering lighthouse in `application:didFinishLaunchingWithOptions:`
```
//Ignore the following code for the games properly connected to MSDK. Call the following code to register the lighthouse for external App that is not connected to MSDK
//******************************
NSString *plistPath = [[NSBundle mainBundle] pathForResource:@"Info" ofType:@"plist"];
NSDictionary *dic = [NSDictionary dictionaryWithContentsOfFile:plistPath];
NSString *appid = dic[@"COOPERATOR_APPID"];
[BeaconBaseInterface setAppKey:appid];
[BeaconBaseInterface enableAnalytics:@"" gatewayIP:nil];
//******************************
```
Note: You need to add `-ObjC` flag in "other linker flag".

#### 3.2 Introduce MSDKDns

### 3.3. File Configuration
Configure the declaration that allows HTTP request in "info.plist". The detailed configurations are as follows:

| Key | Type | Value |
|---------|---------|---------|
| IS_COOPERATOR | Boolean | Enter "YES" for external App |
| COOPERATOR_APPID| String| It is assigned by system after registration |
| TIME_OUT | Number | Set the timeout for requesting HttpDNS (in ms). 1,000 ms is recommended |
| DNS_ID | String | It is assigned by system after registration |
| DNS_KEY | String | It is assigned by system after registration |
| Debug | Boolean| Log switch configuration. "YES" means to enable MSDKDns log, and "No" means to disable it. In the test phase, we recommend that you enable log for troubleshooting. You can disable it after official launch
| IS_TEST | Boolean | Test switch configuration. "YES" means to use demo provided officially for testing, so you don't need to apply for ID and KEY. For an official connection, both ID and KEY are required. After ID and key are assigned to your project, the parameter can be left empty

### 4. API and Examples

#### 4.1 Acquire IP:  WGGetHostByName
Introduce the header file, call the API WGGetHostByName, and then the IP array is returned:
```
/**
 *  @param domain Domain name
 *  @return The queried IP array. The array with a length of 2 is returned, where the first value is the resolved ipv4 address and the second one is the ipv6 address. If no value exists, 0 is returned.
 *  Note: In case of timeout (1s) or if no value is found, an empty array is returned.
 */
std::vector<unsigned char*> WGGetHostByName(unsigned char* domain);
```

Example of API call
```
std::vector<unsigned char*> ipsVector = MSDKDns::GetInstance()->WGGetHostByName((unsigned char *)"www.qq.com");
if (ipsVector.size() > 1){
    NSString* ipv4 = [NSString stringWithUTF8String:(const char*)result[0]];
    NSString* ipv6 = [NSString stringWithUTF8String:(const char*)result[1]];
    if (![ipv6 isEqualToString:@"0"]) {
        //Suggestion: Use ipv6 address as first priority if it exists.
        //ipv6 address is used to connect to TODO. Make sure that ipv6 is enclosed in [ ]. For example: http://[64:ff9b::b6fe:7475]/
    } else {
       //Use ipv4 address for connection
    }
}
```
>Note:
//When ipv6 address is used for connection, make sure that ipv6 is enclosed in [ ]. For example: `http://[64:ff9b::b6fe:7475]/*******`
>Suggestions:
>1. If ipv6 is 0, use ipv4 address directly for connection
>2. If ipv6 address is not 0, it is preferred for connection. If it fails, use ipv4 address. Note: The format of address returned to business is "dns=ipv4,ipv6". If ipv6 address does not exist, 0 is returned, for example, dns=192.168.1.1,0

#### 4.2 Console Log:  WGOpenMSDKDnsLog

For games, you can control whether to print MSDKDns-related Log using switch. Pay attention to the difference between Log and MSDKLog.
```
/**
 *
 *  @param enabled True: Enable; False: Disable
 */
void WGOpenMSDKDnsLog(bool enabled);
```

Example of API call
```
MSDKDns::GetInstance()->WGOpenMSDKDnsLog(true);
```

### 5. Note

1. If an error: "string file not found" is returned during compilation, call ".m" file of the API WGGetHostByName, and change its suffix to ".mm".

2. In case of an exception, resolution through HttpDNS may fail:
Cause: Null is returned from the API WGGetHostByName
Solution: Business sends the request for calling API WGGetHostByName again, or uses the original resolution logic.

3. For versions above iOS 9, disable ATS (Application Transport Secure) feature. That is, add the following configuration items to info.plist:
```
<key>NSAppTransportSecurity</key>
<dict>
	    <key>NSAllowsArbitraryLoads</key>
	    <true/>
</dict>
```

## 6. Offline Inquiry
If you have any other questions, please submit a ticket.

