为了方便您有效地使用智能钛机器学习平台的 Notebook，本文档为您提供入门指导。

## 概述
Notebook 是智能钛机器学习平台为开发者量身打造的灵活的交互式开发工具，您可以在智能钛 Notebook 中完成数据准备、数据预处理、算法调试与模型训练，无需多平台切换。智能钛 Notebook 提供了多种内核供您选择，同时也支持自行安装第三方库。使用过程中，您仅需为运行 Notebook 时所消耗的算力及存储资源付费，没有最低费用，也不需要前期承诺。

## 操作界面
智能钛机器学习平台的 Notebook 整体操作界面如下，右侧为 Notebook 内容展示区域，左栏主要为文件管理和各类功能键。
![](https://main.qcloudimg.com/raw/fd2c462ac8501edb3e77f4e6c5d559d8.png)

## 核心特性

- 提供多种资源规格供用户自由选择。
- 支持各类资源灵活切换，降低使用成本。
- 内置TI SDK，用户可以在 Notebook 中向 TI 提交训练任务。
- 内置多种内核环境，支持自定义安装第三方库。
- 开放 Root 权限，支持自由选择是否使用 Root 权限访问 Notebook。
- 支持自由选择配置自有的 VPC 网络，支持访问外网。

## 资源规格

智能钛 Notebook 提供的算力类型和配额默认如下，计费详情您可以参考 [购买指南](https://cloud.tencent.com/document/product/851/39693)。如果您需要更多的配额项数量，可通过 [配额申请工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=350&level1_name=计算与网络&level2_name=容器服务CCS) 提出配额申请。

| 算力类型                    | 默认值 |
| :-------------------------- | :----- |
| TI.MEDIUM4.2core4g          | 20     |
| TI.MEDIUM8.2core8g          | 20     |
| TI.LARGE8.4core8g           | 20     |
| TI.LARGE16.4core16g         | 20     |
| TI.2XLARGE16.8core16g       | 20     |
| TI.2XLARGE32.8core32g       | 20     |
| TI.3XLARGE24.12core24g      | 20     |
| TI.3XLARGE48.12core48g      | 20     |
| TI.4XLARGE32.16core32g      | 20     |
| TI.4XLARGE64.16core64g      | 20     |
| TI.6XLARGE48.24core48g      | 20     |
| TI.6XLARGE96.24core96g      | 15     |
| TI.8XLARGE64.32core64g      | 17     |
| TI.8XLARGE128.32core128g    | 11     |
| TI.12XLARGE96.48core96g     | 11     |
| TI.12XLARGE192.48core192g   | 8      |
| TI.16XLARGE128.64core128g   | 9      |
| TI.16XLARGE256.64core256g   | 6      |
| TI.20XLARGE320.80core320g   | 5      |
| TI.GN10X.2XLARGE40.1xV100   | 11     |
| TI.GN10X.4XLARGE80.2xV100   | 5      |
| TI.GN10X.9XLARGE160.4xV100  | 2      |
| TI.GN10X.18XLARGE320.8xV100 | 1      |
| 总实例数                    | 20     |



## 使用说明

在体验之前，您需要完成 [注册与开通服务](https://cloud.tencent.com/document/product/851/39086)。
- 您可以通过**快速入门**，了解如何在 Notebook 中 [创建实例](https://cloud.tencent.com/document/product/851/40073) ，[管理实例](https://cloud.tencent.com/document/product/851/41626)， [使用内置案例](https://cloud.tencent.com/document/product/851/40074)。
- 您可以参考**最佳实践** [用 Notebook 实现手写数字识别](https://cloud.tencent.com/document/product/851/38030)，体验使用 Notebook 建模的完整流程。
- 您可以通过**操作指南**，进一步了解如何 [设置内核](https://cloud.tencent.com/document/product/851/41627)，[安装第三方库](https://cloud.tencent.com/document/product/851/40119)，进行 [数据的上传与下载](https://cloud.tencent.com/document/product/851/40143) 等操作。
- 如果您在使用过程中遇到问题，请查看常见问题。



