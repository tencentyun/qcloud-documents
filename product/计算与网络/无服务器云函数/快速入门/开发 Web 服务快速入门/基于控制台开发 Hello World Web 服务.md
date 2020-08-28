以下视频将为您介绍如何使用控制台创建函数：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2939-54952?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 操作场景
本文介绍如何通过腾讯云云函数（Serverless Cloud Function，SCF）控制台开发简单的 Hello World Web 服务。

## 前提条件
- 已注册腾讯云账户。若未注册腾讯云账户，可 [点此](https://cloud.tencent.com/register) 进入注册页面。
-  已登录 [云函数控制台](https://console.cloud.tencent.com/scf)。

## 操作步骤
### 编写函数
1. 单击左侧导航栏【函数服务】，进入“函数服务”页面。
2. 在页面上方选择**广州**地域，单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/c928ecb63d2a5b073287a75653831d76.png)
3. 在“新建函数”页面填写函数基础信息，单击【下一步】。如下图所示： 
![](https://main.qcloudimg.com/raw/d953a84b5987bb26799afda56cc08206.png)
 - **函数名称**：命名为 “helloworld”。
 - **运行环境**：选择 “Python 2.7”。
 - **创建方式**：选择 “模版函数”。
 - **模板搜索**：输入 helloworld 后按 “Enter” 进行搜索，选择 “helloworld” 模版。
4. 函数配置保持默认，并单击【完成】。如下图所示：
函数创建完成后，自动进入创建成功函数的“函数配置”页面，可查看该云函数的函数配置信息。
![](https://main.qcloudimg.com/raw/cdeb91ab9a35d863b2b051360bd24001.png)
 - “执行方法” 的 “index.main_handler” 参数值表示 SCF 控制台会将此段代码自动保存为 `index.py` 文件，并将该文件压缩和上传至 SCF 平台，用于创建云函数。
 - 示例代码中的 `main_handler` 为入口函数，主要参数为：
    - `event` 参数：可以获取触发源的消息。
    - `context` 参数：可以获取本函数的环境及配置信息。
5. 选择【函数代码】，查看或在线编辑函数代码。如下图所示：
![](https://main.qcloudimg.com/raw/6ee744fda5d5fe342c8ad08952ace998.png)


### 部署函数（含配置触发器）
1. 在进行函数代码在线编辑后，单击【保存】，函数会被部署。
2. 在已创建函数的详情页面，选择左侧【触发管理】，并单击【创建触发器】。
3. 在弹出的“创建触发器”窗口中，将“触发方式”设置为 “API网关触发器”，其它参数保持默认配置。如下图所示：
![](https://main.qcloudimg.com/raw/3f41590233c410a04170d8646a31b0f2.png)
4. 单击【提交】，即可完成函数部署及触发器配置。

### 云端测试
#### 函数部署测试
选择【函数代码】，单击【测试】，运行代码并返回测试结果。如下图所示：
>?
>- 如果您需要更换测试模版或模版中的内容。可直接编辑函数内容，或者选择【当前测试模版】，更换后单击【保存】即可生效。
>- 不同的测试模板分别模拟不同的触发器消息源，且不同的触发器和云函数之间传递的消息均为约定好的数据结构。具体详情可参考 [触发器介绍](https://cloud.tencent.com/document/product/583/9705)。
>
![](https://main.qcloudimg.com/raw/e7d4ae5c9408368b1f72da3307ff7565.png)
在本次测试过程中，云函数会在 `main_handler` 的 `event` 参数中，获取 “Hello World事件模版” 的数据结构。
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```

#### 触发器配置测试
1. 触发器创建成功后，会在该函数的“触发管理”页面生成访问路径。如下图所示：
![](https://main.qcloudimg.com/raw/ed71d3e93d86249f1c800c78ae4f7dd1.png)
2. 在浏览器里打开该访问路径，显示 “hello from scf”，则说明函数部署成功。

### 查看日志
在已创建函数的详情页面，选择左侧的【日志查询】，即可查看函数详细日志。如下图所示：
![](https://main.qcloudimg.com/raw/a705ff2f65acbc7423cdf15fbb09121c.png)
更多关于日志信息请参见 [函数日志](https://cloud.tencent.com/document/product/583/36143)。

<span id="see"></span>
#### 查看监控
在已创建函数的详情页面，选择【监控信息】，即可查看函数调用次数/运行时间等情况。如下图所示：
>!监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。
>
![](https://main.qcloudimg.com/raw/201c27811efcde8b67c6e2da28b7f462.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686)。

<sapn id="config"></span>
#### 配置告警
在已创建函数的详情页面，单击【前往新增告警】为云函数配置告警策略，对函数运行状态进行监控。如下图所示：
![](https://main.qcloudimg.com/raw/8f297a29cb80ee42552883884266e129.png)
更多关于配置告警请参见 [告警配置说明](https://cloud.tencent.com/document/product/583/30133)。
