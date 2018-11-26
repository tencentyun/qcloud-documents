## 소개
Tencent Cloud GME SDK의 사용을 환영합니다. Windows 개발자가 Tencent Cloud GME 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 Windows 개발에 적합한 액세스 기술 문서를 소개합니다.


## 사용 프로세스 그림

### 음성 채팅 프로세스 그림
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)
### 오프라인 음성의 문자로 전환 프로세스 그림
![](https://main.qcloudimg.com/raw/4c875d05cd2b4eaefba676d2e4fc031d.png)

### GME 사용 중요사항

|중요 인터페이스     | 인터페이스 의미|
| ------------- |:-------------:|
|Init    		|GME 초기화 	|
|Poll    		|이벤트 콜백 트리거	|
|EnterRoom	 	|방 입장  		|
|EnableMic	 	|마이크 켜기 	|
|EnableSpeaker		|스피커 켜기 	|

>**설명: **

**GME의 인터페이스 호출 성공 후 반환 값은 QAVError.OK이고, 수치는 0입니다.**

**GME의 인터페이스는 같은 스레드에서 호출되어야 합니다.**

**GME가 방을 가입하려면 인증이 필요합니다. 인증 관련 부분 내용을 참조하십시오.**

**GME는 Poll 인터페이스를 주기적으로 호출하여 이벤트 콜백을 트리거해야 합니다.**

**GME 콜백 정보는 콜백 메시지 리스트를 참조하십시오.**

**방에 입장한 후에 장치에 대한 조작을 실행할 수 있습니다.**

**이 문서에 해당하는 GME SDK 버전은 2.2입니다.**

## 관련 인터페이스 초기화
초기화 전에 SDK는 미초기화 단계에 속하고 있습니다. 초기화 인증 후 SDK를 초기화해야 방에 입장할 수 있습니다.

|인터페이스     | 인터페이스 의미   |
| ------------- |:-------------:|
|Init    	|GME 초기화	| 
|Poll    	|이벤트 콜백 트리거	|
|Pause   	|시스템 일시 중지	|
|Resume 	|시스템 다시 시작	|
|Uninit    	|GME 반초기화 	|


### 싱글 인스턴스 획득
GMESDK는 싱글 인스턴스 형식으로 제공되며, 호출은 모두 ITMGContext에서 시작되어 ITMGDelegate를 통해 응용프로그램에 콜백되기 때문에 반드시 사전 설정해야 합니다.    
#### 함수 프로토타입 

```
ITMGContext virtual void TMGDelegate(ITMGDelegate* delegate)
```
#### 샘플 코드  

```
ITMGContext* m_pTmgContext;
m_pTmgContext = ITMGContextGetInstance();
```


### 메시지 전송
Delegate 방법을 채택한 인터페이스는 응용프로그램에 콜백 알림을 발송하는 데 사용됩니다. 메시지 유형은 ITMG_MAIN_EVENT_TYPE를 참조하며 데이터는 Windows 플랫폼에서 json 문자열 형식입니다. 키-값에 대한 자세한 내용은 설명 문서를 참조하십시오.

#### 샘플 코드 

```
//함수 구현:
class Callback : public SetTMGDelegate 
{
	virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data)
	{
  		switch(eventType)
  		{
//메시지 유형 판단 및 처리
  		}
 	}
}

Callback*  p = new Callback ();
m_pTmgContext->TMGDelegate(p);

```

### SDK 초기화

매개변수 획득에 대한 정보는 문서 [GME 액세스 가이드](https://cloud.tencent.com/document/product/607/10782)를 참조하십시오.
해당 인터페이스는 Tencent Cloud 콘솔의 SDKAppID 번호를 매개변수로 써야 합니다. 더불어 OpenID도 필요하며 해당 OpenID는 하나의 사용자를 유일하게 식별합니다. 규칙은 앱 개발자가 자체적으로 제정하고 앱 내에서는 중복하지 않으면 됩니다(현재는 Int64만 지원).
SDK 초기화 후 방에 들아갈 수 있습니다.
#### 함수 프로토타입 

```
ITMGContext virtual void Init(const char* sdkAppId, const char* openId)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| SDKAppID    	|char*   	|Tencent Cloud 콘솔의 SDKAppID 번호					|
| openID    	|char*   	|OpenID는 Int64 유형(string으로 전환 후 가져오기)만 지원하고 반드시 10000보다 크며 사용자 ID 식별에 사용합니다. 	|

#### 샘플 코드  

```
#define SDKAPPID3RD "1400035750"
cosnt char* openId="10001";
ITMGContext* context = ITMGContextGetInstance();
context->Init(SDKAPPID3RD, openId);
```


### 이벤트 콜백 트리거

update에서의 주기적인 Poll 호출을 통해 이벤트 콜백을 트리거할 수 있습니다.
#### 함수 프로토타입

```
class ITMGContext {
protected:
    virtual ~ITMGContext() {}
    
public:    	
	virtual void Poll()= 0;
}

```
#### 샘플 코드
```
//헤드 파일의 선언
//코드 구현
void TMGTestScene::update(float delta)
{
    ITMGContextGetInstance()->Poll();
}
```


### 시스템 일시 중지

시스템에 일시 중지가 발생하는 동시에 엔진에 Pause를 알려야 합니다.
#### 함수 프로토타입

```
ITMGContext int Pause()
```

### 시스템 디시 시작
시스템 이벤트가 다시 시작되면 엔진에도 동시 Resume 진행을 알려야 합니다.
#### 함수 프로토타입

```
ITMGContext  int Resume()
```



### SDK 반초기화
SDK 반초기화, 미초기화 상태에 들어갑니다.

#### 함수 프로토타입 
```
ITMGContext int Uninit()

```
#### 샘플 코드  
```
ITMGContext* context = ITMGContextGetInstance();
context->Uninit();
```


## 음성 채팅 방 관련 인터페이스
초기화 후, SDK로 방 입장을 호출하여 방에 입장해야만 음성 채팅 통화를 진행할 수 있습니다.

|인터페이스     | 인터페이스 의미   |
| ------------- |:-------------:|
|GenAuthBuffer    	|인증 초기화|
|EnterRoom   		|방 가입|
|IsRoomEntered   	|방 입장 여부|
|ExitRoom 		|방 퇴장|
|ChangeRoomType 	|사용자 방 오디오 유형 수정|
|GetRoomType 		|사용자 방 오디오 유형 획득|


### 인증 정보
AuthBuffer를 생성하고 관련 기능의 암호화와 인증에 사용됩니다. 관련 백 엔드 배포는 [GME 키 문서](https://cloud.tencent.com/document/product/607/12218)를 참조하십시오.    
오프라인 음성이 인증을 획득할 때, 방 번호 매개변수는 0을 써야 합니다.

#### 함수 프로토타입
```
QAVSDK_AUTHBUFFER_API int QAVSDK_AUTHBUFFER_CALL QAVSDK_AuthBuffer_GenAuthBuffer(unsigned int nAppId, const char* dwRoomID, const char* strOpenID, const char* strKey, unsigned char* strAuthBuffer, unsigned int bufferLength);
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| nAppID    			|int   		|Tencent Cloud 콘솔의 SDKAppID 번호		|
| dwRoomID    		|char*     |방 번호, 최대 127자 지원(오프라인 음성 방 번호 매개변수는 반드시 0을 써야 함)|
| strOpenID  		|char*    		|사용자 ID								|
| strKey    			|char*	    	|Tencent Cloud [콘솔](https://console.cloud.tencent.com/gamegme)의 키					|
|strAuthBuffer		|char*	    	|반환한 authbuff							|
| buffLenght   		|int    		|반환한 authbuff의 길이					|



#### 샘플 코드  
```
unsigned int bufferLen = 512;
unsigned char retAuthBuff[512] = {0};
QAVSDK_AuthBuffer_GenAuthBuffer(atoi(SDKAPPID3RD), roomId, "10001", AUTHKEY,strAuthBuffer,&bufferLen);
```

### 방 가입
생성한 인증 정보를 사용해 방에 진입하면 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM이라는 콜백을 받게 됩니다. 방 가입 시 기본적으로 마이크 및 스피커를 켜지 않습니다.
일반 음성 방에 입장하고 비즈니스 측면에서 팀 음성 요구가 없는 경우 일반 방 입장 인터페이스를 사용합니다. 세부 정보는 [GME 팀 음성 문서](https://cloud.tencent.com/document/product/607/17972)를 참조하십시오.

#### 함수 프로토타입

```
ITMGContext virtual void EnterRoom(const char*  roomId, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen)//일반 방 입장 인터페이스
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| roomID			| char*    		|방 번호, 최대 127자 지원	|
| roomType 			|ITMG_ROOM_TYPE	|방 오디오 유형		|
| authBuffer    		|char*     	|인증 번호			|
| buffLen   			|int   		|인증 번호 길이		|

|오디오 유형     	|의미|매개변수|음량 유형|콘솔 추천 샘플링 속도 설정|적용 시나리오|
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|보통 음질	|1|스피커: 통화 음량. 헤드폰: 미디어 음량	|음질에 대해 특별한 요구가 없을 경우 16K 샘플링 속도라면 충분합니다.					|유창성이 우선이고 지연 시간이 매우 짧은 음성 채팅으로 게임에서 팀 배틀에 적용되고 FPS, MOBA와 같은 게임에 적합합니다.	|							
| ITMG_ROOM_TYPE_STANDARD			|표준 음질	|2|스피커: 통화 음량. 헤드폰: 미디어 음량	|필요한 음질에 따라 16K/48K 샘플링 속도를 선택할 수 있습니다.				|음질이 비교적 좋고 시간 지연이 적당하여 마피아 게임, 보드게임 등 캐주얼 게임의 실시간 통화 시나리오에 적합합니다.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|고음질	|3|스피커: 미디어 음량, 헤드폰: 미디어 음량	|최적의 효과를 보증하기 위해서 콘솔에서 48K 샘플링 속도의 고음질 구성을 설정하기를 권장합니다. 	|초고음질, 지연시간이 상대적으로 길어서 음악, 댄스 등 게임 및 음성 소셜류 앱에 적용합니다. 음악방송, 온라인 노래방 등 음질 요구가 있는 시나리오에 적용합니다.	|

- 음량 유형 또는 시나리오에 특별한 요구가 있는 경우 온라인 고객 서비스에 연락하십시오.
- 콘솔 샘플링 속도 설정은 게임 음성 효과에 직접 영향을 줄 수 있으므로 [콘솔](https://console.cloud.tencent.com/gamegme)에서 샘플링 속도 설정이 항목 사용 시나리오에 적합한지 다시 확인하십시오.


#### 샘플 코드  

```
ITMGContext* context = ITMGContextGetInstance();
context->EnterRoom(roomId, ITMG_ROOM_TYPE_STANDARD, (char*)retAuthBuff,bufferLen);//일반 음성 방 입장 샘플 코드
```


#### 팀 음성 방
액세스 세부 정보는 [GME 팀 음성 문서](https://cloud.tencent.com/document/product/607/17972)를 참조하십시오.

#### 함수 프로토타입
```
ITMGContext virtual void EnterTeamRoom(const char* roomId, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen, int teamId, int gameAudioMode)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| roomID			| char*    		|방 번호, 최대 127자 지원	|
| roomType 		|ITMG_ROOM_TYPE	|방 오디오 유형				|
| authBuffer    	|char*    	|인증 번호					|
| buffLen   		|int   		|인증 번호 길이				|
| TeamID    		|int    	|가입한 팀 음성 팀 식별 코드(0이 될 수 없음)	|
| audioMode    		|int    	|0은 전역 음석을 의미하고 1은 팀 은성을 나타납니다.		|


|오디오 유형     	|의미|매개변수|음량 유형|콘솔 추천 샘플링 속도 설정|적용 시나리오|
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|보통 음질	|1|스피커: 통화 음량. 헤드폰: 미디어 음량	|음질에 대해 특별한 요구가 없을 경우 16K 샘플링 속도라면 충분합니다.					|유창성이 우선이고 지연 시간이 매우 짧은 음성 채팅으로 게임에서 팀 배틀에 적용되고 FPS, MOBA와 같은 게임에 적합합니다.	|							
| ITMG_ROOM_TYPE_STANDARD			|표준 음질	|2|스피커: 통화 음량. 헤드폰: 미디어 음량	|필요한 음질에 따라 16K/48K 샘플링 속도를 선택할 수 있습니다.				|음질이 비교적 좋고 시간 지연이 적당하여 마피아 게임, 보드게임 등 캐쥬얼 게임의 실시간 통화 시나리오에 적합합니다.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|고음질	|3|스피커: 미디어 음량, 헤드폰: 미디어 음량	|최적의 효과를 보증하기 위해서 콘솔에서 48K 샘플링 속도의 고음질 구성을 설정하기를 권장합니다. 	|초고음질, 지연시간이 상대적으로 커서 음악, 댄스 등 게임 및 음성 소셜류 앱에 적용합니다. 음악방송, 온라인 노래방 등 음질 요구가 있는 시나리오에 적용합니다.	|

#### 샘플 코드  
```
ITMGContext* context = ITMGContextGetInstance();
context->EnterRoom(roomId, ITMG_ROOM_TYPE_STANDARD, (char*)retAuthBuff,bufferLen,1000,0);
```


### 방 가입 이벤트의 콜백
방 가입 완료 후 메시지 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM을 발송하고, OnEvent 함수에서 판단합니다.
#### 코드 설명
```

void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
		}
	}
}
```

### 방 입장 여부 판단
해당 인터페이스를 호출하여 방 입장 여부를 판단할 수 있으며 반환 값은 BOOL 유형입니다.
#### 함수 프로토타입  
```
ITMGContext virtual bool IsRoomEntered()
```
#### 샘플 코드  
```
ITMGContext* context = ITMGContextGetInstance();
context->IsRoomEntered();
```

### 방 퇴장
해당 인터페이스를 호출하여 모든 방에서 퇴장할 수 있습니다. 이것은 동기화 인터페이스이고 호출이 반환되면 점유한 장치의 리소스를 릴리스합니다.
#### 함수 프로토타입  

```
ITMGContext virtual void ExitRoom()
```
#### 샘플 코드  

```
ITMGContext* context = ITMGContextGetInstance();
context->ExitRoom();
```

### 방 퇴장 콜백
방 퇴장 완료 후 콜백이 있으며 메시지는 ITMG_MAIN_EVENT_TYPE_EXIT_ROOM입니다.
#### 샘플 코드  

```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM:
		{
		//처리 진행
		break;
		}
	}
}
```

### 사용자 방 오디오 유형 수정
이 인터페이스는 사용자 방 오디오 유형을 수정하는 데 사용됩니다. 그 결과는 콜백 이벤트를 참조하십시오. 이벤트 유형은 ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE입니다.
#### 함수 프로토타입  
```
IITMGContext TMGRoom public void ChangeRoomType((ITMG_ROOM_TYPE roomType)
```


|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| roomType    |ITMG_ROOM_TYPE    |전환하려는 방 유형, 방 오디오 유형은 EnterRoom 인터페이스를 참조하십시오.|

#### 샘플 코드  
```
ITMGContext* context = ITMGContextGetInstance();
ITMGContextGetInstance()->GetRoom()->ChangeRoomType(ITMG_ROOM_TYPE_FLUENCY);
```


### 사용자 방 오디오 유형 획득
이 인터페이스는 사용자 방 오디오 유형을 획득하는 데 사용되며, 반환 값은 방 오디오 유형입니다. 반환 값이 0이면 사용자 방 오디오 유형에 오류가 발생하였음을 의미합니다. 방 오디오 유형은 EnterRoom 인터페이스를 참조하십시오.

#### 함수 프로토타입  
```
IITMGContext TMGRoom public  int GetRoomType()
```

#### 샘플 코드  
```
ITMGContext* context = ITMGContextGetInstance();
ITMGContextGetInstance()->GetRoom()->GetRoomType();
```


### 방 유형 완료 콜백
방 유형 설정 완료 후 콜백 이벤트 메시지는 ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE이며, 반환한 매개변수는 result, error_info 및 new_room_type이고, new_room_type가 의미하는 정보는 다음과 같습니다. OnEvent 함수에서 이벤트 메시지에 대해 판단합니다.

|이벤트 서브 유형     | 매개변수 표시 값   |의미|
| ------------- |:-------------:|-------------|
| ITMG_ROOM_CHANGE_EVENT_ENTERROOM		|1 	|방 입장 과정에서 자체 보유한 오디오 유형이 방과 부합하지 않아 입장한 방의 오디오 유형으로 수정되었음을 의미합니다.	|
| ITMG_ROOM_CHANGE_EVENT_START			|2	|이미 방 안에 있고 오디오 유형 전환이 시작되었음을 의미합니다(예를 들어, ChangeRoomType 인터페이스 호출 후 오디오 유형 전환)|
| ITMG_ROOM_CHANGE_EVENT_COMPLETE		|3	|이미 방 안에 있고 오디오 유형 전환이 완료되었음을 의미합니다.|
| ITMG_ROOM_CHANGE_EVENT_REQUEST			|4	|방 멤버가 ChangeRoomType 인터페이스를 호출하여 방 오디오 유형 전환을 요청하였음을 의미합니다.|	


#### 샘플 코드  
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE == type)
        {
		//방 유형 이벤트에 대해 처리
	 }
}
```

### 멤버 상태 변화
이 이벤트는 상태가 변화해야 알리며, 상태가 변화하지 않는 상황에서는 알리지 않습니다. 멤버 상태를 실시간으로 획득하려면 상위 계층에서 알림을 수신할 때 캐시를 하십시오. 이벤트 메시지는 ITMG_MAIN_EVNET_TYPE_USER_UPDATE이고 그 중 데이터는 event_ID 및 user_list 2개의 정보를 포함하며 OnEvent 함수에서 정보 event_ID를 판단해야 합니다.
오디오 이벤트 알림에는 임계값이 있어 임계값을 초과해야만 알림이 발송됩니다. 2초 이후에도 오디오 패킷을 수신하지 못해야 ‘어떤 멤버가 오디오 패킷 발송을 중지합니다’ 메시지가 발송됩니다.

|event_ID     | 의미         |앱 관리 내용|
| ------------- |:-------------:|-------------|
|ITMG_EVENT_ID_USER_ENTER    				|멤버 방 입장			|앱에 멤버 리스트 관리		|
|ITMG_EVENT_ID_USER_EXIT    				|멤버 방 퇴장			|앱에 멤버 리스트 관리		|
|ITMG_EVENT_ID_USER_HAS_AUDIO    		|멤버 오디오 패킷 발송		|앱에 통화 멤버 리스트 관리	|
|ITMG_EVENT_ID_USER_NO_AUDIO    			|멤버 오디오 패킷 발송 중지	|앱에 통화 멤버 리스트 관리	|

#### 샘플 코드  

```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
            case ITMG_MAIN_EVNET_TYPE_USER_UPDATE:
		{
		//처리 진행
		//개발자가 매개변수를 해석하여 메시지 event_ID 및 user_list 획득
		    switch (eventID)
 		    {
 		    case ITMG_EVENT_ID_USER_ENTER:
  			    //멤버 방 입장
  			    break;
 		    case ITMG_EVENT_ID_USER_EXIT:
  			    //멤버 방 퇴장
			    break;
		    case ITMG_EVENT_ID_USER_HAS_AUDIO:
			    //멤버 오디오 패킷 발송
			    break;
		    case ITMG_EVENT_ID_USER_NO_AUDIO:
			    //멤버 오디오 패킷 발송 중지
			    break;
 		    default:
			    break;
		    }
		break;
		}
	}
}
```

### 품질 모니터링 이벤트
품질 모니터링 이벤트, 이벤트 메시지는 ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_QUALITY이며, 반환한 매개변수는 weight, floss 및 delay이고 의미하는 정보는 다음과 같습니다. OnEvent 함수에서 이벤트 메시지에 대해 판단합니다.

|매개변수     | 의미         |
| ------------- |-------------|
|weight    				|범위는 1 ~ 50으로 50이면 음질이 매우 우수하며, 1이면 음질이 아주 떨어져 거의 사용할 수 없습니다. 0은 초기값으로 의미가 없습니다.|
|floss    				|패킷 손실률|
|delay    		|오디오 리치 지연 시간(ms)|


### 메시지 세부 정보

|메시지     | 메시지 의미   
| ------------- |:-------------:|
|ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    				       |오디오/비디오 방 입장 메시지|
|ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    				         	|오디오/비디오 방 퇴장 메시지|
|ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    		       |네트워크 등 원인으로 방 연결이 끊김 메시지|
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE				|방 유형 변화 이벤트|

### 메시지에 해당 데이터 세부 정보
|메시지     | 데이터         |예|
| ------------- |:-------------:|------------- |
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    				|result; error_info					|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    				|result; error_info  					|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    		|result; error_info  					|{"error_info":"waiting timeout, please check your network","result":0}|
| ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE    		|result; error_info; new_room_type	|{"error_info":"","new_room_type":0,"result":0}|


## 음성 채팅 오디오 인터페이스
SDK 초기화 후 방에 입장해야 방에서 실시간 오디오 음성 관련 인터페이스를 호출할 수 있습니다.
호출 시나리오 예시:
사용자가 인터페이스에서 마이크/스피커 켜기/끄기 버튼을 클릭할 때 다음 방식을 채택하길 권합니다.
- 대부분의 게임 앱의 경우, EnableMic 및 EnbaleSpeaker 인터페이스를 호출하는 것을 권장합니다. 즉, EnableAudioCaptureDevice/EnableAudioSend 및 EnableAudioPlayDevice/EnableAudioRecv 인터페이스를 동시에 호출해야 합니다.

- 소셜 앱과 같은 다른 유형의 모바일 앱은 캡처 장치를 시작/종료하면 전체 장치(캡처 및 재생)가 다시 시작됩니다. 이때 앱이 배경 음악을 재생 중이라면 그 음악은 재생이 중단됩니다. 업/다운스트림에 대한 제어를 통해 마이크 켜기/끄기를 진행하면 재생 장치가 중단되지 않습니다. 구체적인 호출 방식은 다음과 같습니다. 방에 입장할 때 EnableAudioCaptureDevice(true) && EnabledAudioPlayDevice(true)를 1회 호출하고, 마이크 켜기/끄기를 클릭할 때 EnableAudioSend/Recv만 호출하여 오디오 발송/수신 여부를 제어합니다.

목적이 상호 배타적이라면(녹음 권한을 릴리스하여 다른 모듈에 부여) PauseAudio/ResumeAudio 사용을 권장합니다.

|인터페이스     | 인터페이스 의미   |
| ------------- |:-------------:|
|PauseAudio    				       	   |오디오 엔진 일시 중지		|
|ResumeAudio    				      	 |오디오 엔진 다시 시작		|
|GetMicListCount    				       	|마이크 장치 수량 획득|
|GetMicList    				      	|마이크 장치 열거|
|GetSpeakerListCount    				      	|스피커 장치 수량 획득|
|GetSpeakerList    				      	|스피커 장치 열거|
|SelectMic    				      	|마이크 장치 검색|
|SelectSpeaker    				|스피커 장치 검색|
|EnableMic    						|마이크 켜기/끄기|
|GetMicState    						|마이크 상태 획득|
|EnableAudioCaptureDevice    		|캡처 장치 켜기/끄기		|
|IsAudioCaptureDeviceEnabled    	|캡처 장치 상태 획득	|
|EnableAudioSend    				|오디오 업스트림 시작/종료	|
|IsAudioSendEnabled    				|오디오 업스트림 상태 획득	|
|GetMicLevel    						|실시간 마이크 음량 획득	|
|SetMicVolume    					|마이크 음량 설정		|
|GetMicVolume    					|마이크 음량 획득		|
|EnableSpeaker    					|스피커 켜기/끄기|
|GetSpeakerState    					|스피커 상태 획득|
|EnableAudioPlayDevice    			|재생 장치 켜기/끄기		|
|IsAudioPlayDeviceEnabled    		|재생 장치 상태 획득	|
|EnableAudioRecv    					|오디오 다운스트림 시작/종료	|
|IsAudioRecvEnabled    				|오디오 다운스트림 상태 획득	|
|GetSpeakerLevel    					|실시간 스피커 음량 획득	|
|SetSpeakerVolume    				|스피커 음량 설정		|
|GetSpeakerVolume    				|스피커 음량 획득		|
|EnableLoopBack    					|인이어 켜기/끄기			|

### 오디오 엔진 캡처와 재생 일시 중지
이 인터페이스를 호출하여 오디오 엔진 캡처와 재생을 일시 중지합니다. 이 인터페이스는 동기화 인터페이스로 방 입장 이후에만 유효합니다.
단독으로 캡처를 릴리스하거나 장치를 재생하려면 인터페이스 EnableAudioCaptureDevice 및 EnableAudioPlayDevice를 참조하십시오.

#### 함수 프로토타입  

```
ITMGContext ITMGAudioCtrl int PauseAudio()
```
#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->PauseAudio();
```

