## Overview
Thank you for using Tencent Cloud Game Multimedia Engine SDK. This document provides a detailed description that makes it easy for developers to debug and integrate GME APIs for 3D sound effect.


## Integrating 3D Sound Effect
### Enable/disable 3D sound effect
This function is used to enable/disable 3D sound effect. You need to call this API before you can use 3D sound effect. Any user who only receives 3D sound effect and does not send it also needs to call this API.

#### Function prototype  
```
QAVAudioCtrl virtual int EnableSpatializer(bool enable)
```

| Parameter | Type | Description |
| ------------- |:-------------:|-------------
| enable    |bool         | Specifies whether to enable 3D sound effect |



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

### Update sound source azimuth (including orientation)
This function is used to update the sound source azimuth information. The 3D sound effect can be achieved by calling this function for each frame after user's openID is passed.

The relationship between distance and sound attenuation: In 3D sound effect, there is an attenuation relationship between the volume of the sound source and the distance to the sound source. When the distance exceeds 500 (in a specified unit), the volume attenuates to almost zero.


| Distance Range (In the unit of engine) | Attenuation Formula |
| ------- |---------|
| 0< N <40  	| Attenuation coefficient: 1.0 (no attenuation) |
| N≥40  |Attenuation coefficient: 40/N |

 ![](https://main.qcloudimg.com/raw/50e745c853ab0e3f9f3bbef9d9cfc401.jpg)

#### Function prototype  
```
QAVAudioCtrl virtual int UpdateSpatializer(string identifier,float azimuth,float elevation,float distance_cm)
```
| Parameter | Type | Description |
| ------------- |-------------|-------------
| identifier   		|string	| Input an identifier to identify the user (identifier is already given when the user enters the room) |
| azimuth    		|float	| Azimuth parameter (to be calculated)											|
| elevation    	|float 	| Elevation parameter (to be calculated)											|
| distance_cm    	|float  	| Distance parameter (to be calculated)											|

#### Principle behind the function
![](https://main.qcloudimg.com/raw/0f90e8e84915c3f34482b1d40b0630c0.png)

![](https://main.qcloudimg.com/raw/f59ba4161fd1c9b53ca7e66b2213e851.png)

The formula is as follows:
![](https://main.qcloudimg.com/raw/e1aa4d09b144af4ea920d63cf9cac6bb.png)

#### Sample code
```
private void CalculatePosition()
{
	Transform selftrans = currentPlayer.gameObject.transform;
	Vector3 relativePos = new  Vector3 (playerPrefab.transform.position.x - selftrans.position.x, playerPrefab.transform.position.y - selftrans.position.y, playerPrefab.transform.position.z - selftrans.position.z);
	Vector3 rotation = Quaternion.Inverse(selftrans.rotation) * relativePos;  
	double distance = 0;
	double azimuth = 0;
	double elevation = 0;
	double x = rotation.z;
	double y = rotation.x;
	double z = rotation.y;
	double sqxy = Math.Sqrt(x*x + y*y);
	distance = Math.Sqrt(relativePos.x*relativePos.x + relativePos.y*relativePos.y + relativePos.z*relativePos.z)*10;
	if (y != 0)
	{
		if (x != 0)
		{
			if (x > 0)
			{
				azimuth =  Math.Atan(y / x);
			}
			else
			{
				azimuth = (Math.PI) + Math.Atan(y / x);
			}
		}
		else
		{
			if (y > 0)
			{
				azimuth = -Math.PI/2;
			}
			else
			{
				azimuth = Math.PI/2;
			}
		}
	}
	else
	{
		if (x > 0)
		{
			azimuth = 0;
		}
		else
		{
			azimuth = -Math.PI;
		}
	}

	if (sqxy != 0)
	{
		elevation = Math.Atan(z / sqxy);
	}
	else
	{
		if (z > 0)
		{
			elevation = Math.PI;
		}
		else
		{
			elevation = -Math.PI;
		}
	}
	Debug.LogFormat(string.Format ("3Daudio UpdateSpatializer, azimuth:{0}, elevation:{1}, distance:{2}", (float)(azimuth * 180)/Math.PI, (float)(elevation * 180)/Math.PI,distance));		
}
```






