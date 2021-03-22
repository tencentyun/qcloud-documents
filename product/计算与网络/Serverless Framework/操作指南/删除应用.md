## 基本功能
通过以下指令，可以快速删除云端资源：

```sh
sls remove
```


## 高级功能
- 查看删除过程中的具体日志信息：
```
sls remove --debug
```

- 应用目录下含有多个 Serverless 实例，只需要删除指定项目：
```
sls remove --target xxx
```
例如：在该项目根目录下，通过指令 `sls remove --target ./cos`，仅移除 COS 实例，其它实例不受影响。
```
.
├── src
│   ├── serverless.yml 
│   └── index1.js 
├── cos
│   └── serverless.yml 
├── db
│   └── serverless.yml 
└── .env 
```


## 常见问题
#### 执行 `sls remove` 时，会移除哪些云端资源？
  
Serverless Framework 根据 yml 配置文件完成云端资源的移除，只要通过 yml 文件创建的资源，都会进行删除操作；如果引用的已有资源，则不会进行移除。例如： 
- 通过 SCF 组件部署函数时，选择新建 API 网关触发器进行部署，则在删除时，创建的函数与 API 网关资源都会进行删除。
- 选择已有 API 网关触发器进行部署，则在删除时，仅删除函数资源，使用的 API 网关不会进行删除操作。
