def ocorrencias(word, lista):
    result = []
    for index in range(len(lista)):
        if word.upper() in lista[index].upper():
            result.append({"linha": index + 1})
    return result


def ocorrencias_conteudo(word, lista):
    result = []
    for index in range(len(lista)):
        if word.upper() in lista[index].upper():
            result.append({
                "linha": index + 1,
                "conteudo": lista[index]
            })
    return result


def verify_ocorrencias(lista):
    for data in lista:
        if len(data["ocorrencias"]) != 0:
            return True
    return False


def exists_word(word, instance):
    result = []
    for data in instance._data:
        result.append(
            {
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": ocorrencias(word, data["linhas_do_arquivo"])
            }
        )
    if verify_ocorrencias(result):
        return result
    else:
        return []


def search_by_word(word, instance):
    result = []
    for data in instance._data:
        result.append(
            {
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias":
                    ocorrencias_conteudo(word, data["linhas_do_arquivo"])
            }
        )
    if verify_ocorrencias(result):
        return result
    else:
        return []
