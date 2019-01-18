## 简介
欢迎使用腾讯云游戏多媒体引擎 SDK 。为方便开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍 GME 3D 音效的接入技术文档。


## 3D 音效接入
### 1、初始化 3D 音效引擎
此函数用于初始化 3D 音效引擎，在进房后调用。在使用 3D 音效之前必须先调用此接口，只接收 3D 音效而不发出 3D 音效的用户也需要调用此接口。

#### 函数原型  
```
public abstract int InitSpatializer(string modelPath)
```

|参数	|类型	|意义 |
| ------- |---------|------|
| modelPath    	|string    	|3D音效资源文件路径，资源文件详情咨询腾讯云相关工作人员|

### 2、开启或关闭 3D 音效
此函数用于开启或关闭 3D 音效。开启之后可以听到 3D 音效。

#### 函数原型  
```
public abstract int EnableSpatializer(bool enable, bool applyToTeam)
```

|参数	|类型	|意义 |
| ------- |---------|------|
| enable    	|bool    	|开启之后可以听到 3D 音效|
| applyToTeam  	|bool    	|3D语音是否作用于小队内部，仅 enble 为 true 时有效|

### 3、获取当前 3D 音效状态
此函数用于获取当前 3D 音效状态。

#### 函数原型  
```
public abstract bool IsEnableSpatializer()
```

|返回值	|意义	|
| ------- |---------|
| true    	|开启状态    	|
| false    	|关闭状态	|  

### 4、更新声源方位（包含朝向）
此函数用于更新声源方位角信息，每帧调用便可实现 3D 音效效果。

#### 距离与声音衰减的关系

3D 音效中，音源音量的大小与音源距离有一定的衰减关系。单位距离超过500之后，音量衰减到几乎为零。

|距离范围（引擎单位）|衰减公式	|
| ------- |---------|
| 0< N <range/5  	|衰减系数：1.0 （音量无衰减）	|
| N≥range/5  |衰减系数：40/N          			|

![](https://main.qcloudimg.com/raw/50e745c853ab0e3f9f3bbef9d9cfc401.jpg)

#### 函数原型  
```
public abstract void UpdateAudioRecvRange(int range)
```

|参数     | 类型         |意义|
| ------------- |-------------|-------------|
| range 	|int  	|设定音效可接收的范围|

```
public abstract int UpdateSelfPosition(int position[3], float axisForward[3], float axisRight[3], float axisUp[3])
```

在 GME 中设计的世界坐标系下（此坐标系与 Unreal 引擎坐标系相同，与 Unity 引擎不同，需要开发者注意）：
- x 轴指向前方，y 轴指向右方，z 轴指向上方。

|参数     | 类型         |意义|
| ------------- |-------------|-------------
| position   	|int[]		|自身在世界坐标系中的坐标，顺序是前、右、上|
| axisForward   |float[]  	|自身坐标系前轴的单位向量|
| axisRight    	|float[]  	|自身坐标系右轴的单位向量|
| axisUp    	|float[]  	|自身坐标系上轴的单位向量|

#### 示例代码

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







