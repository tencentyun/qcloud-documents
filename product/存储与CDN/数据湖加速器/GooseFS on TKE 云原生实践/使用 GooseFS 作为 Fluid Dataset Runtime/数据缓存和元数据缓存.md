## 操作场景

本文介绍如何选择数据缓存和元数据缓存方面的参数。

## 操作步骤

### 打开/关闭数据缓存

在 GooseFSRuntime 中，打开数据缓存是 `goosefs.worker.ufs.instream.cache.enabled: "true"`，该属性默认为 true。

可通过在 Runtime 中指定 `goosefs.worker.ufs.instream.cache.enabled: "false"` 来关闭缓存，如下所示：
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: hadoop
spec:
  replicas: 1
  tieredstore:
    levels:
      - mediumtype: SSD
        path: /mnt/disk1/
        quota: 290G
        high: "0.9"
        low: "0.8"
  properties:
    goosefs.worker.ufs.instream.cache.enabled: "false"
```

### 打开元数据缓存

在 GooseFSRuntime 中，可以通过元数据缓存元数据信息。打开元数据缓存数可以指定 `goosefs.user.metadata.cache.enabled: "true"` ，该属性默认是 false。

具体如下：
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: hadoop
spec:
  replicas: 1
  tieredstore:
    levels:
      - mediumtype: SSD
        path: /mnt/disk1/
        quota: 290G
        high: "0.9"
        low: "0.8"
  properties:
    oosefs.worker.ufs.instream.cache.enabled: "true"
    goosefs.user.metadata.cache.enabled: "true"
```