### 오디오 엔진 캡처과 재생 다시 시작
이 인터페이스를 호출하여 오디오 엔진 캡처와 재생을 다시 시작합니다. 이 인터페이스는 동기화 인터페이스로 방 입장 이후에만 유효합니다.
#### 함수 프로토타입  

```
ITMGContext ITMGAudioCtrl int ResumeAudio()
```
#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->ResumeAudio();
```



### 마이크 장치 수량 획득
이 인터페이스는 마이크 장치 수량 획득에 사용됩니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetMicListCount()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicListCount();
```

### 마이크 장치 열거
이 인터페이스는 마이크 장치 열거에 사용됩니다. GetMicListCount 인터페이스와 함께 사용합니다.

#### 함수 프로토타입 
```
ITMGAudioCtrl virtual int GetMicList(TMGAudioDeviceInfo* ppDeviceInfoList, int nCount)

class TMGAudioDeviceInfo
{
public:
	const char* pDeviceID;
	const char* pDeviceName;
};
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| ppDeviceInfoList    	|TMGAudioDeviceInfo   	|장치 리스트		|
| nCount    		|int     		|획득한 마이크 장치 수량	|
#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicList(ppDeviceInfoList,nCount);
```



### 마이크 장치 선택
이 인터페이스는 마이크 장치 선택에 사용됩니다. 호출하지 않거나 공백 문자를 전송하면 시스템의 기본 장치를 선택합니다.
#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int SelectMic(const char* pMicID)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| pMicID    |char*      |마이크 장치 ID|
#### 샘플 코드  
```
const char* pMicID ="1";
ITMGContextGetInstance()->GetAudioCtrl()->SelectMic(pMicID);
```

