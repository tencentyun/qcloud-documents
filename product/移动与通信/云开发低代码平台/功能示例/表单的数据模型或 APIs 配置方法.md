## 通过数据模型生成表单

1. 在编辑器的数据源模块中，按需创建好数据模型。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/db65c35369cc67d2fc52c78a6abc3d81.png" />
2. 在编辑器的页面设计模块，拖入表单容器组件，数据模型属性选择刚才创建好的模型，即可自动渲染出各类表单组件，并自动绑定到对应的字段。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4c30676305502715e14b4de3f49623e5.png" />
3. 表单容器会同步自动生成提交数据到数据源的多个事件，实现数据提交到数据源的需求，可按需对已有事件进行调整，满足个性化表单需求。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7a5a18dc8a2a67ea49beed4b86aaf5f4.png" />
4. 在表单容器的字段属性中，可查看到当前表单中的所有字段，可切换组件类型或调整字段顺序。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3a6df76839cd7796a9c0115f6b363d67.png" />

## 通过 APIs 生成表单

1. 在**编辑器** > **APIs 模块**，创建新的 APIs 方法，配置好表单所需的方法入参与出参。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/8cdf8007127f05ba77f908d9b08c2bdc.png" />
2. 在编辑器的页面设计模块，拖入表单容器组件，数据源属性选择 APIs，APIs 属性选择所需 APIs 及方法，即可自动渲染出各类表单组件，并自动绑定到对应的字段。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/87416e04e3ebeb879726c89357899955.png" />
3. 表单容器对所绑定 APIs 的参数格式要求：
   1. 表单新增场景。
      1. 要求新增方法属性绑定的方法中，业务中的表单字段需作为根节点入参，不能放入对象参数中作为子级参数。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/9428b419472e0a049f6345893e81bcb7.png" />
      2. 表单容器绑定设置如下。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/75bc30a4ef1642315a9225f53239b5dc.png" />
   2. 表单查看场景。
      1. 查询方法属性绑定的方法中，表单字段需作为根节点出参。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/953a3a23658406c5a26f1a0e2979b9dd.png" />
      2. 查询入参无强制要求，完成方法绑定后，方法中的查询入参会在表单容器属性区中展开，便于进行数据绑定操作。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/6defdf46b87f5d074bae1382e5e11257.png" />
   3. 表单更新场景。
      1. 更新方法属性绑定的方法中，表单字段作为根节点入参。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/eb3857acb0e6021f1b0bd46f602c9c4c.png" />
      2. 查询方法属性绑定的方法中，表单字段作为根节点出参。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/56dff135263b6ee780d5d011f6ad66c9.png" />
      3. 查询方法的入参无强制要求，完成方法绑定后，方法中的查询入参会在表单容器属性区中展开，便于进行数据绑定操作。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/a13940b0918e2e7b43d64d85708fac2a.png" />
4. 表单容器会同步自动生成提交数据到数据源的多个事件，实现数据提交到数据源的需求，可按需对已有事件进行调整，满足个性化表单需求。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4bfc9487050ee24c699966c27fb90a56.png" />
5. 在表单容器的字段属性中，可查看到当前表单中的所有字段，可切换组件类型或调整字段顺序。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/6e3ee60f78b5cd44de2dd49b603d4856.png" />
