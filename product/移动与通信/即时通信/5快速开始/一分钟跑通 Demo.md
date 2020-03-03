本文介绍如何快速跑通即时通信 IM 的体验 Demo。

<span id="step1"></span>
## 步骤1：创建应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
 >?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
 >同一个腾讯云账号，最多可创建100个即时通信 IM 应用。若已有100个应用，您可以先 [停用](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.E5.BA.94.E7.94.A8) 并删除无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
 >
2. 单击【+添加新应用】。
3. 在【创建应用】对话框中输入您的应用名称，单击【确定】。
  创建完成后，可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、创建时间以及到期时间。请记录 SDKAppID 信息。
  ![](https://main.qcloudimg.com/raw/2753962b67754a9ebb2a2a5b8042f2ef.png)
  

<span id="step2"></span>
## 步骤2：获取密钥信息

1. 单击目标应用卡片，进入应用的基础配置页面，
2. 在【基本信息】区域，单击【显示密钥】，复制并保存密钥信息。
 >!请妥善保管密钥信息，谨防泄露。

<span id="step3"></span>
## 步骤3：下载并配置 Demo 源码

1. 下载即时通信 IM Demo 工程，具体下载地址请参见 [SDK 下载](https://cloud.tencent.com/document/product/269/36887)。
2. 打开所属终端目录的工程，找到对应的`GenerateTestUserSig`文件。
 <table>
     <tr>
         <th nowrap="nowrap">所属平台</th>  
         <th nowrap="nowrap">文件相对路径</th>  
     </tr>
  <tr>      
      <td>Android</td>   
      <td>Android/app/src/main/java/com/tencent/qcloud/tim/demo/signature/GenerateTestUserSig.java</td>   
     </tr> 
  <tr>
      <td>iOS</td>   
      <td>iOS/TUIKitDemo/TUIKitDemo/Debug/GenerateTestUserSig.h</td>
     </tr> 
  <tr>      
      <td>Mac</td>   
      <td>Mac/TUIKitDemo/TUIKitDemo/Debug/GenerateTestUserSig.h</td>   
     </tr>  
  <tr>      
      <td>Windows</td>   
      <td>cross-platform/Windows/IMApp/IMApp/GenerateTestUserSig.h</td>   
     </tr>  
  <tr>      
      <td>Web（通用）</td>   
      <td>H5/dist/debug/GenerateTestUserSig.js</td>   
     </tr>  
  <tr>      
      <td>小程序</td>   
      <td>WXMini/dist/wx/debug/GenerateTestUserSig.js</td>   
     </tr>  
</table>
3. 设置`GenerateTestUserSig`文件中的相关参数：
 >?本文以使用 Android Studio 打开 Android 工程为例。
  >
 - SDKAPPID：请设置为 [步骤1](#step1) 中获取的实际应用 SDKAppID。
 - SECRETKEY：请设置为 [步骤2](#step2) 中获取的实际密钥信息。
 ![](https://main.qcloudimg.com/raw/e7f6270bcbc68c51595371bd48c40af7.png)


>!本文提到的获取 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

## 步骤4：编译运行
用各端的 IDE 直接编译运行即可，更多详情可参见 [步骤3](#step3) 克隆的 Demo 工程中对应目录下的`README.md`文件。

**其中 iOS 和 Mac Demo 的编译运行需要使用 pod 集成，详情步骤如下：**
1. 终端执行以下命令，检查 pod 版本。
```
pod --version
```
若提示 pod 不存在，或 pod 版本小于 1.7.5，请执行以下命令安装最新 pod。
```
//更换 gem 源
gem sources --remove https://rubygems.org/
gem sources --add https://gems.ruby-china.com/
//安装 pod
sudo gem install cocoapods -n /usr/local/bin
//如果安装了多个 Xcode ，请使用下面的命令选择 Xcode 版本（一般选择最新的 Xcode 版本）
sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
//更新 pod 本地库
pod setup
```
2. 终端执行以下命令，安装依赖库。
```
//iOS
cd iOS/TUIKitDemo
pod install
//Mac
cd Mac/TUIKitDemo
pod install
```
 如果安装失败，执行以下命令更新本地的 CocoaPods 仓库列表。
 ```bash
 pod repo update
```
3. 编译运行：
 - iOS 进入 iOS/TUIKitDemo 文件夹，打开`TUIKitDemo.xcworkspace`编译运行。
 - Mac 进入Mac/TUIKitDemo 文件夹，打开`TUIKitDemo.xcworkspace`编译运行。



