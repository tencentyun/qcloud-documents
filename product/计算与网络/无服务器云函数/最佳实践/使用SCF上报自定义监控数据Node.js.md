## 操作背景
云函数（SCF）可帮助您在无需购买和管理服务器的情况下运行代码。SCF 的配套监控功能已覆盖自身的指标监控，例如函数被调用次数、错误次数、消耗内存等。
自定义监控可以帮助您监控业务逻辑，例如某个逻辑错误的次数、红包活动中用户发送红包的数量、领取红包的数量等。您可以直接在代码内打点上报业务指标，自动汇聚后实时生成监控图表，也可以针对上报指标配置告警，查看指标趋势变化。

本文介绍了如何使用 SCF 上报数据至自定义监控、查看指标及配置告警。

## 示例逻辑
生成一个随机数值，判断数值是否大于100：
 - 是，成功数 (nodejs_scf_suc_coun)+1。
 - 否，失败数 (nodejs_scf_fail_coun)+1。


##  前提条件
- 了解 [云函数](https://cloud.tencent.com/document/product/583)，或直接参考示例代码。
- 已具备一台设备用于构建项目及打包代码，且该设备已安装 Node.js 8.9。本文以操作系统为 CentOS 的 [腾讯云服务器](https://cloud.tencent.com/product/cvm) 为例。



##  操作步骤

### 步骤1：新建本地项目
1. [登录云服务器](https://cloud.tencent.com/document/product/213/5436)，执行以下命令进入 `/data` 目录。
```
cd /data
```
2. 执行以下命令，新建项目 `nodejsProject`。
```
mkdir nodejsProject
```


### 步骤2：编写业务逻辑
进入 `nodejsProject` 目录，新建 `index.js` 文件并写入以下内容：
```
const tencentcloud = require("./node_modules/tencentcloud-sdk-nodejs");

// 导入对应产品模块的client models。
const MonitorClient = tencentcloud.monitor.v20180724.Client;
const models = tencentcloud.monitor.v20180724.Models;

const Credential = tencentcloud.common.Credential;
//const FuncName = "default|scf_nodejs_monitor"

/**  
 * Main函数入口
 */
function main(){
    // 初始化自定义监控
    let client = init_monitor("yourSecretID", "yourSecretKey","ap-guangzhou")

    // 定义实例名,格式 "namespace|functionName"
    let funcName = "default|scf_nodejs_monitor"

    //生成随机数
    var Rand = Math.random();

    if( Rand > 100 ) {
        // 上报指标，指标名：nodejs_scf_suc_count
        API(client,funcName,"nodejs_scf_suc_count",1)
    } else {
        // 上报指标, 指标名: nodejs_scf_fail_count
      API(client,funcName,"nodejs_scf_fail_count",1)
    }
}

// 初始化自定义监控实例
function init_monitor(secretId,secretKey,region) {
	// 实例化一个证书对象，入参需要传入腾讯云账户secretId，secretKey
	 let cred = new Credential(secretId, secretKey, region);
	
	 // （必选项）定义上报机器所在地域,可用地域参考https://cloud.tencent.com/document/api/213/15692文档[地域列表]
	 let client = new MonitorClient(cred, region);
	
	 return client 
}

// 上报自定义监控指标
function API(client,funcName,name,value){	
    // 实例化一个请求对象
    let req = new models.PutMonitorDataRequest();

    // [可选项] 定义上报的scf函数名(规则: 命名规则|函数名 如default|scf_nodejs_monitor),如果不填，将使用请求到云网关接口机最后一跳的外网ip(可能是出口ip或者代理ip)
    req.AnnounceInstance = funcName;
    // [可选项] 定义上报的时间戳，如果不填，将使用服务器系统时间戳
    req.AnnounceTimestamp = (Date.parse(new Date()))/1000;
    // 定义上报指标MetriName和Value，Value必须是整型
    req.Metrics = [
         {"MetricName":name,"Value":value},
    ];

    // 通过client对象调用想要访问的接口，需要传入请求对象以及响应回调函数
    client.PutMonitorData(req, function(err, response) {
    // 请求异常返回，打印异常信息
    if (err) {
        console.log(err);
        return;
    }
    // 请求正常返回，打印response对象
     console.log(response.to_json_string());
    });
}


exports.main_handler = (event,context,callback) => {
    main()
}
```
>?请将示例代码中的 `yourSecretId`、`yourSecretKey` 分别替换为您实际使用账户的 SecretId 及 SecretKey，可前往 **[API密钥管理](https://console.cloud.tencent.com/cam/capi)** 获取。
>



### 步骤3：安装自定义监控 SDK
1. 在 `nodejsProject` 目录下，执行以下命令，将自定义监控的 SDK 以及相关依赖安装到项目目录中。
```
npm install tencentcloud-sdk-nodejs --save
```
2. 安装完成后，可在项目根目录执行以下命令查看文件。
```
ll
```
成功安装，则返回结果如下图所示：
![](https://main.qcloudimg.com/raw/20730a7b44055f70c359fb8a4f3b77fe.png)


### 步骤4：打包项目文件[](id:Step4)
1. 执行以下命令，将整个项目目录打包成 zip 文件。
```
zip newnodeproject.zip * -r
```
2. 将打包好的 `newnodeproject.zip` 下载文件到本地，便于后续将项目上传至云函数。

### 步骤5：上传项目压缩包至云函数
1. 登录 SCF 控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方，选择需上传函数的**地域**及**命名空间**，并单击**新建**。
3. 在“新建函数”页面的“基础信息”步骤中，根据以下信息创建函数，并单击**下一步**。如下图所示：
	- **函数名称**：输入自定义函数名，本文以 `nodejs_scf_monitor_Test` 为例。
	- **运行环境**：选择**Node.js 8.9**。
	- **创建方式**：选择**模板函数**，并选择 helloworld 模板。
![](https://main.qcloudimg.com/raw/cfd27141e0f0cfb105dd29079af3f085.png)
4. 在“函数配置”步骤中，保持默认设置并单击**完成**即可开始创建。
5. 在函数管理页面，选择**函数代码**页签，按照以下步骤上传代码。如下图所示：
![](https://main.qcloudimg.com/raw/b5f74a3d13fa93d094a9a52abe0842a8.png)
  1. 在“提交方法”中，选择**本地上传zip包**。
  2. 单击**上传**，并在弹出的目录中选择 [步骤4](#Step4) 中已准备好的 `newnodeproject.zip` 文件。
  3. 单击**保存**即可上传代码。
  上传成功后，界面自动展示 `index.js` 文件的代码内容。如下图所示：
![](https://main.qcloudimg.com/raw/72e5320b1b8796bc4835a1b85176ad53.png)
  4. 再次单击**保存**，完成项目代码上传。



### 步骤6：触发调试
在**函数代码**页签中，单击界面下方的**测试**，“当前测试模板”使用默认**Hello World事件模板**测试即可。
返回结果如下，则表示监控数据上报成功：
![](https://main.qcloudimg.com/raw/16b4d049cfcb5869fe1d406bc2c35b34.png)

### 步骤7：查看监控视图
进入 [自定义监控](https://console.cloud.tencent.com/monitor/indicator-view) 查看已触发上报的指标视图。如下图所示：
![](https://main.qcloudimg.com/raw/3bd4bb80c9644ce06a8b7ef9bddcd4c2.png)
### 步骤8：配置告警
您可参考 [配置告警策略](https://cloud.tencent.com/document/product/397/40223) 为函数配置告警。



