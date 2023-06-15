云托管推出 CLI 工具，帮助开发者能够在本地或者自定义 CI/CD 中快速进行版本创建和其他操作。

<dx-alert infotype="notice" title="">
CLI 工具仅限云托管新版控制台的环境使用，云开发中的云托管无法使用。
</dx-alert>


## 安装

CLI 工具安装前需要安装 `npm`，具体请看 [此文档](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)。
<dx-codeblock>
:::  shell
npm install -g @cloudbase/cli
:::
</dx-codeblock>


如果 `npm install -g @cloudbase/cli` 失败，您可能需要 [修改 npm 权限](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)，或者以系统管理员身份运行：
<dx-codeblock>
:::  sh
sudo npm install -g @cloudbase/cli
:::
</dx-codeblock>

如果安装过程没有错误提示，一般就是安装成功了。下面，我们可以继续输入命令：
<dx-codeblock>
:::  sh
tcb -v
:::
</dx-codeblock>


如果看到输出版本号，说明已经安装成功。

### 使用代理

使用 CLI 工具 时，需要您的终端能够访问公网。**如果您的终端无法直接访问公网**，您可以设置 HTTP 代理使 CLI 能够正常使用。CLI 会读取 `http_proxy` 或 `HTTP_PROXY` 环境变量，自动设置网络代理服务。

例如，您可以在终端中运行以下命令，设置 CLI 通过 `http://127.0.0.1:8000` 的代理服务访问网络：
<dx-codeblock>
:::  bash
export HTTP_PROXY=http://127.0.0.1:8000
:::
</dx-codeblock>


>!`http://127.0.0.1:8000` 只是一个示例，请勿直接使用，具体的代理配置根据您的网络配置决定。

上面的命令只是临时设置，当您关闭终端后，代理会自动失效，下次开启终端后需要重新设置。如果您需要一直通过代理访问公网，可以把命令加入到终端的配置文件中。

## 查看服务列表

查看指定环境下的所有服务列表：
<dx-codeblock>
:::  shell
tcb run service:list  [OPTIONS]
:::
</dx-codeblock>


参数信息：
<dx-codeblock>
:::  bash
OPTIONS
  -h, --help                     查看帮助信息
  -e, --envId                    环境ID，必填
  -s, --serviceName              服务名
  --json                         以 JSON 形式展示结果
  -r                             地域参数，不填默认操作上海地域环境。可取值：上海（sh）,广州(gz)，北京(bj)
:::
</dx-codeblock>


## 在指定环境下创建服务

创建服务并发布一个版本：
<dx-codeblock>
:::  shell
tcb run service:create [OPTIONS]
:::
</dx-codeblock>


参数信息：
<dx-codeblock>
:::  bash
OPTIONS
  --noConfirm                      发布前是否跳过二次确认
  --override                       缺省的参数是否沿用旧版本配置
  -e, --envId <envId>              环境 Id，必填
  -s, --serviceName <serviceName>  服务名，必填
  -r                               地域参数，不填默认操作上海地域环境。可取值：上海（sh）,广州(gz)，北京(bj)
  --path <path>                    本地代码根目录
  --cpu <cpu>                      单一实例cpu规格，默认0.5
  --mem <mem>                      单一实例内存规格，默认1
  --minNum <minNum>                最小副本数，默认0
  --maxNum <maxNum>                最大副本数，默认50，不能大于50
  --policyDetails <policyDetails>  扩缩容配置，格式为条件类型=条件比例（%），多个条件之间用&隔开，内存条件为mem，cpu条件为cpu，默认内存>60% 或 CPU>60%，即cpu=60&mem=60
  --customLogs <customLogs>        日志采集路径，默认stdout
  --envParams <envParams>          环境变量，格式为xx=a&yy=b，默认为空
  --containerPort <containerPort>  监听端口，必填
  --remark <remark>                版本备注，默认为空
  --targetDir <targetDir>          目标目录
  --dockerfile <dockerfile>        Dockerfile文件名，默认为 Dockerfile
  --custom_image <custom_image>    容器镜像仓库企业版（TCR）镜像 URL
  --json                           以 JSON 形式展示结果
  -h, --help                       查看命令帮助信息
:::
</dx-codeblock>


## 更新发布服务

指定定环境和已存在的服务，发布新的更新：
<dx-codeblock>
:::  shell
tcb run service:deploy [OPTIONS]
:::
</dx-codeblock>


