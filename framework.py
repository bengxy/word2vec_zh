import tensorflow as tf

# statistic
__vocabulary_size = 100
__embedding_size = 20

__word_list = []
__train_df;

# initial embedding matrix
embedding_C = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1, 1))
input_embedding = tf.nn.embedding_lookup(embedding_C, train_X)

## input layer --------------------------
# matrix from embedding_vec 2 output_Y
# nce_weight * embed + bias = predict_Y
# |---|   |-|   |-|   |-|
# |   | * |-| + |-| = |-|
# |---|   |-|   |-|   |-|
nce_weights = tf.Variable(
	tf.truncated_normal([vocabulary_size, embedding_size], 
	stddev=1/math.sqrt(embedding_size)))
nce_biases = tf.Variable(
	tf.zeros([vocabulary_size]))

loss = tf.reduce_mean(
	tf.nn.nce_loss(nce_weights, nce_biases, 
		input_embedding, train_Y,
		num_sampled, vocabulary_size))

optimizer = tf.train.GradientDEscentOPtimizer(learning_rate = 1.0).minimize(loss)

## skip-gram ---------------------------
graph = tf.Graph()

## Training ~
for train_X, train_Y in generate_batch(...):
	feed_dict = {}
	_, cur_loss = session.run([optimizer, loss], feed_dict=feed_dict)

