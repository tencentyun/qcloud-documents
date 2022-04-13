## 组件介绍
`TUIPlayer` 组件是一套开源的、完整的视频直播互动播放组件，它基于腾讯云 [直播 Live SDK](https://cloud.tencent.com/document/product/454/19074) 和 [即时通信 IM SDK](https://cloud.tencent.com/document/product/269/1498) ，实现直播播放，直播连麦等功能，同时支持弹幕、点赞、美颜等外挂插件，通过 `TUIPlayer` 组件您可以轻松实现直播视频拉流，快速搭建诸如秀场直播、电商直播等场景化解决方案。
<table>
<tr>
   <th style="width:50%;text-align:center">观看直播</th>
   <th style="width:50%;text-align:center">发起连麦</th>
 </tr>
<tr>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/9cbd0d20c12b86a87436fc72e0b4950d.jpg"/></td>
<td><img src="https://qcloudimg.tencent-cloud.cn/raw/4125d61586106e87a414d738848ad0c6.jpg"/></td>
</tr>
</table>

[](id:model)
## 组件集成
[](id:model.step1)
### 步骤一：下载并导入 TUIPlayer 组件
- 单击进入 [Github](https://github.com/LiteAV-TUIKit/TUIPlayer) ，选择克隆/下载代码，然后拷贝 `Android/tuiplayer` 目录到您的工程中，在项目的 `setting.gradle` 文件中添加 tuiplayer 模块：

```
include ':tuiplayer'
```

- 在使用 `TUIPlayer` 的 `module` 的 `build.gradle` 文件中添加依赖：

```
api project(":tuiplayer")
```

[](id:model.step2)
### 步骤二：配置权限及混淆规则
1. 在 `AndroidManifest.xml` 中配置 App 的权限，SDK 需要以下权限（6.0以上的 Android 系统需要动态申请相机、麦克风权限等）：

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
```

2. 在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：

```
-keep class com.tencent.** { *; }
```

[](id:model.step3)
### 步骤三：初始化&创建组件
```java
// 1. 创建TUIPlayer组件
TUIPlayerView mTUIPlayerView = new TUIPlayerView(Context);

// 2. 设置诸如拉流开始、拉流结束等事件监听
mTUIPlayerView.setTUIPlayerViewListener(new TUIPlayerViewListener() {
        ...
}
```

[](id:model.step4)
### 步骤四：开始&停止播放
- **开始播放**

```java
mTUIPlayerView.startPlay(String url);
```

腾讯云直播支持两种播放协议：WEBRTC 协议（即快直播，更低延时，更强抗性）、RTMP 协议、此处参数 URL 的生成，您可以参考 [示例工程](https://github.com/LiteAV-TUIKit/TUIPlayer/blob/main/Android/app/src/main/java/com/tencent/qcloud/tuikit/tuiplayer/demo/URLUtils.java#L57) 中封装好的 Utils 方法，更多参数信息请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。
- **停止播放**

```java
mTUIPlayerView.stopPlay();
```

[](id:model.step5)
### 步骤五：实现连麦功能（可选）

#### 5.1. **开通云直播服务**：

如果您未开通腾讯云直播相关服务，请先按照如下步骤开通相关服务并完成SDK鉴权：

-   [开通云直播服务](https://console.cloud.tencent.com/live/livestat) 
-   [创建应用并绑定 License](https://console.cloud.tencent.com/live/license) ，并记录下 `LICENSEURL`、`LICENSEURLKEY` 等关键信息。
- 按照如下方式，完成SDK 推流鉴权：

```java
V2TXLivePremier.setLicence(this, "您的LICENSEURL", "您的LICENSEURLKEY");
```

#### 5.2. 开通连麦服务

因为连麦时需要更低的延时需求，需要在腾讯云直播控制台控制台开通对应的连麦应用服务，如果您未开通，请登录**云直播管理控制台**选择 **[应用管理](https://console.cloud.tencent.com/live/micro/appmanage)** ，单击 **新建连麦应用** 输入应用名称（例如 `TUIPlayer` ），然后在该应用的对应操作栏中，选择**应用信息**进入应用管理页，查看并记录应用的 **SDKAppID** 和 **SECRETKEY（密钥）** 。
![img](https://qcloudimg.tencent-cloud.cn/raw/cb2b2381b92994404dfece3cdaf77608.png)

#### 5.3. 组件登录

因为连麦服务，需要观众与主播相互通信，所以需要进行单独登录，登录流程如下：

```java
  TUILogin.init(this, "您的SDKAppId", config, new V2TIMSDKListener() {
            @Override
            public void onKickedOffline() {  // 登录被踢下线通知（示例：账号在其他设备登录）
            }
            @Override
            public void onUserSigExpired() { // userSig过期通知
            }
  });
  TUILogin.login("您的userId", "您的userSig", new V2TIMCallback() {
            @Override
            public void onError(int code, String msg) {
                Log.d(TAG, "code: " + code + " msg:" + msg);
            }
            @Override
            public void onSuccess() {
            }
  });
```

**登录组件参数说明：**
- **SDKAppID**：即服务开通中记录到的 **SDKAppID** 信息。
- **SECRETKEY**： 即服务开通中记录到的 **SECRETKEY（密钥）**。
- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [示例工程](https://github.com/LiteAV-TUIKit/TUIPlayer/blob/main/Android/app/src/main/java/com/tencent/qcloud/tuikit/tuiplayer/demo/debug/GenerateTestUserSig.java#L125) 自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/454/14548) 。


#### 5.4. 开始&停止连麦

在TUIPlayer 组件内部已经封装好了连麦功能，完成上述步骤后，即可单击**连麦**按钮发起&停止连麦，如您需要修改连麦 icon 或显示位置，详情请参见 [连麦按钮](https://github.com/LiteAV-TUIKit/TUIPlayer/blob/main/Android/tuiplayer/src/main/res/layout/tuiplayer_container_view.xml#L42) 文件。

[](id:model.step6)
### 步骤六：集成弹幕、点赞等挂件功能（可选）
我们在自己的 [小直播](https://github.com/tencentyun/XiaoZhiBo) 工程中使用了该 `TUIPlayer` 组件并集成了其他 `TUIKit` 组件，您可以以此为参考自行实现。

## 交流&反馈

更多帮助信息，详情请参见 [TUI 场景化解决方案常见问题](https://cloud.tencent.com/developer/article/1952880)。欢迎加入 QQ 群：**592465424**，进行技术交流和反馈。
