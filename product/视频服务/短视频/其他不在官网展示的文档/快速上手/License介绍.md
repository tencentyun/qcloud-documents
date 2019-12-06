### 1 License的申请与查看

短视频SDK的License随点播套餐包赠送，相关的信息均在[点播控制台](https://console.cloud.tencent.com/vod/license)中。

1. 登录腾讯云官网，进入 [点播控制台](https://console.cloud.tencent.com/vod/license)，填写相应的信息，在 Package Name 中填写 Android 的包名，Bundle Id 中填写 iOS 的 bundleId。

   **注意: 在购买正式license前会再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请进行修改。**

   ![](https://main.qcloudimg.com/raw/148ea8cee25d6faea2d90bac30685d1c.png)

2. 创建成功后页面会显示生成的 license 信息，这里需要记下 Key 和 LicenseUrl，在SDK的初始化时需要传入这两个参数。

   ![](https://main.qcloudimg.com/raw/e45994fd46982632ad4e29469e67f64f.png)

3. License 版本与 SDK 版本的对应使用关系如下：
    &#10004; 表示可以使用，&#10005;表示不可使用

	<table>
<thead>
<tr><th></th><th>精简版SDK（UGC_Smart）</th><th>基础版SDK（UGC）</th><th>商业版SDK（UGC_Enterprise）</th><th>商业版Pro SDK（EnterprisePro）</th></tr>
</thead>
<tbody>
<tr><td>License精简版（点播套餐精简版）</td><td>&#10004;</td><td>&#10005;</td><td>&#10005;</td><td>&#10005;</td></tr>
<tr><td>License基础版（点播套餐旗舰版2或者3）</td><td>&#10004;</td><td>&#10004;</td><td>&#10005;</td><td>&#10005;</td></tr>
<tr><td>License商业版 （联系商务）</td><td>&#10004;</td><td>&#10004;</td><td>&#10004;</td><td>&#10005;</td></tr>
<tr><td>License商业版Pro （联系商务）</td><td>&#10004;</td><td>&#10004;</td><td>&#10004;</td><td>&#10004;</td></tr>
</tbody>
</table>


### 2 License的使用方法
在调用SDK的相关接口前调用如下所示方法进行license的设置



iOS建议在`- [AppDelegate application:didFinishLaunchingWithOptions:]`中添加
```
[TXUGCBase setLicenceURL:LicenceUrl key:Key];
```

Android建议在 application 中添加:
```
TXLiveBase.getInstance().setLicence(context, LicenceUrl, Key);
```

### 3 License信息的查看
在license设置成功后稍等一段时间(依据网络情况而定), 可以通过调用以下方法查看License信息

iOS:
```
NSLog(@"%@", [TXUGCBase getLicenceInfo]);
```

Android:
```
TXLiveBase.getInstance().getLicenceInfo();
```

### 4.  License的有效期与续费

可以在 [点播控制台](https://console.cloud.tencent.com/vod/license)查看License的有效期，正式版本的License有效期一般为一年，到期后进入 [点播控制台](https://console.cloud.tencent.com/vod/license) 点击购买链接即可。



### 5  关于商业版本License

使用商业版本license可以开启优图实验室的AI功能，License设置方法同上, 工程需要额外进行配置，具体配置参考(动效变脸链接)。

测试申请流程如下

1. 提工单或客服电话（400-9100-100）联系我们商务同学。
2. 下载[示例表格](https://mc.qcloudimg.com/static/archive/766c9092424d0440a31c56c81f34a629/archive.xlsx)，按照表格填好信息后，邮件发送到 wisonxie@tencent.com 并抄送给您联系的商务同学（重要）。
3. 待商务确认后，我们会第一时间向优图实验室申请试用 License，并同压缩包解压密码一起发给您。