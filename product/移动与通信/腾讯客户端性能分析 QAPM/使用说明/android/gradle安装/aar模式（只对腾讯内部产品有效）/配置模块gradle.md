在新版本的 QAPM 中已将相关的依赖资源打包为 aar 模式，可以只通过修改 gradle 的配置进行处理。
在对应模块 gradle 中加入对 QAPM 的模块依赖,如下所示。

```
compile(name: 'QAPM', ext: "aar")
```
