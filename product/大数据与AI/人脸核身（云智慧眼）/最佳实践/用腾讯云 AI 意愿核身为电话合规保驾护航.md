腾讯云 AI 意愿核身功能是结合人脸核身与实时音视频技术打造的一款满足实名、实人、真实意愿的产品，还是首批通过国家信通院人脸识别评估的产品，并且荣获四级（优秀级）安全防护等级。不仅如此，腾讯云 AI 意愿核身也提供了微信小程序、微信 H5、SDK 等多种接入方式。

本文档将详细介绍如何接入腾讯云 AI 意愿核身，降本增效、更加智能地实现对高危电话用户进行二次实人、实名、语音认证等功能，提醒用户使用的电话卡涉嫌法律风险等，用于预防电信诈骗，为电话合规保驾护航。

## 准备工作
1. 开通人脸核身
登录 [人脸核身控制台](https://console.cloud.tencent.com/faceid/access)，若首次使用人脸核身服务，需要先开通人脸核身服务。单击**提交申请**，按照实际情况填写信息，即可提交申请。
>? 
>- 互联网行业和金融行业必须上传业务相关营业资质。
>- 本次接入需要的功能组合为：活体人脸核身（完成活体检测后照片与权威库比对）和活体人脸比对（完成活体检测后照片与上传照片比对）。 
>
![](https://qcloudimg.tencent-cloud.cn/raw/eab2cd89ff2b9c05a6fd15e3a155d84a.jpg)

2. 业务申请
根据业务需求，选择相对应的接入模式，[申请对应的业务](https://console.cloud.tencent.com/faceid/access/scene)。
![](https://qcloudimg.tencent-cloud.cn/raw/6c1518844a774572981cf32c7ac24a66.png)
	- 选择接入方式，微信原生 H5 的接入方式有行业限制，且资质文件中主体与需要接入公众号主体一致，详细行业类目和资质材料请查阅 [微信 HTML5 及小程序资质文件列表](https://cloud.tencent.com/document/product/1007/42684)。
	-  如果需要申请微信原生 H5 和微信小程序，但是没有对应的微信小程序和公众号，可以前往 [微信公众平台](https://mp.weixin.qq.com/) 进行申请。

3. 了解腾讯云 AI 意愿核身
意愿核身详细内容请参见 [意愿核身接入指引](https://cloud.tencent.com/document/product/1007/65416)、[计费错误码](https://cloud.tencent.com/document/product/1007/47912) 等。
4. 意愿核身配置
相关业务通过审核后，请联系 [人脸核身助手](https://cloud.tencent.com/document/product/1007/56130)，完成意愿核身业务的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/4903a75d1536e27fe1cf43600734cdb4.png)

5. 获取 API 密钥
登录官网控制台 [创建 API 密钥](https://console.cloud.tencent.com/cam/capi)（SecretId 和 SecretKey）。
>!  API 密钥需要妥善保管。

## 接入意愿核身
### 第一步：授予权限与设置白名单
- **为人脸核身授权**
小程序开发需要授权，打开 [二维码](https://open.faceid.qq.com/view/auth.html)，小程序管理员扫码后，单击**自定义权限**，只勾选人脸核身权限，将该权限授权给人脸核身第三方平台。
![](https://qcloudimg.tencent-cloud.cn/raw/108743b1b3298b7705f6b0cf948b1966.png)

- **开启实时播放/录制音视频流权限**
使用腾讯云AI 意愿核身需要开启实时播放音视频流 (live-player) 和实时录制音视频流（live-pusher），登录 [微信公众平台](https://mp.weixin.qq.com/) 开启对应的权限。
![](https://qcloudimg.tencent-cloud.cn/raw/4f746140817846c904b55f2d7202cba6.png)

- **相关域名添加白名单**
登录 [微信公众平台](https://mp.weixin.qq.com/)，给意愿核身需要的域名添加白名单权限，相关操作如下所示：
	- 将以下域名添加至 request 合法域名： 
`https://events.tim.qq.com;https://faceid.qq.com;https://grouptalk.c2c.qq.com`。
`https://pingtas.qq.com;https://web.sdk.qcloud.com;https://webim.tim.qq.com;https://yun.tim.qq.com`。
	- 将以下域名添加至 socket 合法域名：`wss://wss.im.qcloud.com;wss://wss.tim.qq.com`。
	- 将以下域名添加至 uploadFile 合法域名：`https://cos.ap-shanghai.myqcloud.com;https://faceid.qq.com`。
	- 将以下域名添加到 uploadFile 合法域名：`https://cos.ap-shanghai.myqcloud.com;https://faceid.qq.com`。
![](https://qcloudimg.tencent-cloud.cn/raw/ce4c6c1b1eb32eaaa0377dc3b4e4964d.png)

### 第二步：初始化意愿核身 SDK
下载 [意愿核身小程序 SDK](https://faceid-verify-temp-1254418846.cos.ap-chengdu.myqcloud.com/asr/cloud-faceid-micro-asr-sdk-v1.0.2.zip) ，将 verify_mpsdk 文件夹放到小程序项目根目录，调用 init 方法，初始化意愿核身 SDK。
```
//app.js
App({
    onLaunch: function () {
        // 初始化意愿核身组件
        const Verify = require('/verify_mpsdk/main');
        Verify.init();
    }
}) 
// app.json
{
    "pages":[
        "verify_mpsdk/index/index"
    ]
}
```
微信小程序接入意愿核身，可参考 [意愿核身 demo](https://faceid-verify-temp-1254418846.cos.ap-chengdu.myqcloud.com/mp_verify_sdk_demo.zip)。

### 第三步：后端接入意愿核身实名核身鉴权接口
调用意愿核身 [实名核身鉴权接口](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=DetectAuth&SignVersion=)，获取意愿核身流程标识 BizToken。Java SDK 的引入可参考 [Java SDK 接入指引](https://cloud.tencent.com/document/sdk/Java?from=10680)。
>! 需传入意愿核身所需字段 IntentionVerifyText。
>
意愿核身提供了多种主流语言接入，包含 Java、Python、Go 等，以 Java 为例：
```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.faceid.v20180301.FaceidClient;
import com.tencentcloudapi.faceid.v20180301.models.*;

public class DetectAuth
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
            // 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
            Credential cred = new Credential("SecretId", "SecretKey");
            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("faceid.tencentcloudapi.com");
            // 实例化一个client选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            FaceidClient client = new FaceidClient(cred, "", clientProfile);
            // 实例化一个请求对象,每个接口都会对应一个request对象
            DetectAuthRequest req = new DetectAuthRequest();
            
            // 返回的resp是一个DetectAuthResponse的实例，与请求对象对应
            DetectAuthResponse resp = client.DetectAuth(req);
            // 输出json格式的字符串回包
            System.out.println(DetectAuthResponse.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
}
```
### 第四步：进入意愿核身流程
接入方服务端将 BizToken 返回给接入方小程序，然后小程序调用核身方法 startVerify 进入核身流程。
```
// 单击某个按钮时，触发该函数
gotoVerify: function () {
    // 去接入方服务端调用DetectAuth接口获取BizToken，需要接入方服务端自行实现
    let BizToken = getBizToken();
    // 调用实名核身功能
    wx.startVerify({
        data: {
            token: BizToken // BizToken
        },
        success: (res) => { // 验证成功后触发
            // res 包含验证成功的token
        },
        fail: (err) => {  // 验证失败时触发
            // err 包含错误码，错误信息
        }
    });
}
```
### 第五步：后端接入获取意愿核身结果接口
调用意愿核身 [获取意愿核身结果接口](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=GetDetectInfoEnhanced&SignVersion=)，拉取意愿核身结果。
小程序在完成意愿核身之后，回调我们的后台，我们的后台通过**获取意愿核身结果接口**和 BizToken，拉取意愿核身结果。
以 Java 为例：
```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.faceid.v20180301.FaceidClient;
import com.tencentcloudapi.faceid.v20180301.models.*;

public class GetDetectInfoEnhanced
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
            // 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
            Credential cred = new Credential("SecretId", "SecretKey");
            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("faceid.tencentcloudapi.com");
            // 实例化一个client选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            FaceidClient client = new FaceidClient(cred, "", clientProfile);
            // 实例化一个请求对象,每个接口都会对应一个request对象
            GetDetectInfoEnhancedRequest req = new GetDetectInfoEnhancedRequest();
            
            // 返回的resp是一个GetDetectInfoEnhancedResponse的实例，与请求对象对应
            GetDetectInfoEnhancedResponse resp = client.GetDetectInfoEnhanced(req);
            // 输出json格式的字符串回包
            System.out.println(GetDetectInfoEnhancedResponse.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
}
```
## 意愿核身效果展示
接入意愿核身的效果展示请参见 [意愿核身实践 Demo 演示](https://cloud.tencent.com/developer/video/31897)。



## 查询调用量
登录 [人脸核身控制台](https://console.cloud.tencent.com/faceid/access)，在**计费统计**页面，可查看意愿核身的计费量情况。
![](https://qcloudimg.tencent-cloud.cn/raw/566f01a9eb12a96540f725f6cd3a38a6.png)
