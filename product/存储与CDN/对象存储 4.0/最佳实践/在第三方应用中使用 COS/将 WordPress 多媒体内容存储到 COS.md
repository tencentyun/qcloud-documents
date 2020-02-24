## 简介

WordPress 可以通过第三方插件将多媒体内容保存在腾讯云 COS上，将多媒体内容保存在 COS 上有以下好处：

- 多媒体内容将拥有更高的可靠性。
- 您的服务器无需为多媒体内容准备额外的存储空间。
- 访问者查看和下载多媒体内容时将直连 COS 服务器，不占用您服务器的下行带宽/流量，访问速度更快。
- 可配合腾讯云 CDN 进一步提升访问者查看和下载多媒体内容的速度。

## 准备工作

1. 搭建 WordPress 。
	- 您可在 [WordPress 官方下载页面](https://wordpress.org/download/) 下载 WordPress 的最新版并查看安装说明。
	- 您也可以在 [腾讯云市场](https://market.cloud.tencent.com/) 中搜索使用已经预装 WordPress 程序的 CVM 镜像。
2. 创建一个**公有读私有写**的存储桶，存储桶的地域建议与运行 WordPress 的 CVM 相同，创建指引可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
3. 在存储桶列表中找到刚刚创建的存储桶，记录**存储桶名称**和**所属地域**的地域简称。了解地域简称，可参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 文档。
	 ![](https://main.qcloudimg.com/raw/3c2b8a9ea71796bc9946cc5cf2bb2dd6.jpg)
4. 进入 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)，记录密钥中的 **SecretId** 和 **SecretKey**。
   ![](https://main.qcloudimg.com/raw/9a328839005ea842f917fcd04acdd118.png)

## 安装并配置 WordPress 插件

1. 登录并进入 WordPress **仪表盘**。
2. 在左侧菜单栏中，选择【插件】>【安装插件】，进入安装插件页面。在此搜索并安装 **Media Cloud** 插件。
   ![](https://main.qcloudimg.com/raw/9c43d1ca979d852b51721bb8f2f63984.png)
3. 启用 **Media Cloud** 插件，此时会自动打开配置向导，然后单击【NEXT】。
>? 如果未能自动打开配置向导，可在 WordPress 左侧菜单中选择【Media Cloud】，并单击【Cloud Storage】下方的 【Setup Wizard】。
> ![](https://main.qcloudimg.com/raw/cf9caa71b2c3ab9ff726b7a3294ab61a.png)
4. 在存储提供商界面选择【S3 Compatible】，并单击【NEXT】。
	 ![](https://main.qcloudimg.com/raw/b0697ba2c8ee9b98a41bc0a2cffd2479.jpg)
5. 在随后的表单中配置如下内容，配置完成后单击 【NEXT】：
<table>
<thead>
<tr>
<th nowrap="nowrap">配置项</th>
<th>配置值</th>
</tr>
</thead>
<tbody><tr>
<td nowrap="nowrap">ACCESS KEY</td>
<td>访问密钥中的 <strong>SecretId</strong></td>
</tr>
<tr>
<td>SECRET</td>
<td>访问密钥中的 <strong>SecretKey</strong></td>
</tr>
<tr>
<td>BUCKET</td>
<td><strong>存储桶名称</strong></td>
</tr>
<tr>
<td>REGION</td>
<td>选择 <strong>Automatic</strong></td>
</tr>
<tr>
<td>CUSTOM ENDPOINT</td>
<td>格式为<code>cos.&lt;Region&gt;.myqcloud.com</code>，其中 &lt;Region&gt; 为存储桶<strong>所属地域</strong>的地域简称。例如，广州地域的地域简称为 ap-guangzhou，则该配置项填<code>cos.ap-guangzhou.myqcloud.com</code></td>
</tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/cc7d9766d5148873fa5fe6ba3eeee2b2.jpg"></img>
6. 此时，Media Cloud 将测试配置是否正确，单击【START TESTS】开始测试，测试全部成功后单击【NEXT】。
	 ![](https://main.qcloudimg.com/raw/db2aba4cd987b9114b9165ae72106e3f.jpg)
7. Media Cloud 提示已就绪，单击【ADVANCED SETTINGS】关闭配置向导。
<img src="https://main.qcloudimg.com/raw/5f838b8215ace7fa20150110f8f7d313.jpg" width="100%"></img>

## 测试多媒体内容

1. 撰写文章，添加多媒体内容并发布。
<img src="https://main.qcloudimg.com/raw/5a9780e676903fcc1f8c4b6b708a34d8.png" width="100%"></img>
2. 复制文章中的图片地址，或通过浏览器调试工具检视图片路径，可以看到图片地址为腾讯云 COS 对象存储上的地址（步骤3图中的1号处）。
3. 查看文章附件的下载地址，可以看到下载地址亦指向腾讯云 COS 对象存储上的地址（下图中的2号处）。
<img src="https://main.qcloudimg.com/raw/7a9d9e50e04bdc9b263ef470c399de9c.png" width="100%"></img>



## 使用腾讯云 CDN

1. 若需为保存在 WordPress 附件的存储桶配置 CDN 加速，请参见 [CDN 加速配置](https://cloud.tencent.com/document/product/436/18670) 文档。
2. 进入 Media Cloud 的管理界面，单击 **Cloud Storage** 下方的【Settings】。
![](https://main.qcloudimg.com/raw/aa744f3a16671bbd2caa873f1ba8f4ae.png)
3. 将 **CDN SETTINGS** 中的 **CDN Base URL** 设置为您的 CDN 域名，例如 COS 的默认加速域名`https://wordpress-1250000000.file.myqcloud.com/`或您的自定义加速域名`https://static.foo.bar/`。
![](https://main.qcloudimg.com/raw/95ea60db11ce736159a888ec8864ff6f.png)
4. 检查先前发布的文章中的多媒体内容，可以看到相关的地址已经指向您配置的 CDN 域名。
![](https://main.qcloudimg.com/raw/e0c3e9b987154c1def4e67676ef736e1.png)
