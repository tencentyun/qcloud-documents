### 初次新建工程时需进行 COS 一键授权，若授权失败，如何手动进行 COS 授权？
登录 [CAM 角色管理界面](https://console.cloud.tencent.com/cam/role)，按以下步骤操作：
1. 单击【新建角色】-选择【腾讯云产品服务】。
2. 勾选中【腾讯智能钛】，单击【下一步】。
3. 在【策略列表】中搜索【QcloudAccessForTIRole】，并选中，单击【下一步】。
![](https://main.qcloudimg.com/raw/30818e5fea2cda0a2bd1a8930b493998.png)
4. 【角色名称】填写【TI_QCSRole】>【角色描述】选填【腾讯智能钛（TI）操作权限含列举对象存储（COS）文件，读取、删除、添加、修改文件内容等 】，单击【完成】，即手动完成 COS 授权。

### 当在创建模型或部署模型过程中报错“无法访问 COS 资源的权限”时怎么办？
1. 登录 [CAM 角色管理界面](https://console.cloud.tencent.com/cam/role)。
2. 检查是否完成 COS 授权给智能钛产品。
3. 若检查结果为已授权，存在角色：TI_QCSRole，建议删除此角色，重新完成 COS 授权。
![](https://main.qcloudimg.com/raw/a08fabf2e8ba541e48238234e5425a94.png)
4. 如不存在角色：TI_QCSRole，请进行 COS 授权。

### 查看中间结果时，如何根据页面上展示的 COS 路径查询到对应文件？
复制蓝色底色中的文字至相应的存储桶的查询窗口，便可搜索到对应文件。
![](https://main.qcloudimg.com/raw/b4e25ef010f1cdbbcbdcf33cf580c7bf.png)

### 在平台训练好的模型是否支持下载到线下使用？
支持，操作步骤如下：
右键【模型图标】，单击【模型操作】>【导出模型】即可。
![](https://main.qcloudimg.com/raw/5a91479e5a0db8b00d10d5eeda977887.png)

### 平台是否支持从外部导入模型？
支持，操作步骤如下：
在【模型仓库】页，单击页面上方【导入模型】，可以将外部的模型导入平台进行统一管理，支持来源为用户的 COS 路径与本地上传。

### 模型部署时如何选择正确的运行环境？
目前平台支持3种运行环境：
1. pmml：一般使用机器学习时选择此运行环境。
2. pb：一般使用深度学习时选择此运行环境。
3. angel：此环境一般针对 angel 算法，后续会支持此种算法。
