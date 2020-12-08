
## 终端部分

按照如下三步操作，可以用 XCode 或者 Android Studio 编译和调试小视频 App 的客户端代码，运行效果如下：
<img src="https://main.qcloudimg.com/raw/345bae7a0a1f5139c525e4d303b9f745.jpg" width="800"/>

### step1. 下载 App 源码
单击 [小视频源码](https://cloud.tencent.com/document/product/584/9366#.E5.85.A8.E5.8A.9F.E8.83.BD.E5.B0.8F.E8.A7.86.E9.A2.91-app.EF.BC.88demo.EF.BC.89.E6.BA.90.E4.BB.A3.E7.A0.81) 可以下载到小视频 App 的源代码。

### step2. 申请 SDK 用的 License
请参见 [申请 License](https://cloud.tencent.com/document/product/584/20333)。

### step3. 准备调试环境
**iOS 平台** 
- XCode 9 或更高版本
- OS X 10.10 或更高版本

**Android 平台**
- Android NDK: android-ndk-r12b
- Android SDK Tools: android-sdk_26.0.2
  - minSdkVersion: 15
  - targetSdkVersion: 21

### step4. 编译运行
单击 XCode 或 Android Studio 的 Build 按钮，即可完成编译和运行工作，源码中默认配置了腾讯云提供的测试服务器地址`http://demo.vod2.myqcloud.com/lite/`，以便您快速在调试环境中运行我们的 App。


## 后台部分

小视频 App 的运行依赖两种后台服务：

- **点播云服务（VOD）**
点播（VOD）服务可以为小视频提供视频的存储和在线分发的能力，您在购买短视频的基础版或者企业版 License 时，会一并购买腾讯云的点播服务套餐包，所以已经有一定量的流量可以使用。

- **业务服务器（CVM）**
小视频 App 需要一台简单的业务服务器，该服务器可以为 App 提供注册、登录、视频列表存储、视频上传签名等能力，您可以将其搭建在腾讯云 CVM 云服务器上，并可以自行修改里面的逻辑。

当您使用小视频源码包内部的默认服务器地址（`http://demo.vod2.myqcloud.com/lite/`）时，使用的点播服务和列表服务器均由腾讯云提供，但该服务有并发限制，仅适合用于调试和体验。

如果您希望自己搭建 App 的后台服务器，可以按照如下步骤自行搭建：

### step1. 开通点播服务（VOD）

登录 [云点播控制台](https://console.cloud.tencent.com/vod) 开通云点播服务，云点播服务可以为小视频提供视频存储和在线播放的能力。

在云点播控制台的[【回调设置】](https://console.cloud.tencent.com/vod/callback)中设置回调模式为可靠回调，【事件回调配置】中选择上传完成回调，该配置需要10分钟左右能生效。
<img src="https://main.qcloudimg.com/raw/fe55d80402a0ae03ad3e45592eb68b39.png" width="800"/>

### step2. 获取云 API 密钥

小视频 App 在上传视频时，需要使用腾讯云密钥，即 SecretId 和 SecretKey，这两个 Key 要从腾讯云控制台中获取并配置到业务服务器上。
- **2.1**：登录控制台，选择【云产品】>【访问管理】>[【API密钥管理】](https://console.cloud.tencent.com/cam/capi)，进入“API 密钥管理”页面。
- **2.2**：获取云 API 密钥。如果您尚未创建密钥，则单击【新建密钥】即可创建一对 SecretId 和 SecretKey。

<img src="https://main.qcloudimg.com/raw/fb0490e2553cd5bc314a4ca9e1fc6913.png" width="800"/>

### step3. 在云服务器上部署后台代码

- **3.1：[新建 CVM 云服务器](https://console.cloud.tencent.com/cvm)**。  
<img src="https://main.qcloudimg.com/raw/85a4ee15e56253b838e5fe30ecaf4655.png" width="800"/>
- **3.2：选择【自定义配置】，进入镜像市场选取镜像**。
![](https://main.qcloudimg.com/raw/baa3c6b05d431393bb08f0431678e284.png)
![](https://main.qcloudimg.com/raw/e74f5eba3cb02f5838d27ea26090bd62.png)
- **3.3：配置硬盘和网络，以及云服务器访问密码，妥善保管好密码，然后设置安全组**。
![](https://main.qcloudimg.com/raw/81655f57778fd5a5ebe192f5db1200a4.png)
- **3.4：登录生成的云服务器**。
单击实例操作栏的【登录】，可以通过腾讯云的网页 shell 进行访问，也可以用 **putty** 或 **SecretCRT** 采用 ssh 登录到云服务器。
![](https://main.qcloudimg.com/raw/4f8c3a12375bdebde7344fcb8c38ea22.png)
- **3.5：修改云服务器配置信息**。
将如下脚本中的`appId`、`SecretId`和`SecretKey`配置**2.2**中获取到的 APPID、SecretId 和 SecretKey。然后登录云服务器，直接在云服务器上执行修改后的脚本。
>! 请在本地修改以下配置并复制，然后登录云服务器在控制台粘贴回车执行。

	```
  echo '{
      "dbconfig":{
          "host":"127.0.0.1",
          "user":"litvideo",
          "password":"litvideo",
          "database":"db_litvideo",
          "port":3306,
          "supportBigNumbers": true,
          "connectionLimit":10
      },
      "tencentyunaccount":{
          "appid":"Your AppId",
          "SubAppId":"",
          "SecretId": "Your SecretId",
          "SecretKey": "Your SecretKey",
          "bucket":"xiaoshipin",
          "region":"ap-guangzhou"
      },
      "server":{
          "ip":"0.0.0.0",
          "port":8001,
          "reliablecb":true
      }
  }' > /home/ubuntu/vod-xiaoshipin-server/conf/localconfig.json
```
在服务器输入启动服务命令直接启动服务，服务启动默认端口为：`8001`。
  启动服务：
```
  cd /home/ubuntu/vod-xiaoshipin-server/;pm2 start app.js --name 'litvideo';
```
  如需关闭或者重启服务，可以使用以下命令：
   重启服务：
```
  pm2 restart litvideo;
```
  关闭服务：
```
  pm2 delete litvideo;
```
查看**3.4**中云服务器的公网 IP，在浏览器中输入`http://IP`查看服务是否启动成功。

### step4. 替换终端源代码中的后台地址
- **iOS** 
源码包解压后在 iOS/Demo/XiaoShiPin/TCConstants.h，将文件里的 `kHttpServerAddr` 改成您的云服务器公网 IP 地址。

- **Android** 
源码包解压后在 XiaoShiPin_Professional_Android/Demo/ugckit/src/main/java/com/tencent/qcloud/ugckit/UGCKitConstants.java ，将文件里的 `APP_SVR_URL` 改成您的云服务器公网 IP 地址。

>! 如果服务器没有配置证书，这里的云服务器地址需要用 HTTP，而不能用 HTTPS。

至此，小视频的服务器模式配置完成，您可以运行 App 体验小视频的各项功能。
