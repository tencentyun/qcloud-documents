为了帮助您快速体验如何将应用接入 TSE Consul 注册中心，本文以一对 Demo 示例（包含一个 provider 应用和一个 consumer 应用）介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 Consul 注册中心，并实现简单的服务访问。



## 前提条件

- 已 [获取访问授权](https://cloud.tencent.com/document/product/1364/56268)
- 已 [购买云服务器](https://buy.cloud.tencent.com/cvm)



## 步骤1：创建 Consul 引擎实例

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏，单击 **consul**，进入 Consul 注册中心页面。
3. 选择好地域后单击**新建**，根据自身业务需求填写以下配置信息：
   <table>
   <thead>
   <tr>
   <th>参数</th>
   <th>说明</th>
   </tr>
   </thead>
   <tbody><tr>
   <td>名称</td>
   <td>最长60个字符，支持中英文大小写、-、_，名称一旦创建后不支持修改</td>
   </tr>
   <tr>
   <td>版本</td>
   <td>1.8.6</td>
   </tr>
   <tr>
   <td>规格</td>
   <td>1C1G、1C2G、2C4G、4C8G、8C16G、16C32G</td>
   </tr>
   <tr>
   <td>节点数</td>
   <td>可选3、5节点</li></ul></td>
   </tr>
   <tr>
   <td>引擎所在地域</td>
   <td>选择与您部署业务最靠近的地域。</li></ul></td>
   </tr>
   <tr>
   <td>集群网络</td>
   <td>所选择的私有网络必须和已购买的云服务器所在的私有网络一致。所选择的子网不用和云服务器所在的私有网络一致</td>
   </tr>
   <tr>
   <td>标签</td>
   <td>用于分类管理资源，选填，具体使用方法可参见 <a href="https://cloud.tencent.com/document/product/1364/74387">标签管理</a></td>
   </tr>
   </tbody></table>
4. 单击**创建**，完成 consul 引擎创建。创建完成后单击引擎实例的“ID”，进入基本信息页面，选择**访问管理**页签可以获取 Consul 注册中心实例访问 IP。
   ![](https://qcloudimg.tencent-cloud.cn/raw/fc5cae7f9723dd275ff059389221997c.png)


[](id:step2)
## 步骤2：准备配置

1. 下载 [Consul](https://releases.hashicorp.com/consul/1.8.6/consul_1.8.6_linux_amd64.zip)，并将下载好的的安装包上传至云服务器 CVM。详细操作请参见 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
2. 登录云服务器，执行如下命令创建相关资源。
   1. 执行如下命令创建数据文件夹。
      ```
      mkdir -p /data/consul/data
      ```
   2. 执行如下命令创建日志文件夹
      ```
      mkdir -p /data/consul/log
      ```
   3. 执行如下命令创建配置文件。
      ```
      vim /data/consul/config/config.json
      ```
      输入`i`，写入如下配置文件内容后，单击`esc`，输入`:wq`后回车，完成配置文件创建。
      ```json
      {
       "datacenter": "dc1",
       "data_dir": "/data/consul/data/",
       "node_name": "consul-agent-node",
       "server": false,
       "bind_addr": "{{ GetInterfaceIP \"eth0\" }}",
       "client_addr": "127.0.0.1",
       "log_json": true,
       "log_level": "info",
       "log_rotate_max_files": 10,
       "log_rotate_duration": "24h",
       "log_file": "/data/consul/log/",
       "retry_join": [
           "[TSE Consul Node1 Address]",
           "[TSE Consul Node2 Address]",
           "[TSE Consul Node3 Address]"
       ]
      }
      ```
      > !
      >
      > Consul Agent 支持本地模式和局域网模式两种部署模式：
      >
      > - 本地模式：本地模式请指定 client_addr 为127.0.0.1，需要在每台 CVM 实例部署 Agent。
      > - 局域网模式：局域网模式请指定 client_addr 为0.0.0.0，只需指定几台 CVM 实例部署 Agent，部署后同一局域网内的 Agent 即可互相连通。
3. 进入 Consul 安装包所在的目录，执行如下命令解压 Consul 安装包。
   ```
   unzip consul_1.8.6_linux_amd64.zip
   ```
4. 执行如下命令启动 Consul Agent。
   ```
   ./consul agent --config-dir=/data/consul/config
   ```

   

## 步骤3：应用接入

1. 下载 Github 的 [Demo 源码](https://github.com/tencentyun/tse-simple-demo) 到本地并解压。
2. 打包 demo 源码成 jar 包。在`tse-simple-demo-main`源码根目录下，打开终端窗口，执行 `mvn clean package` 命令，对项目进行打包编译。编译成功后，可以在如下目录看到生成如下表所示的2个 Consul Jar 包。
<table>
<thead>
<tr>
<th align="left">软件包所在目录</th>
<th align="left">软件包名称</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">\tse-simple-demo-main\tse-consul-provider-demo\target</td>
<td align="left">tse-consul-provider-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务生产者</td>
</tr>
<tr>
<td align="left">\tse-simple-demo-main\tse-consul-consumer-demo\target</td>
<td align="left">tse-consul-consumer-demo-1.0-SNAPSHOT.jar</td>
<td align="left">服务消费者</td>
</tr>
</tbody></table>
3. 将编译好的 jar 包上传至云服务器，详细操作请参见 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
4. 登录云服务器，进入到刚刚上传 jar 文件所在的目录，可看到文件已上传到云服务器。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a58bdbed5957d0cf5aefcad362ec70ce.png)
5. 执行如下命令指定注册中心地址参数并运行该应用。
   > ? `[TSE Consul Client Agent IP]`为 [步骤2：准备配置](#step2) 中的 json 文件中的`client_addr`参数值。
   ```java
   nohup java -Dspring.cloud.consul.host=[TSE Consul Client Agent IP] -jar [jar包名称] &
   ```





## 步骤4：验证服务注册成功

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏选择 **consul**，单击目标实例的 ID，进入基本信息页面。
3. 在页面上方选择**服务管理**页签，出现如下页面代表服务注册成功。单击服务名称或者操作栏的**查看实例列表**可以查看服务的详细信息，如 ID、地址、端口等信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ca437e85cfe5c92c5a9e81990af9889e.png)
4. 登录云服务器，执行如下命令，调用 consumer 接口访问 provider 服务。
   ```curl
   curl http://localhost:18084/ping-provider/str
   ```
   返回结果如下：
   ![](https://qcloudimg.tencent-cloud.cn/raw/434f56a6eb04574b698fdc002596b3b6.png)
