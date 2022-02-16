HTTP 访问服务支持通过 HTTP 链接访问云开发资源。

可以通过 CLI 工具、控制台管理访问域名和云函数访问路径。

## 创建

您可以使用下面的命令，通过 CLI 命令行交互的方式创建 HTTP 访问服务地址

```sh
tcb service create -e envId
```

您也可以指定指定云函数名称 `functionName` 和触发路径 `servicePath` 创建 HTTP 访问服务地址

```
tcb service create -p servicePath -f functionName
```

## 删除 HTTP 访问服务链接

您可以使用下面的命令，通过 CLI 命令行交互的方式删除云函数 HTTP 访问服务链接

```sh
tcb service delete -e envId
```

您也可以通过参数指定需要删除的 HTTP 访问服务信息，如 HTTP 访问服务地址的路径，或者 HTTP 访问服务 Id

```sh
# 指定 HTTP 访问服务绑定的路径
tcb service delete -p servicePath

# 指定 HTTP 访问服务 Id
tcb service delete -i serviceId
```

## 查询 HTTP 访问服务信息

您可以通过下面的命令列出所有的 HTTP 访问服务链接，查看它们的基本信息：

```sh
tcb service list
```

您会得到类似下面的输出：

![](https://main.qcloudimg.com/raw/efb14cddfa4942a1dce615c48547ab6f.png)

### 设置更多的查询约束条件

```sh
-d domain       指定域名
-p servicePath  指定 HTTP 访问服务路径
-i serviceId    指定 HTTP 访问服务 Id
```

## 绑定 HTTP 访问服务自定义域名

:::caution 注意事项
**绑定自定义域名之前，请先设置您的域名的 CNAME 记录值为[默认域名](https://console.cloud.tencent.com/tcb/env/access)，CNAME 记录不存在时会导致域名绑定失败！**
:::

您可以通过下面的命令绑定 HTTP 访问服务域名：

```sh
tcb service domain bind domain
```

## 解绑 HTTP 访问服务自定义域名

您可以通过下面的命令解绑 HTTP 访问服务域名：

```sh
tcb service domain unbind domain
```

## 查询 HTTP 访问服务自定义域名

您可以通过下面的命令列出所有的 HTTP 访问服务域名，查看它们的基本信息：

```sh
tcb service domain list
```

您会得到类似下面的输出：

![](https://main.qcloudimg.com/raw/32b243c13c3f5d6083e7ae502996c83b.png)

### 设置更多的查询约束条件

```sh
-d domain       指定域名
```