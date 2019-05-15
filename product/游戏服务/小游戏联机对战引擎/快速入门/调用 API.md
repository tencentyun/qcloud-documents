1. 在 game.js 中输入以下代码，完成 SDK 初始化，获得 room 实例。
>!gameInfo.gameId、gameInfo.secretKey、config.url 都需要从控制台上获取。

	```
	const gameInfo = {
		version: 'v1.0',
		// 替换 为控制台上的“游戏ID”
		gameId: 965779256,
		// 玩家 ID
		playerId: 'openid_123_test',
		wxAppid: 'wx43c6c54f537cb6de',
		// 替换 为控制台上的“密钥”
		secretKey: 'BjU3QBZLFxxxxxxxxxxxxxxxxxx',
	};

	const config = {
		// 替换 为控制台上的“域名”
		url: '965779256-1.wxlagame.com',
		reconnectMaxTimes: 5,
		reconnectInterval: 1000,
		resendInterval: 1000,
		resendTimeout: 10000,
	};

	// 初始化 Listener
	Listener.init(gameInfo, config);

	// 实例化 Room 对象
	const room = new Room();
	```
2. 调用 room 对象的查询房间接口（getRoomDetail），即可验证是否成功接入对战平台。示例代码如下所示：
 
 ```
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
    console.log("房间名", event.data.roomInfo.roomName);
  }
});
```
3. 在微信开发者工具中编译该项目，控制台中输出“查询成功”信息即表示接入成功。如下图所示：
![SDK 接入后台测试](https://main.qcloudimg.com/raw/4112969668af6d1644f39ebfe45b9f31.png )

详细的 API 的使用方法您可以参考 [SDK 使用流程](https://cloud.tencent.com/document/product/1038/33315) 。
