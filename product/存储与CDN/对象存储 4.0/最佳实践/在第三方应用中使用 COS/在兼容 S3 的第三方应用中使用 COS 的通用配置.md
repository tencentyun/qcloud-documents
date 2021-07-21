Amazon Simple Storage Service（Amazon S3，下文简称 S3）是 AWS 最早推出的云服务之一，经过多年的发展，S3 协议在对象存储行业事实上已经成为标准。腾讯云对象存储 COS（下文简称 COS）提供了兼容 S3 的实现方案，因此您可以在大部分兼容 S3 应用中直接使用 COS 服务。本文将重点介绍如何将此类应用配置为使用 COS 服务。

## 准备工作

### 确认应用是否可以使用 COS 服务

- 如果您在应用的说明中看到类似`S3 Compatible`字样，那么大多数情况可以使用 COS 服务。如果您在实际使用过程中发现应用的某些功能无法正常使用，您可以 [联系我们](https://cloud.tencent.com/document/product/436/37708)。联系时，请说明您是从该文档中看到的指引，并提供相关应用的名称和截图等信息，以便我们可以更快的帮您解决问题。
- 如果您的应用只说明支持`Amazon S3`，这表明该应用可以使用 S3 服务，但能否使用 COS 服务，还需要在相关的配置中进一步尝试，本文也会在后续的配置说明中做进一步的说明。

### 准备 COS 服务

#### 步骤1：注册腾讯云账号

（如果已在腾讯云注册，可忽略此步骤。）

<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;">点此注册腾讯云账号</a></div>

#### 步骤2：完成实名认证

（如果已完成，可忽略此步骤。）

<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/developer" target="_blank"  style="color: white; font-size:16px;"  hotrep="document.guide.3128.btn2">点此完成实名认证</a></div>

详细认证流程，请参见 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证介绍</a>。

#### 步骤3：开通 COS 服务

<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/cos5" target="_blank"  style="color: white; font-size:16px;">点此开通 COS 服务</a></div>

<span id="step4"></span>
#### 步骤4：准备 APPID 和访问密钥

在访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面中获取并记录 **APPID**、**SecretId** 和 **SecretKey**。

![](https://main.qcloudimg.com/raw/9a328839005ea842f917fcd04acdd118.png)

<span id="step5"></span>
#### 步骤5：创建存储桶

部分应用内置创建存储桶的过程，如果您希望由应用去创建存储桶，您可以忽略此步骤。

1. 在 [对象存储控制台](https://console.cloud.tencent.com/cos5) 左侧导航栏中单击【存储桶列表】，进入存储桶管理页。
2. 单击【创建存储桶】，输入存储桶信息。
	- 名称：存储桶名称，如 examplebucket。
	- 所属地域：存储桶存放地域，选择与您最近的一个地区，例如我在 “深圳”，地域可以选择 “广州”。
	- 访问权限：存储桶访问权限，此处我们选择“私有读写”。
		![](https://main.qcloudimg.com/raw/403185f7cc974daf2cb962a45474747d.jpg)
3. 单击【确定】，即可创建存储桶。


## 在应用中配置 COS 服务

### 基本配置

大部分应用在配置使用的存储服务时，都有类似的配置项，下面列举这些配置项的常见名称及相关说明：

>? 如果您在配置过程中有任何疑问，也可以 [联系我们](https://cloud.tencent.com/document/product/436/37708)。联系时，请说明您是从该文档中看到的指引，并提供相关应用的名称和截图等信息，以便我们可以更快的帮您解决问题。
>


<table>
<thead>
<tr>
<th>配置项的常见名称</th>
<th>相关说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>提供商/服务提供商/<br>存储服务提供商/<br>Service&nbsp;Provider/<br>Storage&nbsp;Provider/<br>Provider 等</td>
<td>这里主要是选择应用应使用哪种存储，可能存在以下几种情况：<br><li>如果该选项中有类似 S3 兼容存储/S3 Compatible等字样的选项，那么优先使用这个选项。<br></li><li>如果只有 amazon web services/AWS/Amazon S3 等字样，那么先使用这个选项，但是在后面的配置中需留意我们的进一步说明。<br></li><li>如果没有类似选项，但是在应用的说明中有提到支持 S3 服务或 S3 兼容服务，那么您可以继续后面的配置，但同样需要留意我们的进一步说明。<br></li><li>如果是其他情况，很抱歉，该应用可能不能使用 COS 服务。</li></td>
</tr>
<tr>
<td>服务端点/服务地址/服务&nbsp;URL/Endpoint/Custom Endpoint/Server URL 等</td>
<td>这里用于填写 S3 兼容服务的服务地址，在使用 COS 服务时，这里填写 COS 的服务地址，形式为：<code>cos.&lt;Region&gt;.myqcloud.com</code>或<br><code>https://cos.&lt;Region&gt;.myqcloud.com</code>。<br>是否需要填写<code>https://</code>，根据具体的应用有所不同，您可以自行尝试。其中<code>&lt;Region&gt;</code>代表 COS 的可用地域。<br>在应用中，您只能在服务地址中指定的地域创建或选择存储桶。<br><li>例如您的存储桶在广州地域，那么服务地址应当配置为<code>cos.ap-guangzhou.myqcloud.com</code>，如果您配置成其他地域，那么在应用中您无法找到广州地域下的存储桶。<br><li>如果应用的服务提供商中只能选择<code>Amazon S3</code>，并且服务端点是可以配置的，那么您可以将服务端点修改为前述的<code>cos.&lt;Region>.myqcloud.com</code>或<code>https://cos.&lt;Region>.myqcloud.com</code>。<br><li>如果服务端点是不可配置的或没有服务端点配置项，那么您的应用不能使用 COS 服务。</td>
</tr>
<tr>
<td>Access Key/Access Key ID 等</td>
<td>这里填写 <a href="#step4">步骤4</a> 中记录的 <strong>SecretId</strong>。</td>
</tr>
<tr>
<td>Secret Key/Secret/<br>Secret Access Key 等</td>
<td>这里填写 <a href="#step4">步骤4 </a>中记录的 <strong>SecretKey</strong>。</td>
</tr>
<tr>
<td>地域/Region 等</td>
<td>选择默认、自动、Auto 或 Automatic。</td>
</tr>
<tr>
<td>存储桶/Bucket 等</td>
<td>选择或输入现有的存储桶名称，格式为<code>&lt;BucketName-APPID&gt;</code>，例如<code>examplebucket-1250000000</code>，其中 <code>BucketName</code> 为 <a href="#step5">步骤5</a> 中创建存储桶时填写的存储桶名称，<code>APPID</code> 为 <a href="#step4">步骤4</a> 中记录的 <strong>APPID</strong>。<br>如上文所描述，这里的存储桶将限定在服务地址所指定的地域中，其他地域的存储桶将不会被列出或无法正常使用。如果您需要创建新的存储桶，那么新创建的存储桶名字也需要符合前面所讲的<code>&lt;BucketName-APPID&gt;</code> 格式，否则就无法正常创建存储桶。</td>
</tr>
</tbody></table>


### 其他项与高级配置说明

部分应用除了上述基本配置外，还有一些其他项与高级配置，下面将提供部分 COS 的功能说明，以便您更好的在应用中使用 COS 服务。

- 服务端口与协议
  COS 服务支持 HTTP 协议和 HTTPS 协议，均使用协议默认的80和443端口，基于安全考虑，我们建议您优先通过 HTTPS 协议使用 COS 服务。
- Path-Style 与 Virtual Hosted-Style
  COS 同时支持两种使用风格。
- AWS V2 签名与 AWS V4 签名
  COS 同时支持两种签名格式。

## 结语

COS 不保证与 S3 的完全兼容，如果您在应用中使用 COS 服务时遇到任何问题，您可以 [联系我们](https://cloud.tencent.com/document/product/436/37708)。联系时，请说明您是从该文档中看到的指引，并提供相关应用的名称和截图等信息，以便我们可以更快的帮您解决问题。
