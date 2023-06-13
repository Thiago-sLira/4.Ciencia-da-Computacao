# import sys


class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]


new_queue = Queue()

# for i in range(10):
#     new_queue.enqueue(i)

new_dict = {
    "nome_do_arquivo": "AAAAAAAAAAAAAAAAAA",
    "qtd_linhas": "len(data_file)",
    "linhas_do_arquivo": "data_file",
}

new_queue.enqueue(new_dict)
new_queue.enqueue("Cenoura")
new_queue.enqueue("Beterraba")
new_queue.enqueue("Abacaxi")

file_removed = new_queue.dequeue()
print(f"{file_removed['nome_do_arquivo']}")
print(new_queue.dequeue())
print(new_queue.search(5))
# print(new_queue.__len__(), file=sys.stderr)
