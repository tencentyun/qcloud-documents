
## 通过数据模型生成表单
1. 在编辑器的数据源模块中，按需创建好数据模型。
![](https://qcloudimg.tencent-cloud.cn/raw/db65c35369cc67d2fc52c78a6abc3d81.png)
2. 在编辑器的页面设计模块，拖入表单容器组件，数据模型属性选择刚才创建好的模型，即可自动渲染出各类表单组件，并自动绑定到对应的字段。
![](https://qcloudimg.tencent-cloud.cn/raw/6013a6ff3fb1bf7d140ec643d95a27c1.png)
3. 表单容器会同步自动生成提交数据到数据源的多个事件，实现数据提交到数据源的需求，可按需对已有事件进行调整，满足个性化表单需求。
![](https://qcloudimg.tencent-cloud.cn/raw/f51d083f43f69c63555f6899662237cb.png)
事件配置内容如下：
![](https://qcloudimg.tencent-cloud.cn/raw/eb0af7f318062d3f66b5f8a015dd5eb2.png)
4. 在表单容器的字段属性中，可查看到当前表单中的所有字段，可切换组件类型或调整字段顺序。
![](https://qcloudimg.tencent-cloud.cn/raw/a8e165f04ddaf62d32af061cca1f21b3.png)

## 通过 APIs 生成表单
1. 在**编辑器** > **APIs 模块**，创建新的 APIs 方法，配置好表单所需的方法入参与出参。
![](https://qcloudimg.tencent-cloud.cn/raw/8cdf8007127f05ba77f908d9b08c2bdc.png)
2. 在编辑器的页面设计模块，拖入表单容器组件，数据源属性选择 APIs，APIs 属性选择所需 APIs 及方法，即可自动渲染出各类表单组件，并自动绑定到对应的字段。
![](https://qcloudimg.tencent-cloud.cn/raw/a1ab3d3c91d1111c49ce12f835d4602a.png)
3. 表单容器对所绑定 APIs 的参数格式要求。
<dx-tabs>
::: 表单新增场景下
要求新增方法属性绑定的方法中，业务中的表单字段需作为根节点入参，不能放入对象参数中作为子级参数。绑定逻辑如下：
![](https://qcloudimg.tencent-cloud.cn/raw/9428b419472e0a049f6345893e81bcb7.png)
:::
::: 表单查看场景下
![](https://qcloudimg.tencent-cloud.cn/raw/75bc30a4ef1642315a9225f53239b5dc.png )
1. 查询方法属性绑定的方法中，表单字段需作为根节点出参。
![](https://qcloudimg.tencent-cloud.cn/raw/953a3a23658406c5a26f1a0e2979b9dd.png)
2. 查询入参无强制要求，完成方法绑定后，方法中的查询入参会在表单容器属性区中展开，便于进行数据绑定操作。
![](https://qcloudimg.tencent-cloud.cn/raw/3d1b25b22b44db7220a7a77b82f0df1a.png)
:::
::: 表单更新场景下
1. 更新方法属性绑定的方法中，表单字段作为根节点入参。
![](https://qcloudimg.tencent-cloud.cn/raw/eb3857acb0e6021f1b0bd46f602c9c4c.png)
2. 查询方法属性绑定的方法中，表单字段作为根节点出参。
![](https://qcloudimg.tencent-cloud.cn/raw/56dff135263b6ee780d5d011f6ad66c9.png)
3. 查询方法的入参无强制要求，完成方法绑定后，方法中的查询入参会在表单容器属性区中展开，便于进行数据绑定操作。
![](https://qcloudimg.tencent-cloud.cn/raw/34c926eb3634f342ad80dce3b17bc133.png)
:::
</dx-tabs>
4. 表单容器会同步自动生成提交数据到数据源的多个事件，实现数据提交到数据源的需求，可按需对已有事件进行调整，满足个性化表单需求。
![](https://qcloudimg.tencent-cloud.cn/raw/9704a86cdddb2b5650189889421d94fd.png)
事件配置内容如下：
![](https://qcloudimg.tencent-cloud.cn/raw/8298c787021647f3a5619a23eeddaed2.png)
5. 在表单容器的字段属性中，可查看到当前表单中的所有字段，可切换组件类型或调整字段顺序。
![](https://qcloudimg.tencent-cloud.cn/raw/4cdc1e22d36aa993e51df087c068ea5b.png)
