# -*- coding: utf-8 -*-

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('E:/NusProjects/deep_learning/MNIST_data', one_hot=True)

print('training data size: ', mnist.train.num_examples)
print('validation data size: ', mnist.validation.num_examples)
print('testing data size: ', mnist.test.num_examples)

print('example training data: ', mnist.train.images[0])
print('example training label: ', mnist.train.labels[0])

#
# batch_size = 100
# xs, ys = mnist.train.next_batch(batch_size)
# print('X shape = ', xs.shape)
# print('Y shape = ', ys.shape)
