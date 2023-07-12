## 功能简介
自定义 API 的自定义代码可以触发流程实例。


## 场景示例
1. 配置流程：流程开始节点支持配置变量：
>!如果仅在**方法测试**、应用编辑器的实时预览或者应用的预览环境触发流程，保存流程即可，不需要发布；如果要在应用的正式环境触发流程，需要发布流程。
![](https://qcloudimg.tencent-cloud.cn/raw/75ed865affaac3853107b400495b5d03.png)
>
![](https://qcloudimg.tencent-cloud.cn/raw/8f8812446d5af32ef4982ab390835004.png)
2. **配置自定义 API**。
![](https://qcloudimg.tencent-cloud.cn/raw/6b7f88cce08d7895dce76d3e7b592993.png)
**参考下面的代码配置 APIs 和工作流相关信息即可触发流程，可以通过方法测试验证，验证后通过“出参映射”可以快速配置 API 的出参。**
<dx-codeblock>
:::  js
/**
* 使用 npm 包 node-fetch 发送http请求, 详细使用文档可以参考
*  https://github.com/node-fetch/node-fetch
*/
const fetch = require('node-fetch');
 
module.exports = async function (params, context) {
  // 这里是方法入参
  console.log(params);
 
/**
 * 可以在这里编写业务逻辑，例如：
 * 1. 使用 node-fetch 通过 HTTP 方式请求外部数据，并对获取的数据进行加工；
 * 2. 使用 context.database API 来直接操作云开发云数据库；
 * 3. 使用 context.callModel 来操作其他数据模型数据；
 * 4. 使用 context.callConnector 来使用 API ；
 * 5. 使用 context.app.callFunction 来调用同环境的云开发云函数；
 */
  const response = await context.callWorkflow({action: 'StartProcessWithParams', data: {
    TriggerType: 6,
    ConnectorParam: {
      ConnectorName: "startflow_n17f6cw",
      FunctionName: "method_65d91583fc619"
    },
    ProcessKey: "flow_ttmzhe5",
    StartParams: [
      {
        "name":"form_test3",
        "paramCode": "168049347798818754",
        "fieldType": "object",
        "fieldValueMap":{
          "_id":'50b8a5676425824e001b06661838b821',
          "xh":'1311311236743'
      }
    ],
    ExtraUserInfo: {
      UserId: 1000000000000000000,
      Source: 4
    }
  }});
  return response;
};
:::
</dx-codeblock>

 其中：
 - ConnectorName：触发的 APIs 标识。
![](https://qcloudimg.tencent-cloud.cn/raw/835f9ab332eddae6d7febfdf96ca8773.png)
 - FunctionName：触发的方法标识。
![](https://qcloudimg.tencent-cloud.cn/raw/aaa49c25f8ac248657ded743313627c5.png)
 - ProcessKey：流程的唯一标识。
![](https://qcloudimg.tencent-cloud.cn/raw/54af169e7545f12b9a4ca11df5f9bda0.png)
 - StartParams中：
   - name：开始节点变量名称。
   - paramCode：开始节点变量标识（获取方式参考以下截图示例，对照接口出参中 rightId 字段内容）。
   - fieldType：开始节点变量类型。
   - fieldValueMap：{\_id：数据模型记录 ID，数据模型字段 key-value}。
![](https://qcloudimg.tencent-cloud.cn/raw/c5cbf2859477601485fa98cba3fbb140.png)
![](https://qcloudimg.tencent-cloud.cn/raw/d61e6c3dab9081a456eb0dee54dd6e6a.png)
3. **应用中使用自定义 API**。
自定义 API 发布后，在应用编辑器中可以配置表单容器。
![](https://qcloudimg.tencent-cloud.cn/raw/55af31467226022722524cf1d6d20ec9.png)
 选择配置好的 API 方法，单击**提交**即可触发流程。
![](https://qcloudimg.tencent-cloud.cn/raw/40a0318866c4db98b2ed7fc157313235.png)
如果需要在自定义应用中使用，需要先配置登录组件，确认应用登录授权信息。
![](https://qcloudimg.tencent-cloud.cn/raw/20170ab808bcbedaefe176c7ee5c441f.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ad804ed3c0e9715903ce1dc1b0d0845d.png)
可通过单击应用编辑器右上角**发布成功** > **访问链接**进行访问。
> !如果不配登录组件，只能在自定义代码中指定用户触发，即传入 ExtraUserInfo 参数的 UserId 和 Source（如上文示例所示）。如果已经配置了登录组件则不需要配置该入参。


