
## 功能简介
自定义 API 的自定义代码可以触发流程实例。


## 场景示例
1. 配置流程：流程开始节点支持配置变量：
>!如果仅在“方法测试”、应用编辑器的实时预览或者应用的预览环境触发流程，保存流程即可，不需要发布；如果要在应用的正式环境触发流程，需要发布流程。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/75ed865affaac3853107b400495b5d03.png" style = "width:80%"> 
 >
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/75c3e4a1967101fe208f29d5eff6380a.png" style = "width:80%"> 
2. **配置自定义 API **。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/d1a2b839c2fd084f70c1685d18f46c00.png" style = "width:80%"> 
**按照下面的代码即可触发流程，可以通过方法测试验证，验证后通过“出参映射”可以快速配置 API 的出参。**
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
      ConnectorName: "startflow_0iivqwe",
      FunctionName: "method_5b12595a75119"
    },
    ProcessKey: "flow_012",
    StartParams: [
      {
        "paramCode": "165708798187xxxxxx",
        "fieldType": "string",
        "entityCode": "",
        "value": "test data"
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
3. **应用中使用自定义 API **
自定义 API 发布后，在应用编辑器中可以配置表单容器。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/d9743711ae8f33dc67a037413af68b21.png" style = "width:80%"> 
 选择配置好的 API 方法，单击**提交**即可触发流程。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/4c27249e99d480f4e4a69e2f90ac8f2e.png" style = "width:80%">  
如果需要在自定义应用中使用，需要先配置登录组件：单击**提交**即可触发流程。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/20170ab808bcbedaefe176c7ee5c441f.png" style = "width:80%"> 
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/7ebc730acb65e9c9267b9d10e0cde664.png" style = "width:80%"> 
 登录界面可通过单击右上角**发布成功** > **访问连接**进行访问。
 <img src = "https://qcloudimg.tencent-cloud.cn/raw/d0e613830d0dfc07d46119dd0b037092.png" style = "width:80%"> 


> !如果不配登录组件，只能在自定义代码中指定用户触发，即传入 ExtraUserInfo 参数的 UserId 和 Source（如上文示例所示）。如果已经配置了登录组件则不需要配置该入参。


