对云点播中的视频发起的上传、删除、视频处理等操作，都可以被称为一个事件。事件的执行需要一段时间才能完成，云点播在事件结束时，会立即通知 App 服务操作的执行结果，即事件通知。

云点播支持以下几种事件通知：

<table>
    <tr>
        <th style="width:30%">
            归类
        </th>
        <th style="width:70%">
            事件通知
        </th>
    </tr>
    <tr>
        <td rowspan=3>
            上传删除类
        </td>
        <td>
				    <a href="https://cloud.tencent.com/document/product/266/7830">视频上传完成</a>
        </td>
		<tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/7831">URL 拉取视频上传完成</a>
        </td>
    </tr>
		<tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/13434">视频删除完成</a>
        </td>
    </tr>
    <tr>
        <td rowspan=3>
            视频处理类
        </td>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/9636">任务流状态变更</a>
        </td>
		<tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/33794">视频编辑完成</a>
        </td>
    </tr>
		<tr>
        <td>
            <a href="https://cloud.tencent.com/document/product/266/33795">微信发布完成</a>
        </td>
    </tr>
</table>

事件通知方式分为“普通回调”和“可靠回调”，您可以登录 [云点播控制台](https://console.cloud.tencent.com/vod) 设置回调模式，选择您需要接收回调的事件，具体操作请参见 [回调设置](https://cloud.tencent.com/document/product/266/33781)。

- 普通回调：在控制台上配置一个回调 URL，系统在事件完成后向该 URL 发送 HTTP 请求，请求体中包含通知内容。
- 可靠回调：在事件完成后，云点播系统将通知内容放入内置的队列，App 服务通过服务端 API 消费队列中的通知。



## 普通回调

普通回调是 App 服务被动接收事件通知的模式。配置回调 URL 并选择普通回调模式后，云点播会在事件完成后，向回调 URL 发起回调。

云点播发起的普通回调的形式是 HTTP 请求，请求体为 JSON 格式，内容为不含 EventHandle 参数的 [EventContent 结构](/document/api/266/31773#EventContent)。
以 [任务状态变更通知](https://cloud.tencent.com/document/product/266/9636) 为例，回调中的`EventType`参数为`ProcedureStateChanged`，信息由`ProcedureStateChangeEvent`参数表示（[ProcedureTask](https://cloud.tencent.com/document/api/266/31773#ProcedureTask) 结构）。

## 可靠回调
可靠回调是 App 服务主动向云点播拉取事件通知的模式。选择可靠回调模式后，云点播系统将把事件通知放入队列中，App 服务通过服务端 API 从队列中依次消费事件通知。
App 服务通过 [拉取事件通知](/document/product/266/33433) API 获取消息后，需要调用 [确认事件通知](/document/product/266/33434) API 进行确认。消息必须被确认之后，才会从云点播中的队列中删除，所以“可靠回调”的可靠性高于“普通回调”。**如果对事件通知的可靠性要求高，建议使用“可靠回调”模式**。
