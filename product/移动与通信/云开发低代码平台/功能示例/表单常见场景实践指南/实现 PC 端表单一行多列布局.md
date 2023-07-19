## 需求说明
实现表单在 PC 端一行多列，移动端保持一行一列的布局效果。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/62edc069cc828337aef32b88a5912447.png" />

## 实践方案

1. 在页面编辑器中拖入表单容器组件，绑定所需模型生成表单。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7fe72b22a6b5e4514edb1503a62bcf86.png" />
2. 在表单容器中拖入网格布局组件。
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/de8ea6a861d31956609f499e53da39a5.png" />
3. 将网格布局中所有的列组件的**列宽度·桌面端**属性调整为手动调节 3/12。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/37ba1aba1e1560b529990047e410c12e.png" />
4. 切换到移动端编辑器，将网格布局中所有的列组件的**列宽度·移动端**属性调整为手动调节 12/12。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c4b3c689e4d15312d1525232bc0e3835.png" />
5. 单击列组件的**向右添加列**，实现一共5个列组件，对应5个表单组件。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/6a64e73d5946bff31e77ce50dee75742.png" />
6. 网格布局组件的列间距属性调整为16px。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/5677e67ff3fe8b86a43588b57984134b.png" />
7. 将各个表单组件分别放入各个列组件中，即可实现 PC 端一行多列布局，移动端保持一行一列。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/6937b4224b5e533df546da9ee9276cf6.png" />
8. 预览区或运行态效果。
 - PC 端
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/8539f05c417b9c3ae0b573751a7f6c91.png" />
 - 移动端<br>
<img style="width:300px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c90b4da16909e45bfeb46b4d157f0b4a.png" />
