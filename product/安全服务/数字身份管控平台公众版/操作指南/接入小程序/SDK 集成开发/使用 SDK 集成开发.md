## 操作背景
本文档介绍如何将数字身份管控平台（公众版）的 SDK 集成到小程序应用中。
>?推荐下载 [小程序 Demo](https://ciam-prd-1302490086.cos.ap-guangzhou.myqcloud.com/public/file/%E5%B0%8F%E7%A8%8B%E5%BA%8FSample.zip) 实现快速开发。

## 相关示例
### SDK 实例化
```
	import { WXAppletClient }  from 'ciam-miniapp-sdk';
const authSDK = new WXAppletClient({
      clientId: 'YTFiNjEzM2FiNTJiNDJmNjhlZTIzNzM3MDkzMThjMjE',
      authSourceId: 'f1d2116d-f124-42ad-8a04-5704c2f148f3',
      userDomain: 'https://shingao.demo.tencentciam.com',
	       agreements: [
        {
            "name": "用户协议|隐私协议|附加协议|...", // 必传
            "url": "https://qq.com", // 必传，最大长度1024
            "version": "1.0" // 必传，最大长度10
        },
        {
            "name": "用户协议|隐私协议|附加协议|...", // 必传
            "url": "https://baidu.com", // 必传，最大长度1024
            "version": "2.0.0" // 必传，最大长度10
        }
      ]
    });
```

**初始化参数说明**

| **参数名**   | **类型**         | **是否必填** | **长度限制** | **描述**                               |
| ------------ | ---------------- | ------------ | ------------ | -------------------------------------- |
| clientId     | string           | 是           | -            | 管理端添加的小程序应用 ID              |
| authSourceId | string           | 是           | -            | 管理端添加的小程序认证源 ID            |
| userDomain   | string           | 是           | -            | 租户域名（自定义域名获取）             |
| agreements   | array[Agreement] | 否           | -            | 如协议流程开启则开发者需要上传协议签署 |

**Agreement 参数说明**

| **参数名** | **类型** | **是否必填** | **长度限制** | **描述**                                 |
| ---------- | -------- | ------------ | ------------ | ---------------------------------------- |
| name       | string   | 是           | 100          | 协议名称，如用户协议、隐私协议、附加协议 |
| url        | string   | 是           | 1024         | 协议链接地址                             |
| version    | string   | 是           | 10           | 协议版本号                               |

### 静默授权登录 loginCode 

```
async bindLoginBySlience() {
    try {
      await authSDK.loginCode();
    }
    catch(err) {
      console.log('bindLoginBySlience error', err)
    }
    const userInfo = authSDK.getUser();
    if (userInfo) {
	      ...
	   }
},
```

**参数说明**
无

**返回值**
类型为 Promise[User|null]，User 结构如下：
```
{
	   sub: "69bc2a4d-e575-41cf-bbc6-996e0911e2ec",
	   username: "xxx",
	   name: "xxx",
	   gender: "female",
	   phoneNumber: "+86-13612345678",
	   email: "xxx@qq.com",
	   nickname: "xxxx",
	   wechatUnionId: "xxxxx",
	   wechatOpenid: "xxxxx"
}
```

### 用户信息授权登录 loginUser
>!该方法需要页面产生点击事件（例如：button 上 bindtap 的回调中）后才可调用。详情参见：[获取用户信息](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserProfile.html)。
>
```
	async bindLoginByUserInfo() {
	    try {
	      await authSDK.loginUser();
	    }
	    catch(err) {
	      console.log('bindLoginByUserInfo error', err)
	    }
	    const userInfo = authSDK.getUser();
	    if (userInfo) {
	      ...
	    }
  },
```

**参数说明**
无

**返回值**
类型为 Promise[User|null]，User 结构如下:
```
	{
	   sub: "69bc2a4d-e575-41cf-bbc6-996e0911e2ec",
	   username: "xxx",
	   name: "xxx",
	   gender: "female",
	   phoneNumber: "+86-13612345678",
	   email: "xxx@qq.com",
	   nickname: "xxxx",
	   wechatUnionId: "xxxxx",
	   wechatOpenid: "xxxxx"
}
```

### 用户手机号授权登录 loginPhone
>!该方法需要页面产生点击事件（例如：button 上 bindtap 的回调中）后才可调用。详情参见：[获取手机号](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/getPhoneNumber.html)。
>
```
	async bindLoginByPhone(e) {
	    const loginPromise = await authSDK.loginPhone(); // 此处返回Function
	    const {iv, encryptedData} = e.detail;
	
	    try { 
	      await loginPromise(iv, encryptedData);
	    }
	    catch(err) {
	      console.log('bindLoginByPhone error', err)
	    }
			const userInfo = authSDK.getUser();
			if (userInfo) {
			...
	    }
		
  },

```

**参数说明**
无

**返回值**
类型为 Promise[User|null]，User 结构如下:
```
	{
	   sub: "69bc2a4d-e575-41cf-bbc6-996e0911e2ec",
	   username: "xxx",
	   name: "xxx",
	   gender: "female",
	   phoneNumber: "+86-13612345678",
	   email: "xxx@qq.com",
	   nickname: "xxxx",
	   wechatUnionId: "xxxxx",
	   wechatOpenid: "xxxxx"
}
```

### 获取登录状态 checkLoginState
```
	const isLogin = authSDK.checkLoginState();
	    if (!isLogin) {
	      return;
    }
```

**参数说明**
无

**返回值**
类型为 Boolean，返回 true/false。


### 退出登录 logout
```
await authSDK.logout();
```

**参数说明**
无

**返回值**
类型为 Boolean，返回 true/false。
