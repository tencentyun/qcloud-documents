qGPU 是腾讯云推出的 GPU 共享技术，支持在多个容器间共享 GPU 卡并提供容器间显存与算力强隔离的能力，从而在更小粒度使用 GPU 卡的基础上，保证业务安全，达到提高 GPU 使用率、降低用户成本的目的。
qGPU 依托腾讯云容器服务 TKE 对外开源的 Nano GPU 框架，可实现对 GPU 算力与显存的细粒度调度，并支持多容器共享 GPU 与多容器跨 GPU 资源分配。同时依赖底层强大的 qGPU 隔离技术，可实现 GPU 显存和算力的强隔离，在通过共享使用 GPU 的同时，尽量保证业务性能与资源不受干扰。

<dx-alert infotype="explain" title="">
 qGPU 目前正在内测中，如需使用请通过 [在线咨询](https://cloud.tencent.com/online-service?from=sales&source=PRESALE) 联系我们。
</dx-alert>

## qGPU 功能及优势


qGPU 方案通过对 NVIDIA GPU 卡上任务的有效调度，达到给多个容器共享使用的目的。功能优势如下：

- 灵活性：用户可以自由配置 GPU 的显存大小和算力占比。
- 云原生：支持标准的 Kubernetes 和 NVIDIA Docker 方案。
- 兼容性：镜像不修改、CUDA 库不替换、业务不重编、易部署实现业务无感知。
- 高性能：在底层对 GPU 设备进行操作，高效收敛，吞吐接近0损耗。
- 强隔离：支持显存和算力的严格隔离。

## 方案框架图
qGPU 方案框架图如下：
![](https://main.qcloudimg.com/raw/ac99fd3de566decc2510df90394fb44a.png)

## 使用 qGPU
请参考 [使用 qGPU](https://cloud.tencent.com/document/product/560/66233) 了解并开始使用。
