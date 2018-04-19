## 业务部署在非腾讯云
BGP 高防 IP 使用流程如下图所示：
![](https://main.qcloudimg.com/raw/92c2461462938113c5ad49f94120ed5b.png)

### 登录控制台

1. 登录  [大禹网络安全](https://console.cloud.tencent.com/dayu/bgpip)  控制台。
![](https://main.qcloudimg.com/raw/d9d8a9d3bca8ba7ec791065be15358c0.png)

2. 在 “ BGP 高防 IP ” 控制页中找到您已经开通的业务部署在非腾讯云的高防 IP 实例。
![](https://main.qcloudimg.com/raw/781cd12ebb8e091f83309bf71570bb12.png)

3. 点击实例 ID，进入配置页面。
![](https://main.qcloudimg.com/raw/14df6a26ed04195e04b35b60bc95cf28.png)

### 新建转发规则

1. 在 “ 转发规则 ” 配置栏中选择 “ 非网站类业务 ” 。点击【新建】按钮，新建转发规则。
![](https://main.qcloudimg.com/raw/30d6935cd65fba32f8d86e606a61ea40.png)


2. 添加转发规则操作按下图所示，转发协议支持 TCP 协议，填写转发端口（即最终用于访问高防 IP  端口，一般与源站端口相同）、填写源站端口（源站提供服务的真实端口）和源站 IP ，点击【确定】后会生成一条转发规则。
![](https://main.qcloudimg.com/raw/2f67dac20eceede17aa01e2a0211d5fa.png)

> **注意：**
- 请用回车分隔多个 IP，最多可输入本 IP 转发目标区域内 20 个公网 IP。
- 用多个源站之间会以轮询方式做负载均衡。
- 一个高防 IP 支持配置 60 条转发规则。

### 切换高防 IP
最后将业务切换到高防 IP 即可。

## 业务部署在腾讯云
BGP 高防 IP 使用流程如下图所示：
![](https://main.qcloudimg.com/raw/555b6372f174692b28e14e298cd4cdca.png)

### 登录控制台

1. 登录  [大禹网络安全](https://console.cloud.tencent.com/dayu/bgpip)  控制台；
![](https://main.qcloudimg.com/raw/d9d8a9d3bca8ba7ec791065be15358c0.png)

2. 在 “ BGP 高防 IP ” 控制页中找到您已经开通的业务部署在腾讯云的高防 IP 实例，点击实例 ID，进入配置页面。
![](https://main.qcloudimg.com/raw/5c9765bdac3dcb01d61319cb37d0ecec.png)

### 创建监听器
1. 基本配置根据业务情况设置相应的协议端口，高防 IP 是四层转发， 七层应用协议，如 HTTP 等也是选择 TCP  ，如下图：
![](https://main.qcloudimg.com/raw/483a6ccdab2b8faea478193f8ae25a81.png)

2. 高级配置可以根据业务具体情况配置，如不清楚，默认配置即可。

![](https://main.qcloudimg.com/raw/5b79354281c506be0704a35ea7941f3a.png)

3. 健康检查默认是开启，建议不要自行修改配置，这里可以对出故障的服务器端口进行自动踢除，保障业务可用。

### 绑定云主机
绑定云主机，设置权重即可。
![](https://main.qcloudimg.com/raw/24ab8050b4e33216aa11d534df1ba6cf.png)

### 开启防护
开启相应防护，可以设置弹性防护峰值，并开启 CC 防护,并设置阈值。
![](https://main.qcloudimg.com/raw/bf011c4f1e38b3b1f4e87f4491de515f.png)
