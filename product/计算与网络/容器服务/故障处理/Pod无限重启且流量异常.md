
## 故障现象 
Pod 突然不断重启，期间有流量进入，这部分流量异常。

## 原因 
1.  Pod 之前所在节点异常，重建漂移到了其它节点去启动。
2.  Pod 重建后由于基础镜像中依赖的一个服务有问题导致启动较慢，因为同时配置了 ReadinessProbe 与 LivenessProbe，大概率是启动时所有健康检查都失败，达到 LivenessProbe 失败次数阈值，又被重启。
3.  Pod 配置了 preStop 实现优雅终止，被重启前会先执行 preStop，优雅终止的时长较长，preStop 期间 ReadinessProbe 还会继续探测。
4.  探测方式使用的 TCP 探测，进程优雅终止过程中 TCP 探测仍然会成功（没完全退出前端口监听仍然存在），但实际此时进程已不会处理新请求了。
5.  LivenessProbe 结果不会影响 Pod Ready 状态，是否 Ready 主要取决于 ReadinessProbe 结果，由于 preStop 期间 ReadinessProbe 是成功的，Pod 就变 Ready 了。
6.  Pod Ready 但实际无法处理请求，业务就会异常。

## 总结 
1.  Pod 慢启动 + 存活探测 导致被无限重启。需要延长 `initialDelaySeconds` 或 [StartProbe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-startup-probes) 来保护慢启动容器。
2.  TCP 探测方式不能完全真实反应业务健康状态，导致在优雅终止过程中，ReadinessProbe 探测成功让流量放进来而业务却不会处理，导致流量异常。需要使用更好的探测方式，建议业务提供 HTTP 探活接口，使用 HTTP 探测业务真实健康状态。
 
