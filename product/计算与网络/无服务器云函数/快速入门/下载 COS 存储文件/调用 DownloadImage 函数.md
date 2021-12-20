调用 DownloadImage 函数有以下两种方式，您可以根据实际需求，选择测试：
- [手动模拟测试](#ManualSimulationTest)
- [使用 COS 上传文件测试](#UploadFileTestUsingCOS)

[](id:ManualSimulationTest)
### 手动模拟测试

1. 在新创建的 DownloadImage 函数详情页面中，选择**函数代码**页签。
2. 单击**更换**，弹出 “更换测试模版” 窗口。
3. 在弹出的 “更换测试模版” 窗口中，选择 “COS 上传/删除文件事件模板”，单击**提交**。
4. 单击**测试**，运行代码并返回测试结果。如下图所示：
![](https://main.qcloudimg.com/raw/1fdf28934da1eb51f76b9dbcad497b62.png)
 - 返回结果：显示代码中 **return** 语句返回的函数执行结果。
 - 摘要：显示函数运行的时间、内存等信息。
 - 日志：显示函数运行时生成的日志，包括用户代码中的打印语句、函数运行失败 trace stack 等。
   
 >? 根据上图所示，测试模板在模拟 “COS 上传文件” 消息时，需要将模板中 “COS” 对象下的 Bucket name、appid 等信息替换为真实数据，如果未替换，下载文件时将抛出 “NoSuchBucket” 异常，导致执行结果返回 “Fail”。因此，**建议您直接采用 [使用 COS 上传文件测试](#UploadFileTestUsingCOS)。** 
5. 单击**配置**弹出 “配置测试模版” 窗口。
6. 在弹出的 “配置测试模版” 窗口中，选择 “新建模板”，填写以下信息，并单击**提交**。如下图所示：
 ![](https://main.qcloudimg.com/raw/5b54a54f4ae3df3ab32f78f5b4b803b3.png)
 - 测试事件模版：命名为 “test-scf”。
 - 引用模版代码：选择 “COS 上传/删除文件事件模板”，并修改 “引用模版代码” 中的 **cosBucket** 和 **cosObject** 结构体的参数。
    - 将 “cosBucket” 中的 “name” 更换为 “test-scf”。
    - 将 “cosBucket” 中的 “appid” 更换为 “账号的 appid”。
    - 将 “cosBucket” 中的 “region” 更换为 “guangzhou”。
    - 将 “cosObject” 中的 “key” 更换为真实数据。
    >! “key” 参数中的文件名需替换为 “test-scf” bucket 中的真实文件名。
2. 单击**测试**，运行代码并返回测试结果。如下图所示：
![](https://main.qcloudimg.com/raw/fb05ce67cf556c2b94fa8ba84922a0d3.png)
>? 您也可切换至**运行日志**页签，查看运行结果。

[](id:UploadFileTestUsingCOS)
### 使用 COS 上传文件测试

1. 登录 [对象存储服务控制台](https://console.cloud.tencent.com/cos5/bucket)，进入**存储桶列表**页面。
2. 在 “Bucket列表” 中，选择 “test-scf” bucket，进入 “ test-scf” 详情页面。
3. 单击**上传文件**，上传一张图片或者一个文件。
3. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1)，并选择 “DownloadImage” 函数。
4. 在 “DownloadImage” 详情页面，选择**运行日志**页签，检查运行结果及运行日志。如下图所示：
![](https://main.qcloudimg.com/raw/40fd92e598472c43f669b5982b04bb8c.png)
