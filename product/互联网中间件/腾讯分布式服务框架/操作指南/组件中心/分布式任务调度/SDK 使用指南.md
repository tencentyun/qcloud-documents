分布式任务调度实现了与 TSF 框架的无缝集成，您仅需要引用 SDK，按照规范编写并配置任务，即可实现任务触发、执行、停止等多种管理。

## 准备工作
开始使用分布式任务调度之前，请确保正确配置 Maven 环境（参考 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)）。

## 添加依赖
在 pom.xml 文件中添加如下 dependency。
```xml
<dependency>
	<groupId>com.tencent.cloud </groupId>
	<artifactId>tct-spring-boot-starter </artifactId>
	<version>1.2.0 </version>
</dependency>
```

>!使用原有 spring-cloud-tsf-schedule 组件依赖的用户仅需将项目中 pom 依赖的 spring-cloud-tsf-schedule 组件移除，重新引入 tct-spring-boot-starter 组件依赖，并将对应的 Java 类文件重新 reload 即可完成 SDK 升级操作。

## 添加配置

在 application.yml 文件中添加如下配置，启用任务调度 SDK。
```xml
tct
  // 默认是 false 不启用。
  enabled: true
```

## 编写任务
#### 1. 编写简单任务
实现 `com.tencent.cloud.task.sdk.client.spi.ExecutableTask` 接口，覆写 execute 方法，在方法中实现任务执行逻辑。
SDK  内部通过反射机制，生成任务对象实例，并执行 execute 方法。任务示例如下：

默认的任务生成器情况下，编写的任务对象需要确保具有`无参数构造函数`。 
```java
import com.tencent.cloud.task.sdk.client.model.ExecutableTaskData;
import com.tencent.cloud.task.sdk.client.model.ProcessResult;
import com.tencent.cloud.task.sdk.client.spi.ExecutableTask;
import org.apache.commons.lang3.RandomUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.lang.invoke.MethodHandles;
/**
 * 实现ExecutableTask接口
 */
@Component
public class SimpleTimeoutExecutableTask implements ExecutableTask {

    private static final Logger LOG = LoggerFactory.getLogger(MethodHandles.lookup().lookupClass());

    // Override execute方法，在方法中编写任务逻辑。
    @Override
    public ProcessResult execute(ExecutableTaskData taskData) {
        try {
            // 模拟任务执行逻辑
            // 模拟任务耗时
            long startTime = System.currentTimeMillis();
            long timeOut = RandomUtils.nextLong(30000L, 35000L);
            // 上报日志到控制台
            LOG.info("timeout task start, timeout: {}", timeOut);
            Thread.sleep(timeOut);
            LOG.info("timeout task end, span: {}", System.currentTimeMillis() - startTime);
            // 设置任务执行状态： 执行成功
            return ProcessResult.newSuccessResult();
        } catch (InterruptedException e) {
            return ProcessResult.newCancelledResult(e);
        }
    }

}
```

#### 2. 编写可停止的任务

