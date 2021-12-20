1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，进入**存储桶列表**页面。
2. 单击**创建存储桶**。
3. 在弹出的 “创建存储桶” 窗口中，填写填写以下信息，并单击**确定**。
 - 名称：命名为 “test-scf”。
 - 地域：选择 “广州（华南）”。
 - 访问权限：选择 “私有读写”。
4. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1)，进入**函数服务**页面。
5. 选择**广州**地域，单击**新建**，进入新建函数页面。
6. 填写以下参数信息，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/2fa61bd4c599d0798b48e1faee5e2e9e.png)
 - 创建方式：选择 “模板函数”。
 - 函数名称：命名为 “DownloadImage”。
 - 模板搜索：选择 “语言” 为 “Python2.7” 的 “从对象存储获取文件” 模板。
7. 保持默认配置，单击**完成**，完成函数的创建。
函数创建完成后，云函数平台会根据模板函数信息，自动填充函数配置及执行方法等信息。
8. 在创建的函数详情页面，选择**函数代码**页签。
9. 修改并保存如下图所示的代码片段。
![](https://main.qcloudimg.com/raw/b106350bff4feb54e41785458fea6f66.png)
主要参数信息如下：
 - “执行方法” 的 “Get_COS_Object.main_handler” 参数值表示云函数控制台会将此段代码自动保存为 `Get_COS_Object.py` 文件，并将该文件压缩和上传至 SCF 平台，用于创建云函数。
 - 将以下参数修改为您的实际数据：
    - appid：可在控制台[**账号信息**](https://console.cloud.tencent.com/developer) 中获得。
    - secret_id 和 secret_key：可在控制台[**云 API 密钥**](https://console.cloud.tencent.com/cam/capi) 中获得。
    - region： 设置为 COS Bucket 所在地域，即 “ap-guangzhou”。
    >! 云函数和 COS Bucket 须选择同一个地域。
10. 选择**触发方式**页签，单击**添加触发方式**。
11. 在 “添加触发方式” 页面，填写以下信息，单击**保存**。如下图所示：
![](https://main.qcloudimg.com/raw/0a52a905922ee1c150c203d88df721d1.png)
 - 触发方式：选择 “COS触发”。
 - COS Bucket：选择创建好的 “test-scf” 。
 - 事件类型：选择 “全部创建”。

