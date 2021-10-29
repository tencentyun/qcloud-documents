


<dx-alert infotype="notice" title="">
gameInfo.gameId、gameInfo.secretKey、config.url 均需前往 [游戏联机对战引擎控制台](https://console.cloud.tencent.com/mgobe)，在游戏概览的基本信息里获取。
</dx-alert>


1. 在 game.js 中输入以下代码，完成 SDK 初始化，获得 room 实例。
	```
	const gameInfo = {
		// 替换 为控制台上的“游戏ID”
		gameId: "xxxxxxxx",
		// 玩家 openId
		openId: 'openid_123_test',
		// 替换 为控制台上的“游戏Key”
		secretKey: 'BjU3QBZLFxxxxxxxxxxxxxxxxxx',
	};

	const config = {
		// 替换 为控制台上的“域名”
		url: 'xxxxxxxx.wxlagame.com',
		reconnectMaxTimes: 5,
		reconnectInterval: 1000,
		resendInterval: 1000,
		resendTimeout: 10000,
	};

	// 初始化 Listener
	MGOBE.Listener.init(gameInfo, config, event => {
		if (event.code === 0) {
			console.log("初始化成功");
			// 初始化成功之后才能调用其他 API
			// ...
		}
	});

	// 实例化 Room 对象
	const room = new MGOBE.Room();
	```
2. 修改初始化回调函数，调用 room 对象的查询房间接口（getRoomDetail），即可验证是否成功接入对战平台。示例代码如下所示： 
	```
	// 初始化 Listener
	MGOBE.Listener.init(gameInfo, config, event => {
		if (event.code === 0) {
			console.log("初始化成功");
			// 初始化成功之后才能调用其他 API
			// 查询玩家自己的房间
			room.getRoomDetail(event => {
				if (event.code !== 0 && event.code !== 20011) {
					return console.log(event);
				}

				console.log("查询成功");

				if (event.code === 20011) {
					console.log("玩家不在房间内");
				} else {
					// 玩家已在房间内
					console.log("房间名", event.data.roomInfo.name);
				}
			});
		}
	});
	```
3. 在微信开发者工具中编译该项目，控制台中输出“查询成功”信息即表示接入成功。

<dx-alert infotype="explain" title="">
详细的 API 使用方法，您可以参考 [SDK 使用流程](https://cloud.tencent.com/document/product/1038/33315) 。
</dx-alert>


