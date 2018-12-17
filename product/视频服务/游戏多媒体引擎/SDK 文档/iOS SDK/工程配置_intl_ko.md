## 소개

Tencent Cloud GME SDK의 사용을 환영합니다. iOS 개발자가 Tencent Cloud GME 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 iOS 개발에 적합한 프로젝트 구성을 소개합니다.

## SDK 준비

다음의 방식으로 SDK를 획득할 수 있습니다.

### 1. [다운로드 가이드](https://cloud.tencent.com/document/product/607/18521)에서 관련 Demo 및 SDK를 다운로드하십시오.

### 2. 인터페이스에서 iOS 버전의 SDK 리소스를 찾습니다.

### 3. [다운로드] 버튼을 한 번 클릭합니다.

다운로드한 SDK 리소스의 압축을 풀면 다음과 같습니다.

|이름     | 의미   
| ------------- |:-------------:|
|GMESDK.framework			|GME 관련 리소스

## 시스템 요건

SDK는 iOS7.0 이상의 운영 체제에서 지원됩니다.

## 사전 작업

### 1. SDK 파일 가져오기

상황에 따라 Xcode의 Link Binary With Libraries에서 아래의 의존 라이브러리를 추가하고 SDK 소재 디렉터리를 지향하는 Framework Search Paths를 설정해야 합니다. 다음 그림과 같습니다.  

![](https://main.qcloudimg.com/raw/9dd8d458734bc6e475581049e6cf26b1.png)

### 2. 라이브러리 추가

다음 그림을 참조하십시오.  

![](https://main.qcloudimg.com/raw/b6156b8c7a596248c148607070e38f67.png)

### 3. Bitcode 종료

Bitcode는 프로젝트 의존형의 모든 클래스 라이브러리를 동시 지원합니다. SDK는 현재 Bitcode를 지원하지 않으니 우선 종료할 수 있습니다.
이 설정을 종료하려면 Targets - Build Settings에서 Bitcode를 검색하기만 하면 됩니다. 선택 항목을 찾으면 NO로 설정합니다.
다음 그림과 같습니다.  
![](https://main.qcloudimg.com/raw/82c628e8a7d9a4bebc842c8545d9563a.png)

### 4. 권한 신청

Tencent 오디오/비디오 엔진 iOS 플랫폼에 필요한 사적 권한은 다음과 같습니다.

|key     | 의미   
| ------------- |:-------------:|
|Required background modes    		 |백 엔드 실행 허용|
|Microphone Usaeg Description   	|마이크 권한 허용|

