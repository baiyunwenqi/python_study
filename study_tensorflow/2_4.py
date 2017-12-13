import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

#Placeholders

#Create a placeholder 
a=tf.placeholder(tf.float32,shape=[3])

b=tf.constant([5,5,5],tf.float32)

c=a+b #short for tf.add(a,b)

# Feed the valus to placeholders using a dictionary
with tf.Session () as sess:
    # feed [1,2,3] to placeholder a via the dict{a:[1,2,3]}
    #fetch value of c
    valuec=sess.run(c,feed_dict={a:[1,2,3]}) # the tensor a is the key, not the string 'a'
    # write in short form
    valuec=sess.run(c,{a:[1,2,3]})
    print(valuec)

# Feeding values to TF ops
# create operations, tensors, etc(using the defalut graph)
a=tf.add(2,5)
b=tf.multiply(a,3)
with tf.Session() as sess:
    # define a dictionary that syas to replace the value of 'a' with 15
    replace_dic={a:15}
    #run the session,passing in 'replace_dict' as the value to 'feed_dict'
    print(sess.run(b,feed_dict=replace_dic)) #return 45


