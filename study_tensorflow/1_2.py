import tensorflow as tf
# to put part of a graph on a specific CPU or GPU
# Creates a graph
with tf.device('/gpu:2'):
    a=tf.constant([1.0,2.0, 3.0, 4.0, 5.0, 6.0],name='a')
    b=tf.constant([1.0,2.0, 3.0, 4.0, 5.0, 6.0],name='b')
    c=tf.multiply(a,b)

#Create a session with log_device_palcement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_palcement=True))

# Runs the op.
print(sess.run(c))