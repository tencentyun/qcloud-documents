## 操作背景
本文档介绍如何将数字身份管控平台（公共版）的 SDK 集成到小程序应用中。

## 相关示例
### SDK 实例化
```
	const authSDK = new WXAppletClient(
	{
	      clientId: 'YTFiNjEzM2FiNTJiNDJmNjhlZTIzNzM3MDkzMThjMjE',
	      authSourceId: 'f1d2116d-f124-42ad-8a04-5704c2f148f3',
	      userDomain: 'https://shingao.demo.tencentciam.com'
    }
		);
```

#### 参数说明

| 参数名       | 类型      | 描述                        |
| ------------ | --------- | --------------------------- |
| clientId     | 应用 ID   | 管理端添加的小程序应用 ID   |
| authSourceId | 认证源 ID | 管理端添加的小程序认证源 ID |
| userDomain   | 租户域名  | 租户域名（自定义域名获取）  |

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

#### 参数说明
- 无
- 返回值: 类型为 Promise[User|null]，User 结构如下：
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

#### 参数说明
- 无
- 返回值: 类型为 Promise[User|null]，User 结构如下:
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

#### 参数说明
- 无
- 返回值: 类型为 Promise[User|null]，User 结构如下:
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

#### 参数说明
- 无
- 返回值：true/false

### 退出登录 logout
```
await authSDK.logout();
```

#### 参数说明
- 无
- 返回值： 类型为Boolean，结果为 true/false

### 更新用户信息updateUser
```
	await authSDK.updateUser({
	   nickname: "xxxx",
	   phoneNumber: "xxxxx"
});
```

#### 参数说明
- 传入发生变化的用户属性 code 及属性值。
```
	{
	   nickname: "xxxx",
	   phoneNumber: "xxxxx"
}
```
- 返回值: 类型为 Promise[User|null]，User 结构如下:
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
