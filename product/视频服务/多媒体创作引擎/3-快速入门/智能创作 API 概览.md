通过阅读本文，您可以了解智能创作 API 服务。

## **前提条件**

- 已开通 [腾讯智能创作平台](https://app.v.tencent.com/login?action=logout&redirect=https%3A%2F%2Fapp.v.tencent.com%2F)。具体操作，请参见 [企业版激活](https://cloud.tencent.com/document/product/1156/83467)。
- 部分 API 需要用到平台 ID，当前平台 ID 非外显，无法直接查看，如需查看平台 ID 请扫码添加商务后获取。

<img src="https://qcloudimg.tencent-cloud.cn/raw/6486ac753b5389440c74bc57651c03fe.png" width=30%>

## **客户端 API**

**客户端API汇总**
<table>
<thead>
<tr>
<th width=10>模块</th>
<th width=30>功能类型</th>
<th width=250>描述</th>
<th width=30>参考文档</th>
</tr>
</thead><tbody>
<tr>
<td rowspan="3">云媒资</td>
<td>上传文件</td>
<td>通过调用 API 可将文件上传至智能创作。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/51360">上传相关接口</a></td>
</tr>
<tr>
<td>文件管理</td>
<td>用于对文件进行删除、查看文件信息等操作。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/50862">媒体管理相关接口</a></td>
</tr>
<tr>
<td>分类管理</td>
<td>用于对文件进行分类管理，包括创建、删除、查询和修改分类。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/51362">分类管理相关接口</a></td>
</tr>
<tr>
<td>协作审片</td>
<td>团队管理</td>
<td>用于对项目团队进行管理，包括添加、删除和查询项目里的文件，删除、修改、查询和搜索项目。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/51432">团队管理相关接口</a></td>
</tr>
<tr>
<td>云剪辑</td>
<td>媒资物料处理</td>
<td>用于对需要剪辑的物料进行管理，包括添加、修改、删除帧等。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/51367">媒体物料相关接口</a></td>
</tr>
<tr>
<td>任务中心</td>
<td>任务管理</td>
<td>通过调用 API 可查询任务进度信息以及删除任务。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/51419">任务管理相关接口</a></td>
</tr>
<tr>
<td>项目中心</td>
<td>项目管理</td>
<td>用于添加、删除和查询视频剪辑、直播剪辑、导播台等项目的媒体文件，用于删除、修改、查询和搜索视频剪辑、直播剪辑、视频拆条等项目。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/51507">项目管理相关接口</a></td>
</tr>
</tbody></table>

**客户端 API 调用方式**
客户端API调用方式详见文档客户端 API [调用方式](https://cloud.tencent.com/document/product/1156/50899)。

## **服务端 API**

**服务端API汇总**

<table>
<thead>
<tr>
<th width=10>模块</th>
<th width=30>功能类型</th>
<th width=250>描述</th>
<th width=30>参考文档</th>
</tr>
</thead>
<tbody><tr>
<td>平台</td>
<td>平台管理</td>
<td>用于获取平台列表信息和平台中所有已注册的账号信息。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/51096">平台管理相关接口</a></td>
</tr>
<tr>
<td>登录态</td>
<td>登录态管理</td>
<td>用于查询指定用户的登录态以及删除登录态等。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/40355">登录态管理相关接口</a></td>
</tr>
<tr>
<td rowspan="3">云媒资</td>
<td>媒资管理</td>
<td>用于将云点播文件导入智能创作资源库、获取媒资详情信息、修改媒资信息等。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/43243">媒体资源管理相关接口</a></td>
</tr>
<tr>
<td>媒资授权</td>
<td>通过调用 API 资源归属者可以对个人或者团队授予目标资源相应的权限、查询资源被授权情况或撤销资源授权。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/43249">媒资授权相关接口</a></td>
</tr>
<tr>
<td>分类管理</td>
<td>用于对文件进行分类管理，包括新增分类、获取分类列表、删除分类等。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/43265">分类管理相关接口</a></td>
</tr>
<tr>
<td>协作审片</td>
<td>团队管理</td>
<td>用于创建项目团队、添加项目团队成员、获取团队信息、修改、删除团队成员等。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/43260">团队管理相关接口</a></td>
</tr>
<tr>
<td rowspan="3">云剪辑</td>
<td>视频剪辑&amp;模板剪辑</td>
<td>通过调用API进行视频剪辑或模板剪辑并导出视频。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/44159">Headless 媒体合成相关接口</a></td>
</tr>
<tr>
<td>智能拆条</td>
<td>通过调用 API 发起视频智能拆条任务并支持将拆条片段导出。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/50982">视频编辑相关接口</a></td>
</tr>
<tr>
<td>视频参数配置</td>
<td>用于创建、删除、修改以及查询视频编码配置。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/64067">参数模板相关接口</a></td>
</tr>
<tr>
<td>任务中心</td>
<td>任务管理</td>
<td>用于获取任务列表和获取任务详情，包括任务状态、错误信息、创建时间等。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/40358">任务管理相关接口</a></td>
</tr>
<tr>
<td>项目中心</td>
<td>项目管理</td>
<td>通过调用 API 在智能创作中创建视频剪辑、直播、视频拆条等项目，支持获取项目列表、修改、删除、导出和对项目进行操作等。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/40350">项目管理相关接口</a></td>
</tr>
<tr>
<td>其他</td>
<td>回调事件内容解析</td>
<td>该接口接受制作云回调给客户的事件内容，将其转化为对应的 EventContent 结构，请不要实际调用该接口，只需要将接收到的事件内容直接使用 JSON 解析到 EventContent 即可使用。</td>
<td><a href="https://cloud.tencent.com/document/product/1156/56199">回调事件内容解析</a></td>
</tr>
</tbody></table>

**服务端 API 调用方式**
服务端 API 调用方式详见文档服务端 API [调用方式](https://cloud.tencent.com/document/product/1156/40340)。

## **其他接入方式**

除了提供 API 接入方式之外，智能创作还提供**云剪辑 Web Iframe 接入**，具体介绍请参见 [在线视频剪辑集成综述](https://cloud.tencent.com/document/product/1156/65096)。

## **总结**

通过阅读本文，您已经了解了智能创作的 API 汇总及接入方式。
