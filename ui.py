import numpy as np
import matplotlib.pyplot as plt

# Функція для візуалізації зображень
def plot_image(image, title):
    inverted_image = np.where(image == -1, 0, 1)
    
    plt.imshow(inverted_image.reshape(5, 5), cmap='gray', interpolation='nearest')
    plt.title(title)
    plt.axis('off')  # Вимкнути осі
    plt.gcf().set_facecolor('black')  # Задати чорний фон для фігури
    plt.show()