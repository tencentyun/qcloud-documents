## 操作场景
该文档指导您通过实时服务器直接调用云 API。[下载示例代码 >>](https://mgobe-1258556906.cos.ap-shanghai.myqcloud.com/demo/mgobexs_capi_demo.zip) 

## 操作步骤
### 步骤1：安装云 API Node.js SDK

1. 在实时服务器上使用云 API，您可以直接使用 [云 API Node.js SDK](https://cloud.tencent.com/document/sdk/Node.js)。安装命令如下：
```
npm install tencentcloud-sdk-nodejs --save
```

2. 安装成功后，导入指定版本产品的 Client 对象（代码示例为 MgobeClient 对象）：
```
import * as tencentcloud from "tencentcloud-sdk-nodejs";

// 导入 client
// v20201014 为 api 版本号，可以从具体 api 文档上获得该参数信息
const MgobeClient = tencentcloud.mgobe.v20201014.Client;
```

### 步骤2：使用云 API

1. 登录访问管理控制台，在**[API密钥管理](https://console.cloud.tencent.com/cam/capi)**中，获取腾讯云 API 密钥。


<dx-alert infotype="explain" title="">
关于腾讯云 API 密钥的创建和管理请参考 [访问密钥](https://cloud.tencent.com/document/product/598/40488) 文档。
</dx-alert>



2. 实例化 Client 对象。
<dx-codeblock>
:::  Node.js
const MgobeClient = tencentcloud.mgobe.v20201014.Client;

const clientConfig = {
    credential: {
		secretId: "请填写腾讯云API密钥ID",
		secretKey: "请填写腾讯云API密钥KEY",
    },
    region: "ap-shanghai", // 默认为上海地域
    profile: {
        httpProfile: {
            endpoint: "mgobe.internal.tencentcloudapi.com", // 设置内部接入域名
        }
    }
};

// 实例化 client 对象
const client = new MgobeClient(clientConfig)
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
本地调式时无需实例化 Client 对象，否则会出现超时异常。建议与本地调式分开使用。
</dx-alert>
3. 调用云 API。以 [查询房间信息](https://cloud.tencent.com/document/product/1038/52497) 为例：
<dx-codeblock>
:::  Node.js
const describeRoom = (para: { GameId: string, RoomId: string }, callback: (err: any, res: any) => any) => {
    client.DescribeRoom(para)
        .then(res => callback(null, res))
        .catch(err => callback(err, null));
};
:::
</dx-codeblock>

 在 [onRecvFromClient 广播](https://cloud.tencent.com/document/product/1038/34991#onrecvfromclient-.E6.8E.A5.E5.8F.A3) 中可以直接调用并返回结果到客户端：    
<dx-codeblock>
:::  Node.js
	onRecvFromClient: function onRecvFromClient({ actionData, gameData, SDK, room, exports }) {
		// 查询房间
		describeRoom({ GameId: "填写游戏ID", RoomId: "填写房间ID" }, (err, res) => {
			if (err) {
				try {
					err = JSON.stringify(err);
				} catch(e) {}

				SDK.sendData({ playerIdList: [], data: { res, err: err + "", msg: "fail" } });
				return;
			}

			// 查询成功
			SDK.sendData({ playerIdList: [], data: { res, msg: "success" } });
			return;
		});
	},
:::
</dx-codeblock>


### 步骤3：打包发布代码

由于 tencentcloud-sdk-nodejs 安装在 node_modules 目录中，打包项目时需要注意将 node_modules 也上传到实时服务器。

