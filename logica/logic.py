from data.itemlists import items
from interfaz.componentes.item import ItemShow

def show_empty_containers(frameparent):
    containers_w_stuff = [item['localizacion'] for item in items]
    containers_empty = [num for num in range(1,99+1) if num in containers_w_stuff]
    print(containers_empty)
    print(frameparent)
    for empty in containers_empty:
        ItemShow(frameparent, )