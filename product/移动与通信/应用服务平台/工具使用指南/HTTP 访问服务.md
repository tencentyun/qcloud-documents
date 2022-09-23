HTTP 访问服务支持通过 HTTP 链接访问云开发资源。可以通过 CLI 工具、控制台管理访问域名和云函数访问路径。

## 创建

您可以使用下面的命令，通过 CLI 命令行交互的方式创建 HTTP 访问服务地址。
<dx-codeblock>
:::  sh
tcb service create -e envId
:::
</dx-codeblock>
您也可以指定指定云函数名称 `functionName` 和触发路径 `servicePath` 创建 HTTP 访问服务地址。
<dx-codeblock>
:::  sh
tcb service create -p servicePath -f functionName
:::
</dx-codeblock>


## 删除 HTTP 访问服务链接

您可以使用下面的命令，通过 CLI 命令行交互的方式删除云函数 HTTP 访问服务链接。
<dx-codeblock>
:::  sh
tcb service delete -e envId
:::
</dx-codeblock>
您也可以通过参数指定需要删除的 HTTP 访问服务信息，如 HTTP 访问服务地址的路径，或者 HTTP 访问服务 Id
<dx-codeblock>
:::  sh
# 指定 HTTP 访问服务绑定的路径
tcb service delete -p servicePath

# 指定 HTTP 访问服务 Id
tcb service delete -i serviceId
:::
</dx-codeblock>


## 查询 HTTP 访问服务信息

您可以通过下面的命令列出所有的 HTTP 访问服务链接，查看它们的基本信息：
<dx-codeblock>
:::  sh
tcb service list
:::
</dx-codeblock>
您会得到类似下面的输出：
<table>
<tr>
<th>ID</th>
<th>路径</th>
<th>函数名</th>
<th>创建时间</th>
</tr>
<tr>
<td>39fe3034-86d8-4333-a5ee-541a10xxxxxx</td>
<td>/api</td>
<td>node-sdk</td>
<td>2020-03-17 13:08:17</td>
</tr>
<tr>
<td>Cc8c47d1-a6e6-4654-b184-69d3bcxxxxxx</td>
<td>/list</td>
<td>list</td>
<td>2020-03-13 11:11:24</td>
</tr>
</table>



### 设置更多的查询约束条件

<dx-codeblock>
:::  sh
-d domain       指定域名
-p servicePath  指定 HTTP 访问服务路径
-i serviceId    指定 HTTP 访问服务 Id
:::
</dx-codeblock>


## 绑定 HTTP 访问服务自定义域名

您可以通过下面的命令绑定 HTTP 访问服务域名：
<dx-codeblock>
:::  sh
tcb service domain bind domain
:::
</dx-codeblock>

<dx-alert infotype="notice" title="">
**绑定自定义域名之前，请先设置您的域名的 CNAME 记录值为 [默认域名](https://console.cloud.tencent.com/tcb/env/access)，CNAME 记录不存在时会导致域名绑定失败。**
</dx-alert>



## 解绑 HTTP 访问服务自定义域名

您可以通过下面的命令解绑 HTTP 访问服务域名：
<dx-codeblock>
:::  sh
tcb service domain unbind domain
:::
</dx-codeblock>


## 查询 HTTP 访问服务自定义域名

您可以通过下面的命令列出所有的 HTTP 访问服务域名，查看它们的基本信息：
<dx-codeblock>
:::  sh
tcb service domain list
:::
</dx-codeblock>

您会得到类似下面的输出：
<table>
<tr>
<th>域名</th>
<th>状态</th>
<th>创建时间</th>
</tr>
<tr>
<td>www.xxxxx.com</td>
<td>部署成功</td>
<td>2019-12-17 10:41:45</td>
</tr>
</table>


### 设置更多的查询约束条件
<dx-codeblock>
:::  sh
-d domain       指定域名
:::
</dx-codeblock>
