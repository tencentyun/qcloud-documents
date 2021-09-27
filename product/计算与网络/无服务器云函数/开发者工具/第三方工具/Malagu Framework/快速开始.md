我们可以使用 `@malagu/scf-adapter` 组件将应用部署到腾讯云云函数。基于约定大于配置原则，零配置，开箱即用。



## 云资源


适配器组件有一套默认的部署规则，该规则可以被覆盖。适配器组件在执行部署任务时，将使用平台提供的 SDK，根据部署规则，创建需要的云资源。如果发现云资源已经存在，则差异更新云资源。**适配器组件总是以尽可能安全的方式，创建或更新云资源**。例如，当配置了自定义域名，适配器组件则尝试创建或更新该自定义域名资源。


适配器组件将应用部署到一个函数中，也就是说一个应用对应着一个函数，如果应用较大，应该将大应用拆解成一个个小的微应用或者微服务。如同微服务架构的粒度拆分原则，合理的粒度拆分，能够更好地进行应用管理。框架会保证一个应用在一个函数中运行的性能。


## 环境隔离


在 Malagu 框架中，提供了一个配置属性 stage 表示环境。而在 `@malagu/scf-adapter` 组件约定的部署规则中，使用 mode 属性映射 stage 属性。默认提供了三套环境：测试、预发和生产。表达式规则如下：
```yaml
stage: "${'test' in mode ? 'test' : 'pre' in mode ? 'pre' : 'prod' in mode ? 'prod' : cliContext.prod ? 'prod' : 'test'}" # test, pre, prod
```
stage 取值规则如下：
- **test**：测试环境，当 mode 属性包含 test 模式，或者 mode 都不包含 test、pre、prod，且命令行参数 `-p,--prod` 未被指定。
- **pre**：预发环境，当 mode 属性包含 pre 模式。
- **prod**：生产环境，当 mode 属性包含 prod 模式，或者命令行参数 `-p,--prod` 被指定。



通过指定特殊的 mode 表示不同的部署环境：
```sh
# 部署到测试环境
malagu deploy -m test # 或者 malagu deploy

# 部署到预发环境，也可以直接跳过预发环境的部署，直接部署到生产环境
malagu deploy -m pre

# 部署到生成环境
malagu deploy -m prod
```


## 隔离级别


**环境的隔离级别支持控制**。可以使用账号隔离环境，不同环境对于不同配置文件，不同配置文件分别配置不同的云账号。同理，也可以使用 Region、服务别名来隔离环境。框架默认提供的是服务别名隔离环境。隔离方式可以互相叠加。


stage 属性值与服务别名关联（以下是默认规则，无需配置）：
```yaml
malagu:
  faas-adapter:
    alias:
      name: ${stage}
```
API 网关的 environment 关联（以下是默认规则，无需配置）：
```yaml
malagu:
  faas-adapter:
    apiGateway:
      release:
        environmentName: "${stage == 'pre' ? 'prepub' : stage == 'prod' ? 'release' : stage}"
```



## 部署模式


适配器组件通过 mode 属性定义部署模式，支持的部署模式如下：

- **http**：基于 API 网关 + Web 函数的部署模式。部署过程中，创建或更新 API 网关、命名空间、函数等云资源。
- **timer**：基于定时触发器 + 事件函数的部署模式。部署过程中，创建或更新定时触发器、命名空间、函数等云资源。
- **api-gateway**：基于 API 网关 + 事件函数的部署模式。部署过程中，创建或更新 API 网关、命名空间、函数等云资源。

```yaml
mode:
	- http
```


## 自定义部署规则


可以通过同名覆盖自定义部署规则。


#### 默认规则

默认规则定义在 `@malagu/scf-adapter` 组件的 `malagu-remote.yml` 配置文件中。


#### 自定义部署类型
```yaml
mode:
	- htpp # 默认值是 http，目前支持 http、timer、api-gateway
```
#### 自定义命名空间
```yaml
malagu:
	faas-adapter:
  	namespace:
    	name: xxxx # 默认值是 default
```
>?命名空间的其他属性配置方式类似。

#### 自定义函数名
```yaml
malagu:
	faas-adapter:
    function:
      name: xxxx # 默认值是 ${pkg.name}
```
>?函数的其他属性配置方式类似。


## 属性配置


```yaml
malagu:
	faas-adapter:
    type:
    namespace:
      description:
    function:
    	name: ''
      namespace:
      handler:
      publish:
      l5Enable:
      type:
      codeSource:
      description:
      memorySize:
      timeout:
      runtime:
      role:
      clsLogsetId:
      ClsTopicId:
      env:
      vpcConfig:
        vpcId:
        subnetId:
      layers:
        name:
        version:
      deadLetterConfig:
        type:
        name:
        filterType:
      publicNetConfig:
        PublicNetStatus:
          eipConfig:
            eipStatus:
    alias:
    	name:
      functionName:
      namespace:
      description:
      routingConfig:
      	additionalVersionWeights:
        	version:
          weight:
        addtionVersionMatchs:
        	version:
          key:
          method:
          expression:
    apiGateway:
    	usagePlan:
      	name:
        environment:
        desc:
        maxRequestNum:
        maxRequestNumPreSec:
      strategy:
      	name:
        environmentName:
        strategy:
      api:
        name:
        serviceTimeout:
        protocol:
        desc:
        authType:
        enableCORS:
        businessType:
        serviceScfFunctionName:
        serviceWebsocketTransportFunctionName:
        serviceScfFunctionNamespace:
        serviceScfFunctionQualifier:
        serviceWebsocketTransportFunctionNamespace:
        serviceWebsocketTransportFunctionQualifier:
        isDebugAfterCharge:
        serviceScfIsIntegratedResponse:
        isDeleteResponseErrorCodes:
        responseSuccessExample:
        responseFailExample:
        authRelationApiId:
        userType:
        oauthConfig:
          publicKey:
          tokenLocation:
          loginRedirectUrl:
        responseErrorCodes:
          code:
          msg:
          desc:
          convertedCode:
          needConvert:
        requestConfig:
          ApiRequestConfig:
          path:
          method:
        requestParameters:
          name:
          desc:
          position:
          type:
          defaultValue:
          required:
        RequestParameter:
      service:
      	exclusiveSetName:
      	name:
        protocol:
        description:
        netTypes:
        ipVersion:
        setServerName:
        appIdType:
      release:
      	environmentName:
        desc:
    customDomain:
    	name: 
      isDefaultMapping:
      certificateId:
      protocol:
      netType:
      pathMappingSet:
      	path:
        Environment:
```
