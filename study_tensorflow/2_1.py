import tensorflow as tf
# Learn TensorBoard
a=tf.constant(2,name="a")
b=tf.constant(2,name="b")
x=tf.add(a,b)
with tf.Session() as sess:
    # to activate TensorBoard on this program
    writer = tf.summary.FileWriter('./2_1graphs',sess.graph)

    print(sess.run(x))
# close the writer when you're done using it
writer.close()