本文为您描述如何接入意愿核身 E证通小程序，详细接入操作如下：
1. [开通 E证通](https://cloud.tencent.com/document/product/1007/56642)
2. [申请商户 ID](https://cloud.tencent.com/document/product/1007/56643#spang)
3. [使用商户 ID 获取 E证通服务流程唯一标识 EidToken](https://cloud.tencent.com/document/product/1007/56643#eidtoken)
4. [下载、安装小程序 SDK](https://cloud.tencent.com/document/product/1007/56643#anzhuangsdk)
5. [获取意愿核身（E证通）核验结果信息](https://cloud.tencent.com/document/product/1007/56643#jieguo)
6. [查看错误码](https://cloud.tencent.com/document/product/1007/47912)

详细接入操作如下：
## 申请商户 ID
1.登录腾讯云慧眼 人脸核身控制台，单击**自助接入> E证通服务>申请商户 ID**
![](https://qcloudimg.tencent-cloud.cn/raw/c5b60f45fb48f2316ab4568c3a5c27b6.png)
2. 完全填写相关信息，然后单击**提交**，审核时间需要1-3个工作日，请您耐心等待。
![](https://qcloudimg.tencent-cloud.cn/raw/eeae5f797640c5453f85b2d17772499c.png)
3. 审核通过后，可以看到商户 ID 和 E证通小程序 SDK，后续需要使用商户 ID 获取 E证通服务流程唯一标识 EidToken。
![](https://qcloudimg.tencent-cloud.cn/raw/caf65891cc52c01ce97c6d45053cd067.png)

## 获取 EidToken
接入方服务端调用获取E证通 Token [GetEidToken](https://cloud.tencent.com/document/product/1007/54089) 接口，传入E证通服务所需参数及意愿核身所需参数Config信息，获取到 EidToken。
![](https://qcloudimg.tencent-cloud.cn/raw/c706c94a4e957e5b1324816c7352fca2.png)

## 内嵌小程序 SDK
### 前置条件
#### step 1. 添加服务器域名白名单
小程序前端接口请求有域名白名单限制，未添加白名单的域名只能在调试模式下运行。接入方需要在小程序上线前将以下域名添加至服务器域名白名单：
```
    // request 合法域名
    eid.faceid.qq.com
```

#### step 2. 添加业务域名白名单
在小程序配置业务域名中，将下载后的校验文件在控制台随商户 ID 提交审核时上传，待腾讯侧审核通过后，将域名 `eid.faceid.qq.com` 添加至业务域名白名单。

### 安装 SDK
商户 ID 申请通过后，在 [控制台商户 ID 列表页](https://console.cloud.tencent.com/faceid/access?tab=eid) 可以下载 E证通小程序 SDK。下载完成后将 E证通小程序 SDK 文件夹放在小程序根目录下。

### SDK 调用步骤
#### step 1. 初始化 SDK
1. 在 app.js 文件中引入初始化 SDK 的方法 initEid。
2. 在 App.js 的 onLaunch() 中加入相应代码，在 App.json 文件里添加E证通 SDK 页面。
3. 在 onLaunch 方法中调用 initEid。
```
    //app.js
    import { initEid } from './mp_ecard_sdk/main';

    App({
        onLaunch() {
            initEid();
        },
    });

    // app.json
    {
        "pages":[
            "mp_ecard_sdk/index/index",
            "mp_ecard_sdk/protocol/service/index",
            "mp_ecard_sdk/protocol/privacy/index",
            "mp_ecard_sdk/protocol/userAccredit/index",
            "mp_ecard_sdk/protocol/eid/index",
        ]
    }
```

#### step 2. 调用 SDK
1. 在需要进行核身的地方引入调用 SDK 的方法 startEid。
2. 在业务需要的时机触发 startEid。
```
    import { startEid } from './mp_ecard_sdk/main';

    // 示例方法
    goSDK(token) {
        startEid({
            data: {
                token,
            },
            verifyDoneCallback(res) {  
                const { token, verifyDone } = res;
                console.log('收到核身完成的res:', res);
                console.log('核身的token是:', token); 
                console.log('是否完成核身:', verifyDone);          
            },
        });
    },
```


startEid() 参数说明：
- `startEid(options)`：进入实名认证页面。
- `options`：Object required 接入方传入的参数。
- `options.data.token`：String required 接入方小程序从接入方服务端获取 EidToken。
- `options.verifyDoneCallback`：Function(res) required 核身完成的回调。res 包含验证成功的 token，是否完成的布尔值标志 verifyDone。请根据 res 返回的结果进行业务处理判断。

## 获取意愿核身（E证通）核验结果信息
1. 用户完成人脸核身后，会以回调形式返回 EidToken 以及其他信息，接入方小程序将 EidToken 传给接入方的服务端，接入方服务端即可凭借 EidToken 参数调用获取小程序核身结果信息 [GetEidResult](https://cloud.tencent.com/document/product/1007/54090) 接口去获取本次核身的详细信息，最后将核身结果返回给接入方小程序。
>? EidToken 作为一次核身流程的标识，有效时间为600秒；完成核身后，可用该标识获取3天内验证结果信息。

## 调试 SDK
请在微信开发者工具中使用手机“预览”模式进行调试，请勿使用“真机调试”。

## 卸载 SDK
删除 mp_ecard_sdk 文件夹。
## 接入时序图
![](https://qcloudimg.tencent-cloud.cn/raw/751abb25ef4a11c83d97c8ec5ab70173.png)
## 注意事项
1.从 eID 数字身份小程序返回接入方小程序。
当接入方小程序在初始化E证通 SDK 的时候，E证通 SDK 会通过 wx.onAppShow 注册一个监听从 eID 数字身份小程序跳转回接入方小程序的事件，从而根据情况触发接入方传入的核身完成的回调函数。
2.由于微信的机制，用户在 eID 数字身份小程序跳转回接入方小程序的时候，同时也会触发接入方小程序 app.js 中的 onShow 方法。为了避免冲突，如果接入方小程序在 onShow 中有执行逻辑的话，需要排除掉从 eID 数字身份小程序跳转回接入方小程序这个场景。可通过以下方法实现：
```
// app.js

    onShow(options) {
        const { referrerInfo, scene } = options;
        /* 判断是否从eID数字身份小程序返回 */
        const { appId } = referrerInfo;
        if (scene === 1038 && appId === 'wx0e2cb0b052a91c92') {
            return;
        } else {
            // 执行接入方小程序原本的逻辑
        }
    },
```
    
