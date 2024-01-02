from interfaz.componentes.item import ItemShow
from logica.getDataLogic import getData
from fuzzywuzzy import fuzz
from logica.constants_data import *
import threading


class PopulateManager:
    precision_search = 70  # ratio requerido para considerar un match

    def __init__(self, frame) -> None:
        self.all_items = []
        self.frame = frame
        self._items = getData()
        self._store_data_oop()

    def force_refresh(self):
        self._items = getData()
        self.organize_by("num")

    def _store_data_oop(self):
        for item in self._items:
            self.all_items.append(item)

    def clear_children(self):
        for child in self.frame.winfo_children():
            child.destroy()

    def visualize_all_thread(self):
        thread = threading.Thread(target=self.visualize_all)
        thread.start()

    def visualize_all(self):
        self.clear_children()
        for data_item in self.all_items:
            ItemShow(self.frame, data_item, popmanagerRef=self)

    def visualize_low_qty(self):
        self.clear_children()
        items_low = [
            item for item in self.all_items if item["cantidad"] < item["cantidadAviso"]
        ]
        for item_l in items_low:
            ItemShow(self.frame, item_l, warn=True, popmanagerRef=self)

    def visualize_by_num(self, num: int):
        self.clear_children()
        found_items = [item for item in self.all_items if item["localizacion"] == num]
        for item in found_items:
            ItemShow(self.frame, item, warn=False, popmanagerRef=self)
        if len(found_items) == 0:
            # print(f'cajon vacio {num}')
            ItemShow(par=self.frame, data_dict=ITEM_STRUCTURE, isEmpty=True, boxnum=num)

    def organize_by(self, sortby: str):
        self.clear_children()
        data_sorted = []
        match sortby:
            case "num":
                data_sorted = sorted(
                    self.all_items, key=lambda x: int(x["localizacion"])
                )
            case "name":
                data_sorted = sorted(self.all_items, key=lambda x: x["nombre"])
            case _:
                print("Sort no realizado.")
        for item_s in data_sorted:
            ItemShow(self.frame, item_s, popmanagerRef=self)

    def search_item(
        self, query: str, resolution=precision_search, search_all_fields=0
    ):
        self.precision_search = resolution
        if search_all_fields:
            print('searching in all fields')
        found_results = []
        print(f"Searching for {query}")
        for item_s in self.all_items:
            comparison_result = fuzz.ratio(
                query.lower().strip(), item_s["nombre"].lower()
            )
            if search_all_fields:
                comparison_model = fuzz.ratio(
                    query.lower().strip(), item_s["modelo"].lower()
                )
                comparison_fabricante = fuzz.ratio(
                    query.lower().strip(), item_s["fabricante"].lower()
                )
                comparison_notas = fuzz.ratio(
                    query.lower().strip(), item_s["notas"].lower()
                )
            # print(f'Match: {comparison_result}')
            if comparison_result >= self.precision_search:
                found_results.append(item_s)
            if search_all_fields:
                if (
                    comparison_model >= self.precision_search
                    or comparison_fabricante >= self.precision_search
                    or comparison_notas >= self.precision_search
                ):
                    found_results.append(item_s)

        self.clear_children()
        for match_ in found_results:
            ItemShow(self.frame, match_, popmanagerRef=self)

    def visualize_empty_thread(self):
        thread = threading.Thread(target=self.visualize_empty)
        thread.start()

    def visualize_empty(self):
        self.notempty = set(item["localizacion"] for item in self.all_items)
        self.empty = [num for num in range(1, 100) if num not in self.notempty]
        self.clear_children()
        for empty_num in self.empty:
            ItemShow(
                par=self.frame,
                data_dict=ITEM_STRUCTURE,
                isEmpty=True,
                boxnum=empty_num,
                warn=False,
            )

    def retrieve_item(self, uuid_target):
        for item in self.all_items:
            if item["uuid"] == uuid_target:
                return item
        return {}

    def remove_item_list(self, uuid_target):
        # buscar indice del objeto usando self.retrieve_item
        print("running del on popmanager")
        target_idx = -1
        for idx, item in enumerate(self.all_items):
            if item["uuid"] == uuid_target:
                target_idx = idx
        self.all_items.pop(target_idx)
        self.organize_by("num")
