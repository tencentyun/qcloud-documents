## 1. 功能介绍

腾讯云智营解析SDK MSDKDns 的主要功能是为了有效的避免由于运营商传统LocalDns解析导致的无法访问最佳接入点的方案。原理为使用Http加密协议替代传统的DNS协议，整个过程不使用域名，大大减少劫持的可能性。

您可以通过以下方式获取智营解析 Android SDK：

[从 Github 访问 >>](https://github.com/tencentyun/httpdns-android-sdk)
[点击下载 Android SDK >>](https://mc.qcloudimg.com/static/archive/bb98fef0f1ce611e5fb04aeb01f7eeab/httpdns-android-sdk-master.zip)

注意：
如果客户端的业务是与host绑定的，比如是绑定了host的http服务或者是cdn的服务，那么在用HttpDNS返回的IP替换掉URL中的域名以后，还需要指定下Http头的Host字段。以curl为例，假设你要访问www.qq.com，通过HttpDNS解析出来的IP为192.168.0.111，那么通过这个方式来调用即可：`curl -H "Host:www.qq.com" http://192.168.0.111/aaa.txt`

名词解释：
DNS_KEY，DNS_ID，开通使用httpdns时，会分配对应业务的ID和KEY，ID和KEY是与产品绑定的，不能修改，通过接口使用httpdns时，需要提供ID与KEY，具体参照接口调用手册

## 2. 接入

### 2.1. AndroidMainfest配置
```
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<!-- 添加应用自身的灯塔appkey，如0I000LT6GW1YGCP7-->
<meta-data
    android:name="APPKEY_DENGTA"
    android:value="XXXXXXXXXXXXXXXX" />
<!-- DNS接收网络切换广播 -->
<receiver
    android:name="com.tencent.msdk.dns.HttpDnsCache$ConnectivityChangeReceiver"
    android:label="NetworkConnection" >
    <intent-filter>
        <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
    </intent-filter>
</receiver>
```

注意：`android: value`的值在提供的版本包key_android.txt文件中，即appkey，请按照此文件中的内容修改，AndroidMainfest中的权限如果已经存在不需要重复添加。

### 2.2. 接入HttpDns库
将`HttpDnsDemo\libs\msdkhttpdns_xxxx.jar`库文件拷贝至应用libs相应的位置；
将`HttpDnsDemo\assets\dnsconfig.ini`配置文件拷贝到应用Android\assets目录下；

拷贝`dnsconfig.ini`文件前，先修改此文件里的相关配置，但不要改变文件原有的编码格式，具体修改方法如下：

| 修改项 | 修改字段 | 修改方法|
|-------|---------|---------|
|厂商开关 |	IS_COOPERATOR | 外部应用填"true" |
|外部厂商测试开关 | IS_COOPERATOR_TEST | 如果需要使用测试环境来测试则填"true"，直接使用正式环境填"false" （测试环境将会使用官方提供的demo，无需申请ID与KEY，正式使用时需要申请自己的ID与KEY）|
|厂商上报appID | COOPERATOR_APPID | 注册后由系统或管理员分配|
|SDK日志开关 | IS_DEBUG | true为打开日志开关，false为关闭日志，在测试阶段建议打开日志，以便排查问题，正式上线后可以关闭|
|服务端分配的ID | DNS_ID | 注册后由系统或管理员分配|
|服务端分配的KEY | DNS_KEY | 注册后由系统或管理员分配|

### 2.3. 接入依赖库
> 注意：检查应用是否接入过已经接入了腾讯msdk，如果已经接入了腾讯msdk则忽略此步。

将`HttpDnsDemo\libs\ beacon_android_v1.9.4.jar`拷贝至游戏libs相应的位置。

### 2.4. HttpDns Java接口调用
```
/**
* 初始化HttpDns
* @param context 传入Application Context
*/
MSDKDnsResolver.getInstance().init(MainActivity.this.getApplicationContext());

/**
* 初始化灯塔
* 注意：如果已接入腾讯msdk并且初始化了msdk，则不用再次初始化灯塔
* @param this 传入主Activity或者Application Context
*/
UserAction.initUserAction(MainActivity.this. getApplicationContext ());

/**
* HttpDns同步解析接口
* 注意：domain只能传入域名不能传入IP，返回结果需要做非空判断
* 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求，
* 解析完成返回最新解析结果，若解析失败返回空对象
* @param domain 域名(如www.qq.com)
* @return 域名对应的解析IP结果集合
*/

String ips = MSDKDnsResolver.getInstance(). getAddrByName(domain);
```

## 3. 注意事项

1. 客户端使用代理
当客户端使用代理时HttpDns解析的结果就变成了根据代理的IP来判断用户的所在的依据，从而可能会返回和直接用用户IP访问时的不同的结果。

2. 建议调用HttpDns同步接口时最好在子线程调用，getAddrByName(domain)接口做了超时管理，超时时间由应用自己在dnsconfig.ini文件中配置，默认超时时间为1秒(TIME_OUT=1000)。

3. 若想自己使用灯塔上报内容，在接入HttpDns后可以直接调用灯塔接口上报，例如：
```
Map map = new HashMap();
map.put("resultKey", "resultValue");
UserAction.onUserAction("WGGetHostByNameResult", true, -1, -1, map, true);
```

## 4. 线下咨询
如有其他问题可提交工单咨询。
