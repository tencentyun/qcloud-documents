## 使用背景
在腾讯云托管集群中运行容器化的工作负载时，通常需要访问存储在 Kubernetes 集群之外的一个或多个 SQL 或 NoSQL 数据库，但是将 SQL 数据库与 Kubernetes 一起使用时，存在定期轮换凭证和敏感信息传递到 Kubernetes 集群中的问题。为此，借助凭据管理系统（SSM）和腾讯云访问控制管理（CAM）来简化访问腾讯云数据库的整个过程，从而消除验证腾讯云数据库用户名和密钥存在的安全风险；同时凭据管理系统（SSM）定时轮转访问凭证的特性，间接解决人为操作所带来的负担。
本文向您介绍运行在腾讯云容器服务 TKE 上的工作负载如何使用 CAM 对数据库身份验证。在示例中，首先在腾讯云数据库和凭据管理系统（SSM）中分别创建一个数据库实例和数据库凭据；然后开启 OIDC 资源访问控制能力，将创建的 CAM OIDC 提供商作为创建角色的载体，并关联访问腾讯云数据库和凭据管理系统（SSM）的策略；最后利用 Kubernetes 服务账户、腾讯云访问控制管理（CAM）以及凭据管理系统（SSM）安全地连接到腾讯云数据库。整体架构如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/feb126cc18c32af2c85ff759edfba750.png)

## 限制条件

本示例中，假定您已完成以下限制条件：
- 该功能仅支持 TKE 托管集群。
- 集群版本 >= v1.20.6-tke.27/v1.22.5-tke.1

## 操作步骤


