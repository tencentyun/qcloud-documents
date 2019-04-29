假若使用高防 IP 作为代理，针对不同需求可以利用以下方法获取客户端真实 IP。

## 四层接入
使用高防 IP 四层代理可利用 toa 模块获取客户端真实 IP。
## 支持操作系统
- **centos7.x**

## 注意事项：
1. 建议先在测试环境中进行测试，观察环境稳定后再部署正式上线。
2. 升级内核前，建议将原内核保存，以防出现升级失败等意外。
3. toa 仅支持 IPV4，若环境默认获取 IPV6 便无法正确获得得到客户端 IP。

## 操作步骤
1. 安装编译环境：yum install gcc kernel-headers kernel-devel    
2. 下载内核文件并解压。
![](https://main.qcloudimg.com/raw/00b1a43239ad93e7aefddf9f9a2f77f8.png)
3. 执行 uname -r 命令，更改 Makefile 配置文件中的路径。
![](https://main.qcloudimg.com/raw/93e9e952b7d5a4868b75e8d599f6fb23.png)
4. 执行 make 命令，进行编译。
![](https://main.qcloudimg.com/raw/175226efc35452078aedba9872f90a54.png)
5. 移动模块并启动加载。
mv toa.ko /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
insmod /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
>**注意：**
>加载成功后，主机能正常获取真实客户端源 IP。如果仍无法获取客户端源 IP，可执行 lsmod|grep toa 命令检测 toa 模块加载情况。

## 七层接入
使用高防 IP 七层代理，可通过 X-Forwareded-For 的方式获取客户端真实 IP。X-Forwareded-For 是一个 HTTP 头部扩展字段，格式为：X-Forwarded-For：Client， proxy1，proxy2，proxy3，…。当一个七层代理服务器（如高防 IP）把用户的访问请求转到后端服务器时，中间会经过多层代理服务器，请求用户的真实 IP 处于第一个位置，而后面包含所有经过的中间代理服务器的 IP。因此，只要获取 HTTP 头部的 X-Forwarded-For 字段的内容即可。详情请查看常见的 [应用服务器配置方案](https://cloud.tencent.com/document/product/214/3728)。
