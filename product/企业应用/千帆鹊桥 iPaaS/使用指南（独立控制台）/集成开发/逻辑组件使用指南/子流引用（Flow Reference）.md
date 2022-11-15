## 简介

子流引用（Flow Reference）组件用来引用当前应用中的其他集成流。与**异步处理**（Async）不同，子流引用是一个同步过程，当引用的集成流执行完成后，才会继续执行下一个动作，并且子流引用中的子流执行完成后，message会传递到主流中，下一个节点基于该子流的message继续执行。

当子流引用中的子流包含触发器（Trigger）节点时，如果该子流的执行由子流引用组件触发，那么该子流的触发器节点不会执行，即该子流从第二个节点开始执行。

## 操作说明

### 参数配置

| 参数  | 数据类型   | 描述                     | 是否必填 | 默认值 |
|:----|:-------|:-----------------------|:-----|-----|
| 集成流 | string | 集成流名称。可以选择同项目内其他应用共享的流 | 是    | 无   |

### 配置界面

![img_3.png](https://qcloudimg.tencent-cloud.cn/raw/c0148087ee991060b3d081b8d68a9667.png)

### 数据预览
无

### 输出

| message属性 | 值                  |
|-----------|--------------------|
| payload   | 子流最后一个节点输出的 payload |
| error     | 执行成功后，error 为空     |
| attribute | 子流输出的 attribute     |
| variable  | 子流所有设置过的 variable   |

## 案例

### 同一应用内的集成流引用

1. 新建一条集成流，名称为“子流”。子流中增加**配置Payload**组件，输出“payload”；增加**配置变量**组件，设置变量“a”。
![img_9.png](https://qcloudimg.tencent-cloud.cn/raw/f90b71cc6302c422f4aa56b1685fa48d.png)
2. 添加 Flow Reference 组件，在下拉框中选择流“子流”。
![img_10.png](https://qcloudimg.tencent-cloud.cn/raw/17c50dcda0bf1ddd61930cdeb5534e38.png)
3. 单元测试完成后，单击子流引用组件，选择专家模式查看输出。可以看到子流中设置的 payload 和变量“a”被传递到了当前流。
![img_11.png](https://qcloudimg.tencent-cloud.cn/raw/8f6e2011b54d703d2a8ef94511a1ba7f.png)


### 项目内不同应用之间的集成流引用
#### 集成流引用方式
同一个项目内多个应用可能同时用到某一个通用功能的集成流，例如“用户登录鉴权”。多个应用都要使用“用户登录鉴权”的集成流功能时，通常有三种方式：

| 使用方式 | 优缺点 | 
|---------|---------|
| 每个应用都编辑或复制一个“用户登录鉴权”的集成流 | 存在大量重复集成流，维护不便 |
| 其中某个应用以 HTTP 接口的方式提供公共接口供其他应用调用 | 有 HTTP 调用的消耗，且调试维护不便 |
| 使用子流引用的跨应用流引用 | 跟应用内的流应用体验类似，只需要两个应用同时运行即可 |

#### 使用子流引用的跨应用流引用
1. 建立“共享应用”，该应用内提供通用功能的集成流（名称“共享流”），并设置为共享。
	![img_12.png](https://qcloudimg.tencent-cloud.cn/raw/cab5e848cd68648a282632093caf0763.png)
2. 在共享流中设置 payload 和变量“share”。
	![img_13.png](https://qcloudimg.tencent-cloud.cn/raw/3d47cbb0945a1a55033ac00f0e562189.png)
3. 发布“共享应用”，此时“共享流”的集成流就可以在项目内其他应用的子流引用列表中选择并使用了。
同时启动“应用测试”，这样其他应用内引用“共享流”之后也可以进行测试。
	![img_15.png](https://qcloudimg.tencent-cloud.cn/raw/00cdfa3ae121f163380fd4cff88ad806.png)
4. 在项目内另一个应用编辑集成流，添加子流引用组件，选择引用项目其他应用（“共享应用”）的“共享流”。
	![img_16.png](https://qcloudimg.tencent-cloud.cn/raw/df8e72df8fc930bd8e2e2a16f8cb018d.png)
5. 编辑完成执行单元测试，查看子流引用（“共享流”）的节点输出，切换专家模式，可以看到共享流中设置的 payload 和 变量 “share”被传递到了当前流。
	![img_17.png](https://qcloudimg.tencent-cloud.cn/raw/b8095d87b1dccebbc10bcda9d1796327.png)

       
