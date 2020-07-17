## 创建 COS Bucket
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos)。
2. 创建一个 Bucket，命名为 idcard-detect，并选择**北京**地域，权限选择 “私有读写”。

## 开通 AI 接口
前往 [智能图像控制台](https://console.cloud.tencent.com/ai/ocr/idcard) 开通身份证识别功能，单击【开通服务】即可。

## 创建云函数
1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**北京**地域，并单击【新建】进入新建函数页面。
设置以下参数信息，并单击【下一步】。如下图所示：
 - **函数名称**：命名为 “IDCard_Detecttion”。
 - **运行环境**：选择 “Python 2.7”。
 - **创建方式**：选择【模板函数】。
 - **模糊搜索**：输入“身份证识别”，并进行搜索。
单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
![](https://main.qcloudimg.com/raw/fb3ea1fa8fbcb8011c39cab76c42c782.png)
4. 保持默认配置，单击【完成】，完成函数的创建。
5. 切换到【函数配置】页面，单击【编辑】，修改函数超时时间为5秒。

## 配置触发器
>! “触发方式” 选择 “COS 触发”，COS Bucket 选择 “idcard-detect” ，事件类型选择 “全部创建”，其它保持默认参数。
>
选择【触发方式】页面，单击【添加触发方式】，为云函数添加 COS 触发器。 

## 测试函数功能
1. 切换至 [对象存储控制台](https://console.cloud.tencent.com/cos/bucket)，选择创建好的 Bucket：idcard-detect，单击【上传文件】，选择自己拍好的身份证照片，照片要清晰可读且尽可能大的占满图片，然后上传。
2. 进入云函数控制台查看执行结果，在 **日志** 中可以看到打印出来的日志信息，包含身份证识别的结果。如下图所示：
![](https://main.qcloudimg.com/raw/2f1df813647d9b5061fc9c4e5dfb1400.jpg) 
