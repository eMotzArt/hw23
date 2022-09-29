from flask import abort

def args_reader(**kwargs):
    available_params= ['file_name', 'cmd1', 'value1', 'cmd2', 'value2']
    [abort(400, 'Recieved unavailable parameter') for kwarg in kwargs if kwarg not in available_params]

    if not (file_name := kwargs.get('file_name')):
        abort(400, 'No file_name recieved')

    if not (cmd1 := kwargs.get('cmd1')):
        abort(400, 'Main command not found')
    if not (value1 := kwargs.get('value1')):
        abort(400, 'Value for main command not found')

    cmd2 = kwargs.get('cmd2') # or None
    value2 = kwargs.get('value2')
    return cmd1, value1, cmd2, value2, file_name

def commands_checker(cmd1, cmd2):
    available_commands = ['filter', 'map', 'unique', 'limit', 'sort']
    if cmd1 not in available_commands:
        abort(400, 'Main command not found')
    if not cmd2:
        return
    if cmd2 not in available_commands:
        abort(400, 'Optional command not found')