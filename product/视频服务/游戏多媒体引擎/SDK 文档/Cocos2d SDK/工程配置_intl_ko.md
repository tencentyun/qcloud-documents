Tencent Cloud 게임 멀티미디어 엔진 SDK의 사용을 환영합니다. Cocos2D 개발자가 Tencent Cloud 게임 멀티미디어 엔진 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 Cocos2D 개발에 적합한 프로젝트 구성을 소개합니다.

## SDK 준비
[다운로드 가이드](https://cloud.tencent.com/document/product/607/18521)에서 관련 Demo 및 SDK를 다운로드하십시오.

### SDK 리소스 압축 해제
 1. 획득한 SDK 리소스 압축 해제
 2. 폴더 내용은 다음과 같습니다.


|폴더 이름                     | 폴더 세부 정보
| ----------------------|-----------------------------------        |
| TMG_SDK                    |게임 오디오/비디오 SDK framework 파일        |
| TMGCocosDemo          |게임 오디오/비디오 SDK 사례 프로젝트                        |

## 시스템 요건
SDK는 Mac 시스템에서의 컴파일을 지원합니다.

## iOS Xcode 예비 작업

### 1. SDK 관련 framework 파일 가져오기 
framework를 Xcode 프로젝트에 추가하고 헤더 파일 참조 위치를 설정해야 합니다.

TMG_SDK 폴더에 있는 GMESDK.framework 게임 오디오/비디오 SDK framework 파일을 프로젝트에 추가해야 합니다.


### 2. 의존 라이브러리 추가  
다음 그림을 참조하십시오.  
![](https://main.qcloudimg.com/raw/b6156b8c7a596248c148607070e38f67.png)

## Android 예비 작업
### 1. tmgsdk.jar을 libs 라이브러리에 추가
![](https://main.qcloudimg.com/raw/fe1bde45a15f273aa9b9707420bb2696.png)

### 2. Activity에서 so 파일 가져오기
```
public class AppActivity extends Cocos2dxActivity {
    static final String TAG = "AppActivity";
    static OpensdkGameWrapper gameWrapper ;
    static {
        Log.e(TAG, "Load so begin");
        System.loadLibrary("stlport_shared");
        System.loadLibrary("xplatform");
        System.loadLibrary("UDT");
        System.loadLibrary("qav_tlssign");
        System.loadLibrary("traeimp-armeabi-v7a");
        System.loadLibrary("qavsdk");
        Log.e(TAG, "Load so end");
    }
}
```

### 3. 초기화
oncreate 함수에서 초기화를 진행하며, 순서는 틀려서는 안 됩니다.
```
protected void onCreate(Bundle savedInstanceState) {
        super.setEnableVirtualButton(false);
        super.onCreate(savedInstanceState);

        //초기화, 순서가 틀려서는 안 됩니다.
        AVChannelManager.setIMChannelType(AVChannelManager.IMChannelTypeImplementInternal);
        gameWrapper = new OpensdkGameWrapper(this);
        runOnGLThread(new Runnable() {
            @Override
            public void run() {
                gameWrapper.initOpensdk();
            }
        });
}
```

