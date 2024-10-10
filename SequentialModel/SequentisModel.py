# 引入TensorFlow框架
import  tebsorflow as tf

# 导入keras中的Senquential模型
from tensorflow.keras.models import Sequential
# 导入神经网络层laygers
# Dense属于全连接网络层：例如第一层有2个神经元，第二层有3个神经元
# 第一层的2个神经元和第3个神经元实现互相连接（完全连接），这个就是全连接
from tensorflow.keras.models import Dense

# 1、创建Senquential对象
