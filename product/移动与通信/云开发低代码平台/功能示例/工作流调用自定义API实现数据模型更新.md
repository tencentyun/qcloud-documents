用微搭开发应用经常会遇到这样一种场景，即提交表单保存数据以后希望触发工作流，工作流中审批通过以后系统能够自动更新数据模型中的部分数据，这种情况下我们推荐在工作流中使用自定义 API 实现。实践案例如下：

## 操作步骤
### 步骤1：创建数据模型
创建一个**合同**的数据模型，主要有**合同 ID**、**合同名称**、**审批日期**、**审批状态**四个字段。实践案例计划**合同 ID**、**合同名称**在表单中进行添加，**审批日期**、**审批状态**在工作流中通过自定义 API 完成数据更新。
![](https://qcloudimg.tencent-cloud.cn/raw/94f37e687df26f56c6b3a30dc20adc99.png)

### 步骤2：创建自定义 API	
创建一个**合同 API** 的 APIs，使用**修改合同**方法完成对**合同**数据模型中**审批日期**、**审批状态**两个字段的更新。
![](https://qcloudimg.tencent-cloud.cn/raw/663e20407ecff756e1de754260a93a03.png)
如果不熟悉自定义 APIs 如何创建，请参见 [新建自定义 API](https://cloud.tencent.com/document/product/1301/68457)。
- **修改合同**的相关参数如下截图。
![](https://qcloudimg.tencent-cloud.cn/raw/d62f51002e920f1b532890167dfc15aa.png)
- **修改合同**方法的核心代码如下。
```javascript
module.exports = async function (params, context) {

    const result = await context.callModel({
        dataSourceName: 'ht_nljaaz5', // 数据模型名称
        methodName: 'wedaUpdate', // 更新方法
        params: {
            _id:params.id, // 合同更新数据标识id
            sprq:new Date().getTime(), // 合同审批日期，获取当前时间戳
            spzt:params.spzt // 合同审批状态
        },
    });
    return result;
}
```

如果不熟悉自定义 API 代码如何编写，请参见 [自定义代码（云函数）](https://cloud.tencent.com/document/product/1301/68440)。

### 步骤3：创建工作流
创建一个**合同流程**工作流，流程节点主要有**开始**、**人工任务**（审批节点）、**API**、**结束**四个节点。
因为要通过自定义 API 变更数据模型的字段，所以需要传递两个参数分别是 **ID**（数据标识 ID）和 **spzt**（审批状态）。为了说明变量参数和常量参数的用法，这里把数据标识 ID 作为变量参数，审批状态作为常量参数。变量参数通过页面触发流程传参形式获取，常量参数在调用自定义 API 的时候直接赋值。

#### 开始节点
![](https://qcloudimg.tencent-cloud.cn/raw/18b1b4393777e553411d0578fb81a6c7.png)
开始节点打开**流程中变量输入**开关，在**输入变量**中设置输入变量 **ID** 作为数据标识 ID，用于接收页面传参。
![](https://qcloudimg.tencent-cloud.cn/raw/f30889ccc5c1aca83f93093bd9b42030.png)

#### 人工任务（审批节点）
**是否为审批开始节点**设置成**否**，**任务接收人**设置成**用户**，**用户**选择**超级管理员**。
![](https://qcloudimg.tencent-cloud.cn/raw/2186a1a4d06ba6b77c792f7ee22169d7.png)

#### 自定义 API
**API 配置**选择前面创建的**合同 API**。
![](https://qcloudimg.tencent-cloud.cn/raw/141b38dbbf8060b3263892946f6236ef.png)
**操作设置**中将**数据标识**设置成变量 ID，通过页面传参数获取值；审批状态设置成常量，通过直接赋值**审批通过**。
![](https://qcloudimg.tencent-cloud.cn/raw/a19fd14d90a8a8ab42a020b9e8510ee0.png)
设置完工作流相关节点后保存并发布。

### 步骤4：创建应用
创建一个**合同管理**应用，为了方便查看、验证数据，在创建应用的同时使用**合同**数据模型自动创建了 CRUD 页面。

#### 创建触发工作流页面
创建名称为**合同创建触发工作流**的自定义页面。为了实现通过页面表单提交后触发工作流，这里使用**表单容器**组件绑定数据模型**合同**，保留**合同 ID**、**合同名称**两个字段作为表单提交字段。
![](https://qcloudimg.tencent-cloud.cn/raw/1334f94e78a9ffb8ef29ce142b1d270e.png)

#### 创建存储数据标识 ID 的变量
创建变量 ID，用于存储表单提交保存以后返回的数据标识 ID，以及作为工作流的传递参数。
![](https://qcloudimg.tencent-cloud.cn/raw/6b15262ab0fc664743811e0bb9641b73.png)

#### 增加变量赋值事件
选择**调用数据源**事件，将出参的新记录 ID（即数据标识 ID）保存至上面创建的**变量 ID**。
![](https://qcloudimg.tencent-cloud.cn/raw/17ca3a2f5562ec762c74862ee1411eb7.png)

#### 增加触发流程事件
在**变量赋值**成功时添加**触发流程**动作，流程选择上面创建的**合同流程**。
![](https://qcloudimg.tencent-cloud.cn/raw/4a4619297e193c77a02ae98f11377e37.png)
**参数 ID** 使用上面创建的变量 **ID**，作为流程开发的传入变量参数。
![](https://qcloudimg.tencent-cloud.cn/raw/06d54e7af387a9e16130f31b7c750bb9.png)
以上设置完成后，可以发布应用测试结果。

### 步骤5：结果验证
应用发布以后，在**合同创建触发工作流**页面录入数据。
![](https://qcloudimg.tencent-cloud.cn/raw/c9f38243480817f58c6b4b4214d9fc0c.png)
数据提交后，在数据详情页面会看到**审批状态**、**审批日期**为空。
![](https://qcloudimg.tencent-cloud.cn/raw/0a8191122e09273dfdef41c51aeb9cf1.png)
去流程中心**我的待办**查看流程申请并审批。
![](https://qcloudimg.tencent-cloud.cn/raw/c2e498d479c944628d4d07c3ee2b81d0.png)
审批同意后，在数据详情页面会看到**审批状态**、**审批日期**出现预期值。
![](https://qcloudimg.tencent-cloud.cn/raw/53ed2d685bf5bf4bdf5004141ce378fc.png)

