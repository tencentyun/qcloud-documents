## 接口描述
- **描述：**调用 wemeet.app.setShareOpenAppConfig 设置 webview 顶部栏分享按键显隐及设置。
- **客户端支持：**Win/Mac/IOS/Android
- **支持的版本：**3.3.0
- **是否需要鉴权：**否



**图例**

| ![](https://qcloudimg.tencent-cloud.cn/raw/d4512e204df1f97ba2cf0ed5734e427e.png)| ![](https://qcloudimg.tencent-cloud.cn/raw/587fd87f8da93a76884034dc2f7128ef.png) | ![](https://qcloudimg.tencent-cloud.cn/raw/4d957f17932f711f1ffcd6a976e387ee.png) |
| --- | --- | --- |
| webview 顶部栏功能栏分享键。<br><b>说明：</b>红圈中为支持配置的内容。 | 会中消息通知。<br><b>说明：</b>红圈中为支持配置的内容。 | IM 消息卡片。<br><b>说明：</b>红圈中为支持配置的内容。 |

## 示例
```plaintext
wemeet.app.setShareOpenAppConfig({
    shareEnable: true, // webview顶部栏分享按键是否可见   
    title: '测试标题', //IM消息卡片标题
    desc: "xxxxxxxxx",    // IM消息卡片描述
    notifyDesc: "xxxxxxxxx", //会中消息通知文案
    confirmBtnText: "xxxxxxxxx", //会中消息通知确认按钮文案
    pcUrl: "http://xxxxx",  //桌面端分享url
    mobileUrl: "http://xxxxx",//移动端分享url
})   
   .then((res) => {     
       console.log('succ', res);   
   })   
   .catch((e) => {     
       console.error(e);  
    });
```


## 参数说明

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| shareEnable | Boolean | 控制 webview 顶部栏是否展示分享按键。 |
| title | String | 设置 IM 消息卡片的标题；optional，如不设置则默认标题为：邀请您使用【应用名称】，如设置为空值则不展示。 |
| desc | String | 设置 IM 消息卡片上的描述文案；optional，如不设置则默认为应用简介。 |
| notifyDesc | String | 设置会中消息通知文案；optional，如不设置则默认不展示，如设置为空值则不展示。 |
| confirmBtnText | String | 设置会中消息通知确认按钮文案；optional，如不设置则默认为：打开应用，如设置为空值则不展示。 |
| pcUrl | String | 设置桌面端分享页面 URL；optional，如不设置则默认为创建应用时填写的桌面端主页地址，如设置为空值则不展示。URL 必须为 "`http://`" or "`https://`" |
| mobileUrl | String | 设置移动端分享页面 URL；optional，如不设置则默认为创建应用时填写的移动端主页地址，如设置为空值则不展示。URL 必须为 "`http://`" or "`https://`" |