### 마이크 켜기/끄기
이 인터페이스는 마이크 켜기/끄기에 사용됩니다. 방 가입 시 기본적으로 마이크 및 스피커를 켜지 않습니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual void EnableMic(bool bEnabled)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| bEnabled    |bool     |마이크를 켜야 하는 경우 매개변수 TRUE를 가져오고, 마이크를 꺼야 하는 경우 매개변수 FALSE를 가져옵니다.		|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableMic(true);
```


### 마이크 상태 획득
이 인터페이스는 마이크 상태를 획득하는 데에 사용됩니다. 반환 값 0은 마이크가 꺼져 있음을 의미하며, 반환 값 1은 마이크가 켜져 있음을 의미하며, 반환 값 2는 마이크가 실행 중임을 의미하며, 반환 값 3은 마이크가 없음을 의미하며, 반환 값 4는 장치가 초기화되지 않았음을 의미합니다.
#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetMicState()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicState();
```


### 캡처 장치 켜기/끄기
해당 인터페이스는 캡처 장치 켜기/끄기에 사용합니다. 방 입장 시 기본적으로 장치를 켜지 않습니다.
- 방에 입장한 후에야 해당 인터페이스를 호출할 수 있고 방을 나가면 자동으로 장치를 끕니다.
- 모바일에서 캡처 장치 켜는 동시에 일반적으로 권한 신청, 음량 유형 조정 등 조작이 수반됩니다.

