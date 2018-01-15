## 1. Feature Overview

Tencent Cloud MSDKDns is mainly used to effectively avoid inaccessibility to the best access point caused by ISP's traditional resolution through LocalDNS. It is designed to replace traditional DNS protocol with HTTP encryption protocol, and the domain name is not used across the entire resolution process, therefore greatly lowering the possibility of hijacking.

Acquire MSDKDns for Android SDK in the following way:

[Acquire the latest SDK version from Github >>](https://github.com/tencentyun/httpdns-android-sdk)
[Click to download Android SDK >>](https://mc.qcloudimg.com/static/archive/86d55ba36f96092a82b20c762a5dce59/httpdns-android-sdk-master.zip)

Note:
If the business on the client is bound with host, for example, HTTP service bound with host or CDN service, you still need to specify the Host field of HTTP header after replacing the domain name in URL with the returned IP from HttpDNS. Take curl for example. If you want to visit www.qq.com, and the IP resolved through HttpDNS is 192.168.0.111, then you can call the API using `curl -H "Host:www.qq.com" http://192.168.0.111/aaa.txt`.

Glossary:
DNS_KEY, DNS_ID: When you activate HttpDNS, ID and KEY are assigned to the corresponding business. Both ID and KEY are bound with the product and cannot be modified. They are required when you use HttpDNS via API. For more information, please see API calling guide.

## 2. Accessing

### 2.1. AndroidMainfest Configuration
```
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<!-- Add lighthouse appkey of the App, such as 0I000LT6GW1YGCP7-->
<meta-data
    android:name="APPKEY_DENGTA"
    android:value="XXXXXXXXXXXXXXXX" />
<!-- DNS receives the broadcast of network switching -->
<receiver
    android:name="com.tencent.msdk.dns.HttpDnsCache$ConnectivityChangeReceiver"
    android:label="NetworkConnection" >
    <intent-filter>
        <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
    </intent-filter>
</receiver>
```

Note: The value of `android:  value`, i.e. appkey, is in key_android.txt file of version package provided to you. Please make modifications based on the content of this file. If the permission in AndroidMainfest already exists, you do not need to add it again.

### 2.2. Connect to HttpDns Library
Copy the library file `HttpDnsDemo\libs\msdkhttpdns_xxxx.jar` to the corresponding location in App libs.
Copy the configuration file `HttpDnsDemo\assets\dnsconfig.ini` to the directory "Android\assets" of App.

Before copying `dnsconfig.ini` file, you need to modify relevant configurations in this file, but do not change the original encoding method of the file. Details are as follows:

| Item | Field | Method|
|-------|---------|---------|
| Vendor switch |	IS_COOPERATOR | Enter "true" for external App |
| External vendor test switch | IS_COOPERATOR_TEST | Enter "true" if you need to use test environment for testing, or "false" if you want to use release environment directly (the official demo is used for test environment, so you don't need to apply for ID and KEY. However, you have to apply for your own ID and KEY for the official release) |
| AppID for vendor report | COOPERATOR_APPID | It is assigned by system after registration |
| SDK log switch | IS_DEBUG | "true" means to enable the log, and "false" means to disable the log. In the test phase, we recommend that you enable log for troubleshooting. You can disable it after official launch |
| ID assigned by server | DNS_ID | It is assigned by system after registration |
| KEY assigned by server | DNS_KEY | It is assigned by system after registration |

### 2.3. Connect to Dependent Library
> Note: Check whether the App has been connected to Tencent msdk. If so, you can ignore this step.

Copy `HttpDnsDemo\libs\ beacon_android_v1.9.4.jar` to the corresponding location in game libs.

### 2.4. Call the API HttpDNS Java
```
/**
* Initialize HttpDns
* @param context Pass Application Context
*/
MSDKDnsResolver.getInstance().init(MainActivity.this.getApplicationContext());

/**
* Initialize lighthouse
* Note: If App has been connected to Tencent msdk and msdk has been initialized, you don't need to re-initialize the lighthouse
* @param this Pass main Activity or Application Context
*/
UserAction.initUserAction(MainActivity.this. getApplicationContext ());

/**
* HttpDNS synchronous resolution API
* Note: "domain" can only be specified with domain name, but not IP. Check whether domain name exists before the result is returned.
* First, you need to query cache. Return the result if it exists. Send request for synchronous domain name resolution if it does not exist.
* Return the latest resolution result if the resolution is successful, or null object if failed
* @param domain Domain name (for example, www.qq.com)
* @return Resolved IP result set of domain name
*/

String ips = MSDKDnsResolver.getInstance(). getAddrByName(domain);
```

## 3. Note

3.1. Client uses proxy
When client uses the proxy, the result of resolution through HttpDNS is used to determine the location of the user based on the proxy IP. The returned result may be different from the one when accessing directly with the user IP.

3.2. It is recommended to call HttpDNS synchronous API in the sub-thread. Timeout management is made available for the API getAddrByName (domain). The timeout value is configured in dnsconfig.ini by App. Default value is 1 second (TIME_OUT=1000).

3.3. If you want to use the lighthouse to report content, you can directly call the lighthouse API for reporting after connecting to HttpDNS. For example:
```
Map map = new HashMap();
map.put("resultKey", "resultValue");
UserAction.onUserAction("WGGetHostByNameResult", true, -1, -1, map, true);
```

## 4. Offline Inquiry
If you have any other questions, please submit a ticket.

