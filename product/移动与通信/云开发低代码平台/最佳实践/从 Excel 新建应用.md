
本文主要讲解如何使用 Excel 文件来实现应用的快速创建。

## 步骤1：使用Excel文件创建应用
在 [创建应用入口](https://console.cloud.tencent.com/lowcode/create) 中单击**从 Excel 创建**的应用创建卡片，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bf78aa097d41ffa219a392e1141a3a4b.png)

## 步骤2：选择应用创建方式
目前微搭已提供三种 Excel 应用的创建方式，分别为微搭内置的 Excel 模板、本地 Excel 上传和个人腾讯文档的 Excel 文件，下文会分别讲解如何使用这三种方式进行 Excel 应用的创建。



### 使用模板创建

1. 选择模板类型(以学生信息登记表模板为例)，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/f8198d83d874b91be3f9f6ab3613d65b.png)
2. 设置模板中表头的字段名称、字段类型等参数，确认无误后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/de406194d59e5e856a3869d5ba27d4e6.png)
3. 填写**应用名称**后单击**创建应用**完成应用的创建，之后页面会跳转到编辑器页面。
![](https://qcloudimg.tencent-cloud.cn/raw/37fbc79bfa0ad798fc6292c857364fe5.png)


### 上传本地Excel文件创建
支持上传本地符合格式规范的 Excel 文件，也可以通过下载示例 Excel 模板，在示例模板基础上进行数据修改后上传：
![](https://qcloudimg.tencent-cloud.cn/raw/2e4cd9eee5a1e3bb77d438c41a3f2d00.png)
>? **Excel 文件格式要求：**
- 表头字段名支持中文和英文，英文以字母开头，避免使用特殊字符。
>2. 文件格式仅支持 csv/xls/xlsx 格式，大小不超过 2MB。
>3. 需要确保 Excel 表单中不存在合并的单元格，可参考示例模板。

### 使用腾讯文档创建
1. 通过将腾讯文档账号授权给微搭，读取并解析腾讯文档下的 Excel 文件来进行应用的创建。
![](https://qcloudimg.tencent-cloud.cn/raw/d4850d02035cfd66752ad962130a7b20.png)
2. 完成腾讯文档授权后，选择对应的 Excel 文件，如下图所示:
![](https://qcloudimg.tencent-cloud.cn/raw/cea20339e05552b9fe01aa1299c02a7b.png)
3. 对 Excel 文件的解析结果进行确认和字段编辑。
![](https://qcloudimg.tencent-cloud.cn/raw/63be132a28a3307871cdf4c5fb42a585.png)
>!由于目前 腾讯文档 双向同步机制正在支持中，故应用发布运行后的数据修改，仅存在微搭数据源中，不会同步到腾讯文档。


## 步骤3：生成数据模型应用
使用上文的方式创建完成后，即可在微搭中生成对应的数据模型应用。
![](https://qcloudimg.tencent-cloud.cn/raw/a9a0427d6331cf74c710c0656d90b79d.png)

