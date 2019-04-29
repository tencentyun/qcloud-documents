## 上传步骤

1. 登录[对象存储控制台](https://console.cloud.tencent.com/cos4)，单击【Bucket 列表】，进入存储桶列表。单击想存储对象的存储桶，进入存储桶的文件列表页面。
   ![bucket列表1](//mc.qcloudimg.com/static/img/b04362203a69327f80733d8e7f935108/image.png)
2. 在文件列表中，单击【上传文件】，出现上传文件对话框。
   ![文件列表](//mc.qcloudimg.com/static/img/f8b8db803a7fbcb0b052358698a247c9/image.png)
3. 单击【上传文件】或【上传文件夹】 ，可上传单个或多个本地文件/文件夹，选择本地待上传对象后，单击【确定上传】，弹出创建上传任务成功提示框。
   ![上传文件](//mc.qcloudimg.com/static/img/17e71c6b076742f2b437ee68f8c37c87/image.png)
4. 单击【知道了】完成上传对象操作。
   ![创建上传任务成功](//mc.qcloudimg.com/static/img/cec0b4e40b9d4aa44cc12311fb2bc97f/image.png)

> <font color="#0000cc">**注意：** </font>
> 部分浏览器不支持多文件上传，建议使用 IE10 以上、Firefox、Chrome、QQ 浏览器等主流浏览器。

## 上传成功

对象上传成功后，需手动刷新列表，获取最新对象信息。【刷新】按钮会在有新对象上传成功后提醒，请单击【刷新】，获取最新对象信息。
![刷新](//mc.qcloudimg.com/static/img/cd41e20b1a12dd75510a21e2001a6b78/image.png)

## 上传说明

- 对象数量和容量大小限制
  每个存储桶对存储对象数量无限制。通过对象存储控制台上传，单个文件最大支持 64G，超 64G 的文件将无法成功上传。同时，包含保留字符和字段（请参阅 [创建文件夹-保留字符和字段](https://cloud.tencent.com/document/product/436/6263#保留字符和字段)）的文件夹名称也无法上传成功。
- 断点续传
  上传中断的对象会以 “不完整的文件” 的形式存储下来，可查看该“不完整的文件” 文件信息，但无法进行正常的下载、修改访问权限、设置自定义权限等。当下次上传相同文件时，文件会自动从断点部分继续上传。
  ![断点续传](//mc.qcloudimg.com/static/img/5f529b99d1940099ea7f9c610fa3310d/image.png)