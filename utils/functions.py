def my_filter(data, searched_text):
    res = filter(lambda line: searched_text in line, data)
    return list(res)

def my_map(data, col_num):
    res = map(lambda line: line.split(' ')[int(col_num)], data)
    return list(res)

def my_unique(data, *args):
    return set(data)

def my_sort(data, type):
    return sorted(data, reverse=True) if type.lower() == 'desc' else sorted(data)

def my_limit(data, count):
    return data[:int(count)]
