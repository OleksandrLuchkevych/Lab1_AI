import numpy as np

# Функція активації для біполярного нейрона
def activation_function(sum_input, threshold=0):
    return 1 if sum_input >= threshold else -1

# Алгоритм Хебба
def hebbian_algorithm(x, y, w, learning_rate=1):
    for i in range(len(w)):
        w[i] += learning_rate * x[i] * y
    return w

# Функція для перевірки розпізнавання
def test_neuron(image, w, original, threshold=0, max_changes=3):
    sum_input = np.dot(image, w)
    predicted = activation_function(sum_input, threshold)
    changes = np.sum(original != image)
    return predicted, changes <= max_changes