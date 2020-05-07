## 操作场景
本文介绍如何通过腾讯云云函数（Serverless Cloud Function，SCF）控制台开发简单的 Hello World Web 服务。

## 前提条件
- 已注册腾讯云账户。若未注册腾讯云账户，可 [点此](https://cloud.tencent.com/register) 进入注册页面。
-  已登录 [云函数控制台](https://console.cloud.tencent.com/scf)。

## 操作步骤
### 编写函数
1. 单击左侧导航栏【函数服务】，进入“函数服务”页面。
2. 在页面上方选择**广州**地域，单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/3336661866d7dd0fce459b0d49fb9ee3.png)
3. 在“新建函数”页面填写函数基础信息，单击【下一步】。如下图所示： 
![](https://main.qcloudimg.com/raw/d953a84b5987bb26799afda56cc08206.png)
 - 函数名称：命名为 “helloworld”。
 - 运行环境：选择 “Python 2.7”。
 - 创建方式：选择 “模版函数”。
 - 模板搜索：输入 helloworld 后按 “Enter” 进行搜索，选择 “helloworld” 模版。
4. 函数配置保持默认，并单击【完成】。如下图所示：
函数创建完成后，自动进入创建成功函数的“函数配置”页面，可查看该云函数的函数配置信息。
![](https://main.qcloudimg.com/raw/51904d21bab798a3cd57991e32b8ccb7.png)
 - “执行方法” 的 “index.main_handler” 参数值表示 SCF 控制台会将此段代码自动保存为 `index.py` 文件，并将该文件压缩和上传至 SCF 平台，用于创建云函数。
 - 示例代码中的 `main_handler` 为入口函数，主要参数为：
    - `event` 参数：可以获取触发源的消息。
    - `context` 参数：可以获取本函数的环境及配置信息。
5. 选择【函数代码】，查看或在线编辑函数代码。如下图所示：
![](https://main.qcloudimg.com/raw/6fc47d3b5ffd22daee110f0895c30671.png)


### 部署函数（含配置触发器）
1. 在进行函数代码在线编辑后，单击【保存】，函数会被部署。
2. 在已创建函数的详情页面，选择【触发方式】，并单击【添加触发方式】。如下图所示：
![](https://main.qcloudimg.com/raw/8e248f3c54b2599e6bb70442b61ace4a.png)
3. 在“添加触发方式”页面，将“触发方式”设置为 “API网关触发器”，其它参数保持默认配置。如下图所示：
![](https://main.qcloudimg.com/raw/f3671f30e2981a5433a13f43d84dfad6.png)
4. 单击【保存】，即可完成函数部署及触发器配置。

### 云端测试
#### 函数部署测试
选择【函数代码】，单击【测试】，运行代码并返回测试结果。如下图所示：
>?
>- 如果您需要更换测试模版或模版中的内容。可直接编辑函数内容，或者选择【当前测试模版】，更换后单击【保存】即可生效。
>- 不同的测试模板分别模拟不同的触发器消息源，且不同的触发器和云函数之间传递的消息均为约定好的数据结构。具体详情可参考 [触发器介绍](https://cloud.tencent.com/document/product/583/9705)。
>
![](https://main.qcloudimg.com/raw/7afa811d97a5cad317119bf3fd9f0f9d.png)
在本次测试过程中，云函数会在 `main_handler` 的 `event` 参数中，获取 “Hello World事件模版” 的数据结构。
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```

#### 触发器配置测试
1. 触发器创建成功后，会在该函数的“触发方式”页面生成访问路径。如下图所示：
![](https://main.qcloudimg.com/raw/84c26e86aec04a08b2d6cafd0a3484d4.png)
2. 在浏览器里打开该访问路径，显示 “hello from scf”，则说明函数部署成功。

### 查看日志
在已创建函数的详情页面，选择【运行日志】，即可查看函数详细日志。如下图所示：
![](https://main.qcloudimg.com/raw/0cd8029dd40a4064a0a3eec3e397ba0a.png)
更多关于日志信息请参见 [函数日志](https://cloud.tencent.com/document/product/583/36143)。

<span id="see"></span>
#### 查看监控
在已创建函数的详情页面，选择【监控信息】，即可查看函数调用次数/运行时间等情况。如下图所示：
>!监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。
>
![](https://main.qcloudimg.com/raw/acc4d768c7a23e424fd65e065b1c043f.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686)。

<sapn id="config"></span>
#### 配置告警
在已创建函数的详情页面，单击【前往新增告警】为云函数配置告警策略，对函数运行状态进行监控。如下图所示：
![](https://main.qcloudimg.com/raw/6850e40bca71bfe7ca976004388294c8.png)
更多关于配置告警请参见 [告警配置说明](https://cloud.tencent.com/document/product/583/30133)。
