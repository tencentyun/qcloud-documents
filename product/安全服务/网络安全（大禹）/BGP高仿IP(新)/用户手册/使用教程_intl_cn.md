
## 业务部署在非腾讯云
BGP 高防 IP 使用流程如下图所示：
![](https://main.qcloudimg.com/raw/ca8742c013fa149e542416d786c8314e.png)

### 登录控制台

1. 登录  [大禹网络安全](https://console.cloud.tencent.com/dayu/bgpip)  控制台，找到您购买的转发目标为非腾讯云的 BGP 高防 IP 实例。
 ![1](https://main.qcloudimg.com/raw/464f1a9d0289f2e21b25dea217add1e1.png)
2. 点击实例 ID，进入配置页面。

### 新建转发规则

1. 在 “ 转发规则 ” 配置栏中，点击【新建】按钮，新建转发规则。
 ![2](https://main.qcloudimg.com/raw/4408dc9019be2f7d776bffc482722e4f.png)
2. 添加转发规则操作按下图所示，转发协议支持 TCP 协议，填写转发端口（即最终用于访问高防 IP  端口，一般与源站端口相同）、填写源站端口（源站提供服务的真实端口）和源站 IP ，点击【确定】后会生成一条转发规则。
 ![3](https://main.qcloudimg.com/raw/af31955bf91d13464940496c00e92312.png)
 
> **注意：**
- 请用回车分隔多个 IP，最多可输入本 IP 转发目标区域内 20 个公网 IP。
- 用多个源站之间会以轮询方式做负载均衡。
- 一个高防 IP 支持配置 60 条转发规则。

### 修改 DNS 解析
最后将 A 记录指向的 IP 地址修改为 BGP 高防 IP 即可。

## 业务部署在腾讯云
BGP 高防 IP 使用流程如下图所示：
 ![](https://main.qcloudimg.com/raw/555b6372f174692b28e14e298cd4cdca.png)

### 登录控制台
1. 登录  [大禹网络安全](https://console.cloud.tencent.com/dayu/bgpip)  控制台，在 “ BGP 高防 IP ” 控制页中找到您已经开通的业务部署在腾讯云的高防 IP 实例。
 ![4](https://main.qcloudimg.com/raw/cb571f1fef4ec2f83486a048c3d518b0.png)
2. 点击实例 ID，进入配置页面。

### 创建监听器
1. 基本配置根据业务情况设置相应的协议端口，高防 IP 是四层转发， 七层应用协议，如 HTTP 等也是选择 TCP  ，如下图：
 ![5](https://main.qcloudimg.com/raw/6da402eaf207544f2cef5d03f5a5b4d2.png)
2. 高级配置可以根据业务具体情况配置，如不清楚，默认配置即可。
 ![6](https://main.qcloudimg.com/raw/4235e3c7a062c4d3c027e27f1f7c08c5.png)
3. 健康检查默认是开启，建议不要自行修改配置，这里可以对出故障的服务器端口进行自动踢除，保障业务可用。
 
### 绑定云主机
绑定云主机，设置权重即可。
![7](https://main.qcloudimg.com/raw/b8367df8400d5b83e58d834af4c933d3.png)

