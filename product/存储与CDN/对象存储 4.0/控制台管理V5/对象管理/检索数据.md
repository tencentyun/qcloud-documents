## 简介

通过 COS Select 功能，您可以在存储层面筛选出您所需要的数据，这样可以很大程度的降低 COS 传输的数据量以减小您的使用成本，同时提高您的数据获取效率。在 COS 控制台中，您可以使用我们提供的基本的 SQL 模板，或自行输入符合语法规范的语句，来实现检索存储在存储桶中的单个文件的内容。

## 说明

- 请确保进行检索的文件是符合 COS 规范的，如需了解有关 COS Select 的规范信息，请参见 [Select 概述](https://cloud.tencent.com/document/product/436/37635)。
- 控制台中的检索功能最大支持对128MB的文件，进行40M以下的数据提取，如果您需要处理更大的文件或提取更多的数据，请使用 API 或者 SDK。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航栏中，单击【存储桶列表】。
3. 单击存储桶名称，进入对象所在的存储桶。
   ![](https://main.qcloudimg.com/raw/f0868afb4209d10b0c152b6e364fc460.jpg)
4. 在存储桶的“文件列表”模块下，找到需要进行检索的对象，在其右侧操作栏中，单击【检索】。
	 ![](https://main.qcloudimg.com/raw/a3d0cdac8fe8a17f99ba4ef716d5e68d.png)
5. 进入控制台检索功能页面，根据实际情况选择您进行检索的文件类型，标题字段，分隔符以及压缩格式。
	 ![](https://main.qcloudimg.com/raw/8e8834d1215a79993c7c2d2df6cdcaf0.png)
6. 单击【选择 SQL 模板】，可以勾选您所想进行检索的模板句式，然后单击【确定】。
	 ![](https://main.qcloudimg.com/raw/b9041ac54f06a1d5dc25d525eef9fc9f.png)
7. 您可以根据实际文件在文本框中对语句进行编辑，编辑完成后，单击【运行SQL】。
8. 待运行完毕后，可以在最下方的文本框中直接查看前100条结果，如果想获得完整数据，可单击【导出检索结果】。
	 ![](https://main.qcloudimg.com/raw/0d6c2c32d03f43ac97a4719b38a569b1.png)
	 
