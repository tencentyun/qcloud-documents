# 双螺旋 WGS FPGA测试指引 #
**说明**：本次测试提供的Pipeline为人类全基因组二代分析流程，暂不支持其他物种的分析。
整个测试过程分为数据准备、分析计算、结果查看三个步骤。
## 一、数据准备 ##
用户在测试前，需提前把测试中使用的源数据文件上传至腾讯云双螺旋。文件上传指引如下：
### 1.1 开通双螺旋权限 ###
双螺旋产品当前为受控开放，点此进入[产品控制台](https://console.cloud.tencent.com/helix)。如您登录后可看见控制台操作界面，说明您的账号已经开通权限，请略过本步骤。如您暂无权限，请在控制台出现的内测申请页面（3秒自动跳转）上提交开通申请。

![双螺旋控制台操作页面](https://mc.qcloudimg.com/static/img/5d6fe42b955323dbda84b521e07a95ef/image.png)

图1.双螺旋控制台操作页面

![权限受控页面](https://mc.qcloudimg.com/static/img/6ff612dcbbeb8b4ff58f598393f7e5e3/image.png)

图2.权限受控页面
### 1.2 新建项目 ###
项目是双螺旋中的基本单元，用户上传的数据和创建的作业，都会归属到某个项目。用户进入控制台后，首先进入“项目管理”菜单，创建一个**广州地区**的项目（备注：当前测试环境部署在广州）

![新建项目](https://mc.qcloudimg.com/static/img/adf15e5565d506f6afc4f5cdb3fb2a07/image.png)

图3.新建项目页面

项目新建成功后，系统会自动分配一个COS（腾讯云对象存储）Bucket给该项目，用于存放该项目的数据。用户可在“项目管理”菜单中查看项目关联的COS Bucket名称。

![COS Bucket](https://mc.qcloudimg.com/static/img/261f27ccb63523a651a0943be2771797/COS+Bucket.png)

图4.项目Bucket信息
### 1.3上传数据 ###
新建完项目后，用户进入“数据管理”下的“私有文件”子菜单，上传源数据文件。
#### 1.3.1 web上传 ####
若源文件小于500MB，可直接通过web上传，点击“上传文件”按钮，在弹出的对话框中选择文件上传。

![web上传文件页面](https://mc.qcloudimg.com/static/img/771a25660e72828e5e746973b4defb4f/image.png)

图5.web上传页面
#### 1.3.2 工具上传 ####
若源文件大于500MB，建议使用工具上传文件。

**COSCMD 工具**

有一定Python操作基础的用户，建议使用COSCMD工具。点击下载[COSCMD工具](https://github.com/tencentyun/coscmd)，工具的使用指引点此了解[COSCMD工具使用说明](https://cloud.tencent.com/document/product/436/10976)
。其中重点配置信息说明如下：
![](https://mc.qcloudimg.com/static/img/cb4a6d9006514cbc54e71fe6db395064/image.png)
图6.COSCMD工具配置信息

1. **secret_id**和**secret_key**，指用户的云API密钥，可从云API密钥控制台“API密钥”菜单中获取。若还没有云API密钥，用户可在控制台上新建。点此进入[云API密钥控制台](https://console.cloud.tencent.com/capi "API密钥")
2. **APPID**,指用户在腾讯云的标识，可通过 [腾讯云控制台](https://console.cloud.tencent.com/) 【账号信息】查看 APPID。
3. **Bucket**，指COS Bucket名称，此处使用系统分配的项目关联Bucket，获取方式见上文图4
4. **Region**，指文件所属地域，此处固定为 ap-guangzhou



**COS本地同步工具**

其他用户建议通过腾讯云COS本地同步工具上传。点此下载[本地同步工具](https://github.com/tencentyun/cos_sync_tools_v5 "COS同步工具")
，本地同步工具的使用指引点此了解[工具使用说明](https://cloud.tencent.com/document/product/436/7133 "本地同步工具使用说明")。其中重点配置信息说明如下：

![同步工具配置信息](https://mc.qcloudimg.com/static/img/fcafb9aa397b49c39b720430d27f2350/image.png)

图6.同步工具配置信息

1. **secret_id**和**secret_key**，指用户的云API密钥，可从云API密钥控制台“API密钥”菜单中获取。若还没有云API密钥，用户可在控制台上新建。点此进入[云API密钥控制台](https://console.cloud.tencent.com/capi "API密钥")
2. **Bucket**，指COS Bucket名称，此处使用系统分配的项目关联Bucket，获取方式见上文图4
3. **Region**，指文件所属地域，此处固定为 ap-guangzhou

## 二、分析计算 ##
用户开通双螺旋 WGS FPGA内测权限后，可在“作业管理”菜单中新建FPGA作业进行分析计算，指引如下:
### 2.1 选择作业模版 ###
用户在“新建作业”对话框中，选择FPGA作业，并选中平台提供的WGS FPGA作业模版，点击“下一步”进行作业配置页面。

![新建FPGA作业](https://mc.qcloudimg.com/static/img/cda1f8a4da89153700bc12037194e8bf/image.png)

图7.选择WGS FPGA作业模版
### 2.2 作业详情配置 ###
用户进入作业配置页后，可对各项作业参数进行配置，具体如下：
#### 2.2.1 基本信息 ####

![基本信息配置](https://mc.qcloudimg.com/static/img/02f8b81f6d81fb491f844ffe5eaebe51/image.png)

图8.基本信息配置

其中，项目应选择为存有测试数据的项目 
#### 2.2.2 输入输出配置 ####

![输入输出配置](https://mc.qcloudimg.com/static/img/25b2daf78309b68997799fd51b0a53e5/image.png)

图9.输入输出配置

1. 其中，点击“浏览”按钮可从项目关联的COS Bucket中选择需要进行分析的文件，需提供双末端测序的一对文件作为输入文件；
2. 平台预置了human_g1k_v37_decoy.fasta、Homo_sapiens_assembly38.fasta、ucsc.hg19.fasta三个参考文件供用户选择；
3. 计算完成后的分析结果，默认存放到项目关联COS Bucket的“/stdout/”目录下，用户可修改为其他目录，目录名须以“/”开头。
#### 2.2.3 作业参数配置 ####

![作业参数配置](https://mc.qcloudimg.com/static/img/fef8494116763e4110c365fc980837ee/image.png)

图10.作业参数配置

1. ReadGroup参数：1.tID，指的是Read Group的分组ID，一般设置为测序的lane ID; 2.tPL，指的是所用的测序平台，只允许为ILLUMINA，SLX，SOLEXA，SOLID，454，LS454，COMPLETE，PACBIO，IONTORRENT，CAPILLARY，HELICOS或UNKNOWN；3.tSM，指的是样本ID；
2. stand_call_conf参数：只能为0-100的浮点数，默认为30.0；
3. 需勾选授权腾讯云双螺旋平台从您的存储桶中读取待计算文件和写入计算结果的权限，平台才可以读取需要分析的文件进行计算，并将结果返回给客户。

## 三、结果查看 ##
平台完成分析计算后，会将结果VCF文件回传到项目关联的COS Bucket中，存放目录为用户在创建作业时设置的“输出目录”。用户可在“数据管理”下“私有文件”子菜单中，查看到平台返回的测试结果文件，用户可将结果文件下载至本地进一步的分析。

![结果文件](https://mc.qcloudimg.com/static/img/a2f07c6b2879b776496965fd78b3800c/image.png)

图11. 分析结果文件