#### 함수 프로토타입  
```
ITMGContext virtual int EnableAudioCaptureDevice(bool enable)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| enable    |bool     |캡처 장치를 켜야 하는 경우 매개변수 TRUE를 가져오고, 캡처 장치를 종료해야 하는 경우 FALSE를 가져옵니다.|

> 샘플 코드

```
캡처 장치 켜기
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioCaptureDevice(true);
```

### 캡처 장치 상태 획득
이 인터페이스는 캡처 장치 상태 획득에 사용됩니다.
#### 함수 프로토타입

```
ITMGContext virtual bool IsAudioCaptureDeviceEnabled()
```
#### 샘플 코드

```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioCaptureDeviceEnabled();
```

### 오디오 업스트림 시작/종료
이 인터페이스는 오디오 업스트림 시작/종료에 사용됩니다. 캡처 장치가 이미 시작된 경우, 캡처한 오디오 데이터를 전송합니다. 캡처 장치가 시작되지 않은 경우 여전히 소리가 무성입니다. 캡처 장치의 켜기/끄기는 인터페이스 EnableAudioCaptureDevice를 참조하십시오.

#### 함수 프로토타입

```
ITMGContext  virtual int EnableAudioSend(bool bEnable)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| bEnable    |bool     |오디오 업스트림을 시작해야 하는 경우 매개변수 TRUE를 가져오고, 오디오 업스트림을 종료해야 하는 경우 매개변수 FALSE를 가져옵니다.|

> 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioSend(true);
```

### 오디오 업스트림 상태 획득
이 인터페이스는 오디오 업스트림 상태 획득에 사용됩니다.
#### 함수 프로토타입  
```
ITMGContext virtual bool IsAudioSendEnabled()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioSendEnabled();
```

### 마이크 실시간 음량 획득
이 인터페이스는 마이크 실시간 음량 획득에 사용되며 반환 값은 int 유형입니다.
#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetMicLevel()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicLevel();
```

### 마이크 음량 설정
이 인터페이스는 마이크의 음량 설정에 사용됩니다. 매개변수 volume은 마이크의 음량 설정에 사용되며, 값이 0이면 무성임을, 값이 100이면 음량이 커지지도 작아지지도 않음을 의미합니다. 기본값은 100입니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int SetMicVolume(int vol)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| vol    |int      |음량 설정, 범위: 0 ~ 200|
#### 샘플 코드  
```
int vol = 100;
ITMGContextGetInstance()->GetAudioCtrl()->SetMicVolume(vol);
```

### 마이크 음량 획득
이 인터페이스는 마이크의 음량 획득에 사용됩니다. 반환 값은 int 유형이며 반환 값 101은 인터페이스 SetMicVolume을 호출한 적이 없음을 의미합니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetMicVolume()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetMicVolume();
```

### 스피커 장치 수량 획득
이 인터페이스는 스피커 장치 수량 획득에 사용됩니다.

#### 함수 프로토타입  

```
ITMGAudioCtrl virtual int GetSpeakerListCount()
```
#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerListCount();
```

### 스피커 장치 열거
이 인터페이스는 스피커 장치 열거에 사용됩니다. GetSpeakerListCount 인터페이스와 함께 사용합니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetSpeakerList(TMGAudioDeviceInfo* ppDeviceInfoList, int nCount)

