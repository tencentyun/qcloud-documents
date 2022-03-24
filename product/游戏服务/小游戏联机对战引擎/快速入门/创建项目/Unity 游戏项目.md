>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。



本文档以 Unity Editor 2019.3 版本为例，指导开发者在 Unity 项目中快速接入游戏联机对战引擎 MGOBE。

## 版本支持
Unity Editor 版本： 2019.1.9+。

## 前提条件

- 已在游戏联机对战引擎控制台创建游戏，并开通联机对战服务，您可参考 [开通服务](https://cloud.tencent.com/document/product/1038/33299)。
- 已获取游戏 gameID 和 secretKey，您可在游戏概览的基本信息里查看。


## 操作步骤
### 创建游戏项目
1. 打开 Unity Hub，创建一个游戏项目。如下图所示：
![](https://main.qcloudimg.com/raw/4ef6bac33e204456e4a0870f8ff0186c.jpg)
2. 单击**创建**，进入项目开发界面：
![](https://main.qcloudimg.com/raw/714a449465bec007689a6c2325712356.jpg)



### 导入 Mgobe Package
1. 将 `com.unity.Mgobe.unitypackage` 拖入 editor 中的 Project 栏，单击**import**进行 package 导入。 


<dx-alert infotype="explain" title="">
您可通过 [SDK 下载](https://cloud.tencent.com/document/product/1038/33406) 页面，下载 Package 即 Unity SDK 。
</dx-alert>

![](https://main.qcloudimg.com/raw/77671c4601cd26f2cffdce577b802528.jpg)
![](https://main.qcloudimg.com/raw/2cc301f6917c6a7026558fb2ca920079.jpg)
2. 在 Assets 目录下创建 “Scripts” 文件夹，并新建 Scripts/main.cs 文件。
3. 在 Hierachy 视图下，右击 SampleScene，选中 GameObject > CreateEmpty，新建一个空的游戏对象。
![](https://main.qcloudimg.com/raw/333414f0b3ef02515c56d3546eb161aa.jpg)
4. 选中新建的 GameObject，拖动 main.cs，添加为该 GameObject 的 Component。
![](https://main.qcloudimg.com/raw/b83a9b0bbf7e46ebe09dca89383b016f.jpg)
5. 参考以下示例代码，将 mgobe package 导入 main.cs。
```
using com.unity.mgobe;
```

### 调用 API 
1. 在 main.cs 中输入以下代码，完成 SDK 初始化，获得 room 实例。
<dx-codeblock>
:::  Java
GameInfoPara gameInfo = new GameInfoPara {
		// 替换 为控制台上的“游戏ID”
		GameId = "xxxxxxxxxx",
		// 玩家 openId
		OpenId = "openid_123_test",
		//替换 为控制台上的“游戏Key”
		SecretKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		};
	
	ConfigPara config = new ConfigPara {
		// 替换 为控制台上的“域名”
		Url = "pm01xrp4.wxlagame.com",
		ReconnectMaxTimes = 5,
		ReconnectInterval = 1000,
		ResendInterval = 1000,
		ResendTimeout = 10000
		};
		
	// 初始化监听器 Listener
Listener.Init (gameInfo, config, (ResponseEvent eve) => {
		if (eve.Code == 0) {
				Debug.Log ("初始化成功");
				// 初始化成功之后才能调用其他 API
				var room = new Room(null);
				// ...
		}

		// 初始化广播回调事件
		// ...
});
:::
</dx-codeblock>

2. 修改初始化回调函数，调用 room 对象的查询房间接口（getRoomDetail），即可验证是否成功接入对战平台。示例代码如下所示：
<dx-codeblock>
:::  Java
// 初始化监听器 Listener
Listener.Init (gameInfo, config, (ResponseEvent eve) => {
		if (eve.Code == 0) {
			Debug.Log ("初始化成功");
			// 初始化成功之后才能调用其他 API
			// 查询玩家自己的房间
			var room = new Room (null);
			room.GetRoomDetail ((ResponseEvent e) => {
				if (e.Code != 0 && e.Code != 20011) {
						Debug.Log ("初始化失败");
				}

				Debug.Log ("查询成功");

				if (e.Code == 20011) {
						Debug.Log ("玩家不在房间内");
				} else {
						// 玩家已在房间内
						var res = (GetRoomByRoomIdRsp) e.Data;
						Debug.LogFormat ("房间名 {0}", res.RoomInfo.Name);
						}
				});
			} else {
					Debug.LogFormat ("初始化失败: {0}", eve.Code);
			}
		// 初始化广播回调事件
		// ...
});
:::
</dx-codeblock>



3. 编译并运行项目，控制台中输出“查询成功”信息即表示接入成功。
