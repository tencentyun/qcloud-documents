>?本次测试提供的 Pipeline 为人类全基因组二代分析流程，暂不支持其他物种的分析。


整个测试过程分为数据准备、分析计算、结果查看三个步骤。

## 一、数据准备 ##
用户在测试前，需提前把测试中使用的源数据文件上传至腾讯云双螺旋。文件上传指引如下：
### 1.1 开通双螺旋权限 ###
双螺旋目前处于内测申请阶段，您可通过 [内测申请页面](https://cloud.tencent.com/act/apply/helix) 提交开通申请，若您的账号已获取使用资格，请直接进入 [双螺旋控制台](https://console.cloud.tencent.com/helix) 开始使用。

### 1.2 新建项目 ###
项目是双螺旋中的基本单元，用户上传的数据和创建的作业，都会归属到具体的项目。
登录控制台后，请进入左侧 **项目管理** 菜单，单击【+新建项目】创建一个地域为 **广州** 的项目（当前测试环境部署在广州）。
![新建项目](https://mc.qcloudimg.com/static/img/adf15e5565d506f6afc4f5cdb3fb2a07/image.png)

项目新建成功后，系统会自动分配一个对象存储 COS 的存储桶给该项目，用于存放该项目的数据。用户可在项目管理菜单中查看项目关联的存储桶（Bucket）名称。
![COS Bucket](https://mc.qcloudimg.com/static/img/261f27ccb63523a651a0943be2771797/COS+Bucket.png)


### 1.3 上传数据 ###
项目新建完成后，请进入 **数据管理** 下的 **私有文件** 子菜单，上传源数据文件。上传文件的方式分为三种：本地上传（Web 上传）、超大文件线下上传（工具上传）和从第三方存储上传（不推荐），下面主要介绍前两种上传方式。
- 若源文件小于500MB，建议在控制台直接上传本地文件。
- 若源文件大于500MB，建议使用工具上传文件。

#### 本地上传 
在私有文件页面选择刚创建好的项目，单击【+上传文件】按钮，在弹出的对话框中选择 **本地上传**，上传本地文件即可。
![web上传文件页面](https://mc.qcloudimg.com/static/img/771a25660e72828e5e746973b4defb4f/image.png)

#### 工具上传
在私有文件页面选择刚创建好的项目，单击【+上传文件】按钮，在弹出的对话框中选择 **超大文件线下上传**，根据操作指引上传文件即可。
COS 提供以下工具，您可按照自身需求使用：
- **COSCMD 工具**
 - 有一定 Python 操作基础的用户，建议使用 COSCMD 工具。

 - 点击下载 [COSCMD 工具](https://github.com/tencentyun/coscmd)，使用指引参考 [COSCMD 工具使用说明](/document/product/436/10976)。其中重点配置信息说明如下：
![COSCMD工具配置信息](https://mc.qcloudimg.com/static/img/cb4a6d9006514cbc54e71fe6db395064/image.png)
     1. **secret_id** 和 **secret_key**
指用户的云 API 密钥，可从云 API 密钥控制台的 API 密钥菜单中获取。若还没有云 API 密钥，用户可在控制台上新建。点此进入 [云 API 密钥控制台](https://console.cloud.tencent.com/capi)。
     2. **APPID**
指用户在腾讯云的标识，可通过 [腾讯云控制台](https://console.cloud.tencent.com/) 【账号信息】查看 APPID。
     3. **Bucket**
指对象存储的存储桶名称，此处使用系统分配的项目关联 Bucket，获取方式见步骤 1.2。
     4. **Region**
指文件所属地域，此处固定为 ap-guangzhou。

- **COS 本地同步工具**
 - 其他用户建议通过 COS 本地同步工具上传。

 - 点击下载 [本地同步工具](https://github.com/tencentyun/cos_sync_tools_v5 "COS同步工具")，使用指引参考 [本地同步工具使用说明](/document/product/436/7133 "本地同步工具使用说明")。其中重点配置信息说明如下：
![同步工具配置信息](https://mc.qcloudimg.com/static/img/fcafb9aa397b49c39b720430d27f2350/image.png)
     1. **secret_id** 和 **secret_key**
指用户的云 API 密钥，可从云 API 密钥控制台的 API 密钥菜单中获取。若还没有云 API 密钥，用户可在控制台上新建。点此进入 [云 API 密钥控制台](https://console.cloud.tencent.com/capi)。
     2. **Bucket**
指对象存储的存储桶名称，此处使用系统分配的项目关联 Bucket，获取方式见步骤 1.2。
     3. **Region**
指文件所属地域，此处固定为 ap-guangzhou。

## 二、分析计算 ##
开通双螺旋 WGS FPGA 内测权限后，请在** 作业管理** 菜单中新建 FPGA 作业进行分析计算，操作指引如下：
### 2.1 选择作业模版 ###
在作业管理页面，单击【+新建作业】，请在新建作业对话框中，选择【FPGA 作业】，并选中平台提供的 WGS FPGA 作业模版，单击【下一步】进入作业配置页面。
![新建FPGA作业](https://mc.qcloudimg.com/static/img/cda1f8a4da89153700bc12037194e8bf/image.png)

### 2.2 作业详情配置 ###
用户进入作业配置页后，可对各项作业参数进行配置，具体如下：
#### 2.2.1 基本信息 ####
![基本信息配置](https://mc.qcloudimg.com/static/img/02f8b81f6d81fb491f844ffe5eaebe51/image.png)
其中，项目应选择存有测试数据的项目。

#### 2.2.2 输入输出配置 ####
![输入输出配置](https://mc.qcloudimg.com/static/img/6e7ae17c7cf87efb58d284d956769835/image.png)
-  其中，单击【浏览】按钮可从项目关联的 COS Bucket 中选择需要进行分析的文件，需提供双末端测序的一对文件作为输入文件；
- 平台预置了`Homo_sapiens_assembly38.fasta`、`human_g1k_v37_decoy.fasta`、`ucsc.hg19.fasta`三个参考文件供您选择；
- 计算完成后的分析结果，默认存放到项目关联 COS Bucket 的`/stdout/`目录下，您可修改为其他目录，目录名须以`/`开头。

#### 2.2.3 作业参数配置 ####
![作业参数配置](https://mc.qcloudimg.com/static/img/fef8494116763e4110c365fc980837ee/image.png)
- ReadGroup 参数：
 - tID：Read Group 的分组 ID，一般设置为测序的 lane ID；
 - tPL：所用的测序平台，只允许为 ILLUMINA，SLX，SOLEXA，SOLID，454，LS454，COMPLETE，PACBIO，IONTORRENT，CAPILLARY，HELICOS 或 UNKNOWN；
 - tSM：样本 ID；

- stand_call_conf 参数：只能为 0 ~ 100 的浮点数，默认为 30.0；

- 需勾选 **授予腾讯云双螺旋平台从您的存储桶中读取待计算文件和写入计算结果的权限**，平台才可以读取需要分析的文件进行计算，并将结果返回给您。

## 三、结果查看 ##
平台完成分析计算后，会将结果 VCF 文件回传到项目关联的 COS Bucket 中，存放目录为用户在创建作业时设置的 **输出目录**。您可在 **数据管理** 下的 **私有文件** 子菜单中，查看平台返回的测试结果文件，或将结果文件下载至本地做进一步的分析。
![结果文件](https://mc.qcloudimg.com/static/img/a2f07c6b2879b776496965fd78b3800c/image.png)
