该文档说明 Unity 如何接入 HTTPDNS。

## Android 部分代码

先初始化 HTTPDNS 和灯塔接口：
> ?若已接入 msdk 或者单独接入了腾讯灯塔则不用初始化灯塔。

```
private static AndroidJavaObject m_dnsJo;
private static AndroidJavaClass sGSDKPlatformClass;
public static void Init() {
AndroidJavaClass jc = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
if (jc == null)
return;
AndroidJavaObject joactivety = jc.GetStatic("currentActivity");
if (joactivety == null)
return;
AndroidJavaObject context = joactivety.Call("getApplicationContext");
// 初始化HTTPDNS
AndroidJavaObject joDnsClass = new AndroidJavaObject("com.tencent.msdk.dns.MSDKDnsResolver");
Debug.Log(" WGGetHostByName ===========" + joDnsClass);
if (joDnsClass == null)
return;
m_dnsJo = joDnsClass.CallStatic("getInstance");
Debug.Log(" WGGetHostByName ===========" + m_dnsJo);
if (m_dnsJo == null)
return;
m_dnsJo.Call("init", context);
// 初始化灯塔
AndroidJavaObject joBeaconClass = new AndroidJavaObject("com.tencent.beacon.event.UserAction");
if (joBeaconClass == null)
return;
m_dnsJo.Call("initUserAction", context);
}
```

再调用 HTTPDNS 接口解析域名：
```
// 该操作建议在子线程中处理
public static string GetHttpDnsIP( string strUrl ) {
string strIp = string.Empty;
// 解析得到IP配置集合
strIp = m_dnsJo.Call("getAddrByName", strUrl);
Debug.Log( strIp );
if( strIp != null )
{
// 取第一个
string[] strIps = strIp.Split(';');
strIp = strIps[0];
}
return strIp;
}
```

## iOS 部分代码

在 cs 文件中进行接口声明：
```
#if UNITY_IOS
[DllImport("__Internal")]
private static extern string WGGetHostByName(string domain);
#endif
```

在需要进行域名解析的部分，调用 WGGetHostByName(string domain) 方法，并建议进行如下处理：
```
string ips = WGGetHostByName(string domain);
string[] sArray=ips.Split(new char[] {';'});
if (sArray != null && sArray.Length > 1) {
	  if (!sArray[1].Equals("0")) {
	      //使用建议：当ipv6地址存在时，优先使用ipv6地址
	      //TODO 使用ipv6地址进行连接，注意格式，ipv6需加方框号[ ]进行处理，例如：http://[64:ff9b::b6fe:7475]/
	    } else {
	      //使用ipv4地址进行连接
	    }
}
```

将 unity 工程打包为 xcode 工程，并按如上说明，引入依赖库等操作即可。



