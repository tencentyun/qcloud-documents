## 操作场景
私有网络（Virtual Private Cloud，VPC）是您在腾讯云上自定义的一块逻辑隔离网络空间。您可以在 API 网关中配置后端对接 VPC 的 CLB 资源，实现对 VPC 环境中资源的访问，以及部署在 VPC 中的后端服务能力的开放。

## 前提条件
- 准备两台云服务器 CVM（参考 [创建实例](https://cloud.tencent.com/document/product/213/4855)），分别称为 CVM1 和 CVM2。其中 CVM1 用来访问 API 网关，CVM2 部署在 VPC 内作为后端服务。
- 已创建 API 网关服务（参考 [创建服务](https://cloud.tencent.com/document/product/628/11787)）。

## 操作步骤
### 步骤一：放通 API 网关内网网段
1. 登录 [云服务器 CVM 控制台](https://console.cloud.tencent.com/cvm)，在左侧导航栏单击【安全组】，进入安全组列表。
2. 选择地域后，单击【+新建】，在弹出的对话框中填写内容，创建一个安全组。
![](https://main.qcloudimg.com/raw/74f7a1fa3ef65485befc8d0c39a69c24.png)
3. 单击【确定】后进入安全组详情页面，依次选择【安全组规则】>【入站规则】，即可到达入站规则列表。
4. 单击【添加规则】，在弹出的对话框中依次添加9.0.0.0/8、10.0.0.0/8、100.64.0.0/10、11.0.0.0/8、30.0.0.0/8五个API网关的内网网段，协议端口均填写“ALL”，策略均配置为“允许”。单击【完成】，添加五条入站规则。
![](https://main.qcloudimg.com/raw/42eef818c6597eae5f4647800e9c02f1.png)
5. 返回安全组详情页面，依次选择【关联实例】>【云服务器】>【新增关联】，将刚刚创建好的安全组关联到 CVM2 上，即可实现放通 API 网关内网网段。

### 步骤二：配置负载均衡和监听器
1. 登录 [负载均衡 CLB 控制台](https://console.cloud.tencent.com/clb)，在左侧导航栏单击【实例管理】，进入实例列表。
2. 选择地域后，单击【新建】，创建一个负载均衡实例，网络类型选择“内网”，选择 CVM2 所在的 VPC 作为网络。
3. 创建成功后，在实例列表中单击已创建好的负载均衡实例的 ID，进入负载均衡实例详情页面；在详情页面单击【监听器管理】，进入监听器管理页面。
4. 在“TCP/UDP监听器”区域下单击【新建】，在弹出的对话框中填写内容，创建一个 TCP 监听器。
![](https://main.qcloudimg.com/raw/521e677b3c9a4b9292e23ae7d14cd508.png)
5. 将 TCP 监听器绑定到 CVM2，端口选择后端服务监听的端口（这里的端口为5001-5006）。
![](https://main.qcloudimg.com/raw/03990a0970ccf30543a3daefb23443e7.png)

### 步骤三：配置后端对接 VPC 内的 CLB 资源
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)，在左侧导航栏单击【服务】，进入服务列表。
2. 选择地域后，在服务列表中单击服务名称，进入服务详情页；在服务详情页单击【管理API】，在管理 API 页单击【新建】，进入 API 创建页面。
3. 在 API 创建页面依次填写前端配置、后端配置、响应配置后单击【完成】，完成 API 的创建。
这里需要注意填写后端配置时，后端类型选择“HTTP”，VPC 信息选择 CVM2 所在的 VPC，VPC 内资源选择“CLB”，后端域名选择刚才在负载均衡内创建的监听器。
 ![](https://main.qcloudimg.com/raw/a017e4a99b82ced78ff24c604fdd18fa.png)
 
### 步骤四：配置 Nginx 并测试
1. 登录 CVM2，安装 Nginx。并修改 Nginx 配置，监听配置的端口。
![](https://main.qcloudimg.com/raw/9d93461e84d75241501a228359059f2b.png)
2. 登录 CVM1，通过 API 网关服务子域名即可访问刚才创建的 API，并且可以通过 wrk 做性能压测。
![](https://main.qcloudimg.com/raw/c8ee97d1700b5f20725435c215f905f7.png)
