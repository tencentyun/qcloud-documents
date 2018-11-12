Tencent Cloud GME SDK의 사용을 환영합니다. Unity 개발자가 Tencent Cloud GME 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 Unity 개발에 적합한 프로젝트 구성을 소개합니다.

## SDK 준비

다음의 프로세스를 통해 SDK를 획득할 수 있습니다.

### SDK 다운로드

[다운로드 가이드](https://cloud.tencent.com/document/product/607/18521)에서 관련 Demo 및 SDK를 다운로드하십시오.

페이지에서 Unity 버전의 SDK 리소스를 찾습니다.

[다운로드] 버튼을 한 번 클릭합니다. 다운로드한 SDK 리소스의 압축을 풀면 다음이 포함됩니다.
![](https://main.qcloudimg.com/raw/55494d9bb9145938f0594416f73b29f7.png)
파일 설명:

|파일 이름       | 설명           
| ------------- |:-------------:|
| Plugins   	|SDK 라이브러리 파일|
| Scripts     	|SDK 코드 파일|

## 예비 작업

### 1. Plugins 파일 가져오기

개발 키트 패키지 중 Plugins 폴더의 파일을 Unity 프로젝트의 Assets 하의 Plugins 폴더에 복사합니다. 다음 그림과 같습니다.  
![](https://main.qcloudimg.com/raw/1221a25f62cedd3831cf2bb27bb1ea45.png)

### 2. 코드 파일 가져오기

개발 키트 패키지 중 Scripts 폴더의 파일을 Unity 프로젝트의 코드가 저장되는 폴더에 복사합니다. 다음 그림과 같습니다.  
![](https://main.qcloudimg.com/raw/8904a83c6173fa7c5b04ddb0e48138ca.png)
### 3. 오디오 설정
Unity 편집기에서 Edit-Project Setting-Audio에는 기본값을 사용하면 됩니다. 해당 설정을 수정하는 경우, iOS에 하드웨어 버퍼 설정으로 인해 Unity 효과음 재생은 영향을 받으므로 중단될 수 있습니다.
![](https://main.qcloudimg.com/raw/df14517cac7fc29383c90720627572c7.png)

다음 그림의 모드로 살정하는 경우, iOS에 하드웨어 버퍼 설정으로 인해 Unity 효과음 재생은 영향을 받으므로 중단될 수 있습니다.

![](https://main.qcloudimg.com/raw/69857f53bdc2ee7c7ad5e48777620df1.png)

