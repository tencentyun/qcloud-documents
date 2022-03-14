## 操作场景
本文介绍如何在 M6ce 实例中构建 Tencent SGX 机密计算环境，并演示如何使用 intel SGXSDK 验证 SGX 功能。


## 前提条件
已创建并登录 [M6ce 实例](https://cloud.tencent.com/document/product/213/11518#M6ce)。
 - 如何创建实例，请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。
 - 如何登录实例，请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。


<dx-alert infotype="explain" title="">
本文步骤以使用操作系统为 TencentOS Server 3.1(TK4) 的实例为例，不同操作系统版本步骤有一定区别，请结合实际情况进行操作。
</dx-alert>



## 操作步骤
1. 执行以下命令，检查 kernel 版本。
```
uname -a
```
查看 kernel 版本是否低于5.4.119-19.0008：
 - 是，请执行以下命令更新 kernel。
```
yum update kernel
```   
 - 否，则请执行下一步。
2. 执行以下命令，安装 SGX runtime 所需的软件包。
```
yum install \
    libsgx-ae-le libsgx-ae-pce libsgx-ae-qe3 libsgx-ae-qve \
    libsgx-aesm-ecdsa-plugin libsgx-aesm-launch-plugin libsgx-aesm-pce-plugin libsgx-aesm-quote-ex-plugin \
    libsgx-dcap-default-qpl libsgx-dcap-default-qpl-devel libsgx-dcap-ql libsgx-dcap-ql-devel \
    libsgx-dcap-quote-verify libsgx-dcap-quote-verify-devel libsgx-enclave-common libsgx-enclave-common-devel libsgx-epid-devel \
    libsgx-launch libsgx-launch-devel libsgx-pce-logic libsgx-qe3-logic libsgx-quote-ex libsgx-quote-ex-devel \
    libsgx-ra-network libsgx-ra-uefi libsgx-uae-service libsgx-urts sgx-ra-service \
sgx-aesm-service
``` <dx-alert infotype="explain" title="">
SGX AESM 服务的默认安装目录为 `/opt/intel/sgx-aesm-service`。
</dx-alert>
3. 执行以下命令，安装 intel SGXSDK。
```
yum install sgx-linux-x64-sdk
```
<dx-alert infotype="explain" title="">
Intel SGXSDK 的默认安装目录为 /`opt/intel/sgxsdk`。您可参考 [intel SGXSDK](https://download.01.org/intel-sgx/sgx-linux/2.13/docs/Intel_SGX_Developer_Reference_Linux_2.13_Open_Source.pdf?spm=a2c4g.11186623.0.0.2f8d31b8PMoC1w&file=Intel_SGX_Developer_Reference_Linux_2.13_Open_Source.pdf) 用户手册开发 SGX 程序。
</dx-alert>
4. SGX runtime 和 intel SGXSDK 安装完成后，请重启实例。详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。
5. 配置腾讯云 SGX 远程证明服务。
腾讯云 SGX 远程证明服务采用区域化部署，您可以访问 SGX 云服务器实例所在地域的腾讯云 SGX 远程证明服务来获得最佳体验。安装 intel SGXSDK 后会自动生成远程证明服务的默认配置文件 `/etc/sgx_default_qcnl.conf`，请根据以下步骤手动修改该文件，以适配 SGX 云服务器实例所在地域的腾讯云 SGX 远程证明服务。
<dx-alert infotype="explain" title="">
- 目前仅北京、上海及广州地域支持腾讯云 SGX 远程证明服务。
- Intel Ice Lake 仅支持基于 Intel SGX DCAP 远程证明方式，不支持 Intel EPID 远程证明方式。
</dx-alert>
使用 VIM 编辑器，将 `/etc/sgx_default_qcnl.conf` 修改为如下内容：
```
# PCCS server address
PCCS_URL=https://sgx-dcap-server-tc.[Region-ID].tencent.cn/sgx/certification/v3/
# To accept insecure HTTPS cert, set this option to FALSE
USE_SECURE_CERT=TRUE
```
请将 `[Region-ID]` 替换为 SGX 云服务器实例所在地域的 ID。例如：<br>
 北京地域修改示例如下：
```
# PCCS server address
PCCS_URL=https://sgx-dcap-server-tc.bj.tencent.cn/sgx/certification/v3/
# To accept insecure HTTPS cert, set this option to FALSE
USE_SECURE_CERT=TRUE
```
上海地域修改示例如下：
```
# PCCS server address
PCCS_URL=https://sgx-dcap-server-tc.sh.tencent.cn/sgx/certification/v3/
# To accept insecure HTTPS cert, set this option to FALSE
USE_SECURE_CERT=TRUE
```
广州地域修改示例如下：
```
# PCCS server address
PCCS_URL=https://sgx-dcap-server-tc.gz.tencent.cn/sgx/certification/v3/
# To accept insecure HTTPS cert, set this option to FALSE
USE_SECURE_CERT=TRUE
```

## 验证 SGX 功能示例

### 示例1：启动 Enclave
Intel SGXSDK 中提供了 SGX 示例代码用于验证 SGX 功能，默认目录为 `/opt/intel/sgxsdk/SampleCode`。本示例中的代码（SampleEnclave）效果为启动一个 Enclave，以验证是否正常使用安装的 SGXSDK，以及 SGX 云服务器实例的机密内存资源是否可用。
1. 执行以下命令，设置 intel SGXSDK 相关的环境变量。
```
source /opt/intel/sgxsdk/environment
```
2. 执行以下命令，编译示例代码 SampleEnclave。
```
cd /opt/intel/sgxsdk/SampleCode/SampleEnclave && make
```
3. 执行以下命令，运行编译出的可执行文件。
```
./app
```
返回如下图所示结果，则说明已启动成功。
![](https://qcloudimg.tencent-cloud.cn/raw/ae6cf48bfae18e245cb9c22fe85c5c63.png)



### 示例2：SGX 远程证明
Intel sgx 的 code tree 提供了示例代码用于验证 SGX 远程证明功能（DCAP）。本示例为生成和验证 Quote，示例涉及 Quote 生成方（QuoteGenerationSample）和 Quote 验证方（QuoteVerificationSample）。
1. 执行以下命令，设置 intel SGXSDK 相关的环境变量。
```
source /opt/intel/sgxsdk/environment
```
2. 依次执行以下命令，安装 git 并下载 intel sgx DCAP code tree。
```
cd /root && yum install git
```
```
git clone https://github.com/intel/SGXDataCenterAttestationPrimitives.git
```
3. 依次执行以下命令，编译并运行 Quote 生成方示例代码 QuoteGenerationSample。
    1. 进入 QuoteGenerationSample 目录。 
```
cd /root/SGXDataCenterAttestationPrimitives/SampleCode/QuoteGenerationSample
```
    2. 编译 QuoteGenerationSample。
```
make
```
    3. 运行 QuoteGenerationSample 并生成 Quote。
```
./app
```
4. 执行以下命令，编译 Quote 验证方示例代码 QuoteVerificationSample。
```
cd /root/SGXDataCenterAttestationPrimitives/SampleCode/QuoteVerificationSample && make
```
5. 执行以下命令，对 QuoteVerificationSample Enclave 进行签名。
```
sgx_sign sign -key Enclave/Enclave_private_sample.pem -enclave enclave.so -out enclave.signed.so -config Enclave/Enclave.config.xml
```
6. 执行以下命令，运行 QuoteVerificationSample 以验证 Quote。
```
./app
```
返回如下图所示结果，则说明已验证成功。
![](https://qcloudimg.tencent-cloud.cn/raw/e32430adce18aa76303d9cd73ac9ff2f.png)
