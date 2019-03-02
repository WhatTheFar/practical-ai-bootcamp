import tensorflow as tf

# To clear the defined variables and operations of the previous cell
tf.reset_default_graph()
# Create a scalar variable
x_scalar = tf.get_variable('x_scalar', shape=[], initializer=tf.truncated_normal_initializer(mean=0, stddev=1))

# Step1: Create the scalar summary
first_summary = tf.summary.scalar(name='My_first_scalar_summary', tensor=x_scalar)
init = tf.global_variables_initializer()

# Launch the graph in a session
with tf.Session() as session:
    # Step2: Create the writer inside the session
    writer = tf.summary.FileWriter('./graphs/scalar_summary', session.graph)
    for step in range(100):
        # Loop over several initializations of the variable session.run(init)
        # Step3: Evaluate the scalar summary
        summary = session.run(first_summary)
        # Step4: Add the summary to the writer (i.e. to the event file)
        writer.add_summary(summary, step)
print('Done with writing the scalar summary')
writer.close()
