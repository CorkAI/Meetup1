# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# MINOR ALTERATIONS FOR THE CORK AI MEETUP 
# INSTEAD OF TESTING ON THE ENTIRE TEST-SET AND REPORTING THE AVERAGE
# WE TEST ON INDIVIDUAL TEST IMAGES AND WRITE EXAMPLES OF 
# CORRECT AND INCORRECT CLASSIFICATION TO DISK FOR EXAMINATION
# ==============================================================================


"""A very simple MNIST classifier.

See extensive documentation at
https://www.tensorflow.org/get_started/mnist/beginners
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

FLAGS = None


def main(_):
    # Import data
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    # Create the model
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x, W) + b

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 10])

    # The raw formulation of cross-entropy,
    #
    # tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
    #                              reduction_indices=[1]))
    #
    # can be numerically unstable.
    #
    # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    
    # Train
    for _ in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # Test on individual test examples, writing examples of 
    # successful and failed classifications to disk
    if not os.path.exists(os.path.join(os.getcwd(), 'output_images')):
            os.makedirs(os.path.join(os.getcwd(), 'output_images'))
    prediction = tf.argmax(y, 1)  # output the class that is predicted
    num_each_to_store = 5
    stored_correct = 0
    stored_incorrect = 0
    idx = 0
    while (stored_correct < num_each_to_store or stored_incorrect < num_each_to_store) and idx < len(mnist.test.images):
        pred = sess.run(prediction, feed_dict={x: mnist.test.images[idx].reshape(1, 784)})
        real_label = np.argmax(mnist.test.labels[idx])
        correct = pred == real_label
        
        img = np.reshape(mnist.test.images[idx], [28, 28])
        plt.imshow(img, cmap='gray')
        
        if correct and stored_correct < num_each_to_store:
            stored_correct += 1
            plt.savefig("output_images/success_{}.png".format(real_label.astype(str)))
        elif not correct and stored_incorrect < num_each_to_store:
            stored_incorrect += 1
            plt.savefig("output_images/fail_{}_{}.png".format(real_label.astype(str), pred.astype(str)))
        idx += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                        help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
