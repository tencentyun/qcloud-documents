If you need to make a promotion in WeChat, WeChat Moments, QR Code, SMS and other scenarios and the promotion address is the activity page, the following solutions can be adopted:

When embedding JS SDK in the landing page (activity page), you can set $adtag in the codes to the value of suffix ADTAG in TLink acquired from MTA based on the device system (refer to HTTP Useragent) of the accessed page, and also set $app_key to the Appkey of different platforms acquired from MTA.

```
<script>
var _mta_btn_id = '$download_btn_id';
 var _mta_adtag = '$adtag';
 (function() {
      var mta = document.createElement("script");
      mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
      mta.setAttribute("name", "MTA_CHANNEL");
      mta.setAttribute("app_key", "$app_key");
      mta.setAttribute("app_flag", "$URL_Scheme"); (For Android, this line can be deleted.)
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(mta, s);
    })();
</script>
```

**Example:**
Configure two Tlinks respectively for Android and iOS on MTA console:
- iOS: `http://xxxxx.com?ADTAG=111 `
- Android: `http://xxxx.com?ADTAG=222 `

The AppKey of iOS is AAAAAAAA, and the AppKey of Android is BBBBBBB (see [Management Console](http://mta.qq.com/mta/overview/ctr_all_app_new) -> **Configuration Management** -> **App Information**). Check its value on the activity page. If the device adopts iOS, set $adtag to 111 and $app_key to AAAAAAAA, and if the device adopts Android, set $adtag to 222 and $app_key to BBBBBBB.

(If multiple links need to be redirected to the same landing page and the statistics needs to be performed for every link for both Android and iOS, ADTAG can be attached to the parameters of the URL before the redirecting to the landing page.)

