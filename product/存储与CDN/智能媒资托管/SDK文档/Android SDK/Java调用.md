## 简介

本文档提供关于使用 Java 语言调用 SMH SDK 的说明。

## SMHCollectionFuture

SMHCollectionFuture 是 SMH 资源库封装类，提供适合 Java8 CompletableFuture 风格的 API。
SMHCollection 中所有方法在 CompletableFuture 中都能找到对应的 CompletableFuture 风格的方法，它们名称、参数、返回值（`CompletableFuture<XXX>`）均一样。

## 示例代码

```kotlin
//生成SMHCollectionFuture示例
Context context;
SMHCollectionFuture smh = new SMHCollection(
        context,
        new MySMHSimpleUser()
).future();

//获取目录列表
CompletableFuture<DirectoryContents> cf = smh.list(1, 50);
//阻塞获取结果
// try {
//     DirectoryContents directoryContents = cf.get();
// } catch (Throwable e){
//     e.printStackTrace();
// }

//异步获取结果
// 如果执行成功:
cf.thenApply((result) -> {
    DirectoryContents directoryContents = result;
    return result;
});
// 如果执行异常:
cf.exceptionally((e) -> {
    e.printStackTrace();
    return null;
});
```
