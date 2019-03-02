import tensorflow as tf

# a = tf.constant([2, 2], name="a")
# b = tf.constant([3, 6], name="b")
# x = tf.add(a, b, name="add")
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(x))
#
# writer.close()


# a = tf.zeros([2, 3], tf.int32)
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
# # close the writer when you’re done using it
# writer.close()

#
# input_tensor = [[0, 1], [2, 3], [4, 5]]
# a = tf.zeros_like(input_tensor)
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
# # close the writer when you’re done using it
# writer.close()
#
# a = tf.linspace(10.0, 13.0, 4, name="linspace")
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
# writer.close()


# # 'start' is 3, 'limit' is 18, 'delta' is 3
# a = tf.range(3, 18, 3)
# # 'start'  is  3, 'limit' is 1, 'delta' is -0.5
# b = tf.range(3, 1, -0.5)
# # 'limit' is 5
# c = tf.range(5)
#
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a), session.run(b), session.run(c))
# # close the writer when you’re done using it
# writer.close()

#
# t_0 = 19
# # Treated as a 0-d tensor, or "scalar"
# t_1 = [b"apple", b"peach", b"grape"]
# # treated  as  a  1-d  tensor,  or  "vector"
# t_2 = [[True, False, False], [False, False, True], [False, True, False]]
# # treated as a 2-d tensor, or "matrix"
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(tf.zeros_like(t_0)))
#     print(session.run(tf.ones_like(t_0)))
#     print(session.run(tf.zeros_like(t_1)))
#     # print(session.run(tf.ones_like(t_1)))
#     print(session.run(tf.zeros_like(t_2)))
#     print(session.run(tf.ones_like(t_2)))
# writer.close()


# my_const = tf.constant([1.0, 2.0], name="my_const")
# print(tf.get_default_graph().as_graph_def())


# # create variable a with scalar value
# a = tf.Variable(2, name="scalar")
# # create variable b as a vector
# b = tf.Variable([2, 3], name="vector")
# # create variable c as a 2x2 matrix
# c = tf.Variable([[0, 1], [2, 3]], name="matrix")
# # create variable W as 784 x 10 tensor, filled with zeros
# W = tf.Variable(tf.zeros([784, 10]))
#
# init = tf.global_variables_initializer()
# with tf.Session() as session:
#     session.run(init)
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(b.value()))
# writer.close()


x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
z = tf.add(x, y)
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs', session.graph)
    for _ in range(10):
        session.run(z)
writer.close()


# with tf.Session() as session:
#     session.run(tf.global_variables_initializer())
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     for _ in range(10):
#         session.run(tf.add(x, y))
# writer.close()
