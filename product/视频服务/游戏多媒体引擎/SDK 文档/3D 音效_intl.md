## Overview
Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. This document provides a detailed description that makes it easy for developers to debug and integrate GME APIs for 3D sound effect.


## Integrating 3D Sound Effect
### 1. Initialize 3D sound effect
This function is used to initialize 3D sound effect and can be called after a user enters a room. You need to call this API before you can use 3D sound effect. Any user who only receives 3D sound effect and does not send it also needs to call this API.

#### Function prototype  
```
public abstract int InitSpatializer(string modelPath)
```

| Parameter | Type | Description |
| ------- |---------|------|
| modelPath | string | Indicates the path of 3D sound effect resource files. Contact Tencent Cloud personnel for more information on the resource files. |

### 2. Enable/disable 3D sound effect
This function is used to enable/disable 3D sound effect. You can hear the 3D sound after enabling it.

#### Function prototype  
```
public abstract int EnableSpatializer(bool enable, bool applyToTeam)
```

| Parameter | Type | Description |
| ------- |---------|------|
| enable | bool | You can hear the 3D sound after enabling it |
| applyToTeam | bool | Indicates whether 3D sound applies to the team. This parameter takes effect only when "enable" is true. |

### 3. Obtain status of 3D sound effect
This function is used to obtain status of 3D sound effect.

#### Function prototype  
```
public abstract bool IsEnableSpatializer()
```

| Returned Value | Description |
| ------- |---------|
| true | Indicates "enabled" |
| false | Indicates "disabled" |

### 4. Update sound source azimuth (including orientation)
This function is used to update the sound source azimuth information. The 3D sound effect can be achieved by calling this function for each frame.

#### The relationship between distance and sound attenuation

In 3D sound effect, there is an attenuation relationship between the volume of the sound source and the distance to the sound source. When the distance exceeds 500 (in a specified unit), the volume attenuates to almost zero.

| Distance Range (In the unit of engine) | Attenuation Formula |
| ------- |---------|
| 0< N <range/5  	|Attenuation coefficient: 1.0 (no attenuation)	|
| N≥range/5  |Attenuation coefficient: 40/N  			|

![](https://main.qcloudimg.com/raw/50e745c853ab0e3f9f3bbef9d9cfc401.jpg)

#### Function prototype  
```
public abstract void UpdateAudioRecvRange(int range)
```

| Parameter | Type | Description |
| ------------- |-------------|-------------|
| range | int | Sets the range within which the sound can be received |

```
public abstract int UpdateSelfPosition(int position[3], float axisForward[3], float axisRight[3], float axisUp[3])
```

In the world coordinate system designed in GME (Note: it is the same as that in Unreal engine, but different from that in Unity engine):
- The x axis points forward, the y axis points to the right and the z axis points upward.

| Parameter | Type | Description |
| ------------- |-------------|-------------
| position | int[] | The user's X-Y-Z coordinates in the world coordinate system |
| axisForward | float[] | The unit vector of x axis in the coordinate system |
| axisRight | float[] | The unit vector of y axis in the coordinate system |
| axisUp | float[] | The unit vector of z axis in the coordinate system |

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








