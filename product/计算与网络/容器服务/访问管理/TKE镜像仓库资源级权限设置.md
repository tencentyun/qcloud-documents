## 容器镜像服务权限介绍

腾讯云容器镜像的地址格式是：`ccr.ccs.tencentyun.com/${namespace}/${name}:${tag}`。
镜像仓库的权限围绕以下两个字段进行设置：
- `${namespace}`: 镜像仓库所属命名空间。
- `${name}`: 镜像仓库名称。

>! 命名空间 `${namespace}` 及镜像名字 `${name}` 中不能包含斜杠 “/”。
> `${tag}` 字段目前只实现了删除操作鉴权，请参考 [镜像 Tag 权限](#Tag)。
> 
通过`${namespace}`，`${name}`两个字段，管理者可以为协作者制定详细的权限方案，实现灵活的权限管理。   
例如：
- 允许协作者 A 拉取镜像
- 禁止协作者 A 删除镜像
- 禁止协作者 B 拉取命名空间 ns1 中的镜像

如果您不需要详细管理镜像仓库权限，可以使用 [预设策略授权](#PresetPpolicyAuthorization)。
如果您需要细致地管理协作者权限，请使用 [自定义策略授权](#CustomPolicyAuthorization)。
容器镜像服务权限基于腾讯云 CAM 进行管理，您可以详细了解 CAM 的使用方法：
- [用户管理](https://cloud.tencent.com/document/product/598/10599)
- [策略管理](https://cloud.tencent.com/document/product/598/10601)
- [授权管理](https://cloud.tencent.com/document/product/598/10602)

[](id:PresetPpolicyAuthorization)
## 预设策略授权

为了简化容器镜像服务权限管理，容器镜像服务内置了两个预设策略：
- [镜像仓库（CCR）全读写访问权限](https://console.cloud.tencent.com/cam/policy/detail/419082&QcloudCCRFullAccess&2)
该预设策略配置了容器镜像服务所有权限，如果协作者关联该预设策略后，将与管理者拥有相同的镜像仓库权限。详情请查看 [权限列表](https://cloud.tencent.com/document/product/457/11528)。
- [镜像仓库（CCR）只读访问权限](https://console.cloud.tencent.com/cam/policy/detail/419084&QcloudCCRReadOnlyAccess&2)
该预设策略包含了容器镜像服务只读操作的权限，如果协作者在容器镜像服务中**只**关联了该预设策略，则以下操作将被禁止：
 - `docker push` 推送镜像
 - 新建镜像仓库命名空间
 - 删除镜像仓库命名空间
 - 创建镜像仓库
 - 删除镜像仓库
 - 删除镜像 Tag

如果您不了解如何为协作者关联预设策略，请参考 CAM 文档：[策略](https://cloud.tencent.com/document/product/598/10601)、[授权管理](https://cloud.tencent.com/document/product/598/10602)。

[](id:CustomPolicyAuthorization)
## 自定义策略授权

通过自定义策略，管理者可以为不同的协作者关联不同的权限。
当您分配权限时，请考虑这些要素：
- **资源(resource)**：该权限策略关联哪些镜像仓库，例如所有镜像仓库描述为 `qcs::ccr:::repo/*`，详见 [CAM 资源描述方式](https://cloud.tencent.com/document/product/598/10606)。
- **动作(action)**：该权限策略对**资源(resource)**进行哪些操作，如删除、新建等，通常使用接口进行描述。
- **效力(effect)** ：该权限策略对协作者表现出的效果（允许/拒绝）。

一旦您规划好权限设置，就可以开始进行权限分配。下面我们以“允许协作者创建镜像仓库”为例进行说明：
#### 步骤1：创建自定义 [策略](https://cloud.tencent.com/document/product/598/10601)。
1. 在访问管理控制台的 [策略](https://console.cloud.tencent.com/cam/policy) 页面，单击左上角的**新建自定义策略**。
2. 在弹出的选择创建方式窗口中，单击**按策略语法创建**，进入选择策略模板页面。
3. 在选择策略模板页面，选择**按策略语法创建** > **空白模板**。
4. 单击**下一步**，进入编辑策略页面。
5. 在编辑策略页面，将策略名称设置为 `ccr-policy-demo`，并将以下内容填入“编辑策略内容”编辑框中。
```
        {
            "version": "2.0",
            "statement": [{
                "action": "ccr:CreateRepository",
                "resource": "qcs::ccr:::repo/*",
                "effect": "allow"
            }]
        }
```
6. 确认策略名称、策略内容后单击**完成**，完成按策略语法创建自定义策略操作。

#### 步骤2：关联自定义策略。
步骤1中的策略（ccr-policy-demo）创建完成以后，您可以将其关联到任意协作者，详见 [授权管理](https://cloud.tencent.com/document/product/598/10602)。策略关联完成后协作者即拥有**在任意命名空间下创建镜像仓库权限**。
`"resource": "qcs::ccr:::repo/*"` 格式说明：
 - `qcs::ccr:::` 为固定格式，表示开发商的腾讯云容器镜像仓库服务。
 - `repo` 为固定前缀，代表资源类型，这里是镜像仓库。
 - 斜杠(`/`)后面的 `*` 表示匹配所有镜像仓库。

关于 resource 更详细的描述，请参考 [CAM 资源描述方式](https://cloud.tencent.com/document/product/598/10606)。

#### 按资源进行授权

您可以同时为多个资源进行授权。例如：“允许删除命名空间 foo, bar 中的镜像仓库”，可以创建下面的自定义策略：
```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:BatchDeleteRepository",
            "ccr:DeleteRepository"
        ],
        "resource": [
            "qcs::ccr:::repo/foo/*",
            "qcs::ccr:::repo/bar/*"
        ],
        "effect": "allow"
    }]
}
```

>!
> - `qcs::ccr:::repo/foo/*` 中 `foo/*` 表示镜像仓库命名空间 `foo` 下的所有镜像。
> - `qcs::ccr:::repo/bar/*` 中 `bar/*` 表示镜像仓库命名空间 `bar` 下的所有镜像。

#### 按动作(接口)进行授权

您可以对一个资源配置多个 `action`，实现资源权限的统一管理。例如：“允许创建、删除、push 命名空间 foo 中的镜像仓库”，可以创建下面的自定义策略：
```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:CreateRepository",
            "ccr:BatchDeleteRepository",
            "ccr:DeleteRepository",
            "ccr:push"
        ],
        "resource": "qcs::ccr:::repo/foo/*",
        "effect": "allow"
    }]
}
```

## 权限列表

#### docker client 权限

resource： `qcs::ccr:::repo/${namespace}/${name}`  
action：
- `ccr:pull` 使用 docker 命令行 pull 镜像
- `ccr:push` 使用 docker 命令行 push 镜像

#### 命名空间权限

resource： `qcs::ccr:::repo/${namespace}`  
action:
- `ccr:CreateCCRNamespace`     新建镜像仓库命名空间
- `ccr:DeleteUserNamespace`    删除镜像仓库命名空间



#### 镜像仓库权限

resurce： `qcs::ccr:::repo/${namespace}/${name}`  
action：
- `ccr:CreateRepository`        创建镜像仓库
- `ccr:DeleteRepository`        删除镜像仓库
- `ccr:BatchDeleteRepository`   批量删除镜像仓库
- `ccr:GetUserRepositoryList`  查看镜像仓库列表


>! 若要阻止协作者删除某些镜像，请配置多个 action 来实现。
>
例如，禁止删除任何镜像仓库。
```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:BatchDeleteRepository",
            "ccr:DeleteRepository"
        ],
        "resource": "qcs::ccr:::repo/*",
        "effect": "deny"
    }]
}
```

[](id:Tag)
####  镜像Tag权限

resource： `qcs::ccr:::repo/${namespace}/${name}:${tag}`  
action： `ccr:DeleteTag` 删除镜像 Tag 权限


