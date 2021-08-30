TCCLI 默认会请求就近的接口点访问服务，您也可以针对某一产品指定 Endpoint。

## 操作步骤
- 以云服务器为例，执行以下命令，设置默认 Endpoint 为 ap-guangzhou。
```bash
tccli configure set cvm.endpoint cvm.ap-guangzhou.tencentcloudapi.com
```
- 执行以下命令，调用时实时指定 Endpoint 为 ap-guangzhou。
```bash
tccli cvm DescribeZones --endpoint cvm.ap-guangzhou.tencentcloudapi.com
```
