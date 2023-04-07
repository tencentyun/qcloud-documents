本文将介绍如何管理和使用 API（开放服务）。
[](id:edit)
## 编辑 API 
有两种方式可以对 API 进行编辑：
- 在 [API](https://console.cloud.tencent.com/lowcode/datasource/connector) 页面，找到编辑的 API，在**操作**列单击**编辑**。
- 在 **API 详情**页面，单击右上角**编辑**。 

[](id:refresh)
## 重新授权 API 
在 [API](https://console.cloud.tencent.com/lowcode/datasource/connector) 页面，若在**状态**列出现**鉴权失败**，则可以单击**重新授权**重新发起授权。

[](id:delete)
## 删除 API 
在 **API** 列表页面，找到编辑的 API，在**操作**列单击**更多 > 删除**。
>! API 删除前，必须解绑在所有应用的关联使用。


## 使用 API
目前在应用编辑器、自定义数据模型和自定义 API 中，都可以使用 API，支持可视化和自定义代码两种方式。

[](id:components)
### 通过组件行为调用 
进入应用编辑器，在组件行为可以调用 API 方法，具体可参见 [添加行为事件](https://cloud.tencent.com/document/product/1301/68456#components)。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5b7f24c8675b619f097424eed02609c4.png" width="800px">

[](id:editor)
### 通过低代码编辑器调用 
进入应用编辑器，可以在应用的低代码编辑器及微搭组件的组件代码中使用。具体可参见 [自定义方法](https://cloud.tencent.com/document/product/1301/68456#editor)。
<img src="https://qcloudimg.tencent-cloud.cn/raw/663007350ea32951eb99769ef109a28d.png" width="800px"> 
<dx-codeblock>
:::  js
export default async function({event, data}) {
    const result = await app.cloud.callConnector({
        name: 'API 标识',
        methodName: '方法标识',
        params: {}, // 方法入参
    });
}
:::
</dx-codeblock>

[](id:custom)
### 在自定义数据模型或自定义 API 中调用 
在自定义数据模型和自定义 API 中通过**自定义代码**方式，可以调用其他 API，具体可参见 [自定义代码](https://cloud.tencent.com/document/product/1301/68440#api)。
<img src="https://qcloudimg.tencent-cloud.cn/raw/59e671f13ed079bd7d0a686331f614da.png" width="800px"> 
<dx-codeblock>
:::  js
module.exports = async function (params, context) {
  const result = await context.callConnector({
    name: 'API 标识',
    methodName: '方法标识',
    params: {}, // 方法入参
  });

  return {
    _id: '123456',
  };
};
:::
</dx-codeblock>


