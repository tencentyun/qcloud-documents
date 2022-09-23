- 初始化 HTTPDNS 和灯塔接口。
<dx-alert infotype="notice" title="">
若已接入 msdk 或者单独接入了腾讯灯塔则不用初始化灯塔。
</dx-alert> 示例如下：
```C#
 private static AndroidJavaObject sHttpDnsObj;
 public static void Init() {
 	AndroidJavaClass unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
 	if (unityPlayerClass == null) {
 		return;
 	}	
 	AndroidJavaObject activityObj = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
 	if (activityObj == null) {
 		return;
 	}
 	AndroidJavaObject contextObj = activityObj.Call<AndroidJavaObject>("getApplicationContext");
 	// 初始化 HTTPDNS
 	AndroidJavaObject httpDnsClass = new AndroidJavaObject("com.tencent.msdk.dns.MSDKDnsResolver");
 	if (httpDnsClass == null) {
 		return;
 	}
 	sHttpDnsObj = httpDnsClass.CallStatic<AndroidJavaObject>("getInstance");
 	if (sHttpDnsObj == null) {
 		return;
 	}
 	sHttpDnsObj.Call("init", contextObj, appkey, dnsid, dnskey, debug, timeout);
 }
```
- 调用 getAddrByName 接口解析域名。示例如下：
```C#
// 该操作建议在子线程中或使用 Coroutine 处理
// 注意在子线程中调用需要在调用前后做 AttachCurrentThread 和 DetachCurrentThread 处理 
public static string GetHttpDnsIP(string url) {
	string ip = string.Empty;
	AndroidJNI.AttachCurrentThread(); // 子线程中调用需要加上
	// 解析得到 IP 配置集合
	string ips = sHttpDnsObj.Call<string>("getAddrByName", url);
	AndroidJNI.DetachCurrentThread(); // 子线程中调用需要加上
	if (null != ips) {
		string[] ipArr = ips.Split(';');
        if (2 == ipArr.Length && !"0".Equals(ipArr[0]))
		ip = ipArr[0];
	}
	return ip;
}
```
