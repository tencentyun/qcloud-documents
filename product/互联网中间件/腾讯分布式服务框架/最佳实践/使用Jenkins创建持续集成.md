TSF 应用可以使用 Jenkins 构建持续集成方案。

## 准备工作

在开始持续集成之前，需要完成下述的准备工作。
1. 参考 [使用 Python 脚本部署应用](https://cloud.tencent.com/document/product/649/40407) 获取部署脚本及使用方法的说明。
2. 安装 [Jenkins](https://jenkins.io) ，确保 Jenkins 安装机器上的 Python 不低于2.7.14版本，并已安装 PIP 等 Python 包管理工具。
3. 在 TSF 平台创建了 [虚拟机应用部署组](https://cloud.tencent.com/document/product/649/15524) 或 [容器应用部署组](https://cloud.tencent.com/document/product/649/15525)。

## 安装和配置 Jenkins
1. 在 [Jenkins 官网](https://jenkins.io) 下载安装 Jenkins。  
2. 安装 Maven 并配置 TSF 私服地址，详情请参见 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)。  
3. 在 Jenkins 控制台的菜单栏中，选择【系统管理】>【插件管理】，安装 Maven Integration plugin 插件（已安装请忽略）。
4. 创建 Jenkins 项目  
   4.1 在 Jenkins 首页左侧导航栏中单击【新建】，创建 Jenkins 任务，并选择构建一个自由风格的软件项目。
   ![create jenkins item](https://main.qcloudimg.com/raw/2458ba567a47968634de459fbdbed5a0/create-jenkins-item.png)
   4.2 在源码管理页面中选择 Git，并设置相关参数。
   Repository URL：您的项目的 Git 协议地址。
   Credentials：安全凭证，选择“无”（前提是运行 Jenkins 软件的用户的 SSH RSA 公匙已添加到该 Git 项目所在的 GitLab 或 GitHub 中，否则这里会报错）或者添加用户名密码。
   ![git info](https://main.qcloudimg.com/raw/a3d8d5ab5062a00fd47394e753f89eb1/add_git_url.png)
   ![add username](https://main.qcloudimg.com/raw/3b129735c76cdae1799c17625ed2324e/add_username.png)
   4.3 单击【构建触发器】页签，勾选【Build when a change is pushed to GitLab】。 GitLab webhook URL 中的 IP 要确保能通过 GitLab 访问。
   ![GitLab hook](https://main.qcloudimg.com/raw/9d572d105e3180dea218047dc2e3246d/add_gitlib_hook.png)
   4.4 单击【构建环境】页签，勾选【Add timestamps to the Console Output】，为控制台输出的信息添加时间戳。  
   ![add timestamps](https://main.qcloudimg.com/raw/dec56acb45abcd738117cbde1c7c895b/add_timestamps.png)
   4.5 单击【构建】页签，然后单击【增加构建步骤】，选择【Invoke top-level Maven targets】。
   ![maven targets](https://main.qcloudimg.com/raw/ac6fb1792129776c6ee1da0c84cc611c/invoke%20maven.png)
   目标：填入 clean package （如有其它参数，请根据实际情况填入）
   ![mvn terminal](https://main.qcloudimg.com/raw/e36f220c63547f447a6f97f9e20d65cb/maven_clean.png)
   4.6 单击构建页签，然后单击增加构建步骤，选择 Execute shell
   ![shell](https://main.qcloudimg.com/raw/34b0000efa8263ffdff1d861ec9b1e2a/execute_shell.png)
   命令中填入 [应用部署准备](#)  步骤中准备好的 Shell 命令  
   i. 虚拟机如下：
   ```shell
   python2.7.14 upload_virtual_machine_deploy.py ./consumer-demo/target/consumer-demo-1.10.0-RELEASE.jar application-qab76pxv v001 1300555551 group-gvk5pbdv '-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m'
   ```
   ![python script](https://main.qcloudimg.com/raw/6e25c6ad39621bb8dd81c236f2c35414/python_shell.png)

   ii.容器如下
   ```shell
   python2.7.14 upload_container_deploy.py group-zvw397wa v1
   ```
   ![containe shell](https://main.qcloudimg.com/raw/97d493bf4da1294d290fabec900f9f3d/container_shell.png)
   4.7 配置 GitLab 所需权限  
   i. 管理Jenkins > Configure Global Security 勾选 匿名用户具有可读权限
   ![add read permission](https://main.qcloudimg.com/raw/2bb34492e613e93c3c52b2109e544af1/add_read_permission.png)
   取消防止跨站点请求伪造
   ![cancel cors](https://main.qcloudimg.com/raw/78a30356bc82b9da355db90c06b0da53/cancel_cors.png)
   ii. 管理Jenkins > 系统配置 取消 Enable authentication for '/project' end-point
   ![cancel end point](https://main.qcloudimg.com/raw/aa898eedb091735372c530e795f01187/cancel_endpoint.png)

5. 配置 GitLab 的 Web Hook，实现自动构建  
   5.1 项目 > Settings > Integrations 进入添加webhook界面
   ![gitlib add webhook](https://main.qcloudimg.com/raw/bfbe6dd37c4c7fe109ab8bb913279c4e/gitlib_add_webhook.png)
   5.2 将 4.3 中Jenkins产生的GitLab webhook URL填入URL，其他选项使用默认设置，点击"Add webhook"。
   ![gitlib add jenkens url](https://main.qcloudimg.com/raw/59c4bf4c29f8844a745fd531b2df7050/gitlib_add_jenkens_url.png)
   5.3 测试 WebHook
   ![test webhook](https://main.qcloudimg.com/raw/bef07b027653b2ee74af88b186a2cdab/test_webhook.png)
   成功如图
   ![hook execute success](https://main.qcloudimg.com/raw/bc5b88f98b2989ddef980d0e39f4b1d8/hook_execute_success.png)
   如出现 403 异常，请检查 4.7 配置。
   ![test webhook error](https://main.qcloudimg.com/raw/91f6bf83a0c629f6482f0d2a785a7a4f/test_webhook_error.png)
配置正确后，进行下一步操作（提交变更到  GitLab）

## 提交变更到 GitLab
如果上述步骤配置正确，这次提交会触发一次 GitLab Hook。 Jenkins 在接受到这个 Hook 后会构建您的 Maven 项目，并在构建过程中触发 Python 脚本自动部署 TSF 应用。
1. 虚拟机提交部署成功输出的日志信息（Build Number > 控制台输出）。
    ```Shell
    15:12:40 + python2.7.14 upload_virtual_machine_deploy.py ./consumer-demo/target/consumer-demo-1.10.0-RELEASE.jar application-qab76pxv v001 1300555551 group-gvk5pbdv '-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m'
    15:12:41 POST
    15:12:41 /
    15:12:41 
    15:12:41 content-type:application/json
    15:12:41 host:tsf.tencentcloudapi.com
    15:12:41 
    15:12:41 content-type;host
    15:12:41 0c2f4a50b1dc4df621a84d1731ec07cbd756ac04b1f4853fa792c5dbcf104f28
    15:12:41 TC3-HMAC-SHA256
    15:12:41 1576739561
    15:12:41 2019-12-19/tsf/tc3_request
    15:12:41 46cdc18f96456edef21e4b01e787030d62ce54bb7b300994fed4d5d473709701
    15:12:41 1d501d695675696fef1c2b2576bb21f42f6f31f55f07c7b27c5ca051d20f242e
    15:12:41 TC3-HMAC-SHA256 Credential=AKIDXXXXXXXXXXXXX2rwsp/2019-12-19/tsf/tc3_request, SignedHeaders=content-type;host, Signature=1d501d695675696fef1c2b2576bb21f42f6f31f55f07c7b27c5ca051d20f242e
    15:12:41 {"Response":{"RequestId":"0b6aa4ee-38fe-4782-97e4-be1061e7cdb1", "Result":{"Content":[{"PkgId":"pkg-f51038e0","PkgName":"consumer-demo-1.10.0-RELEASE.jar","PkgType":"fatjar","PkgVersion":"v001","PkgDesc":"","UploadTime":"2019-12-18 11:03:26","Md5":"4ad6fabc1234567896e1d","PkgPubStatus":1}],"TotalCount":1}}}
    15:12:41 [INFO] application-qab76pxv has uploaded version v001, no need upload
    15:12:41 POST
    15:12:41 /
    15:12:41 
    15:12:41 content-type:application/json
    15:12:41 host:tsf.tencentcloudapi.com
    15:12:41 
    15:12:41 content-type;host
    15:12:41 99f3e6ddeaf00f7b64315835fdd6f29d7a0a5520743184c21a43d8a609d6891a
    15:12:41 TC3-HMAC-SHA256
    15:12:41 1576739561
    15:12:41 2019-12-19/tsf/tc3_request
    15:12:41 e5ebc373c1c432910ca0110e48f1fe4cf29ffcdedc21dc79dd59a99bf802ea23
    15:12:41 73e21ed01f4ad54668e94a2839d6de17c07e6188e1ff9e176452b80fb776be15
    15:12:41 TC3-HMAC-SHA256 Credential=AKIDXXXXXXXXXXXXX2rwsp/2019-12-19/tsf/tc3_request, SignedHeaders=content-type;host, Signature=73e21ed01f4ad54668e94a2839d6de17c07e6188e1ff9e176452b80fb776be15
    15:12:41 200
    15:12:41 {"Response":{"RequestId":"86c93d7e-ee44-4c8d-8d34-537a0dbe6871","Result":{"TaskId":"task-76l2v6m7"}}}
    15:12:41 Finished: SUCCESS
    ```
您可以在【[TSF 控制台](https://console.cloud.tencent.com/tsf?rid=1)】>【应用管理】中，单击目标应用的 ID，进入应用详情页的【变更记录】中，查看虚拟机部署变更记录。
 ![](https://main.qcloudimg.com/raw/78e281d72a81387fa51e990b0216c0a2.png)

2. 容器部署成功日志信息
    ```Shell
    16:32:28 + python2.7.14 upload_container_deploy.py group-zvw397wa v1
    16:32:31 {"Result": {"InstanceNum": 1, "NamespaceName": "zsf-test-jenkins-docker_default", "ApplicationType": "C", "CurrentNum": 1, "MicroserviceType": "N", "Status": "Running", "LbIp": "", "MemRequest": "128", "ClusterId": "cls-52tydz2q", "UpdateIvl": 0, "Envs": [{"Name": "tsf_consul_ip", "Value": "169.254.0.77"}, {"Name": "tsf_consul_port", "Value": "8000"}, {"Name": "PATH", "Value": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}, {"Name": "workdir", "Value": "/app/"}, {"Name": "jar", "Value": "consumer-demo-1.10.0-RELEASE.jar"}, {"Name": "tsf_app_id", "Value": "1300555551"}, {"Name": "tsf_token", "Value": "VjCCe9gixVmdeBfTpM74PikHFfU8ZmZVL7Z4FMGvXjI="}, {"Name": "tsf_application_id", "Value": "application-byx3zwdy"}, {"Name": "tsf_cluster_id", "Value": "cls-52tydz2q"}, {"Name": "tsf_namespace_id", "Value": "namespace-py5e9zjy"}, {"Name": "tsf_group_id", "Value": "group-zvw397wa"}, {"Name": "tsf_prog_version", "Value": "v1"}, {"Name": "tsf_region", "Value": "ap-guangzhou"}, {"Name": "tsf_ratelimit_master_ip", "Value": "169.254.0.77"}, {"Name": "tsf_ratelimit_master_port", "Value": "7000"}], "TagName": "v1", "ClusterIp": "172.18.255.122", "MemLimit": "256.00", "CpuLimit": "0.50", "ApplicationId": "application-byx3zwdy", "ApplicationName": "zsf-tsf-docker", "ProtocolPorts": [{"Protocol": "TCP", "TargetPort": 80, "Port": 80}], "UpdateType": 0, "Server": "ccr.ccs.tencentyun.com", "GroupName": "zsf-test-docker-consumer", "NodePort": 30215, "AccessType": 2, "ClusterName": "zsf-test-jenkins-docker", "NamespaceId": "namespace-py5e9zjy", "Reponame": "tsf_100011913960/zsf-tsf-docker", "CpuRequest": "0.25", "Message": "", "CreateTime": "2019-12-17 15:09:08", "GroupId": "group-zvw397wa"}, "RequestId": "aff9a2b6-24f5-44b1-8173-112a6a24b581"}
    16:32:31 {"Result": true, "RequestId": "263c8a64-1bb1-427e-80e2-870aa0bc7d68"}
    16:32:31 Finished: SUCCESS
    ```

您可以在【[TSF 控制台](https://console.cloud.tencent.com/tsf?rid=1)】>【应用管理】中，单击目标应用的 ID，进入应用详情页的【变更记录】中，查看容器部署变更记录。
		![](https://main.qcloudimg.com/raw/94af219b1278ae8a104bd444d6c81fde.png)
		
3. 容器部署成功日志信息 如果部署失败，需要分析 Jenkins console 日志。

