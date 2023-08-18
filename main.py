import os

from order import order

if __name__ == "__main__":

    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    print('Программа запущена')
    order()
    print('Программа успешно завершена')
