## 背景

本文为您介绍如何搭配腾讯云数据开发治理平台 Wedata 和 TI-kit CLI 工具，进行任务周期性调度，该功能适用于同时有数据治理需求和机器学习需求的业务场景，可以在 Wedata 页面进行数据开发任务和机器学习任务的统一调度。

## 操作流程

您可以按照如下最佳实践流程实现 TI-ONE 和 Wedata 平台（数据开发治理平台 WeData 是位于云端的一站式数据开发治理平台,详细介绍请查看[文档](https://cloud.tencent.com/document/product/1267/47990)）的对接。TI-ONE 机器学习任务调度能力当前仅支持 Wedata 广州地域的企业版。

### 步骤一 准备工作
1. 创建用户及项目


   在 Wedata 产品内需要首先创建用户及项目，详情操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72455)。

2. 配置自定义调度资源组


   启用 TI-ONE 对接功能需要首先配置企业版自定义调度资源组，详情操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72631#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B0.83.E5.BA.A6.E8.B5.84.E6.BA.90.E7.BB.84.E5.88.97.E8.A1.A8)。


### 步骤二 初始化环境

在 Wedata 项目空间中添加执行资源组，添加服务器后需要同时安装 Wedata Agent 和 TI-ONE CLI 机器学习环境。登录机器安装完毕之后，可以看到资源组节点的状态为正常。

![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/814b3e82654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKIDzaofywZqHny_dXerJ7TNsogVVxZ3CB129TCpXKg9caCTum8fT6ct5jdTHL7rjkRf&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=83b9d8e6cf91c5518c40dfaf8ddd1d8d4993b2eb&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpa4853996fab0bd3a00db7244bc07028b5VoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIgLXFU3oMH31-xty37G_iRc-_osepKRKqZndlPnzMr9uhiJP06vhn4F-Lnl9ArpmMgY9V8z8GOvtpXdYHUlexRPvR1Ct7lK_LCGAjcFSm7jegVuRZsjK6IcButKpyOTdDbSnZcurKGva_5lVVBRLEH_NHj9GURhFgxXXOKVs6-sKlkT7-R0xL2XkMY6FGtph7R)

### 步骤三 添加数据源

在 Wedata 项目空间中添加数据源，添加一个 HDFS 或者 HIVE 的数据源，测试联通性，需要注意，创建完成后，要授权给需要使用的项目。数据源创建详细操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72456)。
![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/817a3337654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKID3vFTVmJ89qdbmsKttdwNH91BSjIH4hHa-Q0yjqdJsyHK3cvjc9m9n8yhE6iT-pPL&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=2e0543bb6a36211dc0d5690de85c17786a65b373&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpa7cd6cb36ab869a7db5969b69abe99d70VoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIguA7Q6VB00BKAnI98AEEov4kZZXh0F7FyDFQFxFgv8b8OkEvtMEdjCHgN8-853zLKdEeICcoZW63EgxsKk4RYRI-wKkq-wMP_k3PV8s8Q-CuIOz3bllpXId65Lf-R-5P8NYgOkZUkKKcNrKlakVR7sYbKU4SF1_b-geQz4PH6u-S9mFyzl4DlzPSIpXSYpnDP)

### 步骤四 机器学习节点配置
1. 进入**数据开发** > **编排空间**，创建工作流，在工作流编排面板中，单击 TI-ONE 机器学习节点创建。
![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/81aee4df654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKID6czQImNXE14Bd0wpwduGT9LrBqUWTxz9RpX47A193eFw6fQibdjTzgF-jsaZyPW8&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=cb8d2330301dc9d6ba8140b58ec6f11ca2c9ecab&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpa1f3fdc1773f1044111a5ceb1ac110690VoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIgv3MqHbDzcwvgJHnVzZdE1uBgAyRZdYH6bmcxEZMzlyeAefoO_MMPPynZroUBcWVkvdg446YKJUuWA6pHtPdCpaXnC-bVF5pQMyiMTZtLL5l-UOgHVCwODMedhnLnwh2AQ9Qkpolw9p8EbGs9kqheFTEveSF9sb6CojkmwOuQHiupaKWSdtyVTBW2NymYxxYh)![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/81c554fd654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKIDwkiegU4ick8V1At5Tu_FaLN7MJhmGvdp0ZkQzQjMP0vVwcFLKBEBdXfZNP-DvZaV&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=012d651303b86f3142e4f639098982682916c98c&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpadcfdf8000f901aa21e1cbcf687af3800VoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIgQev2MyfyRBHcVS-n4gXCs-3oN0Lu2Zc50OL1CRKMxlpN7v-XpEp8YEuN7WDqA3yg_lKuXadg8-mloNkjCHVWQiEUSbT-GJVqCJQbxW0y1kP_W3KS56bR5TZwZPlw_jQ5HjkvCw3PS39eqpbT1zPdAX54NCXN1UGfOVGct_dKBecBjfWk0v6uGtm2RTKB9U_g)

2. Wedata中的机器学习节点本质上是一个安装了机器学习任务执行环境Tikit的Shell节点，用户需要在这个节点中编写Tikit命令，用于调度TIONE算力提交训练任务。

3. 进入节点配置页面后，单击“机器学习属性”，可进行数据源配置和算法开发配置。其中数据源配置可下拉选择当前训练任务所关联的数据源（若机器学习节点上游连接了其他节点，可在下方展示上游父任务数据源），下拉后会展示数据源ID，该ID可用于脚本开发和训练任务提交。

