本文主要介绍如何快速运行 GME UnrealEngine Demo，以及将工程示例代码接入到项目中。

## 快速跑通 UnrealEngine Demo

### 环境要求

1. UnrealEngine 4.22 及以上版本。
2. Microsoft Visual Studio。
3. 能运行 UnrealEngine 工程的配置环境。

### 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

### 1、申请GME服务

通过[开通指引](https://cloud.tencent.com/document/product/607/10782)申请 GME 实时语音服务，获取到实时语音Appid 和 Key。

### 2、下载工程
通过[下载指引](https://cloud.tencent.com/document/product/607/18521)下载 UnrealEngine Demo。
![](https://qcloudimg.tencent-cloud.cn/raw/272e438685b0aa606367e63c2435957d.png)

### 3、配置工程

下载后打开工程目录，路径 Source\UEDemo1 中，找到 UserConfig.cpp，将图中蓝色框处 appID 及 appKey 修改为步骤 1 中申请的GME实时语音服务 Appid 和 key。

![](https://qcloudimg.tencent-cloud.cn/raw/c49afcc8c67bd631c307bc81801e2e85.png)


### 4、编译运行

#### 1.运行程序

点击编辑器运行按钮，进入 Demo 运行程序。

![](https://qcloudimg.tencent-cloud.cn/raw/eb1b9543db8a5c81c543939313228413.jpg)

#### 2.初始化

- UserId：相当于openid，每个端的openid必须唯一。
- Voice Chat：实时语音功能界面。
- Voice Message：语音消息功能界面。

点击【Login】按钮，进行初始化，再点击【Voice Chat】按钮进入实时语音房间配置界面。

![](https://qcloudimg.tencent-cloud.cn/raw/ae9123a47b09642211b0aab42498daf2.jpg)

#### 3.实时语音进房

- RoomId：房间号码，同房间的人可以互相语音交流。
- RoomType：请使用 Fluency 进入房间。
- JoinRoom：进入语音房间。
- Back：后退到上一个界面。

配置好实时语音房间号后，点击【JoinRoom】进入实时语音房间。

![](https://qcloudimg.tencent-cloud.cn/raw/8917f419ef433e8be8332ab915438667.jpg)


#### 4.实时语音功能
界面上会显示进房的 Roomid 以及本端的 openid。

- Mic：勾选打开麦克风。
- Speaker：勾选打开扬声器。
- 3D Voice Effect：勾选打开3D音效。
- Voice Change：变声效果。

本端勾选 Mic 及 Speaker 后，另一个终端的机器也重复以上步骤，进入相同的房间，也勾选 Mic 以及 Speaker，便可以互相实施沟通。
如果两个终端都勾选 3D Voice Effect，通过键盘 【A】【S】【D】【W】改变方位，体验3D语音方位感。


![](https://qcloudimg.tencent-cloud.cn/raw/fc3e0b71752adf9477f59137a7090e0e.jpg)


#### 5.语音消息功能

- Language：选择转文本的目标语音，比如说的是中文就选普通话。
- Audio：录音后点击可以收听。
- Audio-to-Text：语音转出来的文本内容。
- Push To Talk：按住进行录音。
- Back：后退到上一个界面。

按住 【Push to Talk】按钮，对着麦克风进行说话，放开后语音会转成文本显示在界面中。

![](https://qcloudimg.tencent-cloud.cn/raw/81bea5a9a41cd781bd0f9f4eea7c3241.jpg)


## 工程示例代码介绍

使用 GME 实时语音主要的流程是 Init->EnterRoom->EnableMic->EnableSpeaker。Demo 主要的代码在 BaseViewController.cpp 以及ExperientialDemoViewController.cpp 中。


### 初始化相关

初始化相关的代码在 BaseViewController.cpp 文件中的 InitGME 函数中。这里面包含了初始化、语音消息的鉴权初始化以及设置回调TMGDelegate。

```
int UBaseViewController::InitGME(std::string sdkAppId, std::string sdkAppKey, std::string userId) {

	int nAppid = atoi(sdkAppId.c_str());
	int ret = ITMGContextGetInstance()->Init(sdkAppId.c_str(), userId.c_str());
	ITMGContextGetInstance()->SetTMGDelegate(this);

	int RetCode = (int) ITMGContextGetInstance()->CheckMicPermission();
	FString msg = FString::Printf(TEXT("check Permission retcode =%d"), RetCode);
	GEngine->AddOnScreenDebugMessage(INDEX_NONE, 10.0f, FColor::Yellow, *msg);

	char strSig[128] = {0};
	unsigned int nLength = 128;
	nLength = QAVSDK_AuthBuffer_GenAuthBuffer(nAppid, "0", userId.c_str(), sdkAppKey.c_str(), (unsigned char *)strSig, nLength);
	ITMGContextGetInstance()->GetPTT()->ApplyPTTAuthbuffer(strSig, nLength);
   
	m_appId = sdkAppId;
	m_appKey = sdkAppKey;
	m_userId = userId;
	m_isEnableTips = false;
	m_tipsMark = 0;
	return ret;
}
```

使用 GME 需要周期性的调用 Poll 函数。在 UEDemoLevelScriptActor.cpp 脚本中的 Tick 中调用。

```
void AUEDemoLevelScriptActor::Tick(float DeltaSeconds) {
	Super::Tick(DeltaSeconds);	

	m_pTestDemoViewController->UpdateTips();
	m_pCurrentViewController->UpdatePosition();
	ITMGContextGetInstance()->Poll();
}
```

### 进房相关
进房相关的代码在 BaseViewController.cpp 文件中的 EnterRoom 函数中。

```
void UBaseViewController::EnterRoom(std::string roomID, ITMG_ROOM_TYPE roomType) {
	int nAppid = atoi(m_appId.c_str());
	UserConfig::SetRoomID(roomID);

	char strSig[128] = {0};
	unsigned int nLength = 128;
	nLength = QAVSDK_AuthBuffer_GenAuthBuffer(nAppid, roomID.c_str(), m_userId.c_str(), m_appKey.c_str(), (unsigned char *)strSig, nLength);
	GEngine->AddOnScreenDebugMessage(INDEX_NONE, 10.0f, FColor::Yellow, TEXT("onEnterRoom"));
	ITMGContextGetInstance()->EnterRoom(roomID.c_str(), roomType, strSig, nLength);
}
```

进房回调在同一脚本中的 OnEvent 函数中。

```
if (eventType == ITMG_MAIN_EVENT_TYPE_ENTER_ROOM) {
		int32 result = JsonObject->GetIntegerField(TEXT("result"));
		FString error_info = JsonObject->GetStringField(TEXT("error_info"));
		if (result == 0) {
			GEngine->AddOnScreenDebugMessage(INDEX_NONE, 20.0f, FColor::Yellow, TEXT("Enter room success."));
		}
		else {
			FString msg = FString::Printf(TEXT("Enter room failed. result=%d, info = %ls"), result, *error_info);
			GEngine->AddOnScreenDebugMessage(INDEX_NONE, 20.0f, FColor::Yellow, *msg);
		}
		onEnterRoomCompleted(result, error_info);
```

### 打开设备
进房成功后打开设备，相关代码在 ExperientialDemoViewController.cpp 中。

```
void UExperientialDemoViewController::onCheckMic(bool isChecked) {
	//GEngine->AddOnScreenDebugMessage(INDEX_NONE, 10.0f, FColor::Yellow, L"onCheckMic");
	ITMGContext *pContext = ITMGContextGetInstance();
	if (pContext) {
		ITMGAudioCtrl *pTmgCtrl = pContext->GetAudioCtrl();
		if (pTmgCtrl) {
			pTmgCtrl->EnableMic(isChecked);
		}
	}
}

void UExperientialDemoViewController::onCheckSpeaker(bool isChecked) {
	//GEngine->AddOnScreenDebugMessage(INDEX_NONE, 10.0f, FColor::Yellow, L"onCheckSpeaker");
	ITMGContext *pContext = ITMGContextGetInstance();
	if (pContext) {
		ITMGAudioCtrl *pTmgCtrl = pContext->GetAudioCtrl();
		if (pTmgCtrl) {
			pTmgCtrl->EnableSpeaker(isChecked);
		}
	}
}
```

### 3D音效相关

3D音效的接入可以参考[3D音效文档](https://cloud.tencent.com/document/product/607/18218)。在 Demo 中，首先初始化 3D 音效功能，相关代码在 ExperientialDemoViewController.cpp 中。

```
void UExperientialDemoViewController::onCheckSpatializer(bool isChecked) {
    char buffer[256]={0};
//    snprintf(buffer, sizeof(buffer), "%s3d_model", getFilePath().c_str());
    snprintf(buffer, sizeof(buffer), "%sgme_2.8_3d_model.dat", getFilePath().c_str());
	int ret1 = ITMGContextGetInstance()->GetAudioCtrl()->InitSpatializer(buffer);
	int ret2 = ITMGContextGetInstance()->GetAudioCtrl()->EnableSpatializer(isChecked, false);
	FString msg = FString::Printf(TEXT("InitSpatializer=%d, EnableSpatializer ret=%d"), ret1, ret2);
	GEngine->AddOnScreenDebugMessage(INDEX_NONE, 10.0f, FColor::Yellow, msg);
}
```

在 UEDemoLevelScriptActor.cpp 脚本 Tick 中调用 UpdatePosition 函数。

```
void AUEDemoLevelScriptActor::Tick(float DeltaSeconds) {
	Super::Tick(DeltaSeconds);	

	m_pTestDemoViewController->UpdateTips();
	m_pCurrentViewController->UpdatePosition();
	ITMGContextGetInstance()->Poll();
}


void UBaseViewController::UpdatePosition() {
	if (!m_isCreated)
		return;

	ITMGRoom *pTmgRoom = ITMGContextGetInstance()->GetRoom();
	if (!pTmgRoom)
	{
		return;
	}

	int nRange = GetRange();
	pTmgRoom->UpdateAudioRecvRange(nRange);

	FVector cameraLocation = UGameplayStatics::GetPlayerCameraManager(m_pActor->GetWorld(), 0)->GetCameraLocation();
	FRotator cameraRotation = UGameplayStatics::GetPlayerCameraManager(m_pActor->GetWorld(), 0)->GetCameraRotation();

	FString msg = FString::Printf(TEXT("location(x=%.2f,y=%.2f,z=%.2f),  rotation(pitch=%.2f,yaw=%.2f,roll=%.2f)"),
		cameraLocation.X, cameraLocation.Y, cameraLocation.Z, cameraRotation.Pitch, cameraRotation.Yaw, cameraRotation.Roll);

	int position[] = { (int)cameraLocation.X,(int)cameraLocation.Y, (int)cameraLocation.Z };
	FMatrix matrix = ((FRotationMatrix)cameraRotation);
	float forward[] = { matrix.GetColumn(0).X,matrix.GetColumn(1).X,matrix.GetColumn(2).X };
	float right[] = { matrix.GetColumn(0).Y,matrix.GetColumn(1).Y,matrix.GetColumn(2).Y };
	float up[] = { matrix.GetColumn(0).Z,matrix.GetColumn(1).Z,matrix.GetColumn(2).Z };


	pTmgRoom->UpdateSelfPosition(position, forward, right, up);
	SetPositionInfo(msg);
}

```

在 ExperientialDemoViewController.cpp 中打开3D效果。

```
void UExperientialDemoViewController::onCheckSpatializer(bool isChecked) {
    char buffer[256]={0};
//    snprintf(buffer, sizeof(buffer), "%s3d_model", getFilePath().c_str());
    snprintf(buffer, sizeof(buffer), "%sgme_2.8_3d_model.dat", getFilePath().c_str());
	int ret1 = ITMGContextGetInstance()->GetAudioCtrl()->InitSpatializer(buffer);
	int ret2 = ITMGContextGetInstance()->GetAudioCtrl()->EnableSpatializer(isChecked, false);
	FString msg = FString::Printf(TEXT("InitSpatializer=%d, EnableSpatializer ret=%d"), ret1, ret2);
	GEngine->AddOnScreenDebugMessage(INDEX_NONE, 10.0f, FColor::Yellow, msg);
}

```