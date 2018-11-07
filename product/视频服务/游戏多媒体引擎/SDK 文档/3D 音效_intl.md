## Overview
Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides a detailed description that makes it easy for developers to debug and integrate GME 3D sound effect APIs.


## 3D Sound Effect Integration
### 1. Initialize 3D sound effect
This function is used to Initialize 3D sound effect after entering the room. This API must be called before using 3D sound effect, no matter for receiving or sending the 3D sound effect. 

#### Function prototype  
```
public abstract int InitSpatializer()
```

### 2. Enable/disable 3D sound effect
This function is used to enable/disable 3D sound effect.

#### Function prototype  
```
QAVAudioCtrl virtual int EnableSpatializer(bool enable, bool applyToTeam)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| enable    |bool         | Specifies whether to enable 3D sound effect |
| applyToTeam    |bool         | Specifies whether to use spatial audio in the same team |


### 3. Obtain status of 3D sound effect
This function is used to obtain the status of 3D sound effect and returns a Boolean value.

#### Function prototype  
```
QAVAudioCtrl virtual bool IsEnableSpatializer()
```

| Returned Value | Description |
| ------- |---------|
| true    	|Enabled |
| false    	|Disabled |  

### 4. Update sound source position (including direction)

This function is used to set its own position and direction related information.  This API can be called frame by frame to update the 3D sound effect.

#### relationship between sound source distance and sound volume attenuation.

In 3D sound effect, the sound volume has a certain attenuation relationship with the sound source distance. When the unit distance exceeds 500, the volume attenuates to almost zero

| Distance Range (In the unit of engine) | Attenuation Formula |
| ------- |---------|
| 0< N <range/5	| Attenuation coefficient: 1.0 (no attenuation) |
| N≥range/5  |Attenuation coefficient: 40/N |

 ![](https://main.qcloudimg.com/raw/82892249eab8fea3bcb9149e8eee37f1.jpg)

#### Function prototype  
```
ITMGRoom virtual void UpdateAudioRecvRange(int range)
```

|Parameter | Type | Description |
| ------------- |-------------|-------------
| range 	|int  	|The range of voice can be reveiced|

```
ITMGRoom virtual intUpdateSelfPosition(int position[3], float axisForward[3], float axisRight[3], float axisUp[3])
```
The definition of GME coordinate system is as belows(it is the same as the definition of Unreal's but is not as Unity's)
- x axis points to the front, y axis points to the right, z axis points to the top.

|Parameter | Type | Description |
| ------------- |-------------|-------------
| position   	|int[]		|Self-position, the coordinate order is front, right and top|
| axisForward   |float[]  	|The front axis value of self coordinate system|
| axisRight    	|float[]  	|The right axis value of self coordinate system|
| axisUp    	|float[]  	|The top axis value of self coordinate system|


#### Sample code

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
Unity：
```
Transform selftrans = currentPlayer.gameObject.transform;
Matrix4x4 matrix = Matrix4x4.TRS(Vector3.zero, selftrans.rotation, Vector3.one);
int[] position = new int[3] { selftrans.position.z, selftrans.position.x, selftrans.position.y };
float[] axisForward = new float[3] { matrix.m22, matrix.m02, matrix.m12 };
float[] axisRight = new float[3] { matrix.m20, matrix.m00, matrix.m10 };
float[] axisUp = new float[3] { matrix.m21, matrix.m01, matrix.m11 };
ITMGContext.GetInstance().GetRoom().UpdateSelfPosition(position, axisForward, axisRight, axisUp);
```




