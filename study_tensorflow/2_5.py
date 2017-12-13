import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
# Lazy loading Example

#normal loading
# x=tf.Variable(10,name='x')
# y=tf.Variable(20,name='y')
# z=tf.add(x,y) # u create the node for add node before executing the graph

# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     writer=tf.summary.FileWriter('./my_graph/l2',sess.graph)
#     for _ in range(10):
#         sess.run(z)
#     writer.close()

#Lzay loading
x=tf.Variable(10,name='x')
y=tf.Variable(20,name='y')
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer=tf.summary.FileWriter('./my_graph/l2',sess.graph)
    for _ in range(10):
        sess.run(tf.add(x,y))
    writer.close