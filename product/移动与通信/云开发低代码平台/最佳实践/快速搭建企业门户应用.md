本文以下图展示的企业门户应用为例，我们来学习如何使用微搭进行企业门户应用的快速搭建。
![](https://qcloudimg.tencent-cloud.cn/raw/ee55ffb3742d56c9ac3660fdde99454d.png)



## 使用腾讯文档快速创建数据模型与数据管理后台

我们可以通过导入腾讯文档的 Excel 文件进行数据模型与数据管理后台的快速创建

1. 在控制台的 [创建应用](https://console.cloud.tencent.com/lowcode/create/index?envId=lowcode-2gadiaws6be78eca) 页面，选择新建数据管理应用。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4c96a49dff5e17038e216d7fdd81d588.png)
2. 选择新建方式为**从 Excel 新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/65b08a7396069a5e26cd925db0b40b4e.png)
3. 选择**导入外部文档**，并对腾讯文档进行授权操作。
![](https://qcloudimg.tencent-cloud.cn/raw/8b94ee4873ca1fe7b2c570a1fb0cdd25.png)
4. 授权完成后可以选择对应的 Excel 文件进行导入，可单击下方的**示例模板**进行示例文件的下载。
![](https://qcloudimg.tencent-cloud.cn/raw/9dbd28c58a415bf2e44eead000e00f3c.png)
5. 导入完成后，会自动根据  Excel 文件识别出数据模型字段以及数据模型中存储的数据，如下图所示，确认无误后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/1d3ba72d12c7d208479b90522b537518.png)
6. 输入名称后，即可自动完成数据模型的生成与数据管理后台的创建。
![](https://qcloudimg.tencent-cloud.cn/raw/bec99f057a5b4ab7cdd3cc9bf327cde2.png)

   

## 从空白开始创建门户应用

### 创建空白应用

1. 在控制台的 [创建应用](https://console.cloud.tencent.com/lowcode/create/index?envId=lowcode-2gadiaws6be78eca) 页面，选择新建门户应用。
![](https://qcloudimg.tencent-cloud.cn/raw/fc5b21f0a8e572f474e4205d06e1332f.png)
2. 选择从空白新建。
![](https://qcloudimg.tencent-cloud.cn/raw/0002babdef4ab0c90a823eb99ce61e4f.png)
3. 输入应用名称后即可完成空白应用的创建，创建完成后页面会自动跳转到应用编辑器。
![](https://qcloudimg.tencent-cloud.cn/raw/def191078f117205435285ff7a04c40d.png)

### 创建企业门户主页

1. 在指引中选择空白页进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/622b1f3b8ce5aebbfb98715ff3b9b065.png)
2. 在页面中添加**轮播图**组件。
![](https://qcloudimg.tencent-cloud.cn/raw/f7e9ba055eaf320bcc097213ea1f7b7e.png)
3. 在右侧轮播图的右侧配置区中添加轮播图需要展示的图片。
![](https://qcloudimg.tencent-cloud.cn/raw/c41e575a26e73e2754c6609c60d252d2.png)
4. 随后选择**标题**组件，并修改标题组件的相关配置。
![](https://qcloudimg.tencent-cloud.cn/raw/6cc7ecf2c93e758312d3c2a08c4ee034.png)
5. 随后在标题组件样式配置区中，将标题组件的上下边距调整为20，便于页面展示更加清晰。
![](https://qcloudimg.tencent-cloud.cn/raw/246bdaf6764f99dfc7f792ea8fcdeb89.png)
6. 随后添加**宫格导航**组件，用于场景能力的相关展示。
![](https://qcloudimg.tencent-cloud.cn/raw/9a51d57cf6c86e55d4d983de3ad83824.png)
7. 在右侧的组件配置区中为宫格导航进行图片与标题配置。
![](https://qcloudimg.tencent-cloud.cn/raw/4f6f13c8c2abe8ae03c7fe8d5f465625.png)
8. 宫格导航配置完成后，我们右键选中刚刚创建的**标题组件**，选择克隆，将克隆后的标题组件拖拉至宫格导航组件的下方并修改标题组件文本内容。
![](https://qcloudimg.tencent-cloud.cn/raw/4d4640868a5012d9cb4f15ff973cbf39.png)
9. 添加一个**列表视图**组件，选择模板为**卡片列表**。
![](https://qcloudimg.tencent-cloud.cn/raw/4d4a4639199fe2287c9fe80294a85b63.png)
10. 在右侧对列表视图组件进行数据绑定配置，在右侧数据模型配置中选择通过 Excel 生成的数据模型。
![](https://qcloudimg.tencent-cloud.cn/raw/bea928f40375634513f2085780ededbf.png)
11. 数据配置完成后，我们需要对列表视图的样式进行调整。 在大纲书中选中列表视图下方的**普通容器**，在组件的样式配置区将边框调整为**无**。
![](https://qcloudimg.tencent-cloud.cn/raw/8189fc42bbde27c6506a68085e2ebedd.png)
12. 随后我们对列表视图中的图片进行数据绑定，选中列表视图下的图片组件，随后在右侧配置区中单击**数据绑定按钮**，绑定对应的数据字段。
![](https://qcloudimg.tencent-cloud.cn/raw/f4e92d84d14db4adbfbaa009105e71b2.png)
13. 重复上述方法，为文本组件进行数据绑定，绑定完成后效果如下：
![](https://qcloudimg.tencent-cloud.cn/raw/c1beea7f0961f54c2c55fbd5c5c2118a.png)
14. 之后我们修改列表视图的配置，使此处仅展示4条数据，并且分页模式修改为不分页。
![](https://qcloudimg.tencent-cloud.cn/raw/3bc708bdaf05e2f5a3af217f25f01001.png)
15. 之后我们可以使用相同的方式进行"合作伙伴"模块的构建，合作伙伴的相关数据需要我们通过字段进行查找，我们可以通过列表视图的配置区进行数据筛选。
![](https://qcloudimg.tencent-cloud.cn/raw/2c99ae0efabb820493eaaef2733a7ae5.png)
16. 为列表视图视图配置完成数据模型后，单击下方的数据筛选弹窗，配置筛选条件为 category 等于"合作"，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0b3fc437e1112c960b06a73ca731a236.png)
17. 配置完成后将组件与数据进行绑定，可以看到列表视图仅会展示合作伙伴的相关数据， 至此我们的企业门户主页创建完成。
![](https://qcloudimg.tencent-cloud.cn/raw/9a35ca9d6d94ad08306533f2bc8fc28e.png)

            

    
### 创建企业动态列表页

1. 创建一个新页面，并命名为"企业动态列表"。
![](https://qcloudimg.tencent-cloud.cn/raw/9c6fff10f505d9a71497635936d788ae.png)
2. 拖入列表视图组件，选择模板为**图文列表**。
![](https://qcloudimg.tencent-cloud.cn/raw/f5b8343ebd1e0480feb0df7d206c98dd.png)
3. 为列表视图绑定数据模型后，将列表中的图片、文本依次与数据进行绑定即可完成图文列表页的构建。
![](https://qcloudimg.tencent-cloud.cn/raw/b973aa66bcbef6f1c809c64b58aad15a.png)



### 创建关于我们页面

1. 之后再次新增一个页面，并命名为""关于我们"。
2. 新建一个**普通容器**，在普通容器下添加一个**图片组件**并绑定需要展示的图片素材,并将图片组件的宽度调整为100%。
![](https://qcloudimg.tencent-cloud.cn/raw/a1e8c2a60d19ac61cedd36c0ebacf272.png)
3. 之后再次新建一个普通容器，并在普通容器下添加一个**标题组件**，并按需求进行文案的调整。 标题组件的大小设置为"3",对齐方式设置为"左"。
![](https://qcloudimg.tencent-cloud.cn/raw/a1e8c2a60d19ac61cedd36c0ebacf272.png)
4. 再次新建普通容器，并在普通容器下添加一个**富文本组件**，并在富文本组件的配置区中进行展示内容的输入。
![](https://qcloudimg.tencent-cloud.cn/raw/05654dd118a268807f6da4c199a83d99.png)
5. 之后我们对页面的布局样式进行细微调整，将标题组件的全部内间距调整为20，富文本组件的左右内间距调整为20，至此我们便完成了"关于我们"页面的创建。
![](https://qcloudimg.tencent-cloud.cn/raw/c271f0a39e86e107db0b9b94161cfcbe.png)



### 创建内容详情页面

1. "内容详情""页面与"关于我们"页面布局基本类似，我们可以克隆功能进行页面的复制，并单击**页面设置**按钮修改页面名称为"内容详情"。
![](https://qcloudimg.tencent-cloud.cn/raw/0fd200f2f72bb573c630798ea22acee8.png)
2. 在复制后的页面中添加一个文本组件，并将文本组件的左右间距调整为20，用于详情页子标题的展示。
![](https://qcloudimg.tencent-cloud.cn/raw/621094027bd4be28e66089a2f6db1d88.png)
3. 随后我们在组件区中选择**数据视图组件**，将数据视图组件自带的普通容器删除，并将大纲树的全部组件拖入数据视图组件下。
![](https://qcloudimg.tencent-cloud.cn/raw/be86e1460d39970573029d5105521393.png)
4. 为数据视图组件绑定数据模型，随后依次为内容详情页面的图片、文本、富文本组件进行数据字段绑定，绑定完成后我们便完成了内容详情页的搭建。
![](https://qcloudimg.tencent-cloud.cn/raw/4eb3f6b4a132474c3a11be91f1b3efe9.png)



### 实现内容列表到内容详情页的页面跳转逻辑

1. 选中企业门户主页列表视图下的普通容器组件，并在右侧组件配置区单击行为配置按钮。
![](https://qcloudimg.tencent-cloud.cn/raw/7bc07b4a00cfde27f46941b0bd178cf8.png)
2. 为普通容器配置单击后跳转至内容详情页的事件，单击下方的**新建页面参数**，创建一个名为\_id 的页面参数。
![](https://qcloudimg.tencent-cloud.cn/raw/1c09e8d59e01681c988dcbbbeb1ca895.png)
3. 页面参数创建完成后，单击页面参数右侧的**数据绑定按钮**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/7b07d8354a70350f098a2cff47fb64b9.png)
4. 在数据绑定弹窗中，选择**数据标识**字段，绑定完成后保存即可。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d48ae569cd742cf23826449dd8761acb.png)
5. 之后在**内容详情页**选中数据视图组件，并单击右侧配置区的**数据筛选**，调起数据筛选弹窗。
![](https://qcloudimg.tencent-cloud.cn/raw/e93cca24a8bccbb16852bae97f1e57a5.png)
6. 在弹窗中设置筛选条件为数据标识 等于 \_id 后保存。
![](https://qcloudimg.tencent-cloud.cn/raw/aebc304fc390ac732d4253752a483595.png)
7. 至此我们便完成了内容列表跳转内容详情页面的跳转逻辑，同理我们也同样可以按照上述方式实现动态列表页跳转内容详情页的相关逻辑。



### 配置应用的底部导航

为每一个页面底部添加一个 **Tab 栏**组件来实现应用的底部导航，Tab 栏配置如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/e9467c927b4d3b5f18efaac9967450cb.png)



### 为内容详情页添加顶部导航

进入内容详情页面，添加一个顶部导航组件，并将顶部导航组件移动至大纲树的最上级。

![](https://qcloudimg.tencent-cloud.cn/raw/9a0daafc6d09c6d67472894b15f982c4.png)



### 发布应用

至此我们便已完成了企业门户应用的搭建，单击右上角**发布**，选择对应的发布平台即可完成应用的发布。

![](https://qcloudimg.tencent-cloud.cn/raw/0e54eb34980c38cfe1d72bfd96890725.png)







