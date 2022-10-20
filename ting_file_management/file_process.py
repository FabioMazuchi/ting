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
        "linhas_do_arquivo": data,
    }
    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    try:
        data_removed = instance.dequeue()
        name_arquivo = data_removed["nome_do_arquivo"]
        print(
            f"Arquivo {name_arquivo} removido com sucesso",
            file=sys.stdout,
        )
    except TypeError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
