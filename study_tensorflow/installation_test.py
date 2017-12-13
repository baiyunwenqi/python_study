import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
sess=tf.Session()
hello=tf.constant("Hello word form Tensorflow")
print(sess.run(hello))

a=tf.constant(20)
b=tf.constant(22)
print('a+b={0}'.format(sess.run(a+b)))