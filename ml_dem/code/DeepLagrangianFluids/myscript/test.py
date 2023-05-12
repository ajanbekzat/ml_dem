import open3d.ml.tf as ml3d
import tensorflow as tf
import sys
import numpy as np

# This will be an int32 tensor by default; see "dtypes" below.
rank_0_tensor = tf.constant(4)
print(rank_0_tensor)

# Let's make this a float tensor.
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(rank_1_tensor)

# If we want to be specific, we can set the dtype (see below) at creation time
rank_2_tensor = tf.constant([[1, 2],
                             [3, 4],
                             [5, 6]], dtype=tf.float16)
print(rank_2_tensor)

# There can be an arbitrary number of
# axes (sometimes called "dimensions")
rank_3_tensor = tf.constant([
  [[0, 1, 2, 3, 4],
   [5, 6, 7, 8, 9]],
  [[10, 11, 12, 13, 14],
   [15, 16, 17, 18, 19]],
  [[20, 21, 22, 23, 24],
   [25, 26, 27, 28, 29]],])

print(rank_3_tensor)
#convert a tensor to Numpy array & vice-verse
np.array(rank_2_tensor)
rank_2_tensor.numpy()

#addition, element-wise multiplication, and matrix multiplication.
a = tf.constant([[1, 2],
                 [3, 4]])
b = tf.constant([[1, 1],
                 [1, 1]]) # Could have also said `tf.ones([2,2])`

print(tf.add(a, b), "\n")
print(tf.multiply(a, b), "\n")
print(tf.matmul(a, b), "\n")

c = tf.constant([[4.0, 5.0], [10.0, 1.0]])

# Find the largest value
print(tf.reduce_max(c))
# Find the index of the largest value
print(tf.argmax(c))
# Compute the softmax
print(tf.nn.softmax(c))

rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Type of every element:", rank_4_tensor.dtype)
print("Number of dimensions:", rank_4_tensor.ndim)
print("Shape of tensor:", rank_4_tensor.shape)
print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0])
print("Elements along the last axis of tensor:", rank_4_tensor.shape[-1])
print("Total number of elements (3*2*4*5): ", tf.size(rank_4_tensor).numpy())

#Often axes are ordered from global to local: The batch axis first, followed by spatial dimensions, 
#and features for each location last. This way feature vectors are contiguous regions of memory.
rank_1_tensor = tf.constant([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print(rank_1_tensor.numpy())
print("Everything:", rank_1_tensor[:].numpy())
print("Before 4:", rank_1_tensor[:4].numpy())
print("From 4 to the end:", rank_1_tensor[4:].numpy())
print("From 2, before 7:", rank_1_tensor[2:7].numpy())
print("Every other item:", rank_1_tensor[::2].numpy())
print("Reversed:", rank_1_tensor[::-1].numpy())

print(rank_2_tensor.numpy())
# Get row and column tensors
print("Second row:", rank_2_tensor[1, :].numpy())
print("Second column:", rank_2_tensor[:, 1].numpy())
print("Last row:", rank_2_tensor[-1, :].numpy())
print("First item in last column:", rank_2_tensor[0, -1].numpy())
print("Skip the first row:")
print(rank_2_tensor[1:, :].numpy(), "\n")


# Shape returns a `TensorShape` object that shows the size on each dimension
x = tf.constant([[1], [2], [3]])
print(x.shape)
# You can convert this object into a Python list, too
print(x.shape.as_list())
# You can reshape a tensor to a new shape.
# Note that you're passing in a list
reshaped = tf.reshape(x, [1, 3])
# A `-1` passed in the `shape` argument says "Whatever fits".
print(tf.reshape(rank_3_tensor, [-1]))


x = tf.constant([1, 2, 3])
y = tf.constant(2)
z = tf.constant([2, 2, 2])
# All of these are the same computation
print(tf.multiply(x, 2))
print(x * y)
print(x * z)

def euclidean_distance(a, b, epsilon=1e-9):
    return tf.sqrt(tf.reduce_sum((a - b)**2, axis=-1) + epsilon)
a=tf.constant([[0.1,2,0.1],[0.4,5,0.6]])
mask=np.zeros(a.shape)
mask[:,1] = 1
cx=0.5
cz=0.7
cr=0.6
b = a*mask + cx*(1-mask)
mask[:,0] = 1
b = b*mask + cz*(1-mask)
tf.print(a)
tf.print(b)
d = tf.constant([cr]) - euclidean_distance(a,b)
d = tf.reshape(d,[d.shape[0],1])
c=-(a-b)
e = c/d
tf.print(dist2wallTensor)
'''
res=ml3d.ops.reduce_subarrays_sum(
    values = [1,2,3,4],
    row_splits=[0,2,2,4] # defines 3 subarrays with starts and ends 0-2,2-2,2-4
    )
res1=res.numpy()
res2=tf.make_ndarray(res)
print(res)
print(res2)

tensor = tf.range(10)
tf.print(tf.transpose(tensor), output_stream=sys.stderr)

@tf.function
def f(maxn=10):
    tensor = tf.range(maxn)
    print(tensor)
    tf.print(tensor, output_stream=sys.stderr)
    return tensor

range_tensor = f(7)
range_tensor = f(70)
'''