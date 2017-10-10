The image of Tencent CCS is composed of three parts: `ccr.ccs.tencentyun.com/${namespace}/${name}:$tag`. The permission of image service is configured based on two fields: `namespace` and `name`.
>**Note:**
`namespace` and `name` cannot contain slash "/". 

## Configuration of docker client Permission
Resource:  `qcs::ccr:::repo/${namespace}/${name}`.
Action:
* `ccr:pull`
* `ccr:push`

Enable `push` and `pull` permissions:
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
Enable `push` permission, and disable `pull` permission:
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
Enable permissions of **all images under a namespace**:
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

## Namespace Permission
Resource:  `qcs::ccr:::namespace/${namespace}`.
### Creating Namespace
Action: `ccr:CreateCCRNamespace`.
Allow to create namespace:
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
Disallow the creation of namespace that starts with `test`:
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

### Deleting Namespace
Action:  `ccr:DeleteUserNamespace`.
Allow to delete namespace:
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

## Image Registry Permission
Resource:  `qcs::ccr:::repo/${repository}`.
### Creating Image Registry
Action: `ccr:CreateRepository`.
Allow to create any image registry:
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
Disallow the creation of registry under the namespace `foo`:
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

### Deleting Image Registry
Action:  `ccr:DeleteRepository`.
Allow to delete any image registry:
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

### Allowing Batch Deletion of All Images
Action:  `ccr:BatchDeleteRepository`.
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

>**Note:**
>Because of API implementation, to prevent users from deleting some of the images, configure multiple actions to prohibit collaborators from deleting images.
For example, disallow deletion of any image registry:

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

### Viewing Image Registry
In image registry page, you can configure some of the image registries to be invisible to collaborators.
Action: `ccr:GetUserRepositoryList`.
Allow to view all images:
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

## Tag Permission
Resource:  `qcs::ccr:::tag/${tag}`.
### Deleting Tag
Action:  `ccr:DeleteTag`.
Allow to delete all Tags under the image registry of `namespace1/foo`:
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

### Batch Deletion of Tags
Action:  `ccr:BatchDeleteTag`.
Disallow deletion of any Tag:
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


## CI Permission
Resource:  `*`.
Action: `ccb:ListGitAuth`.
Disallow the configuration of source code authorization:
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


