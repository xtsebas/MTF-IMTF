def move_to_front(config_list, requests):
    """
    Calcula el costo total de acceso utilizando el algoritmo Move-To-Front (MTF).

    El algoritmo simula una lista autorganizable, donde cada elemento accedido es movido al inicio de la lista. El costo de acceso es igual a la posición (1-based) del elemento en la lista antes de moverlo.

    Args:
        config_list (list): Lista inicial de configuración de elementos
        requests (list): Lista de solicitudes (elementos a acceder en orden)

    Returns:
        tuple:
            total_cost (int): Costo total acumulado de todos los accesos.
            history (list of dict): Lista con el historial de cada paso. Cada entrada contiene:
                - 'request': el elemento solicitado,
                - 'cost': costo de acceso (posición actual + 1),
                - 'before': estado de la lista antes del acceso,
                - 'after': estado de la lista después del movimiento.
    """
    total_cost = 0
    history = []

    for req in requests:
        cost = config_list.index(req) + 1
        total_cost += cost

        history.append({
            "request": req,
            "cost": cost,
            "before": config_list[:],
        })

        config_list.remove(req)
        config_list.insert(0, req)

        history[-1]["after"] = config_list[:]

    return total_cost, history
