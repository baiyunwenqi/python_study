import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

#  Constant types
b = tf.constant([[0, 1], [2, 3]], name="b")
print("the constant tensor:", b)

c = tf.zeros([2, 3], tf.int32)
print("the zeros tensor is:", c)

# create a tensor of shape and type as the input_tensor but all elements are zeros.
d = tf.zeros_like(c)
print("The zeros_like tensor is:", d, tf.Session().run(d))

ones = tf.ones([2, 3], tf.int32)
print("ones tensor:", ones, tf.Session().run(ones))

ones_scalar = tf.fill([2, 3], 8)
print("tensor filled with a scalar value:",
      ones, tf.Session().run(ones_scalar))

#Constants as sequences

lin1=tf.linspace(10.0,13.0,4) # include the start and stop number
print("linsapce use tf:",
      lin1, tf.Session().run(lin1))

rang1=tf.range(3,18,3)
print("range use tf:",
      rang1, tf.Session().run(rang1))

# Randomly Generated Constants
print("Randomly normal generated use tf:",
      tf.Session().run(tf.random_normal([3],mean=0.0,stddev=1.0)))

print("random_uniform use tf:",
      tf.Session().run(tf.random_uniform([3],0)))
      