class TMGAudioDeviceInfo
{
public:
	const char* pDeviceID;
	const char* pDeviceName;
};
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| ppDeviceInfoList    	|TMGAudioDeviceInfo    	|장치 리스트		|
| nCount   		|int     		|획득한 스피커 장치 수량	|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerList(ppDeviceInfoList,nCount);
```

### 스피커 장치 선택
이 인터페이스는 재생 장치 선택에 사용됩니다. 호출하지 않거나 공백 문자열을 전송하면 시스템의 기본 재생 장치를 선택합니다.
#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int SelectSpeaker(const char* pSpeakerID)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| pSpeakerID    |char*      |스피커 장치 ID|
#### 샘플 코드  
```
const char* pSpeakerID ="1";
ITMGContextGetInstance()->GetAudioCtrl()->SelectSpeaker(pSpeakerID);
```

### 스피커 켜기/끄기
이 인터페이스는 스피커 켜기/끄기에 사용됩니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual void EnableSpeaker(bool enabled)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| enable   		|bool       	|스피커를 꺼야 하는 경우 매개변수 FALSE를 가져오고, 스피커를 켜는 경우 매개변수 TRUE를 가져옵니다.	|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableSpeaker(true);
```

### 스피커 상태 획득
이 인터페이스는 스피커 상태 획득에 사용됩니다. 반환 값 0은 스피커가 꺼져 있음을 의미하며, 반환 값 1은 스피커가 켜져 있음을 의미하며, 반환 값 2는 스피커가 실행 중임을 의미하며, 반환 값 3은 스피커가 없음을 의미하며, 반환 값 4는 장치가 초기화되지 않았음을 의미합니다.
#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetSpeakerState()
```

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerState();
```

### 재생 장치 켜기/끄기
이 인터페이스는 재생 장치 켜기/끄기에 사용됩니다.

#### 함수 프로토타입  
```
ITMGContext virtual int EnableAudioPlayDevice(bool enable) 
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| enable    |bool        |재생 장치를 꺼야 하는 경우 매개변수 FALSE를 가져오고, 재생 장치를 켜는 경우 매개변수 TRUE를 가져옵니다.|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioPlayDevice(true);
```

### 재생 장치 상태 획득
이 인터페이스는 재생 장치 상태 획득에 사용됩니다.
#### 함수 프로토타입

```
ITMGContext virtual bool IsAudioPlayDeviceEnabled()
```
#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioPlayDeviceEnabled();
```

### 오디오 다운스트림 시작/종료
이 인터페이스는 오디오 다운스트림 시작/종료에 사용됩니다. 재생 장치가 이미 켜져 있는 경우 방의 다른 사람의 오디오 데이터를 재생합니다. 재생 장치가 켜지지 않은 경우 여전히 소리가 무성입니다. 재생 장치의 켜기/끄기는 인터페이스 EnableAudioPlayDevice를 참조하십시오.

#### 함수 프로토타입  

```
ITMGContext virtual int EnableAudioRecv(bool enable)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| enable    |bool     |오디오 다운스트림을 시작해야 하는 경우 매개변수 TRUE를 가져오고, 오디오 다운스트림을 종료해야 하는 경우 매개변수 FALSE를 가져옵니다.|

#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->EnableAudioRecv(true);
```



### 오디오 다운스트림 상태 획득
이 인터페이스는 오디오 다운스트림 상태 획득에 사용됩니다.
#### 함수 프로토타입  
```
ITMGContext virtual bool IsAudioRecvEnabled() 
```

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->IsAudioRecvEnabled();
```

### 스피커 실시간 음량 획득
이 인터페이스는 스피커 실시간 음량 획득에 사용됩니다. 반환 값은 int 유형이며, 스피커 실시간 음량을 나타냅니다.
#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetSpeakerLevel()
```

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerLevel();
```

### 스피커 음량 설정
이 인터페이스는 스피커의 음량 설정에 사용됩니다.
매개변수 volume은 스피커의 음량 설정에 사용되며, 값이 0이면 무성임을, 값이 100이면 음량이 커지지도 작아지지도 않음을 의미합니다. 기본값은 100입니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int SetSpeakerVolume(int vol)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| vol    |int        |음량 설정, 범위: 0 ~ 200|
#### 샘플 코드  
```
int vol = 100;
ITMGContextGetInstance()->GetAudioCtrl()->SetSpeakerVolume(vol);
```

### 스피커 음량 획득
이 인터페이스는 스피커의 음량 획득에 사용됩니다. 반환 값은 int 유형이며 스피커의 음량을 의미합니다. 반환 값 101은 인터페이스 SetSpeakerVolume을 호출한 적이 없음을 의미합니다.
Level은 실시간 음량, Volume은 스피커의 음량으로 최종 음량은 Level*Volume%입니다. 예: 실시간 음량 값이 100, Volume 값이 60이라면 최종 음량 값은 역시 60이 됩니다.

#### 함수 프로토타입  
```
ITMGAudioCtrl virtual int GetSpeakerVolume()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->GetSpeakerVolume();
```


### 인이어 시동
이 인터페이스는 인이어 시동에 사용됩니다.
#### 함수 프로토타입  
``` 
ITMGAudioCtrl virtual int EnableLoopBack(bool enable)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| enable    |bool         |시동 여부 설정|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioCtrl()->EnableLoopBack(true);
```


## 음성 채팅 반주 관련 인터페이스
|인터페이스     | 인터페이스 의미   |
| ------------- |:-------------:|
|StartAccompany    				       |반주 재생 시작|
|StopAccompany    				   	|반주 재생 중지|
|IsAccompanyPlayEnd				|반주 재생 완료 여부|
|PauseAccompany    					|반주 재생 일시 중지|
|ResumeAccompany					|반주 다시 재생|
|SetAccompanyVolume 				|반주 음량 설정|
|GetAccompanyVolume				|반주 재생 음량 획득|
|SetAccompanyFileCurrentPlayedTimeByMs 				|재생 진도 설정|

### 반주 재생 시작
이 인터페이스를 호출하여 반주 재생을 시작합니다. M4A, WAV, MP3 모두 3가지 형식을 지원합니다. 이 API를 호출하면 음량이 리셋됩니다.

#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int StartAccompany(const char* filePath, bool loopBack, int loopCount, int msTime) 
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------
| filePath    	|char* 	|반주 재생 경로						|
| loopBack  	|bool	|믹스하여 발송 여부, 일반적으로 TRUE로 설정하며 다른 사람도 반주를 들을 수 있습니다.|
| loopCount	|int 	|순환 횟수, -1은 무한 순환을 의미합니다.				|
| msTime	|int   	|지연 시간						|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StartAccompany(filePath,true,-1,0);
```

### 반주 재생 콜백
반주 재생 완료 후, 콜백 함수는 OnEvent를 호출합니다. 이벤트 메시지는 ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH이며 OnEvent 함수에서 이벤트 메시지를 판단합니다.
#### 샘플 코드  
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
	   	}
		...
        case ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH:
		{
		//처리 진행
		break;
		}
	}
}
```

### 반주 재생 중지
이 인터페이스를 호출하여 반주 재생을 중지합니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int StopAccompany(int duckerTime)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| duckerTime	|int             |페이드아웃 시간|

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopAccompany(0);
```

### 반주 재생 완료 여부
재생이 완료되면 반환 값은 TRUE이고, 재생이 완료되지 않으면 반환 값은 FALSE입니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual bool IsAccompanyPlayEnd()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->IsAccompanyPlayEnd();
```

### 반주 재생 일시 중지
이 인터페이스를 호출하여 반주 재생을 일시 중지합니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int PauseAccompany()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseAccompany();
```

### 반주 다시 재생
이 인터페이스는 반주를 다시 재생하는 데 사용됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int ResumeAccompany()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAccompany();
```

