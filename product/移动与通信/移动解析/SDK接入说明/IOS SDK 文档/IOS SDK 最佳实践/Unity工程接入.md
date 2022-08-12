
## 操作步骤

1. 将 HTTPDNSUnityDemo/Assets/Plugins/Scripts 下的 **HttpDns.cs** 文件拷贝到 Unity 对应 Assets/Plugins/Scripts 路径下。
2. 在需要进行域名解析的部分，调用 HttpDns.GetAddrByName(string domain) 或者 HttpDns.GetAddrByNameAsync(string domain) 方法。
	- 如使用同步接口 **HttpDns.GetAddrByName**，直接调用接口即可。
	- 如果使用异步接口 **HttpDns.GetAddrByNameAsync**，还需设置回调函数 **onDnsNotify(string ipString)**，函数名可自定义。
	 并建议添加如下处理代码：
``` 
string[] sArray=ipString.Split(new char[] {';'}); 
if (sArray != null && sArray.Length > 1) {
	if (!sArray[1].Equals("0")) {
		//使用建议：当 IPv6 地址存在时，优先使用 IPv6 地址
		//TODO 使用 IPv6 地址进行 URL 连接时，注意格式，需加方框号[ ]进行处理，例如：http://[64:ff9b::b6fe:7475]/
	} else if(!sArray [0].Equals ("0")) {
		//使 IPv4 地址进行连接
	} else {
		//异常情况返回为0,0，建议重试一次
		HttpDns.GetAddrByName(domainStr);
	}
}
```
3. 将 unity 工程打包为 xcode 工程后，引入所需依赖库。
4. 将 HTTPDNSUnityDemo 下的 MSDKDnsUnityManager.h 及 MSDKDnsUnityManager.mm 文件导入到工程中，注意以下地方需要与 Unity 中对应的 GameObject 名称及回调函数名称一致。如下图所示：
![](https://main.qcloudimg.com/raw/f9a10fb9306f73cfd99c6dde705fc956.jpg)
![](https://main.qcloudimg.com/raw/5e34886a01bb50d17df72be53db03984.jpg)

