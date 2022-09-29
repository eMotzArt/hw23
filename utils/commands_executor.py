from .functions import my_filter, my_map, my_unique, my_sort, my_limit

def command_processor(cmd1, value1, cmd2, value2, data):
    commands = {
        'filter': my_filter,
        'map': my_map,
        'unique': my_unique,
        'sort': my_sort,
        'limit': my_limit
    }
    cmd1 = commands.get(cmd1)
    cmd1_result = cmd1(data, value1)
    if not cmd2:
        return cmd1_result

    cmd2 = commands.get(cmd2)
    cmd2_result = cmd2(cmd1_result, value2)
    return cmd2_result
