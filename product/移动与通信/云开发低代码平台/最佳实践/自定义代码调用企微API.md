## 操作步骤
>? 这里以发送应用消息接口为例。

1. 在 APIS 中创建**企业微信**开放服务。
![](https://qcloudimg.tencent-cloud.cn/raw/eaf27e29b54f83daa796bf4abd8ba61d.png)
2. 选中**发送应用消息**接口，复制对应的接口标识。
![](https://qcloudimg.tencent-cloud.cn/raw/43a43977f0b3450cfacaea4c9962917d.png)
3. 再新建一个自定义代码的 APIS。
![](https://qcloudimg.tencent-cloud.cn/raw/1f9c93b5e2b984e02a90ccef250fc8c0.png)
4. 输入以下代码。
>?自定义代码更多操作请参见 [自定义代码-API](https://cloud.tencent.com/document/product/1301/68440#api)。
>
```
/**
* 使用 npm 包 node-fetch 发送http请求, 详细使用文档可以参考
*  https://github.com/node-fetch/node-fetch
*/
const fetch = require('node-fetch');

module.exports = async function (params, context) {

  const result = await context.callConnector({
    name: 'API 标识',
    // 传入 发送应用消息 接口标识
    methodName: 'message_send',
    params: {
        "touser": "接受用户",
        "msgtype": "消息类型",
        "agentid": 应用ID,
        "text": {
            "content": "推送内容"
        }  
    }, // 方法入参
  });

  return {
    result
  };
};
```
![](https://qcloudimg.tencent-cloud.cn/raw/3cd01387df9540e2171f97ad05bb6e10.png)