### 자신이 반주를 들을 수 있는지 여부 설정
이 인터페이스는 자신이 반주를 들을 수 있는지 여부 설정에 사용됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int EnableAccompanyPlay(bool enable)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|--------------|
| enable    |bool             |들을 수 있는지 여부|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyPlay(false);
```

### 다른 사람이 반주를 들을 수 있는지 여부 설정
다른 사람이 반주를 들을 수 있는지 여부 설정합니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int EnableAccompanyLoopBack(bool enable)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|--------------|
| enable    |bool             |들을 수 있는지 여부|

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->EnableAccompanyLoopBack(false);
```

### 반주 음량 설정
DB 음량 설정, 기본값은 100입니다. 값은 100보다 크면 음량이 확대되며, 값은 100보다 작으면 음량이 감소됩니다. 값 범위는 0 ~ 200입니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int SetAccompanyVolume(int vol)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| vol    |int             |음량 값|

#### 샘플 코드  
```
int vol=100;
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetAccompanyVolume(vol);
```

### 반주 재생 음량 획득
이 인터페이스는 DB 음량 획득에 사용됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int GetAccompanyVolume()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyVolume();
```

### 반주 재생 진도 획득
다음 2개의 인터페이스는 반주 재생 진도 획득에 사용됩니다. 주의사항: Current / Total = 현재 순환 횟수, Current % Total = 현재 순환 재생 위치입니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int GetAccompanyFileTotalTimeByMs()
ITMGAudioEffectCtrl virtual int GetAccompanyFileCurrentPlayedTimeByMs()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyFileTotalTimeByMs();
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetAccompanyFileCurrentPlayedTimeByMs();
```

### 재생 진도 설정
이 인터페이스는 재생 진도 설정에 사용됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int SetAccompanyFileCurrentPlayedTimeByMs(unsigned int time)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| time    |int                |재생 진도, 단위: 밀리초|

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetAccompanyFileCurrentPlayedTimeByMs(time);
```



## 음성 채팅 효과음 관련 인터페이스

|인터페이스     | 인터페이스 의미   |
| ------------- |:-------------:|
|PlayEffect    		|효과음 재생|
|PauseEffect    	|효과음 재생 일시 중지|
|PauseAllEffects	|모든 효과음 일시 중지|
|ResumeEffect    	|효과음 다시 재생|
|ResumeAllEffects	|모든 효과음 다시 재생|
|StopEffect 		|효과음 재생 중지|
|StopAllEffects		|모든 효과음 재생 중지|
|SetVoiceType 		|변성 효과|
|SetKaraokeType 		|노래방 효과음|
|GetEffectsVolume	|효과음 재생 음량 획득|
|SetEffectsVolume 	|효과음 재생 음량 설정|


### 효과음 재생
이 인터페이스는 효과음 재생에 사용됩니다. 매개변수에서의 효과음 ID는 앱에서 관리해야 하며, 하나의 독립 파일을 유일하게 식별합니다. 파일은 M4A, WAV, MP3 모두 3가지 형식을 지원합니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int PlayEffect(int soundId,  const char* filePath, bool loop, double pitch, double pan, double gain)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| soundId  	|int        	|효과음 ID						|
| filePath    	|char*     	|효과음 경로						|
| loop    		|bool  	|중복 재생 여부						|
| pitch    	|double	|재생 빈도, 기본값은 1.0입니다. 해당 값이 작을수록 재생 속도는 느려지고 시간은 길어집니다.		|
| pan    		|double	|사운드트랙, 값의 범위는 -1.0 ~ 1.0 사이입니다. -1.0은 좌측 사운드트랙만 열었음을 의미합니다.	|
| gain    		|double	|게인 음량, 값의 범위는 0.0 ~ 1.0 사이이며 기본값은 1.0입니다.		|

#### 샘플 코드  
```
double pitch = 1.0;
double pan = 0.0;
double gain = 0.0;
ITMGContextGetInstance()->GetAudioEffectCtrl()->PlayEffect(soundId,filepath,true,pitch,pan,gain);
```

### 효과음 재생 일시 중지
이 인터페이스는 효과음 재생 일시 중지에 사용됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int PauseEffect(int soundId)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| soundID    |int                    |효과음 ID|

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseEffect(soundId);
```

### 모든 효과음 일시 중지
이 인터페이스를 호출하면 모든 효과음이 일시 중지됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int PauseAllEffects()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->PauseAllEffects();
```

### 효과음 다시 재생
이 인터페이스는 효과음 다시 재생에 사용됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int ResumeEffect(int soundId)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| soundID    |int                    |효과음 ID|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeEffect(soundId);
```

### 모든 효과음 다시 재생
이 인터페이스를 호출하여 모든 효과음을 다시 재생합니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int ResumeAllEffects()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->ResumeAllEffects();
```

### 효과음 재생 중지
이 인터페이스는 효과음 재생 중지에 사용됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int StopEffect(int soundId)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| soundID    |int                    |효과음 ID|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopEffect(soundId);
```

### 모든 효과음 재생 중지
이 인터페이스를 호출하여 모든 효과음 재생을 중지합니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int StopAllEffects()
```


#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->StopAllEffects();
```



### 변성 효과
이 인터페이스를 호출하여 변성 효과를 설정합니다.
#### 함수 프로토타입  
```
TMGAudioEffectCtrl int setVoiceType(int type)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| type    |int                    |로컬 오디오 변성 유형|



|유형 매개변수     |매개변수 표시 값|의미|
| ------------- |-------------|------------- |
|ITMG_VOICE_TYPE_ORIGINAL_SOUND  		|0	|오리지날			|
|ITMG_VOICE_TYPE_LOLITA    				|1	|여자애			|
|ITMG_VOICE_TYPE_UNCLE  				|2	|아저씨			|
|ITMG_VOICE_TYPE_INTANGIBLE    			|3	|고유함			|
|ITMG_VOICE_TYPE_DEAD_FATBOY  			|4	|뚱뚱보			|
|ITMG_VOICE_TYPE_HEAVY_MENTA			|5	|헤비 멘탈			|
|ITMG_VOICE_TYPE_DIALECT 				|6	|외국인			|
|ITMG_VOICE_TYPE_INFLUENZA 				|7	|독감			|
|ITMG_VOICE_TYPE_CAGED_ANIMAL 			|8	|야수			|
|ITMG_VOICE_TYPE_HEAVY_MACHINE			|9	|무거운 기계			|
|ITMG_VOICE_TYPE_STRONG_CURRENT			|10	|강한 전류			|
|ITMG_VOICE_TYPE_KINDER_GARTEN			|11	|유치원생			|
|ITMG_VOICE_TYPE_HUANG 					|12	|미니언즈			|

#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->setVoiceType(0);
```

### 노래방 효과음
이 인터페이스를 호출하여 노래방 효과음을 설정합니다.
####  함수 원형  
```
TMGAudioEffectCtrl int SetKaraokeType(int type)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| type    |int                    |로컬 오디오 변성 유형|


|유형 매개변수     |매개변수 표시 값|의미|
| ------------- |-------------|------------- |
|ITMG_KARAOKE_TYPE_ORIGINAL 		|0	|오리지날			|
|ITMG_KARAOKE_TYPE_POP 				|1	|팝			|
|ITMG_KARAOKE_TYPE_ROCK 			|2	|락			|
|ITMG_KARAOKE_TYPE_RB 				|3	|힙합			|
|ITMG_KARAOKE_TYPE_DANCE 			|4	|댄스곡			|
|ITMG_KARAOKE_TYPE_HEAVEN 			|5	|고유함			|
|ITMG_KARAOKE_TYPE_TTS 				|6	|음성 합성		|

####  인스턴스 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetKaraokeType(0);
```

### 효과음 재생 음량 획득
효과음 재생 음량 획득, 선형 음량으로 기본값은 100입니다. 값이 100보다 크면 효과 게인, 100보다 작으면 효과 감소로 간주됩니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int GetEffectsVolume()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetAudioEffectCtrl()->GetEffectsVolume();
```

### 효과음 재생 음량 설정
이 인터페이스를 호출하여 효과음 재생 음량을 설정합니다.
#### 함수 프로토타입  
```
ITMGAudioEffectCtrl virtual int SetEffectsVolume(int volume)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| volume    |int                    |음량 값|

