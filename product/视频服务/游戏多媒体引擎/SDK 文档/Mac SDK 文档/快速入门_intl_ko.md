## 소개

Tencent Cloud GME SDK의 사용을 환영합니다. Mac 개발자가 Tencent Cloud GME 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 Mac 개발에 적합한 빠른 액세스 문서를 소개합니다.


## 사용 프로세스 그림
![](https://main.qcloudimg.com/raw/bf2993148e4783caf331e6ffd5cec661.png)


### GME 사용 중요사항

GME 시작 가이드 문서는 가장 중요한 연결 인터페이스에 대한 정보만 제공하고 더 많은 세부 인터페이스는 [관련 인터페이스 문서](https://cloud.tencent.com/document/product/607/18739)를 참조하십시오.


|중요 인터페이스     | 인터페이스 의미|
| ------------- |:-------------:|
|InitEngine    				       	|GME 초기화 	|
|Poll    		|이벤트 콜백 트리거	|
|EnterRoom	 	|방 입장  		|
|EnableMic	 		|마이크 켜기 		|
|EnableSpeaker		|스피커 켜기 		|

>**설명: **
**GME의 인터페이스 호출 성공 후 반환 값은 QAVError.OK이고, 수치는 0입니다.**
** GME의 인터페이스 호출은 동일한 스레드에서 진행되어야 합니다.**
** GME가 방을 가입하려면 인증이 필요합니다. 인증 관련 부분 내용을 참조하십시오.**
**GME는 Poll 인터페이스를 주기적으로 호출하여 이벤트 콜백을 트리거해야 합니다.**

**GME 콜백 정보는 콜백 메시지 리스트를 참조하십시오.**

**방에 입장한 후에 장치에 대한 조작을 실행할 수 있습니다.**

**이 문서에 해당하는 GME SDK 버전은 2.2입니다.**
## 빠른 액세스 절차

### 1. 단일 인스턴스 획득
음성 기능 사용 시 먼저 ITMGContext 개체를 획득해야 합니다.
####  함수 원형 

```
ITMGContext ITMGDelegate <NSObject>
```
####  인스턴스 코드  

```
ITMGContext* _context = [ITMGContext GetInstance];
_context.TMGDelegate =self;
```



### 2. SDK 초기화
매개변수 획득에 대한 정보는 문서 [GME 액세스 가이드](https://cloud.tencent.com/document/product/607/10782)를 참조하십시오.
해당 인터페이스는 Tencent Cloud 콘솔의 SDKAppID 번호를 매개변수로 써야 합니다. 더불어 OpenID도 필요하며 해당 OpenID는 하나의 사용자를 유일하게 식별합니다. 규칙은 앱 개발자가 자체적으로 제정하고 앱 내에서는 중복하지 않으면 됩니다(현재는 Int64만 지원).
SDK 초기화 후 방에 들아갈 수 있습니다.
####  함수 원형

```
ITMGContext -(void)InitEngine:(NSString*)sdkAppID openID:(NSString*)openID
```

|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| sdkAppId    	|NSString  |Tencent Cloud 콘솔의 SDKAppID 번호				|
| OpenID    		|NSString  |OpenID는 Int64 유형(string으로 전환 후 가져오기)만 지원하고 반드시 10000보다 크며 사용자 ID 식별에 사용합니다. |

####  인스턴스 코드 
```
[[ITMGContext GetInstance] InitEngine:SDKAPPID3RD openID:_openId];
```

### 3. 이벤트 콜백 트리거
update에서의 주기적인 Poll 호출을 통해 이벤트 콜백을 트리거할 수 있습니다.
####  함수 원형

```
ITMGContext -(void)Poll
```
####  인스턴스 코드
```
[[ITMGContext GetInstance] Poll];
```

### 4. 방 가입
생성한 인증 정보를 사용해 방에 진입하면 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM이라는 콜백을 받게 됩니다.
- 방 가입 시 기본적으로 마이크 및 스피커를 켜지 않습니다.
- EnterRoom 인터페이스를 호출하기 전에 먼저 InitEngine 인터페이스를 호출해야 합니다.

####  함수 원형
```
ITMGContext   -(void)EnterRoom:(NSString*) roomId roomType:(int*)roomType authBuffer:(NSData*)authBuffer
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| RoomID 	|NSString		|방 번호, 최대 127자 지원|
| roomType 	|int		|방 오디오 유형		|
| authBuffer	|NSData	|인증 번호				|

|오디오 유형     	|의미|매개변수|음량 유형|콘솔 추천 샘플링 속도 설정|적용 시나리오|
| ------------- |------------ | ---- |---- |---- |---- |
| ITMG_ROOM_TYPE_FLUENCY			|보통 음질	|1|스피커: 통화 음량. 헤드폰: 미디어 음량	|음질에 대해 특별한 요구가 없을 경우 16K 샘플링 속도라면 충분합니다.					|유창성이 우선이고 지연 시간이 매우 짧은 음성 채팅으로 게임에서 팀 배틀에 적용되고 FPS, MOBA와 같은 게임에 적합합니다.	|							
| ITMG_ROOM_TYPE_STANDARD			|표준 음질	|2|스피커: 통화 음량. 헤드폰: 미디어 음량	|필요한 음질에 따라 16K/48K 샘플링 속도를 선택할 수 있습니다.				|음질이 비교적 좋고 시간 지연이 적당하여 마피아 게임, 보드게임 등 캐주얼 게임의 실시간 통화 시나리오에 적합합니다.	|												
| ITMG_ROOM_TYPE_HIGHQUALITY		|고음질	|3|스피커: 미디어 음량, 헤드폰: 미디어 음량	|최적의 효과를 보증하기 위해서 콘솔에서 48K 샘플링 속도의 고음질 구성을 설정하기를 권장합니다. 	|초고음질, 지연시간이 상대적으로 길어서 음악, 댄스 등 게임 및 음성 소셜류 앱에 적용합니다. 음악방송, 온라인 노래방 등 음질 요구가 있는 시나리오에 적용합니다.	|

- 음량 유형 또는 시나리오에 특별한 요구가 있는 경우 온라인 고객 서비스에 연락하십시오.
- 콘솔 샘플링 속도 설정은 게임 음성 효과에 직접 영향을 줄 수 있으므로 [콘솔](https://console.cloud.tencent.com/gamegme)에서 샘플링 속도 설정이 항목 사용 시나리오에 적합한지 다시 확인하십시오.

####  인스턴스 코드  
```
[[ITMGContext GetInstance] EnterRoom:_roomId roomType:_roomType authBuffer:authBuffer];
```

### 5. 방 가입 이벤트 콜백
방 가입 완료 후 콜백이 있으며 메시지는 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM입니다.
콜백 관련 매개변수 코드를 설정합니다.
```
- (void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary*)data
```
관련 매개변수 코드를 콜백하여 처리합니다.
####  인스턴스 코드  
```
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
    NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
    switch (eventType) {
        case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
        {
            int result = ((NSNumber*)[data objectForKey:@"result"]).intValue;
            NSString* error_info = [data objectForKey:@"error_info"];
            //방 입장 성공 이벤트 수신
        }
            break;
     }
}
```

### 6. 마이크 켜기/끄기
이 인터페이스는 마이크 켜기/끄기에 사용됩니다. 방 가입 시 기본적으로 마이크 및 스피커를 켜지 않습니다.

####  함수 원형  
```
ITMGContext GetAudioCtrl -(void)EnableMic:(BOOL)enable
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean     |마이크를 꺼야 하는 경우 매개변수 NO를 가져오고, 마이크를 켜야 하는 경우 매개변수 YES를 가져옵니다.|
####  인스턴스 코드   
```
[[[ITMGContext GetInstance] GetAudioCtrl] EnableMic:YES];
```


### 7. 스피커 켜기/끄기
이 인터페이스는 스피커 켜기/끄기에 사용됩니다.

####  함수 원형 
```
ITMGContext GetAudioCtrl -(void)EnableSpeaker:(BOOL)enable
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| isEnabled    |boolean       |스피커를 꺼야 하는 경우 매개변수 NO를 가져오고, 스피커를 켜야 하는 경우 매개변수 YES를 가져옵니다.|
####  인스턴스 코드
```
[[[ITMGContext GetInstance] GetAudioCtrl] EnableSpeaker:YES];
```


## 인증
### 인증 정보
AuthBuffer를 생성하고 관련 기능의 암호화와 인증에 사용됩니다. 관련 백 엔드 배포는 [GME 키 문서](https://cloud.tencent.com/document/product/607/12218)를 참조하십시오. 오프라인 음성이 인증을 획득할 때, 방 번호 매개변수는 0을 써야 합니다.    
해당 인터페이스 반환 값은 NSData 유형입니다.

####  함수 원형
```
@interface QAVAuthBuffer : NSObject
+ (NSData*) GenAuthBuffer:(unsigned int)appId roomId:(NSString*)roomId identifier:(NSString*)identifier key:(NSString*)key;
+ @end
```
|매개변수     |유형         |의미|
| ------------- |:-------------:|-------------|
| appId    		|int   		|Tencent Cloud 콘솔의 SDKAppID 번호		|
| roomId    		|NSString  	|방 번호, 최대 127자 지원(오프라인 음성 방 번호 매개변수를 0을 써야 함)	|
| identifier  		|NSString    	|사용자 ID								|
| key    			|NSString    	|Tencent Cloud [콘솔](https://console.cloud.tencent.com/gamegme)의 키					|



#### 샘플 코드  
```
NSData* authBuffer =   [QAVAuthBuffer GenAuthBuffer:SDKAPPID3RD.intValue roomId:_roomId openID:_openId key:AUTHKEY];
```

