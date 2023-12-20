from data.itemlists import items
from interfaz.componentes.item import ItemShow
from logica.DestroyChildren import destroy_children

def show_empty_containers(parent):
    containers_w_stuff = [item['localizacion'] for item in items]
    containers_empty = [num for num in range(1,99+1) if num in containers_w_stuff]
    print(containers_empty)
    
    #antes de pulsarlo, debe destruir todos los children de la lista
    destroy_children(parent)
    for empty_num in containers_empty:
        #todo: Completar funcion mostrar contenedores vacios
        ItemShow(parent,{},isEmpty=True, boxnum=empty_num)