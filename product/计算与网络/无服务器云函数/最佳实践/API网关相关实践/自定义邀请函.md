## 操作场景
本文档介绍如何通过云函数 SCF 结合 API 网关实现自定义邀请函，输入嘉宾名字即可生成邀请函。

## 操作步骤

### 创建存储桶
存储桶用于存储自定义生成的邀请函。具体步骤如下：
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，选择左侧导航栏中的**存储桶列表**。
2. 在“存储桶列表”页面中，单击**创建存储桶**。
3. 在弹出的“创建存储桶”窗口中，参考以下信息进行创建。如下图所示：
![](https://main.qcloudimg.com/raw/06122f00d2a36c15d4879c3f7b0de0f8.png)
主要参数信息如下，其余参数请保持默认设置：
 - **名称**：自定义名称，本文以 test 为例。
 - **所属地域**：选择“广州”。
 - **访问权限**：公有读私有写。
4. 单击**确定**即可完成创建。
5. 选择存储桶左侧的**安全管理**，在“跨域访问CORS设置”中单击**添加规则**。
6. 在弹出的“跨域访问CORS添加规则”窗口中，参考以下信息添加规则。如下图所示：
![](https://main.qcloudimg.com/raw/ab112ead265bc47682bdcab84689f7ed.png)
主要参数信息如下，其余参数请保持默认设置：
 - **来源 Origin**：输入 <b>*</b>。
 - **操作 Methods**：勾选 “GET”。
 - **Expose-Headers**：输入 **-**。
7. 单击**提交**即可添加成功。

### 创建函数及 API 网关触发器
1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方选择**广州**地域，并单击**新建**进入新建函数页面。
3. 按照如下流程搜索自定义邀请函模版，如下图所示，本文以运行环境 Python2.7为例：
 - **创建方式**：选择**模板函数**。
 - **模糊搜索**：输入“自定义邀请函”，并进行搜索。
单击模板中的**查看详情**，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
![](https://main.qcloudimg.com/raw/4cbdd51f662632e5238d4ed0c93aeab7.png)
4. 单击**下一步**，函数名称默认填充，可根据需要自行修改。按照引导在“基础配置”中填入该模版需要的环境变量对应的值，其他保持默认配置。如下图所示：
![](https://main.qcloudimg.com/raw/6262658b1e578f0ba5a294441e1f70bd.png)
环境变量填写可参考下表：
![](https://main.qcloudimg.com/raw/61022c3d9fcada70091530c25aedf7be.png)
<table>
<tr>
<th>key</th><th>value</th>
</tr>
<tr>
<td>region</td><td>存储桶所在地域。以 ap- 开头，加上地域拼音。</td>
</tr>
<tr>
<td>target_bucket</td><td>已创建的存储桶名称。</td>
</tr>
<tr>
<td>target_path</td><td>目标存储桶路径。用于存放邀请函的存储桶目录路径，请前往**<a href="https://console.cloud.tencent.com/cos5/bucket">存储桶列表</a>** > **进入“对应的存储桶”**，查看对应的目录路径。例如目录为 example，则此处的目标路径即为 /example。若在存储桶在未创建目录，那么此处输入 “/” 即可。</td>
</tr>
</table>
<dx-alert infotype="explain" title="">
本示例需要授权 SCF 操作 COS 的权限，已默认勾选“运行角色”并自动完成函数运行角色的创建和所需 COS 操作权限策略 QcloudCOSFullAccess 的关联，如需调整，请选择“使用已有策略”或取消“运行角色”勾选。
</dx-alert>
6. 单击**完成**，完成函数和 API 网关触发器创建。

### 生成邀请函
您可通过以下两种方式，进行邀请函生成：

<dx-alert infotype="explain" title="">
您可在**触发管理**页中获取 API 网关触发器访问路径，如下图所示：
![](https://main.qcloudimg.com/raw/79db3e509fe3710d0da4ef7bd59b1418.png)
</dx-alert>


#### 方式1
在命令行中，执行以下命令。
```
curl API网关触发器地址  -d '邀请嘉宾名字'
```
可在终端获取邀请函的下载地址。例如：
```
curl https://service-xxxx.gz.apigw.tencentcs.com/release/test-123456 -d 'name'
https://testxxxx.com//邀请函-yun-ServerlessDays.jpg%
```

#### 方式2
1. 下载 [HTML 页面](https://github.com/tencentyun/scf-demo-repo/blob/master/Python2.7-Add_Text_To_Pictures/invitation.html)，并将链接修改为 API 网关触发器的链接。如下图所示：
![](https://main.qcloudimg.com/raw/9154ce1a3b16d2f9ee6cb8500d4eb3e4.png)
2. 打开 HTML 页面，输入邀请嘉宾的名字，则可以生成海报，访问链接可直接下载海报。如下图所示：
![](https://main.qcloudimg.com/raw/8d9dcfffa6c095fb20f824eabfd23559.png)
