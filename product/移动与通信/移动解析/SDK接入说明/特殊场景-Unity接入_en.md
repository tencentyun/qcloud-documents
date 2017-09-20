This document describes how to connect Unity to HttpDNS

### Code for Android

First, initialize HttpDNS and lighthouse API:
> Note: If msdk is connected or Tencent lighthouse is connected separately, you don't need to initialize the lighthouse.

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
// Initialize HttpDNS
AndroidJavaObject joDnsClass = new AndroidJavaObject("com.tencent.msdk.dns.MSDKDnsResolver");
Debug.Log(" WGGetHostByName ===========" + joDnsClass);
if (joDnsClass == null)
return;
m_dnsJo = joDnsClass.CallStatic("getInstance");
Debug.Log(" WGGetHostByName ===========" + m_dnsJo);
if (m_dnsJo == null)
return;
m_dnsJo.Call("init", context);
// Initialize lighthouse
AndroidJavaObject joBeaconClass = new AndroidJavaObject("com.tencent.beacon.event.UserAction");
if (joBeaconClass == null)
return;
m_dnsJo.Call("initUserAction", context);
}
```

Call HttpDNS API to resolve domain name:
```
// It is recommended to process this operation in the sub-thread
public static string GetHttpDnsIP( string strUrl ) {
string strIp = string.Empty;
// Perform resolution process and acquire IP configuration set
strIp = m_dnsJo.Call("getAddrByName", strUrl);
Debug.Log( strIp );
if( strIp != null )
{
// Use the first one
string[] strIps = strIp.Split(';');
strIp = strIps[0];
}
return strIp;
}
```

### Code for iOS

Make API declaration in cs file:
```
#if UNITY_IOS
[DllImport("__Internal")]
private static extern string WGGetHostByName(string domain);
#endif
```

For the part that needs domain name resolution, call WGGetHostByName(string domain) method, and proceed as follows:
```
string ips = WGGetHostByName(domainStr);
string[] sArray=ips.Split(new char[] {';'});
if (sArray != null && sArray.Length > 1) {
	  if (!sArray[1].Equals("0")) {
	      //Suggestion: Use ipv6 address as first priority if it exists.
	      //ipv6 address is used to connect to TODO. Make sure that ipv6 is enclosed in [ ]. For example: http://[64:ff9b::b6fe:7475]/
	    } else {
	      //Use ipv4 address for connection
	    }
}
```

Package unity project as xcode project, and perform operations such as introducing dependent libraries, as described above.

