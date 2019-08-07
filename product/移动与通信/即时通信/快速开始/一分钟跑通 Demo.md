本文介绍如何快速跑通即时通信 IM 的体验 Demo。

<span id="step1"></span>
## 步骤1：创建应用
1. 登录即时通信 IM [控制台](https://console.cloud.tencent.com/avc)。
 >?如果您已有应用，请记录其 SDKAppID 并 [配置应用](#step2)。
 >
2. 在【应用列表】页，单击【创建应用接入】。
3. 在【创建新应用】对话框中，填写新建应用的信息，单击【确认】。
 应用创建完成后，自动生成一个应用标识 SDKAppID，请记录 SDKAppID 信息。

<span id="step2"></span>
## 步骤2：获取密钥信息

1. 单击目标应用所在行的【应用配置】，进入应用详情页面。
3. 单击**帐号体系集成**右侧的【编辑】，配置**帐号管理员**信息，单击【保存】。
 ![](https://main.qcloudimg.com/raw/2ad153a77fe6f838633d23a0c6a4dde1.png)
4. 单击【查看密钥】，拷贝并保存密钥信息。
 >!请妥善保管密钥信息，谨防泄露。

<span id="step3"></span>
## 步骤3：下载并配置 Demo 源码

1. 从 [Github](https://github.com/tencentyun/TIMSDK) 克隆即时通信 IM Demo 工程。
2. 打开所属终端目录的工程，找到对应的`GenerateTestUserSig`文件。
 <table>
     <tr>
         <th>编程语言</th>  
         <th nowrap="nowrap">所属平台</th>  
         <th nowrap="nowrap">GenerateTestUserSig 源代码</th>  
     </tr>
	 <tr>      
         <td>Java</td>   
	     <td>Android</td>   
	     <td><a href="https://github.com/tencentyun/TIMSDK/blob/master/Android/app/src/main/java/com/tencent/qcloud/tim/demo/signature/GenerateTestUserSig.java">GenerateTestUserSig.java</a></td>   
     </tr> 
	 <tr>
	     <td>Objective-C</td>   
	     <td>iOS</td>   
	     <td><a href="https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKitDemo/TUIKitDemo/Debug/GenerateTestUserSig.h">GenerateTestUserSig.h</a></td>
     </tr> 
	 <tr>      
         <td>Objective-C</td>   
	     <td>Mac</td>   
	     <td><a href="https://github.com/tencentyun/TIMSDK/blob/master/Mac/TUIKitDemo/TUIKitDemo/Debug/GenerateTestUserSig.h">GenerateTestUserSig.h</a></td>   
     </tr>  
	 <tr>      
         <td>C++</td>   
	     <td>Windows</td>   
	     <td><a href="https://github.com/tencentyun/TIMSDK/blob/master/cross-platform/Windows/IMApp/IMApp/GenerateTestUserSig.h">GenerateTestUserSig.h</a></td>   
     </tr>  
	 <tr>      
         <td>Javascript</td>   
	     <td>Web（通用）</td>   
	     <td><a href="https://github.com/tencentyun/TIMSDK/blob/master/H5/js/debug/GenerateTestUserSig.js">GenerateTestUserSig.js</a></td>   
     </tr>  
	 <tr>      
         <td>Javascript</td>   
	     <td>小程序</td>   
	     <td><a href="https://github.com/tencentyun/TIMSDK/blob/master/WXMini/debug/GenerateTestUserSig.js">GenerateTestUserSig.js</a></td>   
     </tr>  
</table>

 >?本文以使用 Android Studio 打开 Android 工程为例。
  >
3. 设置`GenerateTestUserSig`文件中的相关参数：
 - SDKAPPID：请设置为 [步骤1](#step1) 中获取的实际应用 SDKAppID。
 - SECRETKEY：请设置为 [步骤2](#step2) 中获取的实际密钥信息。
 ![](https://main.qcloudimg.com/raw/5771a4cb0408eb97b6ee073a764fcb30.png)


>!本文提到的获取 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

## 步骤4：编译运行
用各端的 IDE 直接编译运行即可。


