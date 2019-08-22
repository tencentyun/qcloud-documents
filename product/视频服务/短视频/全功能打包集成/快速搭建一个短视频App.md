
## 终端部分

按照如下三步操作，可以用 XCode 或者 Android Studio 编译和调试小视频 App 的客户端代码，运行效果如下：

![](https://main.qcloudimg.com/raw/345bae7a0a1f5139c525e4d303b9f745.jpg)

### step1. 下载 App 源码
单击 [小视频源码](https://cloud.tencent.com/document/product/584/9366#APP) 可以下载到小视频 App 的源代码。

### step2. 申请 SDK 用的 License
请参考 [申请License](https://cloud.tencent.com/document/product/584/20333)

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
点播（VOD）服务可以为小视频提供视频的存储和在线分发的能力，您在购买短视频的基础版或者商业版 License 时，会一并购买腾讯云的点播服务套餐包，所以已经有一定量的流量可以使用。

- **业务服务器（CVM）**
小视频 App 需要一台简单的业务服务器，该服务器可以为 App 提供注册、登录、视频列表存储、视频上传签名等能力，您可以将其搭建在腾讯云 CVM 云服务器上，并可以自行修改里面的逻辑。

当您使用小视频源码包内部的默认服务器地址（`http://demo.vod2.myqcloud.com/lite/`）时，使用的点播服务和列表服务器均由腾讯云提供，但该服务有并发限制，仅适合用于调试和体验。

如果您希望自己搭建 App 的后台服务器，可以按照如下步骤自行搭建：

### step1. 开通点播服务（VOD）

单击 [点播控制台](https://console.cloud.tencent.com/vod) 开通点播服务，点播服务可以为小视频提供视频存储和在线播放的能力。
在腾讯云点播控制台，【视频处理设置】下【回调配置】中设置回调模式为可靠回调，【事件回调配置】中选择上传完成回调，该配置需要 10 分钟左右能生效。
![](https://main.qcloudimg.com/raw/2790946cfc7cae82339385f5345fe3f5.png)

### step2. 获取云 API 密钥

小视频 App 在上传视频时，需要使用腾讯云密钥，即 SecretId 和 SecretKey，这两个 Key 要从腾讯云控制台中获取并配置到业务服务器上。

- 2.1 登录 [腾讯云控制台](https://console.cloud.tencent.com/)。

- 2.2 单击【云产品】，选择【监控与管理】栏下的【云 API 密钥】，进入云 API 密钥管理页面，如下图所示：
![](https://mccdn.qcloud.com/img568f5fb824757.png)

- 2.3 获取云 API 密钥，如下图所示。如果您尚未创建密钥，则单击【新建】即可创建一对 SecretId/SecretKey。
![](https://mc.qcloudimg.com/static/img/23f95aaa97adf3eeae3bf90470fe5122/image.png)


### step3. 在云服务器上部署后台代码

- **3.1： [新建 CVM 云服务器](https://console.cloud.tencent.com/cvm)** 
 ![](http://mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

- **3.2： 进服务市场选取镜像，推荐使用图中的小视频镜像**。
 ![](https://main.qcloudimg.com/raw/798e32b00c84a3809fdbfe7de30ad73d.png)

- **3.3： 配置硬盘和网络，以及云服务器访问密码，妥善保管好密码，然后设置安全组**。
![](https://main.qcloudimg.com/raw/d81d282ab01ce1309ac704c5aa61a544.png)

- **3.4： 付款后生成云服务器**。
单击登录可以通过腾讯云的网页 shell 进行访问，也可以用 **putty** 或 **SecretCRT** 采用 ssh 登录到云服务器。
![](http://mc.qcloudimg.com/static/img/0f29fd40aae5fdac10d3f6262eb6a03e/image.png)

- **3.5： 修改云服务器配置信息**

- 将如下脚本中的 `appId`、 `SecretId` 和 `SecretKey` 配置 2.3 中获取到的 APPID、SecretId 和 SecretKey。然后登录云服务器，直接在云服务器上执行修改后的脚本。
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
- 在服务器输入启动服务命令直接启动服务，服务启动默认端口为: `8001`。
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
- 查看 **3.4** 中云服务器的公网 IP，在浏览器中输入 `http://IP` 查看服务是否启动成功。

### step4. 替换终端源代码中的后台地址
- **iOS** 
源码包解压后在 TXXiaoShiPinDemo/Classes/App/ 目录下有一个 **TCConstants.h** 文件，将文件里的 `kHttpServerAddr` 改成您的云服务器公网 IP 地址。

- **Android** 
源码包解压后在 app/src/main/java/com/tencent/qcloud/xiaoshipin/common/utils/ 目录下有一个 **TCConstants.java** 文件，将文件里的 `APP_SVR_URL` 改成您的云服务器公网 IP 地址。

>! 如果服务器没有配置证书，这里的云服务器地址需要用 HTTP，而不能用 HTTPS。

