import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import xlrd

DATA_FILE="data/fire_theft.xls"


def huber_loss(label, prediction, delta=1.0):
    residual = tf.abs(prediction - label)
    def f1(): return 0.5 * tf.square(residual)
    def f2(): return delta * residual - 0.5 * tf.square(delta)
    return tf.cond(residual < delta, f1, f2)

#Step 1 : read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data=np.asarray([sheet.row_values(i) for i in range(1,sheet.nrows)])
n_samples=sheet.nrows-1

#Step 2: create placeholders for input X and label Y
X=tf.placeholder(tf.float32,name="X")
Y=tf.placeholder(tf.float32,name="Y")

#Step 3: create weight and bias, initialized to 0
w=tf.Variable(0.0,name="weights")
b=tf.Variable(0.0,name="bias")
u=tf.Variable(0.0,name="u")

#Step4: construct model to predict Y form the number of fire
Y_predicted=X*X*w+u*X+b

#Step5: use the square error as the loss function

# loss=tf.square(Y-Y_predicted,name="loss")
loss=huber_loss(Y,Y_predicted)

#Step6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

with tf.Session() as sess:
    #Step7: initialize the necessary variables, in this case, w and b
    sess.run(tf.global_variables_initializer())
    
    # see model in tensorBoard
    writer=tf.summary.FileWriter('./my_graph/l3/linear_reg',sess.graph)
    
    #Step8: train the model
    for i in range(50): #run 100 epochs
        total_loss=0
        for x,y in data:
            # Session runs train_op to minimize loss
            _,l=sess.run([optimizer,loss],feed_dict={X:x,Y:y})
            total_loss+=l
        print('Epoch{0}:{1}'.format(i,total_loss/n_samples))
    
    # close the writer
    writer.close()

    #Step9 : output the values of w andb
    w_value,b_value,u=sess.run([w,b,u])

#plot the results
X,Y=data.T[0],data.T[1]
plt.plot(X,Y,'bo',label='Real data')
plt.plot(X,X*X*w_value+u*X+b_value,'ro',label='Predicted data')
plt.legend()
plt.show()
