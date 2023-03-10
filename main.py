from random import randint


def bubble_sorting(alist: list) -> list:
    """
    Возвращает список, отсортированый пузырьковой сортировкой

    :param alist (list): Список для сортировки
    :return:
            alist (list): Отсортированный список
    """
    n = len(alist)
    for i in range(n - 1):
        swapped = True
        for j in range(n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = False
        if swapped:
            break
    return alist

def sorting_insertion(my_list: list[int]) -> list:
    """
    Сортировка списка вставками

    :param my_list (list): Список целочисленных значений
    """
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (j >= 0 and temp < my_list[j]):
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = temp


def execute_application():
    num_list = [randint(1, 20) for _ in range(20)]
    print(f"Список до сортировки:\n{num_list}")
    num_list = bubble_sorting(num_list)
    print(f"Список после сортировки:\n{num_list}")


    my_list = [randint(-8, 99) for _ in range(20)]
    print(f"Список до сортировки:\n{my_list}")
    my_list = sorting_insertion(my_list)
    print(f"Список после сортировки:\n{my_list}")


if __name__ == "__main__":
    execute_application()
