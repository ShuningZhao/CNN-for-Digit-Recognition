import tensorflow as tf

a = tf.zeros(10)
tf.Print(a)

with tf.Session() as sess:
    sess.run()
    print(sess.run(a))