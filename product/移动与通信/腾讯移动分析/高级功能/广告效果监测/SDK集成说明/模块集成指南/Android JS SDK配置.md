## Android JS SDK配置
### 工程配置
1. 【必选】要在 MTA 前台开通并配置相关的推广计划；
2. 【必选】在 App 的入口处，一般为 Application 或 MainActivity 的 onCreate() 调用`StatConfig.setTLinkStatus(true);`
3. 【可选】若有接入腾讯 TBS 浏览服务 SDK ，请在主线程调用`QbSdk.initX5Environment()`方法后面添加<br>&emsp;&emsp;&emsp;&nbsp;`StatConfig.invokeTBSSdkOnUiThread(context);`

### 落地页 JS 配置
以下为嵌入落地页的 js sdk 格式，必须填写替换参数：

|参数名|参数描述|
| :---: | :---:|
|$download_btn_id | 下载按钮的id
|$app_key|MTA 管理台中 Android 的 App KEY

```
<script>
var _mta_btn_id = '$download_btn_id';
 (function() {
  var mta = document.createElement("script");
  mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
  mta.setAttribute("name", "MTA_CHANNEL");
  mta.setAttribute("app_key", "$app_key");
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```

**使用示例**
```
<a id="download_app">下载应用</a>

<script>
var _mta_btn_id = 'download_app';
(function() {
  var mta = document.createElement("script");
  mta.src = "//pingjs.qq.com/mta/channel_stats.js?v1";
  mta.setAttribute("name", "MTA_CHANNEL");
  mta.setAttribute("app_key", "IB7ZRJ6V8S1T");
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(mta, s);
})();
</script>
```