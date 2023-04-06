## 升级说明

TUICallKit 是腾讯云推出一款新的音视频通话 UI 组件，**是 TUICalling 的升级版本**，TUICallKit 体积更小，稳定性更好，也支持更多特性：

- 更加简单易用的 API、更加全面的通话回调、集成包体体积更小。
- 全面升级群组通话功能：支持通话过程中邀请他人加入，主动加入通话等全新能力。
- 更加灵活的参数设置：新增美颜强度设置，新增编码参数设置，新增渲染参数设置。
- 新增音视频通话专属功能：新增弱网环境通话卡顿优化、A 降噪能力、通话悬浮窗。
- 更多特性：支持多端登录、支持服务端结束通话等等。

欢迎您使用新的 TUICallKit 组件，在升级前您需要了解到：

- **TUICalling 和 TUICallKit 支持相互呼叫**，升级前后，请保持 SDKAppID 不变，否则会影响相互通信；
- TUICallKit 需要搭配 IM 音视频通话能力套餐，可以单击 [IM 控制台](https://console.cloud.tencent.com/im)，进入对应 SDKAppID 应用的 **基本配置** 页面，并在页面的右下角找到 **开通腾讯实时音视频服务** 功能区，单击 **免费体验** 即可开通 TUICallKit 的 7 天免费试用服务。如果需要正式应用上线，可以单击 [**前往加购**](https://buy.cloud.tencent.com/avc) 即可进入购买页面。

<img width= 900px src="https://qcloudimg.tencent-cloud.cn/image/document/f98927f3fc851357ac5e491e6aed442b.png">

>IM 音视频通话能力针对不同的业务需求提供了差异化的付费版本供您选择，您可以在 [IM 购买页](https://buy.cloud.tencent.com/avc) 了解包含功能并选购您适合的版本。


## 升级步骤

TUICallKit 在设计之初就兼顾了 TUICalling 客户的升级诉求，仅需要简单两步就可以升级完成，预计花费 20 分钟；

### 升级依赖为TUICallKit
在您的工程中完成对TUICallKit的依赖升级，对您的工程的配置文件pubspec.yaml进行设置：

```
dependencies:
  #删除旧的依赖tim_ui_kit_calling_plugin，并添加新的依赖tencent_calls_uikit:
  tencent_calls_uikit:
```

设置完成后执行` flutter pub get` 命令。

 > 如果您之前是配合 TUIChat、TUIContact 等IM 组件一起使用的话，执行完这个步骤即可正常使用 TUICallKit，TUICallKit 组件内部已经处理好兼容逻辑。
 > 


### 修改 API 使用

在完成上述步骤后，您的工程就无法正常编译了，需要将 TUICalling API 替换成新的 TUICallKit API，可以参照如下 API 对比信息，搜索替换即可。
<table>
<tr>
<th rowspan="1" colSpan="1" >API 含义</th>

<th rowspan="1" colSpan="1" >TUICalling（tim\_ui\_kit\_calling\_plugin）</th>

<th rowspan="1" colSpan="1" >TUICallKit（tencent\_calls\_uikit）</th>

<td rowspan="1" colSpan="1" >备注</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >创建 TUICallKit 实例</td>

<td rowspan="1" colSpan="1" >TUICalling.sharedInstance</td>

<td rowspan="1" colSpan="1" >TUICallKit.[instance](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >替换引用、名称</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >设置用户的昵称</td>

<td rowspan="1" colSpan="1" >TUICalling.setUserNickname</td>

<td rowspan="1" colSpan="1" >TUICallKit.[setSelfInfo](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >设置头像、昵称的接口整合到`setSelfInfo`接口</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >设置用户的头像</td>

<td rowspan="1" colSpan="1" >TUICalling.setUserAvatar</td>

<td rowspan="1" colSpan="1" >TUICallKit.[setSelfInfo](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >设置头像、昵称的接口整合到`setSelfInfo`接口</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >发起 1v1 通话</td>

<td rowspan="1" colSpan="1" >TUICalling.call</td>

<td rowspan="1" colSpan="1" >TUICallKit.[call](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >详见TUICalling.call 接口变更</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >发起群组通话</td>

<td rowspan="1" colSpan="1" >/</td>

<td rowspan="1" colSpan="1" >TUICallKit.[groupCall](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >/</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >主动加入当前的群组通话中</td>

<td rowspan="1" colSpan="1" >/</td>

<td rowspan="1" colSpan="1" >TUICallKit.[joinInGroupCall](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >/</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >设置自定义来电铃音</td>

<td rowspan="1" colSpan="1" >TUICalling.setCallingBell</td>

<td rowspan="1" colSpan="1" >TUICallKit.[setCallingBell](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >替换引用、名称</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >开启/关闭静音模式</td>

<td rowspan="1" colSpan="1" >TUICalling.enableMuteMode</td>

<td rowspan="1" colSpan="1" >TUICallKit.[enableMuteMode](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >替换引用、名称</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >开启/关闭悬浮窗功能</td>

<td rowspan="1" colSpan="1" >TUICalling.enableFloatWindow</td>

<td rowspan="1" colSpan="1" >TUICallKit.[enableFloatWindow](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >替换引用、名称</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >设置监听事件</td>

<td rowspan="1" colSpan="1" >TUICalling.registerListener</td>

<td rowspan="1" colSpan="1" >TUICallEngine.[addObserver](https://cloud.tencent.com/document/product/647/83053)</td>

<td rowspan="1" colSpan="1" >详见TUICalling.registerListener 接口变更</td>
</tr>

</table>


如下是此次升级过程中，变化较大的两个 API 的适配方案：


#### TUICalling.call 接口变更
- **TUICalling 代码示例**

   ```
   //原接口
   Future<void> call(String userId, CallingScenes type, [OfflinePushInfo? offlinePushInfo]);
 
    ```
- **TUICallKit 代码示例**

   ```
   //新接口
   Future<void> call(String userId, TUICallMediaType callMediaType, [TUICallParams? params]);
   
   //新调用方式
   TUIOfflinePushInfo offlinePushInfo = TUIOfflinePushInfo();
  	offlinePushInfo.title = "Flutter TUICallKit";
  	offlinePushInfo.desc = "This is an incoming call from Flutter TUICallkit";
   	TUICallParams params = TUICallParams(offlinePushInfo: offlinePushInfo);
	TUICallKit.instance.call(callUserId, TUICallMediaType.audio, params);
     ```

#### TUICallKit.setCallingListener 接口变更
- **TUICalling 代码示例**

   ``` java
   TUICalling.sharedInstance().registerListener(TUICallingListener(
   		onInvited: (params) {
   		
   		}
   		
   		onCallingCancel: () {
   		
   		}
   		……
   ));
   ```
- **TUICallKit 代码示例**

   ```
TUICallEngine.instance.addObserver(TUICallObserver(
	onError:(int code, String message) {
 	
 	}, 
  
  	onCallCancelled: (String callerId) {
    },
    
    onCallBegin:(TUIRoomId roomId, TUICallMediaType callMediaType, TUICallRole callRole) {
    },
    
    ……
 ));
   ```

   升级完上述 API 后，即可正常使用`TUICallKit`组件。
