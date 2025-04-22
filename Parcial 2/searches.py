def linear_search(lst: list, target) -> int:
    """
    Busca un elemento en una lista usando búsqueda lineal.

    Args:
        lst (list): Lista a buscar.
        target: Elemento a encontrar.

    Returns:
        int: Índice del elemento o -1 si no existe.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst: list, target) -> int:
    """
    Busca un elemento en una lista ordenada usando búsqueda binaria.

    Args:
        lst (list): Lista ordenada.
        target: Elemento a encontrar.

    Returns:
        int: Índice del elemento o -1 si no existe.
    """
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1