### 步骤1：准备托管集群
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)，新建集群。
<dx-alert infotype="explain" title="">
- 如果您没有托管集群，您可以使用容器服务控制台创建 TKE 标准集群，详情见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。
- 如果您已有托管集群，请在集群详情页检查集群版本，当集群版本不满足要求时，请升级集群。对运行中的 Kubernetes 集群进行升级，详情见 [升级集群](https://cloud.tencent.com/document/product/457/32192)。
</dx-alert>
2. 执行如下命令，确保您可以通过 kubectl 客户端访问托管集群。
```shell
kubectl get node 
```
返回如下结果，则说明可正常访问集群。
```shell
kubectl get node 
NAME         STATUS   ROLES    AGE   VERSION
10.0.4.144   Ready    <none>   24h   v1.22.5-tke.1
```
<dx-alert infotype="explain" title="">
您可以通过 Kubernetes 命令行工具 Kubectl 从本地客户端机器连接到 TKE 集群。详情见 [连接集群](https://cloud.tencent.com/document/product/457/32191)。
</dx-alert>

### 步骤2：开启 OIDC 资源访问控制能力
1. 在集群详情页中，单击 ServiceAccountIssuerDiscovery 右侧的![](https://qcloudimg.tencent-cloud.cn/raw/e407b743109f1c0de2b793e7f06a451f.png)。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/910d3b4c26e088cfdc4b4c375ab2c811.png)
2. 进入“修改 ServicAccountIssuerDiscovery 相关参数”页面，若系统提示您无法修改相关参数，请先进行服务授权。
![](https://qcloudimg.tencent-cloud.cn/raw/f5d8e337938a9da3ae9a98d7302108c3.png)
在角色管理页面，查看授权策略 QcloudAccessForTKERoleInOIDCConfig，单击**同意授权**。
![](https://qcloudimg.tencent-cloud.cn/raw/11835ce347ea41478d70ce6cd859e727.png)
3. 授权完毕后，勾选“创建 CAM OIDC 提供商”和“新建 WEBHOOK 组件”，并填写客户端 ID，单击**确定**。如下图所示：
<dx-alert infotype="explain" title="">
**客户端 ID** 是选填参数，当不填写时，默认值是 "sts.cloud.tencent.com"，本文示例中创建 CAM OIDC 提供商采用默认值。
</dx-alert>

 ![](https://qcloudimg.tencent-cloud.cn/raw/b1733eff123180ac2353d87dd605cb9c.png)
4. 返回集群详情页，当 ServiceAccountIssuerDiscovery 可再次编辑时，表明本次开启 OIDC 资源访问控制结束。
<dx-alert infotype="notice" title="">
"service-account-issuer" 和 "service-account-jwks-uri" 参数值不允许编辑，默认配置规则如下：
1. 不开启公网和内网时，遵循当前默认参数值。本文示例中采用该方式。
2. 仅开启公网：
		- 域名方式开启公网，默认填写公网域名。
		- IP 方式开启公网，默认填写域名公网 IP。
3. 仅开启内网：
		- 域名方式开启内网，默认填写内网域名。
		- IP 方式开启内网，默认填写域名内网 IP。
4. 同时开启内网和公网时，遵循“仅开启公网”规则。
</dx-alert>


### 步骤3：检查 CAM OIDC 提供商和 WEBHOOK 组件是否创建成功

1. 在集群详情页中，单击 ServiceAccountIssuerDiscovery 右侧的![](https://qcloudimg.tencent-cloud.cn/raw/e407b743109f1c0de2b793e7f06a451f.png)。  
2. 进入“修改 ServicAccountIssuerDiscovery 相关参数”页面，系统将提示“您创建的身份提供商已存在，前往查看”。单击**前往查看**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2a4f505fdde83ab994b9769589b03743.png)
3. 查看您刚创建的 CAM OIDC 提供商详细信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cdfae752609ffd6a7070504b65cec6bf.png)
4. 在**集群信息 > 组件管理**中，如在列表看到 pod-identity-webhook 组件状态是“成功”，即表示安装组件成功。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9da267f53621ddb392c2f77ad75383d6.png)
您也可以执行查看命令，以 "pod-identity-webhook" 作为前缀的 Pod 状态是 Running，即表示安装组件成功。
```shell
 kubectl get pod -n kube-system 
 NAMESPACE     NAME                                    READY   STATUS    RESTARTS   AGE
 kube-system   pod-identity-webhook-78c76****-9qrpj   1/1     Running   0          43h
```
   
[](id:pn)	 
### 步骤4：确认数据库实例
您需要确认是否存在腾讯云数据库实例，若没有腾讯云数据库实例，请您先行创建，并在数据库实例中创建数据库。若已有腾讯云数据库实例，请您跳过数据库创建。
本示例采用腾讯云 MySQL 实例，同时开启 MySQL 实例公网。创建步骤请参考 [创建 MySQL 实例](  https://cloud.tencent.com/document/product/236/46433)。
![](https://qcloudimg.tencent-cloud.cn/raw/89acce1082b2ba97ad0ea1fa88645dd2.png)
>! 
- **外网地址**的 value 值标识为`$db_address`。
- **端口**的 value 值标识为`$db_port`。
>

[](id:sg)
### 步骤5：更新数据库安全组
   
托管集群上的 Pod 想要被允许访问腾讯云 MySQL 数据库，需要给腾讯云 MySQL 数据库的安全组添加一些规则。在数据库实例的安全组页面中，修改安全组规则。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7c6202bbf77143384d930f7cfd7917af.png)

为了给 Kubernetes Pod 创建入站规则，您需要单击**安全组 ID**后跳转到安全组实例页面。在安全组实例详情页，选择**安全组规则 > 入站规则 > 添加规则**。在“添加入站规则”弹窗中，进行入站规则的创建。本示例中使用**来源**为`0.0.0.0/0`，**协议端口**为 `TCP:3306`。
![](https://qcloudimg.tencent-cloud.cn/raw/b4619e36b8d445d51206a2ddc473139e.png)
 
### 步骤6：测试数据库连接性
   
在安装 MySQL 客户端的实例中，确认您使用用户名 root 和您在创建数据库设置的密码连接到数据库。如果无法连接到数据库，请返回查看是否开启 [公网](#pn) 及是否正确配置 [安全组](#sg)。
```shell
mysql -h $db_address  -P $db_port -uroot -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 4238098
Server version: 5.7.36-txsql-log 20211230

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]>
```

### 步骤7：创建数据库、表、数据

为了对数据库连通性和操作权限进行验证，请您先创建个人数据库。
```shell
MySQL [(none)]> CREATE DATABASE mydb;
Query OK, 1 row affected (0.00 sec)

MySQL [(none)]> CREATE TABLE mydb.user (Id VARCHAR(120), Name VARCHAR(120));
Query OK, 0 rows affected (0.00 sec)

MySQL [(none)]> INSERT INTO mydb.user (Id,Name) VALUES ('123','tke-oidc');
Query OK, 1 row affected (0.01 sec)

MySQL [(none)]> SELECT * FROM mydb.user;
+------+----------+
| Id   | Name     |
+------+----------+
| 123  | tke-oidc |
+------+----------+
1 row in set (0.01 sec)
```
创建完成后，在控制台查看已创建的数据库。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/46a45493a42c65bd76f2d53ee39d756c.png)

<dx-alert infotype="notice" title="">
**数据库名**的 value 值标识为`$db_name`。
</dx-alert>


[](id:ssm)
### 步骤8：在凭据管理系统中创建数据库凭据实例
请您检查是否存在数据库凭据。如果不存在数据库凭据，请您在凭据管理系统控制台中创建数据库凭据，开启凭据轮转及选择加密，降低账号的泄露风险与安全威胁。在本文示例中，将创建两个数据库凭证，两者的区别是是否具备对数据库的 select 权限，为了增强可读性，通过**描述** value 值加以区分。
 
1. 登录 [凭据管理系统控制台](https://console.cloud.tencent.com/ssm)。
2. 在“新建凭据”页面，参考如下信息进行数据库账号设置。字段详情可参考 [创建数据库凭据](https://cloud.tencent.com/document/product/1140/57648)。
![](https://qcloudimg.tencent-cloud.cn/raw/e4ff04b8bb08c0d1cde35e3894cb31b3.png)
	- **关联的实例**：选择新建数据库实例或者已存在数据库实例。
	- **主机**：是指客户端 IP，不指定时填写`%`。
	- **权限配置**：根据对数据库实例的操作需求进行授权。
 <dx-tabs>
::: 创建第一个数据库凭证
单击**授权**，在“权限配置”页面，勾选如下权限：
![](https://qcloudimg.tencent-cloud.cn/raw/33e163d8764eac0ee29690d6c56a6b44.png)
:::
::: 创建第二个数据库凭证
单击**授权**，在“权限配置”页面，勾选**全部**权限，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0ff50a143b9ededc96f40fcb7b543f19.png)
:::
</dx-tabs>
>! 
>- **凭据名称**的 value 值标识为`$ssm_name`
>- **凭据所在地域**标识为`$ssm_region_name`
>
3. 单击**创建**。在凭据列表页面查看已创建的凭据，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7c6cf51e0bb7a9418b0be4398b5e850d.png)

 

 
### 步骤9：创建 CAM 角色并关联访问腾讯云数据库和凭据管理系统的策略
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/role)。
2. 在角色页中，单击**新建角色 > 身份提供商**。
3. 在“新建自定义角色”页，参考以下信息进行设置。
![](https://qcloudimg.tencent-cloud.cn/raw/a216a43e17a7156d4fe6f5343f5c37f5.png)
>! 
>- **odic:aud** 的 value 值需要和 CAM OIDC 提供商的**客户端 ID** value 值保持一致。
>- **odic:aud** 的 value 值标识为`$my_pod_audience`，当**odic:aud**的 value 值有多个时，任选其中之一即可。
>
![](https://qcloudimg.tencent-cloud.cn/raw/683b300cb8d663bd903151304ed532d4.png)
>! 根据您自身业务需求，选择或创建自定义的策略进行关联。本示例中在搜索框中搜索 QcloudSSMReadOnlyAccess 和 QcloudCDBReadOnlyAccess 进行与角色关联。
>
![](https://qcloudimg.tencent-cloud.cn/raw/0a419ec1c8fde2edf4be8d54ca44dc61.png)
>! **RoleArn**的 value 值标识为`$my_pod_role_arn`。
>
 
 
[](id:demo)
### 步骤10：部署示例应用程序
1. 创建一个 Kubernetes 命名空间来部署资源。
```shell
kubectl create namespace my-namespace
```
2. 将以下内容保存到 **my-serviceaccount.yaml** 中。将`$my_pod_role_arn`替换为 RoleArn 的 value 值，将`$my_pod_audience`替换为 odic:aud 的 value 值。
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-serviceaccount
  namespace: my-namespace
  annotations:
    tke.cloud.tencent.com/role-arn: $my_pod_role_arn
    tke.cloud.tencent.com/audience: $my_pod_audience
    tke.cloud.tencent.com/token-expiration: "86400"
```
3. 将以下内容保存到**sample-application.yaml**中。
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: my-namespace
spec:
  selector:
    matchLabels:
      app: my-app
  replicas: 1
  template:
    metadata:
    labels:
      app: my-app
    spec:
      serviceAccountName: my-serviceaccount
      containers:
        - name: nginx
          image: $image
          ports:
            - containerPort: 80
```
需注意，在本示例中，`$image`选择`ccr.ccs.tencentyun.com/tkeimages/sample-application:latest`，该镜像集成了编译的 [demo文件](#file)，方便进行示例演示。您可以根据自身业务进行填写。
4. 部署示例。
```shell
kubectl apply -f my-serviceaccount.yaml
kubectl apply -f sample-application.yaml
```
5. 查看使用示例应用程序部署的 Pod。
```shell
kubectl get pods -n my-namespace
```
示例输出如下：
```shell
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-6bfd845f47-9zxld   1/1     Running   0          67s
```
6. 查看工作负载环境变量信息。
```shell
kubectl describe pod nginx-deployment-6bfd845f47-9zxld -n my-namespace 
```
示例输出如下：
![](https://qcloudimg.tencent-cloud.cn/raw/cb71c455f7a1e680ee8677a0d1fc3c79.png)

>! 环境变量 TKE_REGION/TKE_PROVIDER_ID/TKE_ROLE_ARN/TKE_WEB_IDENTITY_TOKEN_FILE 作为 AssumeRoleWithWebIdentity 接口参数。
>

### 步骤11：访问数据库 demo 伪代码实现
1. 确认子账号所有访问 AssumeRoleWithWebIdentity 接口的权限。如果没有权限请联系管理员添加，添加完毕后，您可以通过 curl 方式检查是否可以换取临时密钥，详情见 [申请OIDC角色临时密钥](https://cloud.tencent.com/document/product/1312/73070)。
2. 将 AssumeRoleWithWebIdentity 接口 SecretId /SecretKey/Token 作为访问 DB+SSM 的参数，详情见 [数据库凭据的应用]( https://cloud.tencent.com/document/product/1140/59166)。
3. 克隆 ssm-rotation-sdk-golang 代码。
```shell
shell git clone https://github.com/TencentCloud/ssm-rotation-sdk-golang.git
```
4. [](id:file) 替换 demo 中伪代码实现：
```
      package main

      import (
         "flag"
         "fmt"
         _ "github.com/go-sql-driver/mysql"
         "github.com/tencentcloud/ssm-rotation-sdk-golang/lib/db"
         "github.com/tencentcloud/ssm-rotation-sdk-golang/lib/ssm"
         "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
         "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
         sts "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sts/v20180813"
         "io/ioutil"
         "log"
         "os"
         "sync"
         "time"
      )

      var (
         roleArn, tokenPath, providerId, regionName, saToken string
         secretName, dbAddress, dbName, ssmRegionName        string
         dbPort                                              uint64
         dbConn                                              *db.DynamicSecretRotationDb
         Header                                              = map[string]string{
             "Authorization":      "SKIP",
             "X-TC-Action":        "AssumeRoleWithWebIdentity",
             "Host":               "sts.internal.tencentcloudapi.com",
             "X-TC-RequestClient": "PHP_SDK",
             "X-TC-Version":       "2018-08-13",
             "X-TC-Region":        regionName,
             "X-TC-Timestamp":     "1659944952",
             "Content-type":       "application/json",
         }
      )

      type Credentials struct {
         TmpSecretId  string
         TmpSecretKey string
         Token        string
         ExpiredTime  uint64
      }

      func getEnv() error {
         roleArn = os.Getenv("TKE_ROLE_ARN")
         tokenPath = os.Getenv("TKE_WEB_IDENTITY_TOKEN_FILE")
         providerId = os.Getenv("TKE_PROVIDER_ID")
         regionName = os.Getenv("TKE_REGION")
         fmt.Println("TKE_IDENTITY_TOKEN_FILE is:", tokenPath)
         data, err := ioutil.ReadFile(tokenPath)
         if err != nil {
             fmt.Printf("file path:%s,reading error:%s", tokenPath, err)
             return err
         }
         saToken = string(data)
         return nil
      }

      func main() {
         flag.StringVar(&secretName, "ssmName", "", "ssm名称")
         flag.StringVar(&ssmRegionName, "ssmRegionName", "", "ssm地域")
         flag.StringVar(&dbAddress, "dbAddress", "", "数据库地址")
         flag.StringVar(&dbName, "dbName", "", "数据库名称")
         flag.Uint64Var(&dbPort, "dbPort", 0, "数据库端口")
         flag.Parse()

         if err := getEnv(); err != nil {
             log.Fatal("failed to get env, err:", err)
         }
         cred := common.NewCredential("", "")
         cpf := profile.NewClientProfile()
         cpf.HttpProfile.Endpoint = "sts.internal.tencentcloudapi.com"
         cpf.SignMethod = ""
         stsClient, _ := sts.NewClient(cred, regionName, cpf)

         assumeReq := sts.NewAssumeRoleWithWebIdentityRequest()
         assumeReq.SetSkipSign(true)
         assumeReq.BaseRequest.SetHeader(Header)
         assumeReq.ProviderId = common.StringPtr(providerId)
         assumeReq.WebIdentityToken = common.StringPtr(saToken)
         assumeReq.RoleArn = common.StringPtr(roleArn)
         assumeReq.RoleSessionName = common.StringPtr("tke-oidc-test")
         assumeReq.DurationSeconds = common.Int64Ptr(int64(5000))

         assumeResp, err := stsClient.AssumeRoleWithWebIdentity(assumeReq)
         if err != nil {
             log.Fatal("failed to assume role with web identity, err:", err)
         }
         var sys sync.RWMutex
         var credential Credentials
         if assumeResp.Response != nil && assumeResp.Response.Credentials != nil {
             sys.Lock()
             defer sys.Unlock()
             credential = Credentials{
                 TmpSecretId:  *assumeResp.Response.Credentials.TmpSecretId,
                 TmpSecretKey: *assumeResp.Response.Credentials.TmpSecretKey,
                 Token:        *assumeResp.Response.Credentials.Token,
                 ExpiredTime:  *assumeResp.Response.ExpiredTime,
             }
         }
         log.Printf("secretId:%v,secretey%v,token%v\n", credential.TmpSecretId, credential.TmpSecretKey, credential.Token)
         DB(credential)
      }

      func DB(credential Credentials) {
         // 初始化数据库连接
         dbConn = &db.DynamicSecretRotationDb{}
         err := dbConn.Init(&db.Config{
             DbConfig: &db.DbConfig{
                 MaxOpenConns:        100,
                 MaxIdleConns:        50,
                 IdleTimeoutSeconds:  100,
                 ReadTimeoutSeconds:  5,
                 WriteTimeoutSeconds: 5,
                 SecretName:          secretName, // 凭据名
                 IpAddress:           dbAddress,  // 数据库地址
                 Port:                dbPort,     // 数据库端口
                 DbName:              dbName,     // 可以为空，或指定具体的数据库名
                 ParamStr:            "charset=utf8&loc=Local",
             },
             SsmServiceConfig: &ssm.SsmAccount{
                 SecretId:  credential.TmpSecretId,  // 需填写实际可用的SecretId
                 SecretKey: credential.TmpSecretKey, // 需填写实际可用的SecretKey
                 Token:     credential.Token,
                 Region:    ssmRegionName, // 选择凭据所存储的地域
             },
             WatchChangeInterval: time.Second * 10, // 多长时间检查一下 凭据是否发生了轮转
         })
         if err != nil {
             fmt.Errorf("failed to init dbConn, err:%v\n", err)
             return
         }
         // 模拟业务处理中，每过一段时间（一般是几毫秒），需要拿到db连接，来操作数据库的场景
         t := time.Tick(time.Second)
         for {
             select {
             case <-t:
                 accessDb()
                 queryDb()
             }
         }
      }

      func accessDb() {
         fmt.Println("--- accessDb start")
         c := dbConn.GetConn()
         if err := c.Ping(); err != nil {
             log.Fatal("failed to access db with err:", err)
         }
         log.Println("--- succeed to access db")
      }

      func queryDb() {
         var (
             id   int
             name string
         )
         log.Println("--- queryDb start")
         c := dbConn.GetConn()
         rows, err := c.Query("select id, name from user where id = ?", 1)
         if err != nil {
             log.Printf("failed to query db with err: ", err)
             log.Fatal(err)
         }
         defer rows.Close()
         for rows.Next() {
             err := rows.Scan(&id, &name)
             if err != nil {
                 log.Fatal(err)
             }
             log.Println(id, name)
         }
         err = rows.Err()
         if err != nil {
             log.Fatal(err)
         }
         log.Println("--- succeed to query db")
      }     
```





### 步骤12：测试 demo 示例

基于 [部署示例](#demo) 的部署结果，进入到 nginx 容器：
```shell
kubectl exec -ti  nginx-deployment-6bfd845f47-9zxld   -n my-namespace  -- /bin/bash
cd /root/
```
将 **$ssm_name** 和 **$ssm_region_name** 标识参照 [SSM实例](#ssm) 进行替换，将 **$db_address**、**$db_name**和**$db_port** 标识参照 [数据库实例](#pn) 进行替换。
```shell
./demo  --ssmName=$ssm_name --ssmRegionName=$ssm_region_name --dbAddress=$db_address --dbName=$db_name --dbPort=$db_port 
```
在本示例中，当 $ssm_name=tke-oidc-1 时，没有数据库的 select 权限。
![](https://qcloudimg.tencent-cloud.cn/raw/7bd3b6f9fb224b73f7babb195d3a30eb.png)
在本示例中，当 $ssm_name=tke-oidc-2 时，有数据库的 select 权限。
![](https://qcloudimg.tencent-cloud.cn/raw/fe385244b42a52dd0d275942cb1f139c.png)

### 测试结论
    
测试表明满足预期的效果。通过 CAM 对托管集群工作负载短暂的身份验证令牌的验证，确保了身份验证的安全性；另外借助凭据管理系统对数据库用户名和密码的轮转和加密特性，使得您不必担心数据库凭据的存储和生命周期问题，这样您在托管集群连接到数据库时无需使用用户名和密码。
