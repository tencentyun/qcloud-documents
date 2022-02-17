为方便 Unity 开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍适用于 Unity 实时语音高清音质房间的使用文档。


## 前提条件

在 GME SDK v2.9 版本开始，GME Unity SDK 默认不支持使用实时语音高清音质房间。如非 2.9 及以上版本无需以下操作。

## 涉及功能
如果没有进行适配，Unity SDK 缺失以下功能：

实时语音高清音质房间，参考 [音质选择](https://cloud.tencent.com/document/product/607/18522)。
播放伴奏功能，参考 [实时语音伴奏](https://cloud.tencent.com/document/product/607/34377)。
实时语音变声、语音消息变声功能，参考 [变声音效文档](https://cloud.tencent.com/document/product/607/34378#.E5.8F.98.E5.A3.B0.E7.89.B9.E6.95.88)。

## 更新 SDK

### 下载链接
在通过 [下载指引](https://cloud.tencent.com/document/product/607/18521) 下载了标准版本 Unity SDK 的情况下，需要再下载其他的库文件，请提工单或者通过 [在线咨询](https://cloud.tencent.com/online-service?from=connect-us) 联系腾讯云工作人员进行获取。


### 库文件替换
将之前的 GME 库文件删除，使用下载后的库文件。增加的库文件示例如下图：

![](https://qcloudimg.tencent-cloud.cn/raw/5d218010fd171e5d098e49a609f7390d.png)


### 库文件对应功能

可以根据自己的需求只引入相应的库文件。例如只需要变声功能，则只需引入 libgme_soundtouch。

|库文件|对应功能|
|----|-----|
|libgme_fdkaac|1. 用于进入标准、高清音质房间 2. 用于播放 acc 格式伴奏文件|
|libgme_faad2|用于播放 mp4 格式伴奏文件|
|libgme_ogg|用于播放 ogg 格式伴奏文件|
|libgme_lamemp3|用于播放 mp3 格式伴奏文件|
|libgme_soundtouch|用于变声、变调功能|


## 导出配置
配置完成所需要的库文件后，iOS 平台打包动态库需要在导出时候进行配置，其他平台默认导出即可。

### Unity 2019及以上版本

#### 配置原理

新建一个 Editor OnPostprocessBuild 脚本，利用UnityEditor.iOS.Xcode.PBXProject.AddDynamicFramework，这个 API 会自动将动态库拷贝到最终出包 Bundle 的 framework 目录下，并为其签名。

#### 示例代码
可参考 Demo 工程中的 add_dylib.cs 脚本文件，根据自己工程需求将此部分代码放在工程中 Editor 文件夹下。

```
[UnityEditor.Callbacks.PostProcessBuild(1002)]
	public  static void OnPostprocessBuild (UnityEditor.BuildTarget BuildTarget, string path){  
		if (BuildTarget == UnityEditor.BuildTarget.iOS) {
			UnityEngine.Debug.Log ("OnPostprocessBuild add_dylib:" + path);
			{
				string projPath = UnityEditor.iOS.Xcode.PBXProject.GetPBXProjectPath (path);  
				UnityEditor.iOS.Xcode.PBXProject proj = new UnityEditor.iOS.Xcode.PBXProject ();  

				proj.ReadFromString (System.IO.File.ReadAllText (projPath));  
				string targetGuid = proj.TargetGuidByName (UnityEditor.iOS.Xcode.PBXProject.GetUnityTargetName ()); 
				
				//根据导入的 framework 进行删减
				string[] framework_names = {
					"libgme_fdkaac.framework",
					"libgme_lamemp3.framework",
					"libgme_ogg.framework",
					"libgme_soundtouch.framework"
				};

				for (int i = 0; i < framework_names.Length; i++)
				{
					string framework_name = framework_names[i];
					string dylibGuid = null;
					dylibGuid = proj.FindFileGuidByProjectPath("Frameworks/Plugins/iOS/" + framework_name);

					if (dylibGuid == null) {
						UnityEngine.Debug.LogWarning (framework_name + " guid not found");
					} else {
						UnityEngine.Debug.LogWarning (framework_name + " guid:" + dylibGuid);
						proj.AddDynamicFramework (targetGuid, dylibGuid);
						System.IO.File.WriteAllText (projPath, proj.WriteToString ());
					}
				}
			}
		}
	}
```


### Unity 版本低于2019

目前只有 Unity 2019 及以后版本可以使用 UnityEditor.iOS.Xcode，如果是早期 Unity 版本，可以从高版本 Unity 导出 UnityEditor.iOS.Xcode 包给低版本 Unity 使用，或者直接参考附件  [UnityEditorAV.iOS.XCode.zip](http://dldir1.qq.com/hudongzhibo/QCloud_TGP/GME/GME2.9.0/Other/UnityEditorAV.iOS.XCode.zip) 将此文件解压后放置于工程目录 Editor 文件夹下。

![](https://qcloudimg.tencent-cloud.cn/raw/a141d2c41dc4494148e9451d3d63cd38.png)