#### 샘플 코드  
```
int volume=1;
ITMGContextGetInstance()->GetAudioEffectCtrl()->SetEffectsVolume(volume);
```
## 오프라인 음성
오프라인 음성 및 문자 전환 기능을 사용하려면 우선 SDK를 초기화해야 합니다.

|인터페이스     | 인터페이스 의미   |
| ------------- |:-------------:|
|ApplyPTTAuthbuffer    |인증 초기화	|
|SetMaxMessageLength    |최대 음성 메시지 시간 제한	|
|StartRecording		|녹음 시작		|
|StartRecordingWithStreamingRecognition		|스트리밍 녹음 시작		|
|StopRecording    	|녹음 중지		|
|CancelRecording	|녹음 취소		|
|UploadRecordedFile 	|음성 파일 업로드		|
|DownloadRecordedFile	|음성 파일 다운로드		|
|PlayRecordedFile 	|음성 재생		|
|StopPlayFile		|음성 재생 중지		|
|GetFileSize 		|음성 파일 크기		|
|GetVoiceFileDuration	|음성 파일 시간		|
|SpeechToText 		|음성을 문자로 인식		|


### 인증 초기화
SDK 초기화 후 인증 초기화를 호출하여 authBuffer를 획득하려면 상기 음성 채팅 인증 정보 인터페이스를 참조하십시오.
#### 함수 프로토타입  
```
ITMGPTT virtual void ApplyPTTAuthbuffer(const char* authBuffer, int authBufferLen)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| authBuffer    |char*                    |인증|
| authBufferLen    |int                |인증 길이|

#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->ApplyPTTAuthbuffer(authBuffer,authBufferLen);
```

### 최대 음성 메시지 시간 제한
최대 음성 메시지 길이를 60초로 제한합니다.
#### 함수 프로토타입  
```
ITMGPTT virtual void SetMaxMessageLength(int msTime)
```

|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| msTime    |int                    |음성 시간, 단위: 밀리초|
#### 샘플 코드  
```
int msTime = 10;
ITMGContextGetInstance()->GetPTT()->SetMaxMessageLength(msTime);
```

### 녹음 시작
이 인터페이스는 녹음 시작에 사용됩니다. 녹음 파일을 업로드해야 음성을 문자로 전환 등 조작을 진행할 수 있습니다.
#### 함수 프로토타입  
```
ITMGPTT virtual void StartRecording(const char* fileDir)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| fileDir    |char*                      |저장한 음성 경로|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->SetMaxMessageLength(fileDir);
```

### 녹음 시작 콜백
녹음 시작 완료 후 콜백 함수는 OnEvent를 호출합니다. 이벤트 메시지는 ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE이며 OnEvent 함수에서 이벤트 메시지를 판단합니다.

#### 샘플 코드  
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE:
		{
		//처리 진행
		break;
		}
	}
}

```

### 스트리밍 녹음 시작
이 인터페이스는 스트리밍 녹음 시작에 사용되며, 동시에 콜백 과정에서 실시간으로 음성을 문자로 전환하여 반환할 수 있습니다.

#### 함수 프로토타입  
```
ITMGPTT virtual int StartRecordingWithStreamingRecognition(const char* filePath,const char*translateLanguage) 
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| filePath    	|char*	|저장한 음성 경로	|
| translateLanguage 	|char*	|전환해야 할 언어 코드: “cmn-Hans-CN”|

#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->StartRecordingWithStreamingRecognition(filePath,"cmn-Hans-CN");
```

### 스트리밍 녹음 시작 콜백
녹음 시작 완료 후 콜백은 함수 OnEvent를 호출합니다. 이벤트 메시지는 ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE이며 OnEvent 함수에서 이벤트 메시지를 판단합니다. 전달한 매개변수는 다음 4가지 정보를 포함합니다.

|메시지 이름     | 의미         |
| ------------- |:-------------:|
| result    	|스트리밍 녹음 성공 여부를 판단하는 반환 코드			|
| text    		|음성을 문자로 전환하여 인식한 텍스트	|
| file_path 	|녹음 저장 로컬 주소		|
| file_id 		|녹음의 백 엔드 URL 주소	|

|오류 코드     | 의미         |처리 방식|
| ------------- |:-------------:|:-------------:|
|32775	|스트리밍 음성을 텍스트로 전환에 실패했지만, 녹음이 성공했습니다.	|UploadRecordedFile 인터페이스를 호출하여 녹음을 업로드하고 SpeechToText 인터페이스를 호출하여 음성을 문자로 전환합니다.
|32777	|스트리밍 음성을 텍스트로 전환에 실패했지만, 녹음이 성공했고, 업로드도 성공했습니다.	|반환한 정보에 업로드가 성공한 백 엔드 URL 주소가 있으며, SpeechToText 인터페이스를 호출하여 음성을 문자로 전환합니다.

#### 샘플 코드  
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE:
		{
		//처리 진행
		break;
		}
	}
}

```

### 녹음 중지
이 인터페이스는 녹음 중지에 사용됩니다.
#### 함수 프로토타입  
```
ITMGPTT virtual int StopRecording()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->StopRecording();
```

### 녹음 취소
이 인터페이스를 호출하여 녹음을 취소합니다.
#### 함수 프로토타입  
```
ITMGPTT virtual int CancelRecording()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->CancelRecording();
```

### 음성 파일 업로드
이 인터페이스는 음성 파일 업로드에 사용됩니다.
#### 함수 프로토타입  
```
ITMGPTT virtual void UploadRecordedFile(const char* filePath)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| filePath    |char*                       |업로드한 음성 경로|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->UploadRecordedFile(filePath);
```

### 음성 업로드 완료 콜백
음성 업로드 완료 후, 이벤트 메시지는 ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE이며 OnEvent 함수에서 이벤트 메시지를 판단합니다.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE:
		{
		//처리 진행
		break;
		}
	}
}
```

### 음성 파일 다운로드
이 인터페이스는 음성 파일 다운로드에 사용됩니다.
#### 함수 프로토타입  
```
ITMGPTT virtual void DownloadRecordedFile(const char* fileId, const char* filePath) 
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| fileID  		|char*   	|파일의 URL 경로	|
| filePath 	|char*  	|파일의 로컬 저장 경로	|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->DownloadRecordedFile(fileID,filePath);
```

### 음성 파일 다운로드 완료 콜백
음성 다운로드 완료 후, 이벤트 메시지는 ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE이며 OnEvent 함수에서 이벤트 메시지를 판단합니다.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE:
		{
		//처리 진행
		break;
		}
	}
}
```

### 음성 재생
이 인터페이스는 음성 재생에 사용됩니다.
#### 함수 프로토타입  
```
ITMGPTT virtual void PlayRecordedFile(const char* filePath)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| filePath    |char*                       |파일 경로|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->PlayRecordedFile(filePath);
```

### 음성 재생 콜백
음성 재생 콜백, 이벤트 메시지는 ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE이며 OnEvent 함수에서 이벤트 메시지를 판단합니다.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE:
		{
		//처리 진행
		break;
		}
	}
}
```

### 음성 재생 중지
이 인터페이스는 음성 재생 중지에 사용됩니다.
#### 함수 프로토타입  
```
ITMGPTT virtual int StopPlayFile()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->StopPlayFile();
```
### 음성 파일 크기 획득
이 인터페이스를 통해 음성 파일 크기를 획득할 수 있습니다.
#### 함수 프로토타입  
```
ITMGPTT virtual int GetFileSize(const char* filePath)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| filePath    |char*                      |음성 파일 경로|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->GetFileSize(filePath);
```

### 음성 파일 시간 획득
이 인터페이스는 음성 파일 시간 획득에 사용되며 단위는 밀리초입니다.
#### 함수 프로토타입  
```
ITMGPTT virtual int GetVoiceFileDuration(const char* filePath)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| filePath    |char*                      |음성 파일 경로|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->GetVoiceFileDuration(filePath);
```



### 지정한 음성 파일을 문자로 식별
이 인터페이스는 지정한 음성 파일을 문자로 식별하는 데 사용됩니다.
#### 함수 프로토타입  
```
ITMGPTT virtual void SpeechToText(const char* fileID)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| fileID    |char*                      |음성 파일 URL|
#### 샘플 코드  
```
ITMGContextGetInstance()->GetPTT()->SpeechToText(fileID);
```

