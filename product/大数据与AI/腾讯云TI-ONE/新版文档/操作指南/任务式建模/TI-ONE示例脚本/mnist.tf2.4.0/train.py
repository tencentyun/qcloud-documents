# 安装 TensorFlow
import argparse
import os
import sys
import time

import tensorflow as tf


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--log_dir',
        type=str,
        default=os.path.join(os.getenv('TEST_TMPDIR', '/tmp'),
                             'tensorflow/mnist/logs/fully_connected_feed'),
        help='Directory to put the log data.'
    )
    parser.add_argument(
        '--ckpt_dir',
        type=str,
        default=os.path.join(os.getenv('TEST_TMPDIR', '/tmp'),
                             'tensorflow/mnist/ckpts/fully_connected_feed'),
        help='Directory to put the checkpoint data.'
    )
    parser.add_argument(
        '--model_dir',
        type=str,
        default=os.path.join(os.getenv('TEST_TMPDIR', '/tmp'),
                             'tensorflow/mnist/models/fully_connected_feed'),
        help='Directory to put the model result data.'
    )
    parser.add_argument(
        '--epochs',
        type=int,
        default=5,
        help='epochs to run'
    )
  
    FLAGS, unparsed = parser.parse_known_args()
    
    if tf.io.gfile.exists(FLAGS.log_dir):
      tf.io.gfile.rmtree(FLAGS.log_dir)
      tf.io.gfile.makedirs(FLAGS.log_dir)
    if tf.io.gfile.exists(FLAGS.ckpt_dir):
      tf.io.gfile.rmtree(FLAGS.ckpt_dir)
      tf.io.gfile.makedirs(FLAGS.ckpt_dir)
    if tf.io.gfile.exists(FLAGS.model_dir):
      tf.io.gfile.rmtree(FLAGS.model_dir)
      tf.io.gfile.makedirs(FLAGS.model_dir)
    
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation='softmax')
    ])
    

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
                  
    # 保存tensorboard所需数据
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=FLAGS.log_dir, histogram_freq=1)
    # 保存checkpoint
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=FLAGS.ckpt_dir,
                                                 save_weights_only=False,
                                                 verbose=1)
    

    model.fit(x_train, y_train, epochs=FLAGS.epochs,callbacks=[cp_callback,tensorboard_callback])
    model.evaluate(x_test,  y_test, verbose=2)


    #save the final model
    model.save(filepath=os.path.join(FLAGS.model_dir, 'model'))
