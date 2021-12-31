在初始化 MGOBE SDK 时，为了避免在客户端泄露游戏项目的游戏密钥，可以使用签名的方式初始化 SDK。在开发者服务器通过游戏 ID、游戏密钥、玩家 openId 等信息计算出游戏签名，然后下发给客户端。客户端在初始化、掉线重连、前后台切换等场景中均会验证玩家签名信息。



## 签名计算方式


签名涉及到的字段如下：

|字段名|类型|含义|
|--|--|--|
|game_id|string|游戏 ID|
|nonce|uint64|随机数|
|open_id|string|玩家 openId|
|timestamp|uint64|时间戳（单位：秒）|
|secretKey|string|游戏密钥|

1. 拼接字符串 str：
```
// 注意字段的顺序为 game_id、nonce、open_id、timestamp
// 字段和值之间使用 = 连接
// 不同字段之间使用 & 连接
const str = "game_id=您的游戏ID&nonce=1655790837&open_id=玩家openId&timestamp=1571902273"
```
2. 计算字符串 str、secretKey 的 HMACSHA1 值，然后使用 BASE64 编码即可得到签名 sign：
```
// 使用 secretKey 作为密钥计算 str 的 HmacSHA1 值
// 然后使用 BASE64 编码
const sign = Base64.encode(HmacSHA1(str, secretKey));
```
3. 将 sign、nonce、timestamp 传给客户端 SDK 进行验证。

## 使用示例

#### 服务端

服务端可使用一个 HTTPS 服务计算签名，然后将签名 sign、随机数 nonce、时间戳 timestamp 返回给客户端。计算签名的 TypeScript 示例代码如下：

```
const Base64 = require("crypto-js/enc-base64");
const HmacSHA1 = require("crypto-js/hmac-sha1");

/**
 * 生成SDK初始化签名
 * @param secretKey {string} 游戏密钥
 * @param gameId {string} 游戏 ID
 * @param openId {string} 玩家 ID
 */
function getSignature(secretKey: string, gameId: string, openId: string): { sign: string, nonce: number, timestamp: number } {

	// 随机正整数
	const nonce = Math.floor(Math.random() * (Math.pow(2, 32) - 1));
	// 时间戳，秒
	const timestamp = Math.floor(Date.now() / 1000);

	const fields = [
		["game_id", gameId],
		["nonce", nonce],
		["open_id", openId],
		["timestamp", timestamp],
	].sort();

	const str = fields.map((field) => field.join("=")).join("&");
	const hmac = HmacSHA1(str, secretKey);
	const sign = Base64.stringify(hmac);

	return { sign, nonce, timestamp };
}

export default getSignature;
```

单击 [这里](https://mgobe-1258556906.cos.ap-shanghai.myqcloud.com/sdk_signature.zip)，下载签名示例代码。

#### 客户端

客户端在初始化 SDK 时，需要实现一个 createSignature 签名函数，从服务端获取签名信息然后回调给 SDK。示例代码如下：

```
const gameInfo = {
    gameId: "xxxxx",
    openId: "xxxxxx",
    // 实现签名函数，初始化、掉线重连时会被调用
    createSignature: callback => {
        fetch("https://example.com/sign").then(rsp => rsp.json()).then(json => {
            const sign = json.sign;
            const nonce = json.nonce;
            const timestamp = json.timestamp;

            return callback({ sign, nonce, timestamp });
        });
    },
};

const config = {
    url: "xxxxxxx.com",
};

const room = new MGOBE.Room();

Listener.init(gameInfo, config, event => {
    if (event.code === MGOBE.ErrCode.EC_OK) {
        console.log("初始化成功");
        // 初始化后才能添加监听
        Listener.add(room);
    } else {
        console.log("初始化失败");
    }
});
```


<dx-alert infotype="explain" title="">
示例代码帮助您理解如何使用签名的方式初始化 SDK，具体业务里的服务端部署、请求方式、请求协议格式，由您自行实现。
</dx-alert>

