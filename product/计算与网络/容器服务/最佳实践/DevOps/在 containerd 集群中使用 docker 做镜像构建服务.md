## 操作场景

在 Kubernetes 集群中，部分 CI/CD 流水线业务可能需要使用 Docker 来提供镜像打包服务。可通过宿主机的 Docker 实现，将 Docker 的 UNIX Socket（`/var/run/docker.sock`）作为 hostPath 挂载到 CI/CD 的业务 Pod 中，之后在容器里通过 UNIX Socket 来调用宿主机上的 Docker 进行构建。该方式操作简单，比真正意义上的 Docker in Docker 更节省资源，但该方式可能会遇到以下问题：
- 无法运行在 Runtime 是 containerd 的集群中。
- 如果不加以控制，可能会覆盖掉节点上已有的镜像。
- 在需要修改 Docker Daemon 配置文件的情况下，可能会影响到其他业务。
- 在多租户的场景下并不安全，当拥有特权的 Pod 获取到 Docker 的 UNIX Socket 之后，Pod 中的容器不仅可以调用宿主机的 Docker 构建镜像、删除已有镜像或容器，甚至可以通过 `docker exec` 接口操作其他容器。

针对上述第1个问题，Kubernetes 在官方博客宣布将在1.22版本之后弃用 Docker，这部分用户可能会将业务转投到 containerd。对于部分需要 containerd 集群，而不改变 CI/CD 业务流程仍使用 Docker 构建镜像一部分的场景，可以通过在原有 Pod 上添加 DinD 容器作为 Sidecar 或者使用 DaemonSet 在节点上部署专门用于构建镜像的 Docker 服务。
本文将为您介绍以下两种方式实现在 CI/CD 流水线业务上使用 Docker 构建镜像：
- [方式1：使用 DinD 作为 Pod 的 Sidecar](#DinD)
- [方式2：使用 DaemonSet 在每个 containerd 节点上部署 Docker](#DaemonSet)

## 操作步骤

### 方式1：使用 DinD 作为 Pod 的 Sidecar[](id:DinD)

DinD（Docker in Docker）实现原理可参见 [DinD](https://hub.docker.com/_/docker) 官方文档，本文示例将为 clean-ci 容器添加一个 Sidecar，配合 emptyDir 使 clean-ci 容器可以通过 UNIX Socket 访问 DinD 容器。示例如下：
```yaml
apiVersion: v1
kind: Pod
metadata:
   name: clean-ci
spec:
   containers:
   - name: dind
     image: 'docker:stable-dind'
     command:
     - dockerd
     - --host=unix:///var/run/docker.sock
     - --host=tcp://0.0.0.0:8000
     securityContext:
       privileged: true
     volumeMounts:
     - mountPath: /var/run
       name: cache-dir
   - name: clean-ci
     image: 'docker:stable'
     command: ["/bin/sh"]
     args: ["-c", "docker info >/dev/null 2>&1; while [ $? -ne 0 ] ; do sleep 3; docker info >/dev/null 2>&1; done; docker pull library/busybox:latest; docker save -o busybox-latest.tar library/busybox:latest; docker rmi library/busybox:latest; while true; do sleep 86400; done"]
     volumeMounts:
     - mountPath: /var/run
       name: cache-dir
   volumes:
   - name: cache-dir
     emptyDir: {}
```

### 方式2：使用 DaemonSet 在每个 containerd 节点上部署 Docker[](id:DaemonSet)

该方式较为简单，直接在 containerd 集群中下发 DaemonSet 即可（挂载 hostPath），为不影响节点上 `/var/run` 路径，可以指定其他路径。

1. 使用以下 YAML 部署 DaemonSet。示例如下：
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
      name: docker-ci
spec:
      selector:
        matchLabels:
          app: docker-ci
      template:
        metadata:
          labels:
            app: docker-ci
        spec:
          containers:
          - name: docker-ci
            image: 'docker:stable-dind'
            command:
            - dockerd
            - --host=unix:///var/run/docker.sock
            - --host=tcp://0.0.0.0:8000
            securityContext:
              privileged: true
            volumeMounts:
            - mountPath: /var/run
              name: host
          volumes:
          - name: host
            hostPath:
              path: /var/run
```
2. 将业务 Pod 与 DaemonSet 共享同一个 hostPath。示例如下：
```yaml
apiVersion: v1
kind: Pod
metadata:
      name: clean-ci
spec:
      containers:
      - name: clean-ci
        image: 'docker:stable'
        command: ["/bin/sh"]
        args: ["-c", "docker info >/dev/null 2>&1; while [ $? -ne 0 ] ; do sleep 3; docker info >/dev/null 2>&1; done; docker pull library/busybox:latest; docker save -o busybox-latest.tar library/busybox:latest; docker rmi library/busybox:latest; while true; do sleep 86400; done"]
        volumeMounts:
        - mountPath: /var/run
          name: host
      volumes:
      - name: host
        hostPath:
          path: /var/run
```
