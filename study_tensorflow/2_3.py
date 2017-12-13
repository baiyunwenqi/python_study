import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
# Variables
my_const=tf.constant([1.0,2.0],name="my_const")
# print(tf.get_default_graph().as_graph_def())

a=tf.Variable(2,name="scalar")
b=tf.Variable([2,3],name="vector")

#Initialize all varibales at once 
init = tf.global_variables_initializer()

# with tf.Session() as sess:
#     sess.run(init)
#     print("varible a after initialization",sess.run(a))
#     print("varible b after initialization",sess.run(b))

# another way
# w=tf.Variable(tf.truncated_normal([10,7]))
# with tf.Session() as sess:
#     sess.run(w.initializer)
#     print(w)
#     print(w.eval())   # to get the value


#Assign values to varibales
# w = tf.Variable(10)
# assign_op=w.assign(100)
# with tf.Session() as sess:
#     sess.run(w.initializer)
#     sess.run(assign_op)
#     print(w.eval())

# Each session maintaions its own copy of variable
# W=tf.Variable(10)

# sess1=tf.Session()
# sess2=tf.Session()

# sess1.run(W.initializer)
# sess2.run(W.initializer)

# print(sess1.run(W.assign_add(10)))
# print(sess2.run(W.assign_add(2)))

# sess1.close()
# sess2.close()

#InteractiveSession
sess=tf.InteractiveSession()
a=tf.constant(5.0)
b=tf.constant(6.0)
c=a*b
# We can just use 'c.eval()' without specifying the context 'sess'
print(c.eval())
sess.close()