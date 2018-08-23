## 소개
Tencent Cloud 게임 멀티미디어 엔진 SDK의 사용을 환영합니다. Mac 개발자가 Tencent Cloud 게임 멀티미디어 엔진 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 Mac 개발에 적합한 프로젝트 구성을 소개합니다.

## SDK 준비
다음의 방식으로 SDK를 획득할 수 있습니다.

### 1. [다운로드 가이드](https://cloud.tencent.com/document/product/607/18521)에서 관련 Demo 및 SDK를 다운로드하십시오.

### 2. 인터페이스에서 Mac 버전의 SDK 리소스를 찾습니다.

### 3. [다운로드] 버튼을 한 번 클릭합니다.
다운로드한 SDK 리소스의 압축을 풀면 다음과 같습니다.

|이름     | 의미   
| ------------- |:-------------:|
|GMESDK.framework			|게임 멀티미디어 엔진 관련 리소스

## 사전 작업

### 1. SDK 파일 가져오기  
상황에 따라 Xcode의 Link Binary With Libraries에서 아래의 의존 라이브러리를 추가하고 SDK 소재 디렉터리를 지향하는 Framework Search Paths를 설정해야 합니다. 다음 그림과 같습니다.  


### 2. 의존 라이브러리 추가  
다음 그림을 참조하십시오.  

![](https://main.qcloudimg.com/raw/b6156b8c7a596248c148607070e38f67.png)
  


