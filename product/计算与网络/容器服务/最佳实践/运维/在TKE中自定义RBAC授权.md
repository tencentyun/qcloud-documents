## 操作场景

容器服务 TKE 支持通过在控制台使用**授权管理**功能管理子账号的常用授权，也可以使用自定义 YAML 的方式（ [RBAC 授权](https://kubernetes.io/zh/docs/reference/access-authn-authz/rbac/) ）来满足更加个性化的授权需求，Kubernetes RBAC 授权说明和原理如下：

- **权限对象（Role 或 ClusterRole）**： 权限对象使用 apiGroups、resources 和 verbs 来定义权限情况。其中：
	- Role 权限对象：作用于特定命名空间。 
	- ClusterRole 权限对象：可复用于多个命名空间授权 （Rolebinding）或为整个集群授权（ClusterRoleBinding）。 
- **授权对象（Subjects）**： 权限授予的主体对象，分别为 User、Group 和 ServiceAccount 三种类型主体。 
- **权限绑定（Rolebinding 或 ClusterRoleBinding）**： 将权限对象和授权对象进行组合绑定。其中：
	- Rolebinding：作用于某个命名空间。 
	- ClusterRoleBinding：作用于整个集群。 

![RBAC](https://main.qcloudimg.com/raw/4ec83327aca864ded5798c1018d39d8e.jpg)


如上图所示， Kubernetes RBAC 授权主要提供以下3种常用权限绑定方式，本文将为您分别介绍如何使用这3种权限绑定方式实现对用户的授权管理。 


|方式 | 说明 | 
|---------|---------|
| [方式1：作用于单个命名空间的权限绑定](#way1) |  RoleBinding 引用 Role 对象，为 Subjects 只授予某单个命名空间下资源权限。 |
|[方式2：多个命名空间复用集群权限对象绑定](#way2) | 多个命名空间下不同的 Rolebinding 可引用同一个 ClusterRole 对象模板为 Subjects 授予相同模板权限。 | 
|[方式3：整个集群权限的绑定](#way3) | ClusterRoleBinding 引用 ClusterRole 模板，为 Subjects 授予整个集群的权限。 | 


>?除上述3种方式之外，从 Kubernetes RBAC 1.9版本开始，集群角色（ClusterRole）还可通过使用 aggregationRule 组合其他 ClusterRoles 的方式进行创建，本文不作详细介绍，您可参见官网文档 [Aggregated ClusterRoles]( https://kubernetes.io/zh/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles) 说明。 






## 操作步骤


### 方式1：作用于单个命名空间的权限绑定[](id:way1)

此方式主要用于为某一个用户绑定某一个命名空间下的相关权限，适用于需要细化权限的场景。例如，开发、测试、运维人员只能在各自的命名空间下对资源操作。以下将为您介绍如何在 TKE 中实现作用于单个命名空间的权限绑定。 

1. 使用以下 Shell 脚本，创建测试命名空间、ServiceAccount  类型的测试用户并设置集群访问凭证（token）认证 。示例如下：
```bash
USERNAME='sa-acc' # 设置测试账户名
NAMESPACE='sa-test' # 设置测试命名空间名
CLUSTER_NAME='cluster_name_xxx' # 设置测试集群名
# 创建测试命名空间
kubectl  create namespace ${NAMESPACE} 
# 创建测试 ServiceAccount 账户
kubectl create sa ${USERNAME} -n ${NAMESPACE} 
# 获取 ServiceAccount 账户自动创建的 Secret token 资源名
SECRET_TOKEN=$(kubectl get sa ${USERNAME} -n ${NAMESPACE} -o jsonpath='{.secrets[0].name}')
# 获取 secrets 的明文 Token
SA_TOKEN=$(kubectl get secret ${SECRET_TOKEN} -o jsonpath={.data.token} -n sa-test | base64 -d)
# 使用获取到的明文 token 信息设置一个 token 类型的访问凭证
kubectl config set-credentials ${USERNAME} --token=${SA_TOKEN}
# 设置访问集群所需要的 context 条目
kubectl config set-context ${USERNAME} --cluster=${CLUSTER_NAME} --namespace=${NAMESPACE} --user=${USERNAME}
```
2. 执行 `kubectl config get-contexts` 命令，查看生成的 contexts 条目。如下图所示： 
![image-20201020105559159](https://main.qcloudimg.com/raw/40f7223c29d2c78b5e1671afe28933ba.png)
3. 创建一个 Role 权限对象资源 sa-role.yaml 文件。示例如下：
<dx-codeblock>
:::  yaml
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata: 
  namespace: sa-test # 指定 Namespace
  name: sa-role-test
rules: # 设置权限规则
- apiGroups: ["", "extensions", "apps"]
  resources: ["deployments", "replicasets", "pods"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
:::
</dx-codeblock>
4. 创建一个 RoleBinding 对象资源 sa-rb-test.yaml 文件。如下权限绑定表示，添加 ServiceAccount 类型的 sa-acc 用户在 sa-test 命名空间具有 sa-role-test（Role 类型）的权限。示例如下：
<dx-codeblock>
:::  yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata: 
  name: sa-rb-test
  namespace: sa-test 
subjects: 
- kind: ServiceAccount
  name: sa-acc
  namespace: sa-test # ServiceAccount 所在 Namespace 
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
roleRef: 
  kind: Role
  name: sa-role-test
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
:::
</dx-codeblock>
5. 从下图验证结果可以得出，当 Context 为 sa-context 时，默认命名空间为 sa-test，且拥有 sa-test 命名空间下 sa-role-test（Role）对象中配置的权限，但在 default 命名空间下不具有任何权限。 
![image-20201020111456470](https://main.qcloudimg.com/raw/237a717756c26ed8ed654851c2d7aa01.png)




### 方式2：多个命名空间复用集群权限对象绑定[](id:way2)

此方式主要用于为用户授予多个命名空间下相同的权限，适用于使用一个权限模板为多个命名空间绑定授权的场景，例如需要为 DevOps 人员在多个命名空间绑定相同资源操作的权限。以下将为您介绍如何在 TKE 中使用多个命名空间复用集群权限绑定授权。 

1. 使用以下 Shell 脚本，创建使用 X509 自签证书认证的用户、证书签名请求（CSR）和证书审批允许信任并设置集群资源访问凭证 Context。示例如下：
```bash
USERNAME='role_user' # 设置需要创建的用户名
NAMESPACE='default' # 设置测试命名空间名
CLUSTER_NAME='cluster_name_xxx' # 设置测试集群名
# 使用 Openssl 生成自签证书 key
openssl genrsa -out ${USERNAME}.key 2048
# 使用 Openssl 生成自签证书CSR 文件, CN 代表用户名，O 代表组名
openssl req -new -key ${USERNAME}.key -out ${USERNAME}.csr -subj "/CN=${USERNAME}/O=${USERNAME}" 
# 创建 Kubernetes 证书签名请求（CSR）
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1beta1
kind: CertificateSigningRequest
metadata:
      name: ${USERNAME}
spec:
      request: $(cat ${USERNAME}.csr | base64 | tr -d '\n')
      usages:
      - digital signature
      - key encipherment
      - client auth
EOF
# 证书审批允许信任
kubectl certificate approve ${USERNAME}
# 获取自签证书 CRT
kubectl get csr ${USERNAME} -o jsonpath={.status.certificate} | base64 --decode > ${USERNAME}.crt
# 设置集群资源访问凭证（X509 证书）
kubectl config set-credentials ${USERNAME} --client-certificate=${USERNAME}.crt --client-key=${USERNAME}.key
# 设置 Context 集群、默认Namespace 等
kubectl config set-context  ${USERNAME} --cluster=${CLUSTER_NAME} --namespace=${NAMESPACE} --user=${USERNAME}
```
2. 创建一个 ClusterRole 对象资源 test-clusterrole.yaml 文件。示例如下：
<dx-codeblock>
:::  yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata: 
  name: test-clusterrole
rules: 
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list", "create"]
:::
</dx-codeblock>
3. 创建一个 RoleBinding 对象资源 clusterrole-rb-test.yaml 文件，如下权限绑定表示，添加自签证书认证类型的 role_user 用户在 default 命名空间具有 test-clusterrole（ClusterRole 类型）的权限。示例如下：
<dx-codeblock>
:::  yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata: 
  name: clusterrole-rb-test
  namespace: default 
subjects: 
- kind: User
  name: role_user
  namespace: default # User 所在 Namespace 
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
roleRef: 
  kind: ClusterRole
  name: test-clusterrole
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
:::
</dx-codeblock>
4. 从下图验证结果可以得出，当 Context 为 role_user 时，默认命名空间为 default，且拥有 test-clusterrole 权限对象配置的规则权限。 
![image-20201020114653469](https://main.qcloudimg.com/raw/2d57f7719b3f8d1b187b41943e396bd5.png)
5. 创建第二个  RoleBinding 对象资源 clusterrole-rb-test2.yaml 文件，如下权限绑定表示，添加自签证书认证类型的 role_user 用户在 default2 命名空间具有 test-clusterrole（ClusterRole 类型）的权限。 
<dx-codeblock>
:::  yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata: 
  name: clusterrole-rb-test
  namespace: default2 
subjects: 
- kind: User
  name: role_user
  namespace: default # User 所在 Namespace 
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
roleRef: 
  kind: ClusterRole
  name: test-clusterrole
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
:::
</dx-codeblock>
6. 从下图验证结果可以得出，在 default2 命名空间下， role_user 同样拥有 test-clusterrole 配置的规则权限。至此通过上述步骤实现了多个命名空间复用集群权限的绑定。 
![image-20201020114512915](https://main.qcloudimg.com/raw/b948a35d0e49f1f99084b2cf8e6b7eb9.png)



### 方式3：整个集群权限的绑定[](id:way3)

此方式主要用于为某个用户绑定所有命名空间下的权限（集群范围），适用于集群范围内授权的场景。例如，日志收集权限、管理人员权限等，以下将为您介绍在如何在 TKE 中使用多个命名空间复用集群权限绑定授权。 

1. 创建一个 ClusterRoleBinding 对象资源 clusterrole-crb-test3.yaml 文件，如下权限绑定表示，添加证书认证类型的 role_user 用户在整个集群具有 test-clusterrole（ClusterRole 类型） 的权限。 
<dx-codeblock>
:::  yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata: 
  name: clusterrole-crb-test
subjects: 
- kind: User
  name: role_user
  namespace: default # User 所在 Namespace 
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
roleRef: 
  kind: ClusterRole
  name: test-clusterrole
  apiGroup: ""  # 默认 apiGroup 组为 rbac.authorization.k8s.io
:::
</dx-codeblock>
2. 从下图验证结果可以得出，应用了权限绑定的 YAML 后，role_user 拥有集群范围的 test-clusterrole 权限。 
![image-20201020141737129](https://main.qcloudimg.com/raw/5f3415f45bac5b622264fd4929e104a5.png)



## 总结

容器服务 TKE 控制台授权管理功能结合了腾讯云访问权限管理和 Kubernetes RBAC 授权模式，界面配置简单方便，能满足大部分腾讯云子账号的权限控制场景，自定义 YAML 权限绑定方式适用于复杂和个性化的用户权限控制场景，更具灵活性，用户可根据实际授权需求选择合适的权限管理方式。 