参数信息：
<dx-codeblock>
:::  bash
OPTIONS
  --noConfirm                      发布前是否跳过二次确认
  --override                       缺省的参数是否沿用旧版本配置
  -e, --envId <envId>              环境 Id，必填
  -s, --serviceName <serviceName>  服务名，必填
  -r                               地域参数，不填默认操作上海地域环境。可取值：上海（sh）,广州(gz)，北京(bj)
  --path <path>                    本地代码根目录
  --cpu <cpu>                      单一实例cpu规格，默认0.5
  --mem <mem>                      单一实例内存规格，默认1
  --minNum <minNum>                最小副本数，默认0
  --maxNum <maxNum>                最大副本数，默认50，不能大于50
  --policyDetails <policyDetails>  扩缩容配置，格式为条件类型=条件比例（%），多个条件之间用&隔开，内存条件为mem，cpu条件为cpu，默认内存>60% 或 CPU>60%，即cpu=60&mem=60
  --customLogs <customLogs>        日志采集路径，默认stdout
  --envParams <envParams>          环境变量，格式为xx=a&yy=b，默认为空
  --containerPort <containerPort>  监听端口，必填
  --remark <remark>                版本备注，默认为空
  --dockerfile <dockerfile>        Dockerfile文件名，默认为 Dockerfile
  --custom_image <custom_image>    容器镜像仓库企业版（TCR）镜像 URL
  --json                           以 JSON 形式展示结果
  -h, --help                       查看命令帮助信息
:::
</dx-codeblock>



## 更新或新建服务

在指定的环境中，新增或更新服务（如果服务不存在会创建）。
<dx-codeblock>
:::  shell
tcb run deploy [OPTIONS]
:::
</dx-codeblock>


参数信息：
<dx-codeblock>
:::  bash
OPTIONS
  --noConfirm                      发布前是否跳过二次确认
  --override                       缺省的参数是否沿用旧版本配置
  -e, --envId <envId>              环境 Id，必填
  -s, --serviceName <serviceName>  服务名，必填
  -r                               地域参数，不填默认操作上海地域环境。可取值：上海（sh）,广州(gz)，北京(bj)
  --path <path>                    本地代码根目录
  --cpu <cpu>                      单一实例cpu规格，默认0.5
  --mem <mem>                      单一实例内存规格，默认1
  --minNum <minNum>                最小副本数，默认0
  --maxNum <maxNum>                最大副本数，默认50，不能大于50
  --policyDetails <policyDetails>  扩缩容配置，格式为条件类型=条件比例（%），多个条件之间用&隔开，内存条件为mem，cpu条件为cpu，默认内存>60% 或 CPU>60%，即cpu=60&mem=60
  --customLogs <customLogs>        日志采集路径，默认stdout
  --envParams <envParams>          环境变量，格式为xx=a&yy=b，默认为空
  --containerPort <containerPort>  监听端口，必填
  --remark <remark>                版本备注，默认为空
  --targetDir <targetDir>          目标目录
  --dockerfile <dockerfile>        Dockerfile文件名，默认为 Dockerfile
  --custom_image <custom_image>    容器镜像仓库企业版（TCR）镜像 URL
  --json                           以 JSON 形式展示结果
  -h, --help                       查看命令帮助信息
:::
</dx-codeblock>



## 更新服务配置

指定环境和服务，更新服务的基础配置：
<dx-codeblock>
:::  shell
tcb run service:config [OPTIONS]
:::
</dx-codeblock>


参数信息：
<dx-codeblock>
:::  bash
OPTIONS
  -e, --envId <envId>              环境 Id，必填
  -s, --serviceName <serviceName>  服务名，必填
  -r                               地域参数，不填默认操作上海地域环境。可取值：上海（sh）,广州(gz)，北京(bj)
  --cpu <cpu>                      单一实例cpu规格，默认0.5
  --mem <mem>                      单一实例内存规格，默认1
  --minNum <minNum>                最小副本数，默认0
  --maxNum <maxNum>                最大副本数，默认50，不能大于50
  --policyDetails <policyDetails>  扩缩容配置，格式为条件类型=条件比例（%），多个条件之间用&隔开，内存条件为mem，cpu条件为cpu，默认内存>60% 或 CPU>60%，即cpu=60&mem=60
  --customLogs <customLogs>        日志采集路径，默认stdout
  --envParams <envParams>          环境变量，格式为xx=a&yy=b，默认为空
  --json                           以 JSON 形式展示结果
  -h, --help                       查看命令帮助信息
:::
</dx-codeblock>

