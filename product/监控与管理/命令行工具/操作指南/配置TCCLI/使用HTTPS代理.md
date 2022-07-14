本文介绍如何配置和使用 HTTPS 代理。

## 操作步骤
您可通过以下两种方式，配置 HTTPS 代理。

- 对应实际使用的操作系统，执行以下命令，在环境变量中配置 HTTPS 代理。
<dx-tabs>
::: Linux\Unix 和 MacOS
```
export https_proxy=https://192.168.1.1:1111
export https_proxy=https://myproxy.com:1111
```
:::
::: Windows
```
setx http_proxy=https://192.168.1.1:1111
set  http_proxy=https://myproxy.com:1111
# setx表示设置永久环境变量，设置后重启终端生效
```
:::
</dx-tabs>
- 执行以下命令，在命令行中使用 `--https-proxy` 选项设置 HTTPS 代理。
```bash
# 例如
tccli cvm DescribeRegions --https-proxy https://192.168.1.1:1111
```
