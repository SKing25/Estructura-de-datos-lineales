def merge_sort(lst: list) -> list:
    """
    Ordena una lista usando el algoritmo Merge Sort (ordenamiento por mezcla).

    Args:
        lst (list): Lista a ordenar.

    Returns:
        list: Nueva lista ordenada.
    """
    if len(lst) <= 1:
        return lst.copy()
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return _merge(left, right)

def _merge(left: list, right: list) -> list:
    """Combina dos listas ordenadas en una lista ordenada."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(lst: list, low: int, high: int) -> None:
    """
    Ordena una lista usando Quick Sort (ordenamiento rápido in-place).

    Args:
        lst (list): Lista a ordenar.
        low (int): Índice inicial del subrango.
        high (int): Índice final del subrango.
    """
    if low < high:
        pi = _partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)

def _partition(lst: list, low: int, high: int) -> int:
    """Particiona la lista usando el último elemento como pivote."""
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1