分布式任务调度框架支持任务的停止操作，通过实现`com.tencent.cloud.task.sdk.client.spi.TerminableTask`接口，覆写 cancel 方法，实现停止逻辑，并返回停止结果。任务示例如下：
```java
import com.tencent.cloud.task.sdk.client.LogReporter;
import com.tencent.cloud.task.sdk.client.model.ExecutableTaskData;
import com.tencent.cloud.task.sdk.client.model.ProcessResult;
import com.tencent.cloud.task.sdk.client.model.ProcessResultCode;
import com.tencent.cloud.task.sdk.client.model.TerminateResult;
import com.tencent.cloud.task.sdk.client.remoting.TaskExecuteFuture;
import com.tencent.cloud.task.sdk.client.spi.ExecutableTask;
import com.tencent.cloud.task.sdk.client.spi.TerminableTask;
import com.tencent.cloud.task.sdk.core.utils.ThreadUtils;
import org.apache.commons.lang3.RandomUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.lang.invoke.MethodHandles;

/**
 * 实现ExecutableTask,TerminableTask接口
 */
public class SimpleLogExecutableTask implements ExecutableTask,TerminableTask {

    private static final Logger LOG = LoggerFactory.getLogger(MethodHandles.lookup().lookupClass());
    // Override execute 方法，在方法中编写任务逻辑。
    @Override
    public ProcessResult execute(ExecutableTaskData taskData) {
        ProcessResult result = new ProcessResult();
        try {
            // 上报日志到控制台
            LogReporter.log(taskData,"start to execute SimpleLogExecutableTask...");
            LogReporter.log(taskData,"hello, this is a demo for SimpleLogExecutableTask");
            // 模拟任务执行逻辑
            // 模拟任务耗时
            long sleepTime = RandomUtils.nextLong(10000, 15000);
            Thread.sleep(sleepTime);
            // 设置任务执行状态： 执行成功
            result.setResultCode(ProcessResultCode.SUCCESS);
            LogReporter.log(taskData,"success to execute SimpleLogExecutableTask... ");
        } catch (InterruptedException e) {
            result.setResultCode(ProcessResultCode.TERMINATED);
            LogReporter.log(taskData,"task is terminated... ");
        } catch (Throwable t) {
            LOG.error(t.getMessage(), t);
            // 设置任务执行状态： 执行失败
            result.setResultCode(ProcessResultCode.FAIL);
        }
        // 返回执行结果
        return  result;
    }

    @Override
    public TerminateResult cancel(TaskExecuteFuture future, ExecutableTaskData taskData) {
        LogReporter.log(taskData,"task start to cancel");
        // 编写任务停止执行逻辑， 例如这里通过调用 Future 的 cancel 方法。
        future.cancel(true);
        // 返回终止结果。
        LogReporter.log(taskData,"task cancel success");
        return TerminateResult.newTerminateSuccessResult();
    }
}
```
通过 Future 的 cancel 方法，**不一定**能停止正在运行中的任务, 通常需要配合业务逻辑标识符的方式进行终止（参考 [任务停止原理及实践](https://cloud.tencent.com/document/product/649/41640)）。


## 普通自定义任务工厂

SDK 内部默认的任务生成工厂 `com.tencent.cloud.task.sdk.client.DefaultTaskFactory` 是通过 Java 的反射机制来生成任务对象的实例。我们也支持用户自定义任务生成器。

### 1. 编写任务工厂
```java

package com.tencent.cloud.task.factory

public class SimpleExecuteTaskFactory extends DefaultTaskFactory {
    private static final Logger LOG = LoggerFactory.getLogger(MethodHandles.lookup().lookupClass());

    public SimpleExecuteTaskFactory() {
        super(Thread.currentThread().getContextClassLoader());
    }

    public SimpleExecuteTaskFactory(ClassLoader classLoader) {
        super(classLoader);
    }

    @Override
    public ExecutableTask newExecutableTask(ExecutableTaskData taskData) throws InstancingException {
        LOG.info("generate task: {}", taskData.getTaskContent());
        return super.newExecutableTask(taskData);
    }
}
```

### 2. 在 application.yml 中添加配置
```xml
tct:
  client:
    properties:
	   # 配置自定义的任务工厂类名称
      "task.factory.name": "com.tencent.cloud.task.factory.SimpleExecuteTaskFactory"  
```

## 集成 Spring 框架自定义任务工厂

### 1. 定义 Bean 类型的任务工厂
```java

package com.tencent.cloud.task.factory;
// 将工厂类定义为Bean
@Component
public class SpringExecuteTaskFactory implements ExecutableTaskFactory, ApplicationContextAware {

    private static final Logger LOG = LoggerFactory.getLogger(MethodHandles.lookup().lookupClass());

    private ApplicationContext applicationContext;

    private final ExecutableTaskFactory defaultFactory = new DefaultTaskFactory(Thread.currentThread().getContextClassLoader());

    @Override
    public ExecutableTask newExecutableTask(ExecutableTaskData executableTaskData) throws InstancingException {
        try {
            ExecutableTask executableTask = (ExecutableTask)applicationContext.getBean(Class.forName(executableTaskData.getTaskContent()));
                    applicationContext.getBean(executableTaskData.getTaskContent(),ExecutableTask.class);
            LOG.info("generate executableTask bean SpringExecutableTaskFactory. taskName: {}", executableTaskData.getTaskContent());
            return executableTask;
        } catch (Throwable t) {
            return defaultFactory.newExecutableTask(executableTaskData);
        }
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        this.applicationContext = applicationContext;
    }
}

```
### 2. 定义 Bean 类型的任务
```java
// 将任务定义为Bean
@Component
public class SimpleSpringBeanLogTask implements ExecutableTask {
    @Override
    public ProcessResult execute(ExecutableTaskData executableTaskData) {
        LogReporter.log(executableTaskData,"spring bean task start to execute");
        ThreadUtils.waitMs(5000);
        LogReporter.log(executableTaskData,"spring bean task end to execute");
        return ProcessResult.newSuccessResult();
    }
}
```

### 3. 在 application.yml 中添加配置
```xml
tct:
  client:
    properties:
	   # 配置自定义的Bean类型的任务工厂类名称
      "task.factory.name": "com.tencent.cloud.task.factory.SpringExecuteTaskFactory"  
```

## 更多

### 说明

为适配 Spring 容器的运行环境，自定义任务 Factory 实现逻辑中，有如下逻辑：
 - 优先尝试从 ApplicationContext 中，通过 Bean 加载的方式获取对应的 Factory 实例。
 - Spring 容器获取 Bean 实例失败后，通过反射方式创建自定义的 Factory 对象实例。 

### 配置
SDK 中存在一些参数可以允许通过配置方式进行调配，如下所示：
```xml
tct:
  // 是否开启任务调度功能，默认 false 为关闭，true 则开启。
  enabled: true
  client:
    properties:
      // 任务执行的线程总数，默认200
      task.max.threads: 200
      // 线程池核心线程数量，默认 CPU 核数 + 1
      task.core.threads: <CPU核数+1>
      // 线程类型: FIXED、CACHED、LIMITED、EAGER
      thread.pool.type: FIXED
```





