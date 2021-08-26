本文介绍如何配置和使用HTTPS代理

## 代理配置

在环境变量中配置https代理
```bash
# 在Linux/Unix和macOS中执行如下类似命令配置环境变量
export https_proxy=https://192.168.1.1:1111
export https_proxy=https://myproxy.com:1111
# 在Windows的终端中执行如下类似命令配置环境变量
setx http_proxy=https://192.168.1.1:1111
set  http_proxy=https://myproxy.com:1111
# setx表示设置永久环境变量，设置后重启终端生效
```

直接在命令行中使用'--https-proxy'选项设置https代理
```bash
# 例如
tccli cvm DescribeRegions --https-proxy https://192.168.1.1:1111
```