本文介绍如何使用 qGPU 离在线混部能力。
## 步骤1：部署相关组件
部署离在线混部功能的 qGPU 组件，需要部署 nano-gpu-scheduler 和 nano-gpu-agent。
#### 部署 nano-gpu-scheduler
nano-gpu-scheduler 涉及到 cluserole 及 cluserrolebinding，deployment 及 service，使用如下 yaml 部署。
调度策略如下：
- 对于调度在线 Pod 默认使用 spread 算法优先调度到没有离线 Pod 的 GPU 上。
- 对于调度离线 Pod 默认使用 binpack 算法优先调度到没有在线 Pod 的 GPU 上。

```
kind: Deployment
apiVersion: apps/v1
metadata:
  name: qgpu-scheduler
  namespace: kube-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: qgpu-scheduler
  template:
    metadata:
      labels:
        app: qgpu-scheduler
      annotations:
        scheduler.alpha.kubernetes.io/critical-pod: ''
    spec:
      hostNetwork: true
      tolerations:
        - effect: NoSchedule
          operator: Exists
          key: node-role.kubernetes.io/master
      serviceAccount: qgpu-scheduler
      containers:
        - name: qgpu-scheduler
          image: ccr.ccs.tencentyun.com/lionelxchen/mixed-scheduler:v61         
          command: ["qgpu-scheduler", "--priority=binpack"]
          env:
            - name: PORT
              value: "12345"
          resources:
            limits:
              memory: "800Mi"
              cpu: "1"
            requests:
              memory: "800Mi"
              cpu: "1"
---
apiVersion: v1
kind: Service
metadata:
  name: qgpu-scheduler
  namespace: kube-system
  labels:
    app: qgpu-scheduler
spec:
  ports:
    - port: 12345
      name: http
      targetPort: 12345
  selector:
    app: qgpu-scheduler
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: qgpu-scheduler
rules:
  - apiGroups:
      - ""
    resources:
      - nodes
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - events
    verbs:
      - create
      - patch
  - apiGroups:
      - ""
    resources:
      - pods
    verbs:
      - update
      - patch
      - get
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - bindings
      - pods/binding
    verbs:
      - create
  - apiGroups:
      - ""
    resources:
      - configmaps
    verbs:
      - get
      - list
      - watch
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: qgpu-scheduler
  namespace: kube-system
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: qgpu-scheduler
  namespace: kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: qgpu-scheduler
subjects:
  - kind: ServiceAccount
    name: qgpu-scheduler
    namespace: kube-system`
```

#### 部署 nano-gpu-agent
nano-gpu-agent 涉及到 cluserole 及 cluserrolebinding，deployment 及 service，使用如下 yaml 部署。
```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: qgpu-manager
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: qgpu-manager
  template:
    metadata:
      annotations:
        scheduler.alpha.kubernetes.io/critical-pod: ""
      labels:
        app: qgpu-manager
    spec:
      serviceAccount: qgpu-manager
      hostNetwork: true
      nodeSelector:
        qgpu-device-enable: "enable"
      initContainers:
        - name: qgpu-installer
          image: ccr.ccs.tencentyun.com/lionelxchen/mixed-manager:v27
          command: ["/usr/bin/install.sh"]
          securityContext:
            privileged: true
          volumeMounts:
            - name: host-root
              mountPath: /host
      containers:
        - image: ccr.ccs.tencentyun.com/lionelxchen/mixed-manager:v27
          command: ["/usr/bin/qgpu-manager", "--nodename=$(NODE_NAME)", "--dbfile=/host/var/lib/qgpu/meta.db"]
          name: qgpu-manager
          resources:
            limits:
              memory: "300Mi"
              cpu: "1"
            requests:
              memory: "300Mi"
              cpu: "1"
          env:
            - name: KUBECONFIG
              value: /etc/kubernetes/kubelet.conf
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
          securityContext:
            privileged: true
          volumeMounts:
            - name: device-plugin
              mountPath: /var/lib/kubelet/device-plugins
            - name: pod-resources
              mountPath: /var/lib/kubelet/pod-resources
            - name: host-var
              mountPath: /host/var
            - name: host-dev
              mountPath: /host/dev
      volumes:
        - name: device-plugin
          hostPath:
            path: /var/lib/kubelet/device-plugins
        - name: pod-resources
          hostPath:
            path: /var/lib/kubelet/pod-resources
        - name: host-var
          hostPath:
            type: Directory
            path: /var
        - name: host-dev
          hostPath:
            type: Directory
            path: /dev
        - name: host-root
          hostPath:
            type: Directory
            path: /
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: qgpu-manager
rules:
  - apiGroups:
      - ""
    resources:
      - "*"
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - events
    verbs:
      - create
      - patch
  - apiGroups:
      - ""
    resources:
      - pods
    verbs:
      - update
      - patch
      - get
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - nodes/status
    verbs:
      - patch
      - update
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: qgpu-manager
  namespace: kube-system
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: qgpu-manager
  namespace: kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: qgpu-manager
subjects:
  - kind: ServiceAccount
    name: qgpu-manager
    namespace: kube-system
```

## 步骤2：配置节点 Label
集群里的所有 qGPU 节点上都会自动打上 label："qgpu-device-enable=enable"。除此之外，对于期望开启了离在线功能的节点，需要您额外打上离在线 Label："mixed-qgpu-enable=enable"。

## 步骤3：配置业务属性
<dx-tabs>
::: 离线 Pod
通过`tke.cloud.tencent.com/app-class: offline`标识是一个离线 Pod，通过`tke.cloud.tencent.com/qgpu-core-greedy`申请离线算力，需要注意的是，离线 Pod 不支持多卡，申请的算力必须小于等于100。
```yaml
apiVersion: v1
kind: Pod
annotations:
 tke.cloud.tencent.com/app-class: offline
 spec:
  containers:
  - name: offline-container
    resources:
      requests:
	   tke.cloud.tencent.com/qgpu-core-greedy: xx // 离线算力
       tke.cloud.tencent.com/qgpu-memory: xx
```
:::
::: 在线 Pod
通过`tke.cloud.tencent.com/app-class: online`标识是一个在线 Pod，不需要申请算力，只需要申请显存。
```yaml
apiVersion: v1
kind: Pod
annotations:
 tke.cloud.tencent.com/app-class: online
 spec:
  containers:
  - name: online-container
    resources:
      requests:
	     tke.cloud.tencent.com/qgpu-memory: xx
```
:::
::: 普通 Pod
没有`tke.cloud.tencent.com/app-class`这个 Annotation，普通 Pod 支持多卡。
```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: common-container
    resources:
      requests:
       tke.cloud.tencent.com/qgpu-core: xx    
       tke.cloud.tencent.com/qgpu-memory: xx                                       
```              

:::
</dx-tabs>

 
