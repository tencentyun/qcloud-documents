本文将介绍如何使用和管理自定义 API。

## 使用自定义 API
目前在应用编辑器和自定义代码中，都可以使用自定义 API，支持可视化和自定义代码两种方式。

[](id:components)
### 通过组件行为调用 
进入应用编辑器，在组件行为事件中可以调用 API 方法，详情可参见 [行为事件-执行动作](https://cloud.tencent.com/document/product/1301/61120#.E8.B0.83.E7.94.A8.E6.95.B0.E6.8D.AE.E6.BA.90.E6.96.B9.E6.B3.95-calldatasource)。


[](id:editor)
### 通过低代码编辑器调用 
进入应用编辑器，可以在应用的低代码编辑器及微搭组件的组件代码中使用，详情可参见 [代码编辑器](https://cloud.tencent.com/document/product/1301/57912)。
示例代码：
<dx-codeblock>
:::  js
export default async function({event, data}) {
    const result = await app.cloud.callDataSource({
        name: '自定义 API 标识',
        methodName: '方法标识',
        params: {}, // 方法入参
    });
}
:::
</dx-codeblock>


[](id:custom)
### 在自定义代码中调用 
在自定义 APIs 中通过**自定义代码**方式，可以调用其他自定义 API。详情请参见 [自定义代码](https://cloud.tencent.com/document/product/1301/68440)。
示例代码：
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

[](id:edit)
## 编辑 API 
有两种方式可以对 API 进行编辑：
- 在 **控制台 APIs 列表** 页面，找到编辑的 API，在**操作**列单击**编辑**。
- 在 **控制台 APIs 详情**页面，单击右上角**编辑**。 

[](id:publish)
## 发布数据模型 
数据模型需要发布才会在正式环境生效，有两种方式可以发布数据模型：
- 在**数据模型列表**页面，找到编辑的数据模型，在**操作**列单击**更多 > 发布**。
- 在**自定义 API 详情**页面，在**基础信息**卡片中**状态 > 立即发布**。 

[](id:delete)
## 删除 API 
在**自定义 API** 列表页面，找到编辑的自定义 API，在**操作**列单击**更多 > 删除**。
>! 自定义 API 删除前，必须解绑在所有应用的关联使用。
