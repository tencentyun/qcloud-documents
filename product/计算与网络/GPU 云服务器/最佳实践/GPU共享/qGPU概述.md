qGPU 是腾讯云推出的 GPU 共享技术，支持在多个容器间共享 GPU 卡并提供容器间显存与算力强隔离的能力，从而在更小粒度使用 GPU 卡的基础上，保证业务安全，达到提高 GPU 使用率、降低用户成本的目的。
qGPU 依托腾讯云容器服务 TKE 对外开源的 Nano GPU 框架，可实现对 GPU 算力与显存的细粒度调度，并支持多容器共享 GPU 与多容器跨 GPU 资源分配。同时依赖底层强大的 qGPU 隔离技术，可实现 GPU 显存和算力的强隔离，在通过共享使用 GPU 的同时，尽量保证业务性能与资源不受干扰。

## qGPU 功能及优势


qGPU 方案通过对 NVIDIA GPU 卡上任务的有效调度，达到给多个容器共享使用的目的。功能优势如下：

- 灵活性：用户可以精细配置 GPU 的显存大小和算力占比。
- 强隔离：支持显存和算力的严格隔离。
- 在离线：支持业界唯一在离线混部能力，GPU 利用率压榨到极致。
- 覆盖度：支持主流架构 Volta（如 V100）、Turing（如 T4 等）、Ampere（如 A100、A10）。
- 云原生：支持标准的 Kubernetes 和 NVIDIA Docker。
- 兼容性：业务不重编、CUDA 库不替换、业务无感。
- 高性能：在底层对 GPU 设备进行操作，高效收敛，吞吐接近0损耗。

## 方案框架图
qGPU 方案框架图如下：
![](https://main.qcloudimg.com/raw/ac99fd3de566decc2510df90394fb44a.png)

## 使用 qGPU
请参考 [qGPU 使用](https://cloud.tencent.com/document/product/560/66233) 了解并开始使用。
