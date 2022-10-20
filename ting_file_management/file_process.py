# from queue import Queue
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    for inst in instance._data:
        if inst["nome_do_arquivo"] == path_file:
            return "Arquivo já existe"
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# queue = Queue()
# process("statics/arquivo_teste.txt", queue)
# print(queue._data)
# print(process("statics/arquivo_teste.txt", queue))
