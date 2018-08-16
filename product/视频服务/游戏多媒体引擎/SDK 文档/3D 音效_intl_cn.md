## 简介
欢迎使用腾讯云游戏多媒体引擎 SDK 。为方便开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍 GME 3D 音效的接入技术文档。


## 3D 音效接入
### 开关 3D 音效
此函数用于开关 3D 音效。在使用 3D 音效之前必须先调用此接口，只接收 3D 音效而不发出 3D 音效的用户也需要调用此接口。

#### 函数原型  
```
QAVAudioCtrl virtual int EnableSpatializer(bool enable)
```

|参数     | 类型         |意义|
| ------------- |:-------------:|-------------
| enable    |bool         |设置是否开启|



### 获取当前 3D 音效状态
此函数获取当前 3D 音效的状态，返回值为 bool 类型数值。

#### 函数原型  
```
QAVAudioCtrl virtual bool IsEnableSpatializer()
```

|返回值	|意义	|
| ------- |---------|
| true    	|开启状态     |
| false    	|关闭状态       |  

### 更新声源方位（包含朝向）
此函数用于更新声源方位角信息，传入用户 openID 后每帧调用便可实现 3D 音效效果。

距离与声音衰减的关系：3D 音效中，音源音量的大小与音源距离有一定的衰减关系。单位距离超过 500 之后，音量衰减到几乎为零。


|距离范围（引擎单位）|衰减公式	|
| ------- |---------|
| 0< N <40  	|衰减系数：1.0 （音量无衰减）|
| N≥40  |衰减系数：40/N          |

 ![](https://main.qcloudimg.com/raw/50e745c853ab0e3f9f3bbef9d9cfc401.jpg)

#### 函数原型  
```
QAVAudioCtrl virtual int UpdateSpatializer(string identifier,float azimuth,float elevation,float distance_cm)
```
|参数     | 类型         |意义|
| ------------- |-------------|-------------
| identifier   		|string	|传入一个 identifier，以识别用户（identifier 在进房时候已经确定）	|
| azimuth    		|float	|方位参数（需要计算）											|
| elevation    	|float 	|角度参数（需要计算）											|
| distance_cm    	|float  	|距离参数（需要计算）											|

#### 函数原理
![](https://main.qcloudimg.com/raw/0f90e8e84915c3f34482b1d40b0630c0.png)

![](https://main.qcloudimg.com/raw/f59ba4161fd1c9b53ca7e66b2213e851.png)

则计算公式为：
![](https://main.qcloudimg.com/raw/e1aa4d09b144af4ea920d63cf9cac6bb.png)

#### 示例代码
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





