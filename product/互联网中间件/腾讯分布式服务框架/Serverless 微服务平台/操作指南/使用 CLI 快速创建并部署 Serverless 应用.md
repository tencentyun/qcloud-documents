## 操作场景
本文指导您使用 CLI 工具创建并部署 Serverless 应用。

## 前提条件
完成本教程中的步骤需要完成以下前提任务：
1. [安装并配置 TCCLI](https://cloud.tencent.com/document/product/440/39027)
2. [安装 COSCMD](https://cloud.tencent.com/document/product/436/10976)
3. 执行脚本的环境需包含以下命令和工具：md5sum、date、awk

>?
- 在安装 TCCLI 工具时，**需要预先 [配置密钥和地域相关的用户信息](https://cloud.tencent.com/document/product/440/34012)**。
- 在安装 COSCMD 时，**无需配置 COS 的相关信息**。下述操作步骤的脚本会自动完成对 COSCMD 的配置。


## 操作步骤
以下是一个基于 TCCLI 和 COSCMD 通过脚本完成应用创建和自动部署（Continuous Deployment）的示例，您可以按照实际需要对脚本进行调整。
### 1. 使用 CLI 快速创建 Serverless 应用
参考以下脚本，快速创建并部署一个 Serverless 应用。在以下脚本里，我们会创建一个 Serverless 应用、上传程序包、创建部署组。

新建 shell 脚本（文件名称可自定义）：
```shell
touch create_app.sh
```

赋予 create_app.sh 可执行权限：
```shell
chmod +x create_app.sh
```

使用 Vim 或者本地 IDE 编辑脚本：
```shell
#!/bin/sh

# 这里需要按照您实际部署的 region 进行调整，例如 ap-shanghai、ap-beijing
REGION="ap-guangzhou"

# 这里需要按您实际需要的应用名称（不能和当前地域下已有应用重名）进行调整
APPLICATION_NAME="hello_world"

# 这里需要按您实际需要的部署组名称（不能和当前命名空间下已有部署组重名）进行调整
GROUP_NAME="hello-world"

# 程序包版本（采用时间戳自动生成）
PKG_VERSION=$(date "+%Y%m%d%H%M%S")

# 这里需要按您实际上传的程序包名称进行调整
PKG_NAME="hello_world_node.zip"

# 这里需要按您实际上传的程序包的本地路径进行调整
PKG_LOCAL_PATH="/root/hello_world_node.zip"

# 这里需要按您实际上传的程序包类型（zip 或者 tar.gz）进行调整
PKG_TYPE="zip"

# 配置地域
tccli configure set region $REGION

# 获取程序包 MD5 和大小
PKG_MD5=$(md5sum $PKG_LOCAL_PATH | awk  '{print $1}')
PKG_SIZE=$(ls -l $PKG_LOCAL_PATH | awk  '{print $5}')
echo "your pkg md5: $PKG_MD5, size: $PKG_SIZE"

# Step1. 创建 Serverless 应用
echo tccli tsf CreateApplication --ApplicationName $APPLICATION_NAME --ApplicationType S --MicroserviceType N
OUT=$(tccli tsf CreateApplication --ApplicationName $APPLICATION_NAME --ApplicationType S --MicroserviceType N)
APPLICATION_ID=$(echo "$OUT"  | grep '"Result"' | sed -r 's/.*"Result":\s*"(.*)".*/\1/g')

if [ "$APPLICATION_ID" = "" ];then
  echo "$OUT"
  exit 1
fi

# Step2. 获取上传程序包所需配置信息
echo tccli tsf DescribeUploadInfo --ApplicationId "$APPLICATION_ID" --PkgName $PKG_NAME --PkgType $PKG_TYPE --PkgVersion $PKG_VERSION --PkgDesc $PKG_NAME
OUT=$(tccli tsf DescribeUploadInfo --ApplicationId "$APPLICATION_ID" --PkgName $PKG_NAME --PkgType $PKG_TYPE --PkgVersion $PKG_VERSION --PkgDesc $PKG_NAME)
COS_SECRET_ID=$(echo "$OUT" | grep '"TmpSecretId"' | sed -r 's/.*"TmpSecretId":\s*"(.*)".*/\1/g')
COS_SECRET_KEY=$(echo "$OUT" | grep '"TmpSecretKey"' | sed -r 's/.*"TmpSecretKey":\s*"(.*)".*/\1/g')
COS_SESSION_TOKEN=$(echo "$OUT" | grep '"SessionToken"' | sed -r 's/.*"SessionToken":\s*"(.*)".*/\1/g')
COS_BUCKET=$(echo "$OUT" | grep '"Bucket"' | sed -r 's/.*"Bucket":\s*"(.*)".*/\1/g')
COS_REGION=$(echo "$OUT" | grep '"Region"' | sed -r 's/.*"Region":\s*"(.*)".*/\1/g')
COS_CODE_PATH=$(echo "$OUT" | grep '"Path"' | sed -r 's/.*"Path":\s*"(.*)".*/\1/g')
COS_CONFIG_PATH=$(echo "$COS_CODE_PATH"  | sed -r "s/(.*)$PKG_NAME/\1/g")
PKG_ID=$(echo "$OUT" | grep '"PkgId"' | sed -r 's/.*"PkgId":\s*"(.*)".*/\1/g')

if [ "$COS_SECRET_ID" = "" ];then
  echo "$OUT"
  exit 1
fi

# Step3. 上传程序包
echo config -a "$COS_SECRET_ID" -s "$COS_SECRET_KEY" -t "$COS_SESSION_TOKEN" -b "$COS_BUCKET" -r "$COS_REGION"
coscmd config -a "$COS_SECRET_ID" -s "$COS_SECRET_KEY" -t "$COS_SESSION_TOKEN" -b "$COS_BUCKET" -r "$COS_REGION"

echo upload "$PKG_LOCAL_PATH" "$COS_CODE_PATH"
coscmd upload "$PKG_LOCAL_PATH" "$COS_CODE_PATH"

# 当前需要额外上传一份 spec.yaml（注意控制台上传程序包不需要该文件），后续我们会对此进行优化
echo "
apiVersion: v1kind: Application
spec:
  services:
  - name: hello_world # 服务名，可以设成和部署组名相同
    ports:
    - targetPort: 8080 # 服务监听端口
      protocol: http # 目前仅支持 http
" > "spec.yaml"

coscmd upload "spec.yaml" "$COS_CONFIG_PATH"

# Step4. 更新上传成功状态
echo tccli tsf ModifyUploadInfo --ApplicationId "$APPLICATION_ID" --PkgId "$PKG_ID" --Result 0 --Md5 "$PKG_MD5" --Size "$PKG_SIZE"
tccli tsf ModifyUploadInfo --ApplicationId "$APPLICATION_ID" --PkgId "$PKG_ID" --Result 0 --Md5 "$PKG_MD5" --Size "$PKG_SIZE"

# Step5. 创建 Serverless 部署组
echo tccli tsf CreateServerlessGroup --ApplicationId "$APPLICATION_ID" --PkgId "$PKG_ID" --GroupName $GROUP_NAME
OUT=$(tccli tsf CreateServerlessGroup --ApplicationId "$APPLICATION_ID" --PkgId "$PKG_ID" --GroupName $GROUP_NAME)
GROUP_ID=$(echo "$OUT"  | grep '"Result"' | sed -r 's/.*"Result":\s*"([a-zA-Z0-9-]*)".*/\1/g')

if [ "$GROUP_ID" != "" ];then
  echo "A serverless application is deployed, ApplicationId: \033[32m $APPLICATION_ID \033[0m, GroupId: $GROUP_ID"
else
  echo "$OUT"
  exit 1
fi
```

执行脚本：
```bash
./create_app.sh
```

### 2. 使用 CLI 快速部署 Serverless 应用

如果您已经创建了一个应用和部署组，可参考以下脚本快速更新部署组的程序包版本。
您可以按照实际需要对脚本进行调整，实现自动部署（Continuous Deployment）。

新建 shell 脚本（文件名称可自定义）：
```shell
touch deployment.sh
```

赋予 deployment.sh 可执行权限：
```shell
chmod +x deployment.sh
```

更新部署脚本：
```shell
#!/bin/sh

# 这里需要按照您实际部署的 region 进行调整，例如ap-shanghai、ap-beijing
REGION="ap-guangzhou"

# 填写应用 ID，您可以通过前一个脚本或者控制台查看您的应用 ID
APPLICATION_ID="application-py5qo79y"

# 程序包版本（采用时间戳自动生成）
PKG_VERSION=$(date "+%Y%m%d%H%M%S")

# 这里需要按您实际上传的程序包名称进行调整
PKG_NAME="hello_world_node.zip"

# 这里需要按您实际上传的程序包的本地路径进行调整
PKG_LOCAL_PATH="/root/hello_world_node.zip"

# 这里需要按您实际上传的程序包类型（zip或者tar.gz）进行调整
PKG_TYPE="zip"

# 配置地域
tccli configure set region $REGION

# 获取部署组（若应用下有多个部署组，默认获取更新时间最新的部署组）的 ID 和状态
OUT=$(tccli tsf DescribeServerlessGroups --ApplicationId $APPLICATION_ID)
GROUP_ID=$(echo "$OUT" | grep '"GroupId"' | sed -r 's/.*"GroupId":\s*"([a-zA-Z0-9-]*)".*/\1/g')
APP_STATUS=$(echo "$OUT" | grep '"Status"' | sed -r 's/.*"Status":\s*"([a-zA-Z0-9-]*)".*/\1/g')

if [ "$GROUP_ID" = "" ];then
  echo "$OUT"
  exit 1
fi

if [ "$APP_STATUS" = "Updating" ];then
  echo "Your groupId: $GROUP_ID, status is [\033[31m $APP_STATUS \033[0m], can not deploy, please wait!"
  exit 1
fi

echo "Your groupId: $GROUP_ID, status: $APP_STATUS"

# 获取程序包 MD5 和大小
PKG_MD5=$(md5sum $PKG_LOCAL_PATH | awk  '{print $1}')
PKG_SIZE=$(ls -l $PKG_LOCAL_PATH | awk  '{print $5}')
echo "Your pkg md5: $PKG_MD5, size: $PKG_SIZE"

# Step1. 获取上传程序包所需配置信息
echo tccli tsf DescribeUploadInfo --ApplicationId $APPLICATION_ID --PkgName $PKG_NAME --PkgType $PKG_TYPE --PkgVersion "$PKG_VERSION" --PkgDesc $PKG_NAME
OUT=$(tccli tsf DescribeUploadInfo --ApplicationId $APPLICATION_ID --PkgName $PKG_NAME --PkgType $PKG_TYPE --PkgVersion "$PKG_VERSION" --PkgDesc $PKG_NAME)
COS_SECRET_ID=$(echo "$OUT" | grep '"TmpSecretId"' | sed -r 's/.*"TmpSecretId":\s*"(.*)".*/\1/g')
COS_SECRET_KEY=$(echo "$OUT" | grep '"TmpSecretKey"' | sed -r 's/.*"TmpSecretKey":\s*"(.*)".*/\1/g')
COS_SESSION_TOKEN=$(echo "$OUT" | grep '"SessionToken"' | sed -r 's/.*"SessionToken":\s*"(.*)".*/\1/g')
COS_BUCKET=$(echo "$OUT" | grep '"Bucket"' | sed -r 's/.*"Bucket":\s*"(.*)".*/\1/g')
COS_REGION=$(echo "$OUT" | grep '"Region"' | sed -r 's/.*"Region":\s*"(.*)".*/\1/g')
COS_CODE_PATH=$(echo "$OUT" | grep '"Path"' | sed -r 's/.*"Path":\s*"(.*)".*/\1/g')
COS_CONFIG_PATH=$(echo "$COS_CODE_PATH"  | sed -r "s/(.*)$PKG_NAME/\1/g")
PKG_ID=$(echo "$OUT" | grep '"PkgId"' | sed -r 's/.*"PkgId":\s*"(.*)".*/\1/g')

if [ "$COS_SECRET_ID" = "" ];then
  echo "$OUT"
  exit 1
fi

# Step2. 上传程序包
echo config -a "$COS_SECRET_ID" -s "$COS_SECRET_KEY" -t "$COS_SESSION_TOKEN" -b "$COS_BUCKET" -r "$COS_REGION"
coscmd config -a "$COS_SECRET_ID" -s "$COS_SECRET_KEY" -t "$COS_SESSION_TOKEN" -b "$COS_BUCKET" -r "$COS_REGION"

echo upload "$PKG_LOCAL_PATH" "$COS_CODE_PATH"
coscmd upload "$PKG_LOCAL_PATH" "$COS_CODE_PATH"

# 当前需要额外上传一份 spec.yaml（注意控制台上传程序包不需要该文件），后续我们会对此进行优化
echo "
apiVersion: v1kind: Application
spec:
  services:
  - name: test # 服务名
    ports:
    - targetPort: 8080 # 服务监听端口
      protocol: http # 目前仅支持 http
" > "spec.yaml"

coscmd upload "spec.yaml" "$COS_CONFIG_PATH"

# Step3. 更新上传成功状态
echo tccli tsf ModifyUploadInfo --ApplicationId "$APPLICATION_ID" --PkgId "$PKG_ID" --Result 0 --Md5 "$PKG_MD5" --Size "$PKG_SIZE"
tccli tsf ModifyUploadInfo --ApplicationId "$APPLICATION_ID" --PkgId "$PKG_ID" --Result 0 --Md5 "$PKG_MD5" --Size "$PKG_SIZE"

# Step4. 部署程序包
echo tsf DeployServerlessGroup --GroupId "$GROUP_ID" --PkgId "$PKG_ID"
tccli tsf DeployServerlessGroup --GroupId "$GROUP_ID" --PkgId "$PKG_ID"

# 获取部署组状态
OUT=$(tccli tsf DescribeServerlessGroups --ApplicationId $APPLICATION_ID)
GROUP_ID=$(echo "$OUT" | grep '"GroupId"' | sed -r 's/.*"GroupId":\s*"([a-zA-Z0-9-]*)".*/\1/g')
APP_STATUS=$(echo "$OUT" | grep '"Status"' | sed -r 's/.*"Status":\s*"([a-zA-Z0-9-]*)".*/\1/g')

if [ "$GROUP_ID" = "" ];then
  echo "$OUT"
  exit 1
fi

echo "New software is deployed, GroupId: \033[32m $GROUP_ID \033[0m, status: $APP_STATUS"

```

执行脚本：
```bash
./deployment.sh
```
