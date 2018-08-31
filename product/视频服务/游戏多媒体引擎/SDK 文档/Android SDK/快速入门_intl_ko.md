## 소개

Tencent Cloud 게임 멀티미디어 엔진 SDK의 사용을 환영합니다. Android 개발자가 Tencent Cloud 게임 멀티미디어 엔진 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 Android 개발에 적합한 빠른 액세스 문서를 소개합니다.


## 사용 프로세스 그림
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)


### GME 사용 주의사항

GME 시작 가이드 문서는 가장 중요한 연결 인터페이스에 대한 정보를 제공하고 더 많은 세부 인터페이스는 [관련 인터페이스 문서]를 참고하십시오(https://cloud.tencent.com/document/product/607/15210).


|중요 인터페이스     | 인터페이스 의미|
| ------------- |:-------------:|
|Init    		|GME 초기화	|
|Poll    		|이벤트 콜백 트리거	|
|EnterRoom	 	|방 입장  		|
|EnableAudioCaptureDevice	 	|캡처 장치 켜기/끄기 	|
|EnableAudioSend		|오디오 업스트림 시작/종료 	|
|EnableAudioPlayDevice    			|재생 장치 켜기/끄기		|
|EnableAudioRecv    					|오디오 다운스트림 시작/종료	|

**설명**
** GME의 인터페이스 호출 성공 후 반환 값은 QAVError.OK, 값은 0입니다.**
** GME의 인터페이는 같은 스레드에서 호출되어야 합니다.**
** GME가 방을 가입하려면 인증이 필요합니다. 인증 관련 부분 내용을 참조하십시오.**

** GME는 Poll 인터페이스를 호출하여 이벤트 콜백을 트리거해야 합니다.**


## 빠른 액세스 절차

### 1. 단일 인스턴스 획득
음성 기능 사용 시 먼저 ITMGContext 개체를 획득해야 합니다.

####  함수 프로토타입 

```
public static ITMGContext GetInstance(Context context)
```

|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| context    |Context |응용프로그램 컨텍스트 개체|


####  샘플 코드  

```
import com.tencent.TMG.ITMGContext; 
TMGContext.getInstance(this);
```

### 2. SDK 초기화
매개변수 획득은 [게임 멀티미디어 엔진 액세스 가이드](https://cloud.tencent.com/document/product/607/10782) 문서를 참조하십시오.
해당 인터페이스는 Tencent Cloud 콘솔의 SDKAppID를 매개변수로 써야 합니다. 더불어 OpenID도 필요하며 해당 OpenID는 하나의 사용자를 유일하게 식별합니다. 규칙은 앱 개발자는 자체적으로 제정하고 앱 내에서는 중복하지 않으면 됩니다(현재는 Int64만을 지원합니다).
SDK 초기화 후 방에 들아갈 수 있습니다.
####  함수 프로토타입

```
ITMGContext public int Init(String sdkAppId, String openID)
```

|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| sdkAppId    	|String  |Tencent Cloud 콘솔의 SDKAppID 번호				|
| openID    		|String  |OpenID는 Int64 유형(string으로 전환 후 가져오기)만 지원하고 반드시 10000보다 크고 사용자 식별에 사용됩니다.|

####  샘플 코드 
```
ITMGContext.GetInstance(this).Init(sdkAppId, openId);
```

### 3. 이벤트 콜백 트리거
업데이트에서의 주기적인 Poll 호출을 통해 이벤트 콜백을 트리거할 수 있습니다.
####  함수 프로토타입

```
ITMGContext int Poll()
```
####  샘플 코드
```
ITMGContext.GetInstance(this).Poll();
```

### 4. 방 가입
생성한 인증 정보를 사용해 방에 입장하면 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM이라는 콜백을 받게 됩니다.
- 방 가입 시 기본적으로 마이크 및 스피커를 켜지 않습니다.
- EnterRoom 인터페이스 호출 전에 먼저 Init 인터페이스를 호출해야 합니다.

####  함수 프로토타입
```
ITMGContext public abstract void  EnterRoom(int roomId, int roomType, byte[] authBuffer)
```

|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| roomId 	|int		|방 번호, 32비트만 지원|
| roomType 	|int		|방 오디오 유형		|
| authBuffer	|byte[]	|인증 번호				|

|오디오 유형     	|의미|매개변수|음량 유형|콘솔 추천 샘플링 속도 설정|적용 시나리오|
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|일반 음질	|1|스피커: 통화 음량. 헤드폰: 미디어 음량	|음질에 특별한 요구가 없는 경우, 16K 샘플링 속도이면 충분합니다.					|유창성이 우선이고 지연 시간이 매우 짧은 음성 채팅으로 게임에서 팀 배틀에 적용되고 FPS, MOBA와 같은 게임에 적합합니다.	|							
| ITMG_ROOM_TYPE_STANDARD			|표준 음질	|2|스피커: 통화 음량. 헤드폰: 미디어 음량	|필요한 음질에 따라 16K/48K 샘플링 속도를 선택할 수 있습니다.				|음질이 비교적 좋고 시간 지연이 적당하여 마피아 게임, 보드게임 등 캐쥬얼 게임의 실시간 통화 시나리오에 적합합니다.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|고음질	|3|스피커: 미디어 음량. 헤드폰: 미디어 음량	|최적의 효과를 보증하기 위해서 콘솔에서 48K 샘플링 속도의 고음질 구성을 설정하기를 권장합니다.	|초고음질, 지연시간이 상대적으로 커서 음악, 댄스 등 게임 및 음성 소셜류 앱에 적합합니다. 음악방송, 온라인 노래방 등 음질 요구가 있는 시나리오에 적합합니다 	|

- 음량 유형 또는 시나리오에 특별한 요구가 있는 경우 온라인 고객 서비스에 연락하십시오.
- 콘솔 샘플링 속도 설정은 게임 음성 효과에 직접 영향을 줄 수 있으므로 [콘솔](https://console.cloud.tencent.com/gamegme)에서 샘플링 속도 설정이 항목 사용 시나리오에 적합한지 다시 확인하십시오.
####  샘플 코드  
```
ITMGContext.GetInstance(this).EnterRoom(Integer.parseInt(relationId),roomType, authBuffer);    
```

### 5. 방 가입 이벤트 콜백
방 가입 완료 후 콜백이 있으며 메시지는 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM입니다.
콜백 관련 매개변수 코드를 설정합니다.
```
private ITMGContext.ITMGDelegate itmgDelegate = null;
itmgDelegate= new ITMGContext.ITMGDelegate() {
            @Override
 			public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
                }
        };
```
관련 매개변수 코드를 콜백하여 처리합니다.
####  샘플 코드  
```
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_ENTER_ROOM == type)
        {
           	 //방 입장 성공 이벤트 수신
        }
	}
```

### 6. 캡처 장치 켜기/끄기
해당 인터페이스는 캡처 장치 켜기/끄기에 사용합니다. 방 가입 시 기본적으로 장치를 켜지 않습니다.
- 방에 입장한 후에야 해당 인터페이스를 호출할 수 있고 방을 나가면 자동으로 장치를 끕니다.
- 모바일에서 캡처 장치 켜는 동시에 일반적으로 권한 신청, 음량 유형 조정 등을 조작이 수반됩니다.

####  함수 프로토타입  
```
ITMGContext public int EnableAudioCaptureDevice(boolean isEnabled)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |캡처 장치를 켜야 하는 경우 매개변수 true를 가져오고, 캡처 장치를 종료해야 하는 경우 false를 가져옵니다.|

#### 샘플 코드

```
캡처 장치 켜기
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioCaptureDevice(true);
```


### 7. 오디오 업스트림 시작/종료
해당 인터페이스는 오디오 업스트림 시작/종료에 사용합니다. 캡처 장치가 이미 시작된 경우, 캡처한 오디오 데이터를 전송합니다. 캡처 장치가 시작되지 않은 경우 여전히 소리가 무성입니다. 캡처 장치의 켜기/끄기는 인터페이스 EnableAudioCaptureDevice를 참조합니다.

#### 함수 프로토타입

```
ITMGContext public int EnableAudioSend(boolean isEnabled)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |오디오 업스트림을 시작해야 하는 경우 매개변수 TRUE를 가져오고, 오디오 업스트림을 종료해야 하는 경우 매개변수 FALSE를 가져옵니다.|

#### 샘플 코드  

```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioSend(true);
```


### 8. 재생 장치 켜기/끄기
해당 인터페이스는 재생 장치 켜기/끄기에 사용합니다.

#### 함수 프로토타입  
```
ITMGContext public int EnableAudioPlayDevice(boolean isEnabled)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| isEnabled    |Boolean        |재생 장치를 닫아야 하는 경우 가져온 매개변수는 FALSE이고, 재생 장치를 열어야 하는 경우 매개변수는 TRUE입니다.|
#### 샘플 코드  
```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioPlayDevice(true);
```

###9. 오디오 다운스트림 시작/종료
해당 인터페이스는 오디오 다운스트림 시작/종료에 사용합니다. 재생 장치가 이미 켜져 있는 경우 방의 다른 사람의 오디오 데이터를 재생합니다. 재생 장치가 켜지지 않은 경우 여전히 소리가 무성입니다. 재생 장치의 켜기/끄기는 인터페이스 EnableAudioPlayDevice를 참고합니다.

#### 함수 프로토타입  

```
ITMGContext public int EnableAudioRecv(boolean isEnabled)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |오디오 다운스트림을 시작해야 하는 경우 매개변수 TRUE를 가져오고, 오디오 다운스트림을 종료해야 하는 경우 매개변수 FALSE를 가져옵니다.|

#### 샘플 코드  

```
ITMGContext.GetInstance(this).GetAudioCtrl().EnableAudioRecv(true);
```



## 인증
### 음성 채팅 인증 정보
AuthBuffer를 생성하고 관련 기능의 암호화와 인증에 사용됩니다. 관련 매개변수 획득 및 세부 정보는 [GME 키 문서](https://cloud.tencent.com/document/product/607/12218)를 참조하십시오.    
해당 인터페이스 반환 값은 Byte[] 유형입니다. 오프라인 음성이 인증을 획득할 때 방 번호 매개변수는 반드시 0을 입력해야 합니다.

####  함수 프로토타입
```
AuthBuffer public native byte[] genAuthBuffer(int sdkAppId, int roomId, String identifier, String key)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| appId    		|int   		|Tencent Cloud 콘솔의 SDKAppID 번호		|
| roomId    		|int   		|방 번호, 32비트만 지원				|
| openID    	|String 	|사용자 ID					|
| key    		|string 	|Tencent Cloud 콘솔의 키				|


####  샘플 코드  
```
import com.tencent.av.sig.AuthBuffer;//헤더 파일
byte[] authBuffer=AuthBuffer.getInstance().genAuthBuffer(Integer.parseInt(sdkAppId), Integer.parseInt(strRoomID),identifier, key);
```

