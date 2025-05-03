def improved_move_to_front(config_list, requests):
    """
    Calcula el costo total de acceso utilizando el algoritmo mejorado IMTF (Improved Move-To-Front).

    IMTF solo mueve el elemento accedido al frente si aparece nuevamente dentro de las próximas (cost - 1) posiciones en la secuencia de solicitudes.

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
                - 'after': estado de la lista después de aplicar la regla IMTF.
    """
    total_cost = 0
    history = []

    for i, req in enumerate(requests):
        cost = config_list.index(req) + 1
        total_cost += cost

        history.append({
            "request": req,
            "cost": cost,
            "before": config_list[:],
        })

        lookahead = requests[i+1:i + cost] if cost > 1 else []
        if req in lookahead:
            config_list.remove(req)
            config_list.insert(0, req)

        history[-1]["after"] = config_list[:]

    return total_cost, history
