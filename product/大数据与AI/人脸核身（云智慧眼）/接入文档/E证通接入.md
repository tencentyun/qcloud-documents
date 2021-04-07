## 前提条件
注册企业账号，并完成实名认证。

如果还未完成以上操作，可参考 [企业实名认证指引](https://cloud.tencent.com/document/product/378/10496) 完成操作。

## 接入流程

![image.png](https://ai-sdk-release-1254418846.cos.ap-guangzhou.myqcloud.com/image/dongjh/eid_77f519b8-eda0-441d-9740-082c4615507b.png)

1. 登录 [人脸核身控制台](https://console.cloud.tencent.com/faceid) 完成 EID 自助申请。
2. 接入方服务端调用获取小程序 token [GetEidToken](https://cloud.tencent.com/document/product/1007/54089) 接口，传入核身所需信息获取到 EidToken。
3. 客户后端将 EidToken 返回给客户小程序端，小程序跳转参考下方指引。
4. 用户完成人脸核身后，会以回调形式返回 EidToken 以及其他信息，接入方小程序将 EidToken 传给接入方服务端，接入方服务端即可凭借 EidToken 参数调用获取小程序核身结果信息 [GetEidResult](https://cloud.tencent.com/document/product/1007/54090) 接口去获取本次核身的详细信息，最后将核身结果返回给接入方小程序。

## 从接入方小程序跳转到腾讯云 E 证通小程序

1. 接入方小程序从接入方服务端获取 EidToken。
2. 接入方小程序调用`wx.navigateToMiniProgram()`方法跳转到腾讯云 E 证通小程序指定的页面。

```javascript
    wx.navigateToMiniProgram({
      appId: 'wxa0a9f6f0154bbe7d', // 腾讯云 E 证通小程序的 AppId
      path: 'pages/authPage/auth', // 目标页面
      extraData: {
        token: EidToken, // 接入方服务端获取的 EidToken
      },
      envVersion: 'release', // 跳转到正式版本
      /* 跳转成功的回调函数 */
      success(res) {
        console.log('跳转成功', res); // 接入方小程序自己的业务逻辑
      },
      /* 跳转失败的回调函数 */
      fail(err) {
        console.log('跳转失败', err); // 接入方小程序自己的业务逻辑
      }
    })
``` 

## 从腾讯云 E 证通小程序跳转回接入方小程序
1. 当核身完成后，腾讯云 E 证通小程序会调用`wx.navigateBackMiniProgram()`方法跳转回接入方小程序，并携带相应的参数。

```javascript
    wx.navigateBackMiniProgram({
        extraData: {
            token, // 接入方小程序传入的token
            verifyDone: true // 核身完成
        }
    })
``` 

2. 接入方小程序可以在 app.js 中的 onShow 方法中获得传入的参数，具体代码请根据需要实现，示例代码：

```javascript
    onShow(options) {
      const { referrerInfo, scene } = options;
      /* 判断是否从腾讯云E证通返回 */
      const { appId } = referrerInfo;
      if(scene === 1038 && appId === 'wxa0a9f6f0154bbe7d') {
        const { extraData } = referrerInfo;
        if(extraData) {
          const { token, verifyDone } = extraData;
          console.log(token, verifyDone);
          if(verifyDone) {
            console.log('核身完成');
          } 
        };
      return
    }
  },
``` 

3. 如果接入方传入的 token 有误或者过期，腾讯云 E 证通会返回接入方小程序，并在 extraData 中携带对应的 token 和 token 状态字段 tokenStatus：

```javascript
  /* 返回接入方小程序 */
  wx.navigateBackMiniProgram({
    extraData: {
        token,
        tokenStatus: 1 // 1.token有误 2.token过期
    },
  })
``` 

4. 在核身的过程中有可能存在用户中途关闭腾讯云 E 证通，导致核身未完成的情况，这个时候微信会返回到接入方小程序，触发 app.js 中的 onShow 方法。请注意此时的 extraData 中不会携带 verifyDone 字段。请注意判断。
