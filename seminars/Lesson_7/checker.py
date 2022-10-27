def checker(data = ''):
    operations = ['+', '-', '/', '*']
    data = data.split()

    if len(data) == 1 and data[0].replace('.', '', 1).isnumeric():
        return 1, float(data[0])

    elif len(data) == 2 and data[0].replace('.', '', 1).isnumeric() and data[1].replace('.', '', 1).isnumeric():
        return 1, float(data[0]), float(data[1])
    elif len(data) == 1 and (data[0] in operations):
        return 3, 0.0, 0.0
    else:
        return -1, 0.0, 0.0



