### 接入说明
1.注册应用后，按【SDK 配置说明】下载 SDK；
2.在小程序开发设置中，将`https://pingtas.qq.com` 添加为可信域名；
3.将 SDK 放置入项目中，目录自定义，并在应用入口 app.js 中引入 SDK，例如：var mta= require('path/to/mta_analysis.js')；
4.在应用入口 app.js 的 App.onLaunch 方法调用如下代码段，做统计信息初始化（可在【应用管理】选择配置并拷贝代码），以下为示例代码：

```javascript
mta.App.init({
   
 "appID":"500013092",
    
 "eventID":"500015824",// 高级功能-自定义事件统计ID，配置开通后在初始化处填写
  
 "lauchOpts":options, //渠道分析,需在onLaunch方法传入options,如onLaunch:function(options){...}
         
 "statPullDownFresh":true, // 使用分析-下拉刷新次数/人数，必须先开通自定义事件，并配置了合法的eventID
  
 "statShareApp":true, // 使用分析-分享次数/人数，必须先开通自定义事件，并配置了合法的eventID
    
 "statReachBottom":true // 使用分析-页面触底次数/人数，必须先开通自定义事件，并配置了合法的eventID
});
```

5.在需要统计的页面js中引入SDK，在Page.onLoad调用mta.Page.init()，完成初始化和统计。