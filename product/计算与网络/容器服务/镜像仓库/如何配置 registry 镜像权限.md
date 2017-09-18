腾讯云容器服务的镜像由三部分组成，其形式为：`ccr.ccs.tencentyun.com/${namespace}/${name}:$tag`。镜像服务的权限配置围绕着命名空间 `namespace` 及名字 `name` 这两个字段进行。
>**注意：**
>命名空间 `namespace` 及名字 `name` 中不能包含斜杠 “ / ”。 

## docker client 权限配置
资源： `qcs::ccr:::repo/${namespace}/${name}`。
action：
* `ccr:pull`
* `ccr:push`

分配 `push` 和 `pull` 权限：
```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:pull",
            "ccr:push"
        ],
        "resource": "qcs::ccr:::repo/${namespace}/${name}",
        "effect": "allow"
    }]
}
```
分配 `pull` 权限，禁止 `push` 权限：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:pull",
        "resource": "qcs::ccr:::repo/${namespace}/${name}",
        "effect": "allow"
    }, {
        "action": "ccr:push",
        "resource": "qcs::ccr:::repo/${namespace}/${name}",
        "effect": "deny"
    }]
}
```
分配某个 **命名空间下所有镜像** 权限：
```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:pull",
            "ccr:push"
        ],
        "resource": "qcs::ccr:::${namespace}/*",
        "effect": "allow"
    }]
}
```

## 命名空间权限
资源： `qcs::ccr:::namespace/${namespace}`。
### 新建命名空间
action：`ccr:CreateCCRNamespace`。
允许创建命名空间：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:CreateCCRNamespace",
        "resource": "qcs::ccr:::namespace/*",
        "effect": "allow"
    }]
}
```
禁止创建以 `test` 开头的命名空间：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:CreateCCRNamespace",
        "resource": "qcs::ccr:::namespace/test*",
        "effect": "deny"
    }]
}
```

### 删除命名空间
action： `ccr:DeleteUserNamespace`。
允许删除命名空间：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:DeleteUserNamespace",
        "resource": "qcs::ccr:::namespace/*",
        "effect": "allow"
    }]
}
```

## 镜像仓库权限
资源： `qcs::ccr:::repo/${repository}`。
### 创建镜像仓库
action：`ccr:CreateRepository`。
允许创建任意的镜像仓库：
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
禁止在命名空间 `foo` 下创建：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:CreateRepository",
        "resource": "qcs::ccr:::repo/foo/*",
        "effect": "deny"
    }]
}
```

### 删除镜像仓库
action： `ccr:DeleteRepository`。
允许删除任何镜像仓库：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:DeleteRepository",
        "resource": "qcs::ccr:::repo/foo/*",
        "effect": "deny"
    }]
}
```

### 允许批量删除所有镜像仓库
action： `ccr:BatchDeleteRepository`。
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:BatchDeleteRepository",
        "resource": "qcs::ccr:::repo/*",
        "effect": "deny"
    }]
}
```

>**注意：**
>由于接口实现的原因，要阻止用户删除某些镜像，请配置多个 action 来阻止协作者删除镜像。
例如：禁止删除任何镜像仓库：

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

### 查看镜像仓库
在镜像仓库页面，可以配置某些镜像仓库对协作者不可见。
action：`ccr:GetUserRepositoryList`。
允许查看所有镜像：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:GetUserRepositoryList",
        "resource": "qcs::ccr:::repo/*",
        "effect": "allow"
    }]
}
```

## Tag 权限
资源： `qcs::ccr:::tag/${tag}`。
### 删除 Tag
action： `ccr:DeleteTag`。
允许删除 `namespace1/foo` 镜像仓库下的所有 Tag：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccr:DeleteTag",
        "resource": "qcs::ccr:::tag/namespace1/foo/*",
        "effect": "allow"
    }]
}
```

### 批量删除 Tag
action： `ccr:BatchDeleteTag`。
禁止删除任何 Tag：
```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "ccr:BatchDeleteTag",
            "ccr:DeleteTag"
        ],
        "resource": "qcs::ccr:::tag/namespace1/foo/*",
        "effect": "allow"
    }]
}
```


## CI 权限
资源： `*`。
action：`ccb:ListGitAuth`。
禁止配置源代码授权：
```
{
    "version": "2.0",
    "statement": [{
        "action": "ccb:ListGitAuth",
        "resource": "qcs::ccb:::auth/write",
        "effect": "deny"
    }]
}
```

