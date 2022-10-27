本文将介绍如何使用和管理自定义 API。

## 使用自定义 API

目前在应用编辑器和自定义代码中，都可以使用自定义 API，支持可视化和自定义代码两种方式。


### 通过组件行为调用 [](id:components)

进入应用编辑器，在组件行为可以调用 API 方法：
<img src="https://qcloudimg.tencent-cloud.cn/raw/ba57655c3db7d1b8f67e37a850cb939b.png" width="600px">

### 通过低代码编辑器调用 [](id:editor)

进入应用编辑器，可以在应用的低代码编辑器及微搭组件的组件代码中使用。
<img src="https://qcloudimg.tencent-cloud.cn/raw/663007350ea32951eb99769ef109a28d.png" width="600px">
<dx-codeblock>
:::  js
export default async function({event, data}) {
    const result = await app.cloud.callConnector({
        name: '自定义 API 标识',
        methodName: '方法标识',
        params: {}, // 方法入参
    });
}
:::
</dx-codeblock>



### 在自定义代码中调用 [](id:custom)
在自定义代码中通过 **自定义代码** 方式，都可以调用其他自定义 API。
<img src="https://qcloudimg.tencent-cloud.cn/raw/59e671f13ed079bd7d0a686331f614da.png" width="800px">
<dx-codeblock>
:::  js
module.exports = async function (params, context) {
  const result = await context.callConnector({
    name: '自定义 API 标识',
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
- 在 [](https://console.cloud.tencent.com/lowcode/datasource/custom-connector) 页面，找到编辑的 API，在 **操作** 列单击 **编辑**。
- 在 [](https://console.cloud.tencent.com/lowcode/datasource/custom-connector) 页面，点击右上角 **编辑**。 

## 发布数据模型 [](id:publish)

数据模型需要发布才会在正式环境生效，有两种方式可以发布数据模型：
- 在  [](https://console.cloud.tencent.com/lowcode/datasource/custom-connector) 页面，找到编辑的数据模型，在 **操作** 列单击 **更多 > 发布**。
- 在 **自定义 API 详情** 页面，在 **基础信息** 卡片中 **状态 > 立即发布**。 
![](https://qcloudimg.tencent-cloud.cn/raw/87df0723ef1c41d965ea5ac41a84e553.png)

	
## 删除 API [](id:delete)

在 **自定义 API** 列表页面，找到编辑的自定义 API，在 **操作** 列单击 **更多 > 删除**。

>! 自定义 API 删除前，必须解绑在所有应用的关联使用。