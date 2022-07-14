在启用了 istio 的 Smart DNS（智能 DNS）后，我们发现有些情况下 DNS 解析失败，例如：

- 基于 alpine 镜像的容器内解析 dns 失败。
- grpc 服务解析 dns 失败。

## 原因

Smart DNS 初期实现存在一些问题，响应的 DNS 数据包格式跟普通 DNS 有些差别，走底层库 glibc 解析没问题，但使用其它 dns 客户端可能就会失败:

- alpine 镜像底层库使用 musl libc，解析行为跟 glibc 有些不一样，musl libc 在这种这种数据包格式异常的情况会导致解析失败，而大多应用走底层库解析，导致大部分应用解析失败。
- 基于 c/c++ 的 grpc 框架的服务，dns 解析默认使用 c-ares 库，没有走系统调用让底层库解析，c-ares 在这种数据包异常情况，部分场景会解析失败。

## 修复

在 istio 1.9.2 的时候修复了这个问题，参考关键 PR [#31251](https://github.com/istio/istio/pull/31251) 以及其中一个 [issue](https://github.com/istio/istio/issues/31295) 。

## 规避

如果暂时无法升级 istio 到 1.9.2 以上，可以通过以下方式来规避：

- 基础镜像从 alpine 镜像到其它镜像 (其它基础镜像底层库基本都是 glibc)。
- c/c++ 的 grpc 服务，指定 `GRPC_DNS_RESOLVER` 环境变量为 `native`，表示走底层库解析，不走默认的 c-ares 库。环境变量解释参考 [GRPC 官方文档](https://github.com/grpc/grpc/blob/master/doc/environment_variables.md) 。