4. 在提交训练任务前，我们需要准备训练代码，TIONE提供轻量便捷的交互式开发环境Notebook，可点击右侧进入TIONE Notebook进行代码编写（跳转至TIONE Notebook实例创建页面后，会默认带上选中数据源的网络信息，若数据源为HDFS，也会默认在数据目录中选中该数据源）。若当前机器学习任务关联了某个Notebook实例，可直接下拉选中，页面会显示快速跳转链接和实例运行状态。
![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/81da67b7654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKIDCVVdIsswq4mvgLG6WWnRjdx3v7ehoPFtTUeGWqnVMuXcUcWIYHkEr5emMX83s11V&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=a4e8fa082969497e42a2819712c62ea8dac63d14&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpa05175db7f70d5a69a37399d32827bb17VoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIgU3XrlOuaRWctI2rTz2KxwISTBAPcPxAuH3bKFCDdZSCcSCP-5h43KkUaF0vvwHkMnaHKVAAGmR0P9S7OuqGcs8gHeuYys5uX7n35Qa-jqX4-YeAvx7fZ3yZUeDMjEWzeZ26q31NavHZozdHMmTHtiIe1uOR7adxR2VUp8gBOGzE6FozH_Vnj1icb1FDgULtx)


### 步骤五 使用TICLI编写训练任务提交命令
1. 进入机器学习节点后，使用前请先执行 tikit init --secretid=xxx --secretkey=xxx，进行初始化。secretId 和 secretKey 是腾讯云的访问密钥，获取方式：进入控制台，单击右上角头像，进入**访问管理** >  **API 密钥管理**获取。

2. 使用前输入tikit -h，获 tikit CLI 工具各命令的运行方式。

3. 根据当前所需的任务类型提交任务，可在当前 shell 节点运行命令测试，任务提交后可在运行日志中打印对应的 TI-ONE 任务 URL，可前 [TI-ONE 控制台](https://console.cloud.tencent.com/tione/v2) 查看训练任务详情。


### 步骤六 提交工作流进行周期调度

当完成工作流开发后，可以配置工作流周期调度参数，并且将工作流整体提交。提交完成后，可在**任务运维**模块查看工作流和任务，当生成周期性实例后，可在**实例运维**页面查看实例详情。调度相关详细操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72586)。
![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/820e0c1f654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKID-Y8fZ-aXrhYU_jPHiqiXl_U0xGjxnm8EfdLHp_09KFXs8IJ2nFt3ABLvsFlFTDxS&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=9feb47178bcb5fcf6ab10d82775de37853ad972f&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpa918c82d588de0d461ea9bb710152684bVoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIgZzzZ3_6JPsAw40YAcLkASjaSx-5b7V6adeO8FSpBXIixM6vdxhqZGubUWJrYy6mIHMLUWpgSmi6u4U6b6gFW_sVpgdz-eF69OdFbOePGDOh0MASQu1mexUyP_LW8QDBqsRvJSB-LDNr6RXKhDhIgx7yoHwkaB5dZgJxJ8_MK1c8h6Ph9tKJiZFBCbSocvnWO)![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/822166b5654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKIDUbZyOMCd6hA1lhFiFT47fDnHJS_0dFpQz07IgJ5zZvvhYdLVO1_xoiVwumiTcLBD&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=3525664c2a5330b66884578795b888b4d33e0a51&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpac7d94c9897b604155319e7f308dcd8faVoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIgm0BvlhPagnVBxSD55RLyuCUToN2XGLHqpbkyiFkCUNUsGgd4SJhiitmUWaAAHrzFse0euFPkOm9EKC6PxngEZDevMPxfbno19EbjZ-pUpxDzRDhRagCbNV_s9FmFVT34p7wTXzfeDVAEPtS7QCdI21TDuDjEiETDNYypES92lxuFro6zVvnfpNtiOZb0ZjdE)![](https://write-document-release-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/100022348635/82421839654e11ed87ca525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKIDI3ykH6iTs1L5aXyJ49Xl29mfjxpTi4lKqqXvcuoWL7xjVFt62xc3G6QO8gT7VT-c&q-sign-time=1671444923;1671448523&q-key-time=1671444923;1671448523&q-header-list=&q-url-param-list=&q-signature=b03b9f432ac92a8b3ea7e54f6dd884e3e1d11501&x-cos-security-token=AcimQGNTiVZ5EsUz9cJO7i1R2Qdsevpaa22ccc8583f236bf95d97fdd1f174134VoGKl4s7R1xQEAip9mIst5JCgrnj2bLOizQ2LkRRf6J872QkXTRT9gnKIgcxk9WywF7omXx4PEu-tZesec18gWBySgXa7-ATu87okipr1DRiHwjwrV-Oy0ugSz56APz-mH3XiC1pQVVmIXR5RoQ-lqeqGxE6SKTFbbs0l3-iLLmmGAJgHF5-x544bD81EoIgcsyzrEohvEuh1Uq4xAYNRhOKCjLY6FfzlfbxtrQ8mikHVW70FSn1b3PcuxPD1yJHEGJSVXOmImEGgcFPEiN5uQ2I5wOHKLaSP8okFPnmmEO6Hp2j3jqprP9ZfG_-bpApdHADJ_60uVoUJAUj_fWhGDaK7MEqbGaKWRAMXaF74uB_kQA6TP48rTJ-_hZEcrDn)