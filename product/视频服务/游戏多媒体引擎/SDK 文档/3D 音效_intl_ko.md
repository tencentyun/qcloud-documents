## 소개
Tencent Cloud 게임 멀티미디어 엔진 SDK의 사용을 환영합니다. 개발자가 Tencent Cloud 게임 멀티미디어 엔진 제품 API를 디버깅하고 연결하는 데 도움이 되도록 여기에 GME 3D 사운드의 액세스 기술 문서를 소개합니다.


## 3D 사운드 액세스
### 3D 사운드 엔진 초기화
이 함수는 3D 사운드 엔진 초기화에 사용되며 방 입장 후 호출합니다. 3D 사운드를 사용하기 전에 반드시 이 인터페이스를 호출해야 합니다. 3D 사운드를 수신만 하고 발송하지 않은 사용자도 마찬가지입니다.

#### 함수 프로토타입  
```
public abstract int InitSpatializer()
```

### 3D 사운드 활성화 또는 비활성화
이 함수는 3D 사운드 활성화 또는 비활성화에 사용됩니다. 활성화하면 3D 사운드를 들을 수 있습니다.

#### 함수 프로토타입  
```
public abstract int EnableSpatializer(bool enable)
```
|매개변수	|유형	|의미 |
| ------- |---------|------|
| enable    	|BOOL    	|활성화하면 3D 사운드를 들을 수 있습니다.|

### 현재 3D 사운드 상태 획득
이 함수는 현재 3D 사운드 상태 획득에 사용됩니다.

#### 함수 프로토타입  
```
public abstract bool IsEnableSpatializer()
```

|반환 값	|의미	|
| ------- |---------|
| true    	|활성화 상태    	|
| false    	|비활성화 상태	|  

### 사운드 소스 방위 업데이트(방향 포함)
이 함수는 사운드 소스 방위각 정보를 업데이트하는 데 사용되며, 프레임별 호출하면 3D 사운드를 실현할 수 있습니다.

#### 거리와 소리 감쇠의 관계

3D 사운드 중, 사운드 소스 음량의 크기와 사운드 소스 거리는 어느 정도의 감쇠 관계가 존재합니다. 단위 거리가 500을 초과하면 음량이 0에 가깝게 감쇠됩니다.

|거리 범위(엔진 단위)|감쇠 공식	|
| ------- |---------|
| 0< N <range/5  	|감쇠 계수: 1.0(음량 감쇠하지 않음)	|
| N≥range/5  |감쇠 계수: 40/N          			|

 ![](https://main.qcloudimg.com/raw/50e745c853ab0e3f9f3bbef9d9cfc401.jpg)

#### 함수 프로토타입  
```
public abstract int UpdateSelfPosition(int x, int y, int z, int pitch, int yaw, int roll, int range)
```
GME에 설계한 글로벌 좌표계(이 좌표계는 Unreal 엔진 좌표계와 같고, Unity 엔진과 같지 않으므로 개발자는 주의해야 합니다):
- X, Y, Z축은 각자 앞쪽, 오른쪽, 그리고 위쪽을 가리킵니다.
- pitch: 오른쪽 축(Y축)을 중심으로 회전하여, 위 아래를 관찰하고 0은 앞을 가리킵니다. 아래를 향하면 수치가 증가하고, 위를 향하면 수치가 감소합니다. 가상 좌표계와 상반됩니다.
- yaw: 위쪽 축(Z축)을 중심으로 회전하여, 좌우를 관찰하고 0은 동쪽을 가리킵니다. 북쪽을 향하면 수치가 증가하고, 남쪽을 향하면 수치가 감소합니다.
- roll: 정축(X축)을 중심으로 회전하여, 머리를 기울여 관찰하고 0은 사람의 몸이 바닥과 수직 상태임을 뜻합니다. 시계 반대 방향으로 기울면 수치가 증가하고, 시계 방향으로 기울면 수치가 감소합니다. 가상 좌표계와 상반됩니다.

|매개변수     |유형         |의미|
| ------------- |-------------|-------------
| x   		|int		|자체 좌표 X축 좌표	|
| y    	|int		|자체 좌표 Y축 좌표	|
| z    	|int 		|자체 좌표 Z축 좌표	|
| pitch   	|int  	|Y축을 중심으로 회전하여, 피치각이라고도 합니다. 범위는 -90 ~90이며 90은 Z축 반대 방향을 보고 있음을 의미합니다.|
| yaw    	|int  	|Z축을 중심으로 회전하여, 편주각이라고도 합니다. 범위는 -180 ~ 180이며 90은 X축 방향을 보고 있음을 의미합니다.|
| roll    	|int  	|X축을 중심으로 회전하여, 롤 각이라고도 합니다. 범위는 -180 ~ 180이며 90은 사용자의 몸이 바닥과 평행하고 머리가 Y축 방향을 향하고 있음을 의미합니다.|
| range 	|int  	|효과음 수신 가능 범위 설정|




#### 함수 원리

![](https://main.qcloudimg.com/raw/f59ba4161fd1c9b53ca7e66b2213e851.png)

그림의 매개변수에서 볼 수 있듯이, 수신측 사용자가 A 포인트에 있고, 발신측 사용자가 B 포인트에 있음을 가정하면, <a href="https://www.codecogs.com/eqnedit.php?latex=\angle&space;CAB'" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\angle&space;CAB'" title="\angle CAB'" /></a>는 azimuth 방위이고, <a href="https://www.codecogs.com/eqnedit.php?latex=\angle&space;B'AB" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\angle&space;B'AB" title="\angle B'AB" /></a>는 elevation 각도이며 AB의 거리는 곧 distance_cm이 됩니다.
좌표 <a href="https://www.codecogs.com/eqnedit.php?latex=A\left&space;(&space;x_{1},&space;y_{1},&space;z_{1}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A\left&space;(&space;x_{1},&space;y_{1},&space;z_{1}&space;\right&space;)" title="A\left ( x_{1}, y_{1}, z_{1} \right )" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=B\left&space;(&space;x_{2},&space;y_{2},&space;z_{2}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B\left&space;(&space;x_{2},&space;y_{2},&space;z_{2}&space;\right&space;)" title="B\left ( x_{2}, y_{2}, z_{2} \right )" /></a>를 <a href="https://www.codecogs.com/eqnedit.php?latex=A\left&space;(&space;0,&space;0,0&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A\left&space;(&space;0,&space;0,0&space;\right&space;)" title="A\left ( 0, 0,0 \right )" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=B\left&space;(&space;x,&space;y,z\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B\left&space;(&space;x,&space;y,z\right&space;)" title="B\left ( x, y,z\right )" /></a>로 전환하면, 그 중에 <a href="https://www.codecogs.com/eqnedit.php?latex=x=x_{2}-x_{1},y=y_{2}-y_{1},z=z_{2}-z_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x=x_{2}-x_{1},y=y_{2}-y_{1},z=z_{2}-z_{1}" title="x=x_{2}-x_{1},y=y_{2}-y_{1},z=z_{2}-z_{1}" /></a>
계산 공식은 다음과 같습니다.
![](https://main.qcloudimg.com/raw/e1aa4d09b144af4ea920d63cf9cac6bb.png)






