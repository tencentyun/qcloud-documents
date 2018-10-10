## Overview
Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. This document provides a detailed description that makes it easy for developers to debug and integrate GME APIs for 3D sound effect.


## Integrating 3D Sound Effect
### Initialize 3D sound effect
This function is used to Initialize  3D sound effect.

#### Function prototype  
```
public abstract int InitSpatializer()
```

### Enable/disable 3D sound effect
This function is used to enable/disable 3D sound effect. You need to call this API before you can use 3D sound effect. Any user who only receives 3D sound effect and does not send it also needs to call this API.

#### Function prototype  
```
QAVAudioCtrl virtual int EnableSpatializer(bool enable, bool applyToTeam)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| enable    |bool         | Specifies whether to enable 3D sound effect |
| applyToTeam    |bool         | Be valid while bEnable=true, specifies whether to use spatial audio in the same team |



### Obtain status of 3D sound effect
This function is used to obtain the status of 3D sound effect and returns a Boolean value.

#### Function prototype  
```
QAVAudioCtrl virtual bool IsEnableSpatializer()
```

| Returned Value | Description |
| ------- |---------|
| true    	|Enabled |
| false    	|Disabled |  

### Update self position (including orientation)
Set own position and rotate information to GME for function: Spatializer && WorldMode.
The relationship between distance and sound attenuation.

| Distance Range (In the unit of engine) | Attenuation Formula |
| ------- |---------|
| 0< N <range/5	| Attenuation coefficient: 1.0 (no attenuation) |
| N≥range/5  |Attenuation coefficient: 40/N |

 ![](https://main.qcloudimg.com/raw/50e745c853ab0e3f9f3bbef9d9cfc401.jpg)

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

|Parameter | Type | Description |
| ------------- |-------------|-------------
| position   	|int[]		|Position of self, the order is forword, right and up|
| axisForward   |float[]  	|The forward axis of self coordinate system|
| axisRight    	|float[]  	|The right axis of self coordinate system|
| axisUp    	|float[]  	|The up axis of self coordinate system|


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




