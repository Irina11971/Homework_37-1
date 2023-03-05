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


def execute_application():
    num_list = [randint(1, 20) for _ in range(20)]


if __name__ == "__main__":
    execute_application()