### 식별 콜백
지정한 음성 파일을 문자로 식별한 콜백, 이벤트 메시지는 ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE이며 OnEvent 함수에서 이벤트 메시지를 판단합니다.
```
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
	switch (eventType) {
		case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
		{
		//처리 진행
		break;
	    }
		...
        case ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE:
		{
		//처리 진행
		break;
		}
	}
}
```


## 고급 API

### 진단 정보 획득
실시간 영상/음성 통화 품질 관련 정보를 획득합니다. 해당 인터페이스는 주로 실시간 통화 품질을 확인하고 문제점을 조사하는 데 사용되므로 비즈니스 축에서는 무시할 수 있습니다.
#### 함수 프로토타입  

```
ITMGRoom virtual const char* GetQualityTips()
```
#### 샘플 코드  

```
ITMGContextGetInstance()->GetRoom()->GetQualityTips();
```


### 버전 번호 획득
SDK 버전 번호 획득, 분석에 사용됩니다.
#### 함수 프로토타입
```
ITMGContext virtual const char* GetSDKVersion()
```
#### 샘플 코드  
```
ITMGContextGetInstance()->GetSDKVersion();
```

### 로그 인쇄 등급 설정
로그 인쇄 등급 설정에 사용됩니다.
#### 함수 프로토타입
```
ITMGContext virtual void SetLogLevel(int logLevel, bool enableWrite, bool enablePrint)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| logLevel    		|int   		|로그 인쇄 등급		|
| enableWrite    	|bool   				|파일에 쓰기 여부, 기본값은 예	|
| enablePrint    	|bool   				|콘솔에 쓰기 여부, 기본값은 예	|


|ITMG_LOG_LEVEL|의미|
| -------------------------------|:-------------:|
|TMG_LOG_LEVEL_NONE=0		|로그 인쇄하지 않음			|
|TMG_LOG_LEVEL_ERROR=1		|오류 로그 인쇄(기본값)	|
|TMG_LOG_LEVEL_INFO=2			|알림 로그 인쇄		|
|TMG_LOG_LEVEL_DEBUG=3		|개발 디버깅 로그 인쇄	|
|TMG_LOG_LEVEL_VERBOSE=4		|고빈도 로그 인쇄		|

#### 샘플 코드  
```
ITMGContext* context = ITMGContextGetInstance();
context->SetLogLevel(0,true,true);
```

### 로그 인쇄 경로 설정
로그 인쇄 경로 설정에 사용됩니다.
기본 경로는 다음과 같습니다.

|플랫폼     |경로        |
| ------------- |:-------------:|
|Windows 	|%appdata%\Tencent\GME\ProcessName|
|iOS    		|Application/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/Documents|
|Android	|/sdcard/Android/data/xxx.xxx.xxx/files|
|Mac    		|/Users/username/Library/Containers/xxx.xxx.xxx/Data/Documents|

#### 함수 프로토타입
```
ITMGContext virtual void SetLogPath(const char* logDir) 
```

|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| logDir    		|char*    		|경로|
#### 샘플 코드  
```
cosnt char* logDir = ""//사용자가 경로를 설정
ITMGContext* context = ITMGContextGetInstance();
context->SetLogPath(logDir);
```

### 오디오 데이터 블랙리스트에 추가
어느 ID 하나를 오디오 데이터 블랙리스트에 추가합니다. 반환 값 0은 호출 실패를 의미합니다.
#### 함수 프로토타입  

```
ITMGContext ITMGAudioCtrl int AddAudioBlackList(const char* openId)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| openID    |char*       |블랙리스트에 추가할 ID|
#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->AddAudioBlackList(openId);
```

### 오디오 데이터 블랙리스트에서 제거
어느 ID 하나를 오디오 데이터 블랙리스트에서 제거합니다. 반환 값 0은 호출 실패를 의미합니다.
#### 함수 프로토타입  

```
ITMGContext ITMGAudioCtrl int RemoveAudioBlackList(const char* openId)
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| openID    |char*       |블랙리스트에서 제거할 ID|
#### 샘플 코드  

```
ITMGContextGetInstance()->GetAudioCtrl()->RemoveAudioBlackList(openId);
```


## 콜백 메시지

#### 메시지 리스트:

|메시지     | 메시지 의미   
| ------------- |:-------------:|
|ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		|오디오 방 입장 메시지		|
|ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		|오디오 방 퇴장 메시지		|
|ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT		|네트워크 등 원인으로 방 연결이 끊김 메시지	|
|ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE		|방 유형 변경 메시지			|
|ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    	|마이크 장치 추가 메시지		|
|ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    	|마이크 장치 분실 메시지		|
|ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE	|스피커 장치 추가 메시지		|
|ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE	|스피커 장치 분실 메시지		|
|ITMG_MAIN_EVENT_TYPE_ACCOMPANY_FINISH		|반주 종료 메시지			|
|ITMG_MAIN_EVNET_TYPE_USER_UPDATE		|방 멤버 변경 메시지		|
|ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE	|PTT 녹음 완료			|
|ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE	|PTT 업로드 완료			|
|ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE	|PTT 다운로드 완료			|
|ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE		|PTT 재생 완료			|
|ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE	|음성을 문자로 전환 완료			|

#### 데이터 리스트:

|메시지     | Data         |예|
| ------------- |:-------------:|------------- |
| ITMG_MAIN_EVENT_TYPE_ENTER_ROOM    		|result; error_info			|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_EXIT_ROOM    		|result; error_info  			|{"error_info":"","result":0}|
| ITMG_MAIN_EVENT_TYPE_ROOM_DISCONNECT    	|result; error_info  			|{"error_info":"waiting timeout, please check your network","result":0}|
| ITMG_MAIN_EVENT_TYPE_CHANGE_ROOM_TYPE    	|result; error_info; new_room_type	|{"error_info":"","new_room_type":0,"result":0}|
| ITMG_MAIN_EVENT_TYPE_SPEAKER_NEW_DEVICE	|result; error_info  			|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"스피커 (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":false,"result":0}|
| ITMG_MAIN_EVENT_TYPE_SPEAKER_LOST_DEVICE    	|result; error_info  			|{"deviceID":"{0.0.0.00000000}.{a4f1e8be-49fa-43e2-b8cf-dd00542b47ae}","deviceName":"스피커 (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":false,"result":0}|
| ITMG_MAIN_EVENT_TYPE_MIC_NEW_DEVICE    	|result; error_info  			|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"마이크 (Realtek High Definition Audio)","error_info":"","isNewDevice":true,"isUsedDevice":true,"result":0}|
| ITMG_MAIN_EVENT_TYPE_MIC_LOST_DEVICE    	|result; error_info 			|{"deviceID":"{0.0.1.00000000}.{5fdf1a5b-f42d-4ab2-890a-7e454093f229}","deviceName":"마이크 (Realtek High Definition Audio)","error_info":"","isNewDevice":false,"isUsedDevice":true,"result":0}|
| ITMG_MAIN_EVNET_TYPE_USER_UPDATE    		|user_list;  event_id			|{"event_id":1,"user_list":["0"]}|
| ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE 	|result; file_path  			|{"filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_UPLOAD_COMPLETE 	|result; file_path;file_id  		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_DOWNLOAD_COMPLETE	|result; file_path;file_id  		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_PLAY_COMPLETE 	|result; file_path  			|{"filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_SPEECH2TEXT_COMPLETE	|result; file_path;file_id		|{"file_id":"","filepath":"","result":0}|
| ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE	|result; text; file_path;file_id		|{"file_id":"","filepath":","text":"","result":0}|

