为了方便您有效地使用腾讯云 TI 平台 TI-ONE 的 TI SDK，本文档为您提供入门指导。

## 概述
TI SDK 是腾讯云 TI 平台 TI-ONE 提供的开源软件包，让用户可以通过代码（SDK/API）向 TI-ONE 提交机器学习和深度学习的训练任务。SDK 简单易用，让用户专注于模型和算法等业务逻辑，无需关心底层硬件和系统配置；同时 SDK 又通过镜像规范和集成云上各种组件服务提供了强大的灵活性，例如，用户可以通过 SDK 提供的训练日志、资源监控和指标监控等特性对训练过程了如指掌。目前您可以在腾讯云 TI 平台的 Notebook 内直接使用 TI SDK；也可以在本地 IDE 环境中使用 TI SDK，直接使用 pip 命令安装：pip install ti-sdk-python 。

## 核心特性

- 内置了深度优化的 TensorFlow 和 PyTorch 等多种流行的深度学习框架，提供单机和多机多卡训练的能力。
- 对接丰富的云上服务（CLS、CM、COS、CBS、CFS、VPC、CAM、CLB 等），利用对象存储 COS、容器服务 TKE、日志服务 CLS、云监控 Monitor 等腾讯云上成熟的组件作为支撑，帮助用户在云上快速搭建自己的机器学习和深度学习训练任务。
- 通过 API/SDK 方式使用机器学习平台能力，支持 CPU 和 GPU 等多种算力类型。
- 跟用户 VPC 互通、安全访问用户 VPC 内的服务和资源。 
- 对接 CFS（Cloud File System），支持超大文件和高速 I/O 的述求。
- 支持自定义镜像（满足腾讯云 TI 平台镜像规范）。

## 资源规格

TI SDK 提供的算力类型和配额默认如下，计费详情您可以参考 [购买指南](https://cloud.tencent.com/document/product/851/39693)。如果您需要更多的配额项数量，可通过 [配额申请工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=350&level1_name=计算与网络&level2_name=容器服务CCS) 提出配额申请。

| 算力类型                    | 默认值 |
| :-------------------------- | :----- |
| TI.SMALL2.1core2g           | 20     |
| TI.SMALL4.1core4g           | 20     |
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
