本文主要介绍如何快速地将腾讯云WEBIM Demo(Web) 工程运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建应用
登录腾讯云通信（IM）[控制台](https://console.cloud.tencent.com/avc)，在**应用列表**页，单击【创建应用接入】，在**创建新应用**弹框中，填写新建应用的信息，单击【确认】：
![](https://main.qcloudimg.com/raw/a7769d15f050286162b0cbcdadca5f03.png)

应用创建完成后，自动生成一个应用标识：SdkAppId，如下图：
![](https://main.qcloudimg.com/raw/bf8fe4f38d782741a6e142c24648c9e0.png)

## 2. 配置应用
完成创建应用之后返回应用列表，单击对应 SdkAppId 的**应用配置**链接，在应用详情页，找到当前页面的**帐号体系集成**部分，单击**编辑**链接，配置**账号管理员**信息，然后单击【保存】：

>?账号管理员可以随便填写，在使用云通信后台的 REST API 发送消息时才会用到。

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)


## 3. 获取测试 userSig
完成账号管理员配置后，单击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包。解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到**开发辅助工具**的私钥文本输入框中。

其中：**identifier** 即为您的测试账号（也就是 userId），私钥为 private_key 文件里的文本内容，生成的签名就是**userSig**。identifier 和 userSig 是一一对应的关系。
>! 可以多生成4组以上的 userid 和 usersig，方便在 Demo 中调试使用。

![](https://main.qcloudimg.com/raw/a1b9bb35760e1e52825c754bd3ef9a52.png)


## 4. 下载 Demo 源码
从 [Github](https://github.com/tencentyun/TIMSDK) 下载 IMSDK H5 开发包。

## 5. 修改源码配置
使用编辑器打开 index.html ，修改以下参数配置。  
``` 
var sdkAppID = '', // 填写第一步获取到的 sdkappid
    accountType = ''; // 填写第二步设置账号体系集成获取到的 accountType
```

## 6. 运行 Demo
- step1：浏览器打开 index.html。
- step2：在页面上输入通过控制台**开发辅助工具**获取到 identifier 和 userSig，单击确定。
![](https://main.qcloudimg.com/raw/77bfeddae0703b84d12fa51f38508adf.png)
- step3：登录成功后，就可以进行查找好友，建群，聊天等操作了。
![](https://main.qcloudimg.com/raw/87e6f5eae834907cab89f50d5ce49b49.png)
- setp4: 搜索并添加好友。
![](https://main.qcloudimg.com/raw/ef4c39f1ec649ad4f10cd8764ca51d1c.png)
- setp5：选择好友发消息。
![](https://main.qcloudimg.com/raw/ff8c787aa814edefd96468de2da59f26.png)
- setp6：给好友发消息。
![](https://main.qcloudimg.com/raw/d55732975bb5d3e8e44a283e1a26ba4b.png)








