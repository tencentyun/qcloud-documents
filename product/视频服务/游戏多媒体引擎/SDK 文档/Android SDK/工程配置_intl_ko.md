Tencent Cloud GME SDK의 사용을 환영합니다. Android 개발자가 Tencent Cloud GME 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 Android 개발에 적합한 프로젝트 구성을 소개합니다.

## SDK 준비

다음의 방식으로 SDK를 획득할 수 있습니다.

### SDK 다운로드

[다운로드 가이드](https://cloud.tencent.com/document/product/607/18521)에서 관련 Demo 및 SDK를 다운로드하십시오.

인터페이스에서 Android 버전의 SDK 리소스를 찾았습니다.

압축 해제된 SDK 리소스는 다음과 같이 구성됩니다.

|파일 이름       | 설명           
| ------------- |:-------------:|
| Libs     	| 개발 키트 Libs     |

## 시스템 요건
SDK는 Android 4.2 이상 운영 체제에서 지원됩니다. 그러나 하드웨어 인코딩은 (Android 4.3) API 18 이상에서만 사용할 수 있습니다.

## 사전 작업

### SDK 파일 가져오기

개발 키트 중 Libs 디렉터리의 mobilepb.jar, tmgsdk.jar과 wup-1.0.0-SNAPSHOT.jar을 Android 프로젝트의 Libs 디렉터리(프로젝트에 Libs 디렉터리가 없다면 직접 생성하십시오. armeabi 및 armeabi-v7a가 없다면 Libs 디렉터리에 함께 복사하십시오.)에 복사합니다. 다음 그림과 같습니다.  
![](https://main.qcloudimg.com/raw/006cc0fab7b4c2f370b9b31fdbc93f90.png)

### 프로젝트 구성

참조 라이브러리의 코드를 프로젝트의 앱 디렉터리 아래에 build.gradle에 추가합니다.  

```
sourceSets {
        main {
            jniLibs.srcDirs = ['libs']
        }
}
```

### 앱 권한 구성

프로젝트 AndroidManifest.xml 파일에 다음 권한을 추가합니다.

```
  <uses-permission android:name="android.permission.RECORD_AUDIO" />
  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
  <uses-permission android:name="android.permission.READ_PHONE_STATE" />
  <uses-permission android:name="android.permission.BLUETOOTH"/>
  <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
  <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
	```

