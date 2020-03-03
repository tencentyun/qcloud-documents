
机器学习系统相较其他系统，有以下特点：
- 迭代性：模型的更新并非一次完成，需要循环迭代多次。
- 容错性：即使在每个循环中产生一些错误，模型最终仍能收敛。
- 参数收敛的非均匀性：有些参数几轮迭代就会收敛，而有的参数却需要上百轮迭代。

工业界需要训练大型的机器学习模型，一些广泛应用的特定的模型在规模上有两个特点：
1. 参数很大，超过单个机器的容纳的能力（大型 LR 和神经网络）。
2. 训练数据太大，需要并行提速（大数据）。

设计一个上述系统时，我们需要解决很多问题，例如频繁访问修改模型参数需要消耗巨大带宽，如何提高并行度，减少同步等待造成的延迟等，在此类场景下，类似 MapReduce 的框架无法满足需求，参数服务器应运而生。Parameter Server 适用于大规模深度学习系统，大规模 Logistic Regression 系统，大规模主题模型，大规模矩阵分解等依赖 SGD 或 L-BFGS 最优化的算法。

## 参数
#### 组件参数
组件参数与普通 TensorFlow 组件一样，框架提供了支持 py2 或 py3 的 TensorFlow 1.12 的镜像。
####  资源参数
配置多机多卡的资源，worker_num 数量即机器数，ps_num 即 parameter server 数。

## 示例代码

```
#coding=utf-8
import numpy as np
import tensorflow as tf

# Define parameters
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_float('learning_rate', 0.00003, 'Initial learning rate.')
tf.app.flags.DEFINE_integer('steps_to_validate', 1000,
                     'Steps to validate and print loss')

# For distributed
tf.app.flags.DEFINE_string("ps_hosts", "",
                           "Comma-separated list of hostname:port pairs")
tf.app.flags.DEFINE_string("worker_hosts", "",
                           "Comma-separated list of hostname:port pairs")
tf.app.flags.DEFINE_string("job_name", "", "One of 'ps', 'worker'")
tf.app.flags.DEFINE_integer("task_index", 0, "Index of task within the job")
tf.app.flags.DEFINE_integer("issync", 0, "是否采用分布式的同步模式，1表示同步模式，0表示异步模式")

# Hyperparameters
learning_rate = FLAGS.learning_rate
steps_to_validate = FLAGS.steps_to_validate

def main(_):
  ps_hosts = FLAGS.ps_hosts.split(",")
  worker_hosts = FLAGS.worker_hosts.split(",")
  cluster = tf.train.ClusterSpec({"ps": ps_hosts, "worker": worker_hosts})
  server = tf.train.Server(cluster,job_name=FLAGS.job_name,task_index=FLAGS.task_index)

  issync = FLAGS.issync
  if FLAGS.job_name == "ps":
    server.join()
  elif FLAGS.job_name == "worker":
    with tf.device(tf.train.replica_device_setter(
                    worker_device="/job:worker/task:%d" % FLAGS.task_index,
                    cluster=cluster)):
      global_step = tf.Variable(0, name='global_step', trainable=False)

      input = tf.placeholder("float")
      label = tf.placeholder("float")

      weight = tf.get_variable("weight", [1], tf.float32, initializer=tf.random_normal_initializer())
      biase  = tf.get_variable("biase", [1], tf.float32, initializer=tf.random_normal_initializer())
      pred = tf.multiply(input, weight) + biase

      loss_value = loss(label, pred)
      optimizer = tf.train.GradientDescentOptimizer(learning_rate)

      grads_and_vars = optimizer.compute_gradients(loss_value)
      if issync == 1:
        #同步模式计算更新梯度
        rep_op = tf.train.SyncReplicasOptimizer(optimizer,
                                                replicas_to_aggregate=len(
                                                  worker_hosts),
                                                replica_id=FLAGS.task_index,
                                                total_num_replicas=len(
                                                  worker_hosts),
                                                use_locking=True)
        train_op = rep_op.apply_gradients(grads_and_vars,
                                       global_step=global_step)
        init_token_op = rep_op.get_init_tokens_op()
        chief_queue_runner = rep_op.get_chief_queue_runner()
      else:
        #异步模式计算更新梯度
        train_op = optimizer.apply_gradients(grads_and_vars,
                                       global_step=global_step)


      init_op = tf.initialize_all_variables()

      saver = tf.train.Saver()
      tf.summary.scalar('cost', loss_value)
      summary_op = tf.summary.merge_all()

    sv = tf.train.Supervisor(is_chief=(FLAGS.task_index == 0),
                            logdir="./checkpoint/",
                            init_op=init_op,
                            summary_op=None,
                            saver=saver,
                            global_step=global_step,
                            save_model_secs=60)

    with sv.prepare_or_wait_for_session(server.target) as sess:
      # 如果是同步模式
      if FLAGS.task_index == 0 and issync == 1:
        sv.start_queue_runners(sess, [chief_queue_runner])
        sess.run(init_token_op)
      step = 0
      while  step < 100000:
        train_x = np.random.randn(1)
        train_y = 2 * train_x + np.random.randn(1) * 0.33  + 10
        _, loss_v, step = sess.run([train_op, loss_value,global_step], feed_dict={input:train_x, label:train_y})
        if step % steps_to_validate == 0:
          w,b = sess.run([weight,biase])
          print("step: %d, weight: %f, biase: %f, loss: %f" %(step, w, b, loss_v))

    sv.stop()

def loss(label, pred):
  return tf.square(label - pred)



if __name__ == "__main__":
  tf.app.run()
```

