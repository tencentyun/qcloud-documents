本文将介绍如何使用和管理 API。

## 使用 API

目前在应用编辑器、自定义数据模型和自定义 API 中，都可以使用 API，支持可视化和自定义代码两种方式。


### 通过组件行为调用 [](id:components)

进入应用编辑器，在组件行为可以调用 API 方法：

<img src="https://qcloudimg.tencent-cloud.cn/raw/5b7f24c8675b619f097424eed02609c4.png" width="600px">

### 通过低代码编辑器调用 [](id:editor)

进入应用编辑器，可以在应用的低代码编辑器及微搭组件的组件代码中使用。
<img src="https://qcloudimg.tencent-cloud.cn/raw/663007350ea32951eb99769ef109a28d.png" width="600px"> 
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



### 在自定义数据模型或自定义 API 中调用 [](id:custom)
在自定义数据模型和自定义 API 中通过 **自定义代码** 方式，可以调用其他 API：
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


## 编辑 API [](id:edit)

有两种方式可以对 API 进行编辑：
- 在 [API](https://console.cloud.tencent.com/lowcode/datasource/connector) 页面，找到编辑的 API，在 **操作** 列点击 **编辑**。
- 在 **API 详情** 页面，单击右上角 **编辑**。 

## 重新授权 API [](id:refresh)
在 [API](https://console.cloud.tencent.com/lowcode/datasource/connector) 页面，若在 **状态** 列出现 **鉴权失败** ，则可以单击 **重新授权** 按钮重新发起授权。
	
## 删除 API [](id:delete)

在 **API** 列表页面，找到编辑的 API，在 **操作** 列单击 **更多 > 删除** 。

>! API 删除前，必须解绑在所有应用的关联使用。
