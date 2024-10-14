import numpy as np
from neuron import hebbian_algorithm, test_neuron
from ui import plot_image

# Зображення цифри "3"
x1 = np.array([ 1,  1,  1,  1, 1, 
               -1, -1, -1, -1, 1, 
                1,  1,  1,  1, 1,
               -1, -1, -1, -1, 1, 
                1,  1,  1,  1, 1])

# Зображення літери "O"
x2 = np.array([1,  1,  1,  1, 1,
               1, -1, -1, -1, 1, 
               1, -1, -1, -1, 1, 
               1, -1, -1, -1, 1, 
               1,  1,  1,  1, 1])

# Початкові ваги (нульові)
w = np.zeros(25)

# Бажаний вихід
y1 = 1  # Для цифри "3"
y2 = -1  # Для літери "O"

# Навчання нейрона
w = hebbian_algorithm(x1, y1, w)
w = hebbian_algorithm(x2, y2, w)

# Головне меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Вивести початкові зображення")
        print("2. Внести зміни в зображення цифри '3'")
        print("3. Внести зміни в зображення літери '0'")
        print("4. Вийти")
        
        choice = input("Виберіть варіант (1-4): ")
        
        if choice == '1':
            print("Початкова цифра '3':")
            plot_image(x1, "Цифра '3'")
            print("Початкова літера 'O':")
            plot_image(x2, "Літера 'O'")
            
        elif choice == '2':
            modified_x1 = x1.copy()
            print("Внесіть зміни в зображення цифри '3' ( 1 або -1)")
            for i in range(len(modified_x1)):
                new_value = input(f"Значення для пікселя {i} (поточне: {modified_x1[i]}): ")
                if new_value in ['1', '-1']:
                    modified_x1[i] = int(new_value)
            
            changes = np.sum(x1 != modified_x1)
            test_neuron(modified_x1, w, x1)
            if changes <= 3:
                print("Зображення цифри '3' розпізнано.")
            else:
                print("Зображення цифри '3' не розпізнано.")
            plot_image(modified_x1, "Змінена цифра '3'")

        elif choice == '3':
            modified_x2 = x2.copy()
            print("Внесіть зміни в зображення літери 'O' ( 1 або -1)")
            for i in range(len(modified_x2)):
                new_value = input(f"Значення для пікселя {i} (поточне: {modified_x2[i]}): ")
                if new_value in ['1', '-1']:
                    modified_x2[i] = int(new_value)

            changes = np.sum(x2 != modified_x2)
            test_neuron(modified_x2, w, x2)
            if changes <= 3:
                print("Зображення літери 'O' розпізнано.")
            else:
                print("Зображення літери 'O' не розпізнано.")
            plot_image(modified_x2, "Змінена літера 'O'")

        elif choice == '4':
            print("Вихід з програми.")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")


main_menu()