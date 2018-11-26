## 소개
Tencent Cloud GME SDK의 사용을 환영합니다. 개발자가 Tencent Cloud GME 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 GME 3D 사운드의 액세스 기술 문서를 소개합니다.


## 3D 사운드 액세스
### 1. 3D 사운드 엔진 초기화
이 함수는 3D 사운드 엔진 초기화에 사용되며 방 입장 후 호출합니다. 3D 사운드를 사용하기 전에 반드시 이 인터페이스를 호출해야 합니다. 3D 사운드를 수신만 하고 발송하지 않은 사용자도 마찬가지입니다.

#### 함수 프로토타입  
```
public abstract int InitSpatializer(string modelPath)
```

|매개변수	|유형	|의미 |
| ------- |---------|------|
| modelPath    	|string    	|3D 사운드 리소스 파일 경로, 리소스 파일 세부 정보는 Tencent Cloud 관련 직원에게 문의하십시오.|

### 2. 3D 사운드 활성화 또는 비활성화
이 함수는 3D 사운드 활성화 또는 비활성화에 사용됩니다. 활성화하면 3D 사운드를 들을 수 있습니다.

#### 함수 프로토타입  
```
public abstract int EnableSpatializer(bool enable, bool applyToTeam)
```

|매개변수	|유형	|의미 |
| ------- |---------|------|
| enable    	|bool    	|활성화하면 3D 사운드를 들을 수 있습니다.|
| applyToTeam  	|bool    	|3D 음성의 팀 내 적용 여부, enble이 true일 때에만 유효합니다.|

### 3. 현재 3D 사운드 상태 획득
이 함수는 현재 3D 사운드 상태 획득에 사용됩니다.

#### 함수 프로토타입  
```
public abstract bool IsEnableSpatializer()
```

|반환 값	|의미	|
| ------- |---------|
| true    	|활성화 상태    	|
| false    	|비활성화 상태	|  

### 4. 사운드 소스 방위 업데이트(방향 포함)
이 함수는 사운드 소스 방위각 정보를 업데이트하는 데 사용되며, 프레임별 호출하면 3D 사운드를 실현할 수 있습니다.

#### 거리와 소리 감쇠의 관계

3D 사운드 중, 사운드 소스 음량의 크기와 사운드 소스 거리는 어느 정도의 감쇠 관계가 존재합니다. 단위 거리가 500을 초과하면 음량이 0에 가깝게 감쇠됩니다.

|거리 범위(엔진 단위)|감쇠 공식	|
| ------- |---------|
| 0< N <range/5  	|감쇠 계수: 1.0(음량 감쇠하지 않음)	|
| N≥range/5  |감쇠 계수: 40/N          			|

![](https://main.qcloudimg.com/raw/50e745c853ab0e3f9f3bbef9d9cfc401.jpg)

#### 함수 프로토타입  
```
public abstract void UpdateAudioRecvRange(int range)
```

|매개변수     |유형         |의미|
| ------------- |-------------|-------------|
| range 	|int  	|효과음 수신 가능 범위 설정|

```
public abstract int UpdateSelfPosition(int position[3], float axisForward[3], float axisRight[3], float axisUp[3])
```

GME에 설계한 글로벌 좌표계(이 좌표계는 Unreal 엔진 좌표계와 같고, Unity 엔진과 같지 않으므로 개발자는 주의해야 합니다):
- X, Y, Z축은 각자 앞쪽, 오른쪽, 그리고 위쪽을 가리킵니다.

|매개변수     |유형         |의미|
| ------------- |-------------|-------------
| position   	|int[]		|자체가 세계 좌표계의 좌표로, 순서는 앞쪽, 오른쪽, 위쪽입니다.|
| axisForward   |float[]  	|자체 좌표계 앞쪽 축의 단위 백터|
| axisRight    	|float[]  	|자체 좌표계 오른쪽 축의 단위 백터|
| axisUp    	|float[]  	|자체 좌표계 위족 축의 단위 백터|

#### 샘플 코드

Unreal:
```
FVector cameraLocation = UGameplayStatics::GetPlayerCameraManager(GetWorld(), 0)->GetCameraLocation();
FRotator cameraRotation = UGameplayStatics::GetPlayerCameraManager(GetWorld(), 0)->GetCameraRotation();
int position[] = { (int)cameraLocation.X,(int)cameraLocation.Y, (int)cameraLocation.Z };
FMatrix matrix = ((FRotationMatrix)cameraRotation);
float forward[] = { matrix.GetColumn(0).X,matrix.GetColumn(1).X,matrix.GetColumn(2).X };
float right[] = { matrix.GetColumn(0).Y,matrix.GetColumn(1).Y,matrix.GetColumn(2).Y };
float up[] = { matrix.GetColumn(0).Z,matrix.GetColumn(1).Z,matrix.GetColumn(2).Z};
ITMGContextGetInstance()->GetRoom()->UpdateSelfPosition(position, forward, right, up); 	
```
Unity:
```
Transform selftrans = currentPlayer.gameObject.transform;
Matrix4x4 matrix = Matrix4x4.TRS(Vector3.zero, selftrans.rotation, Vector3.one);
int[] position = new int[3] { selftrans.position.z, selftrans.position.x, selftrans.position.y };
float[] axisForward = new float[3] { matrix.m22, matrix.m02, matrix.m12 };
float[] axisRight = new float[3] { matrix.m20, matrix.m00, matrix.m10 };
float[] axisUp = new float[3] { matrix.m21, matrix.m01, matrix.m11 };
ITMGContext.GetInstance().GetRoom().UpdateSelfPosition(position, axisForward, axisRight, axisUp);
```








