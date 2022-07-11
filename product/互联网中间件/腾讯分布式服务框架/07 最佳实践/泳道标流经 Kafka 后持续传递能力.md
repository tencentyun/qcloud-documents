

## 操作场景

创建好泳道后，当有组件为 Kafka 时，我们希望染色流量能在流经 Kafka 后被对应泳道中的部署组消费，而未染色的消息被不在任何泳道中的部署组消费。并且希望泳道标（即 `LaneId`）能在消息流经 Kafka 后继续传递给下游服务。

名词解释

- 基线部署组：不在任何泳道中的部署组
- 泳道部署组：在任意泳道的部署组

## 前提条件

- 当前仅 1.23.17-Greenwich 及其之后的版本的 SDK 支持该能力。
- 需要使用 `KafkaTemplate` 发送消息，使用 `KafkaListener` 接受消息。

## 操作步骤

### 开启泳道标流经 Kafka 后持续传递能力

配置 `tsf.lane.kafka.laneOn` 为 `true`。该能力默认关闭，可通过本地配置或应用配置修改。

开启后，使用 `KafkaTemplate` 发送消息时，若消息生产者所在部署组为泳道部署组，发送到 Kafka 的消息将会带有当前泳道部署组所在泳道的泳道标（即 `LaneId`）。

开启后，使用 `KafkaListener` 接受消息时，基线部署组将消费不带泳道标的消息，即消费未染色消息。当服务**没有泳道部署组**时，即该服务仅有基线部署组，此时基线部署组将默认消费带泳道标的消息，即消费染色消息。消息消费者所在部署组的泳道标也会被替换为消息携带的泳道标。

### 支持基线部署组消费带泳道标的消息

当服务**有泳道部署组**，但是泳道部署组**不在线或手动下线**时，支持通过配置 `tsf.lane.kafka.mainConsumeLane = true` 使得基线部署组消费带泳道标的消息。该配置默认为 `false`。

### 支持泳道部署组消费基线消息

支持通过配置 `tsf.lane.kafka.laneConsumeMain = true` 使得泳道部署组可消费基线消息。该配置默认为 `false`。

### 跨线程能力支持

我们实验性地提供了支持泳道标跨线程传递的能力。

`CrossThreadLocal` 提供了跨线程场景下的线程池实现，`CrossCallable` 与 `CrossRunnable` 实现了对原生 `Callable` 和 `Runable` 的增强以提供跨线程能力。以`CrossThreadLocal` 和 `CrossRunnable` 为例，使用方法如下所示。
<dx-codeblock>
:::  java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CrossRunnableTest {

    private static ExecutorService executorService = Executors.newCachedThreadPool();

    private static ThreadLocal<Integer> threadLocal = new CrossThreadLocal<>();

    public static void main(String[] args) {

        for (int i = 0; i < 10; i++) {
            Integer val1 = (int) (Math.random() * 100);
            threadLocal.set(var1);

            executorService.submit(CrossRunnable.get(() -> {
                Integer val2 = threadLocal.get();
                System.out.println(val2.equals(var1));  // true
            }));
        }

        executorService.shutdown();
    }
}
:::
</dx-codeblock>



当开启基线部署组消费带泳道标的消息，此时基线部署组将消费带泳道标消息。为了使得下游服务知道当前消息是染色流量，我们将在 `KafkaListener` 处理该消息时候临时将消费者所在部署组的泳道标修改，并在 `KafkaListener` 处理完消息后将泳道标清除。因此开发者可利用跨线程能力将泳道标传递到下游的服务中。

下面是一个简单的 demo 展示对跨线程能力的支持。当基线服务消费泳道消息时，注释 `1`、`2`、`3` 处将打印泳道标，而注释 `4` 处不会打印泳道标，因为 `3` 使用了跨线程功能 `CrossRunnable`，使得泳道标可跨线程传递。当基线服务在消费泳道消息后，泳道标将会从线程中清理，此处再次消费基线消息，注释 `1`、`2`、`3`、`4`都不会打印泳道标。从而实现了基线服务消费泳道消息后能将泳道标传递到下游服务，并且不污染基线服务。
<dx-codeblock>
:::  java
@Component
public class KafkaReceiver {
    private static ExecutorService executorService = Executors.newCachedThreadPool();

    private static ExecutorService executorService1 = Executors.newCachedThreadPool();

    @KafkaListener(topics = "test")
    public void listen(ConsumerRecord<?, ?> record) {
        Optional<?> kafkaMessage = Optional.ofNullable(record.value());

        if (kafkaMessage.isPresent()) {
            Object message = kafkaMessage.get();
            
            logger.info("before lane id: {}", TsfLaneIdHolder.getLaneId());								// 1
            logger.info("before cross lane id: {}", TsfLaneIdHolder.getCrossLaneId()); 		// 2

            executorService.submit(CrossRunnable.get(() -> {
                String laneId = TsfLaneIdHolder.getCrossLaneId();
                logger.info("cross lane id: {}", laneId);																	// 3
            }));

            executorService1.submit(() -> {
                String laneId = TsfLaneIdHolder.getLaneId();
                logger.info("no cross lane id: {}", laneId);															// 4
            });

        }

    }
}
:::
</dx-codeblock>





