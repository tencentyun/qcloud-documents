
本文主要讲解如何使用 Excel 文件来实现应用的快速创建。

## 步骤1：使用 Excel 文件创建应用
在新建表单应用或数据管理应用时，都可以选择从 Excel 新建。
![](https://qcloudimg.tencent-cloud.cn/raw/5db210989ed33b285ff7aebe3695f68f.png)

## 步骤2：选择应用创建方式
目前微搭已提供三种 Excel 应用的创建方式，分别为微搭内置的 Excel 模板、本地 Excel 上传和个人腾讯文档的 Excel 文件，下文会分别讲解如何使用这三种方式进行 Excel 应用的创建。



### 使用模板创建
1. 选择模板类型(以学生信息登记表模板为例)，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/d5691c264d0b72af8310581efb5c8f84.png)
2. 设置模板中表头的字段名称、字段类型等参数，确认无误后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/8d1d783d2f6ef91039c97948bb7a6b26.png)


### 上传本地 Excel 文件创建
支持上传本地符合格式规范的 Excel 文件，也可以通过下载示例 Excel 模板，在示例模板基础上进行数据修改后上传：
![](https://qcloudimg.tencent-cloud.cn/raw/06c9e9ff814625b80de6637936a83aa5.png)
>? **Excel 文件格式要求：**
- 表头字段名支持中文和英文，英文以字母开头，避免使用特殊字符。
>2. 文件格式仅支持 csv/xls/xlsx 格式，大小不超过 2MB。
>3. 需要确保 Excel 表单中不存在合并的单元格，详情可单击上图的**示例模板**下载参考。

### 使用腾讯文档创建
1. 通过将腾讯文档账号授权给微搭，读取并解析腾讯文档下的 Excel 文件来进行应用的创建。
![](https://qcloudimg.tencent-cloud.cn/raw/27b308ed277fe925abefd3ff6a9b46d1.png)
2. 完成腾讯文档授权后，选择对应的 Excel 文件，如下图所示:
![](https://qcloudimg.tencent-cloud.cn/raw/ad02126574e01eb5347320e2e2dc26d4.png)
3. 对 Excel 文件的解析结果进行确认和字段编辑。

>!由于目前**腾讯文档**双向同步机制正在支持中，故应用发布运行后的数据修改，仅存在微搭数据源中，不会同步到腾讯文档。


## 步骤3：生成数据模型应用
使用上文的方式创建完成后，即可在微搭中生成对应的数据模型应用。
![](https://qcloudimg.tencent-cloud.cn/raw/2f769ac5bf281c5517979764ea4f7fff.png)

