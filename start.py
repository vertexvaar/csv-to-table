fObj = open('data.csv', 'r')

header = fObj.readline().strip('\n')
cols = header.split(';')

# Rewind to beginning to include header in length calculation
fObj.seek(0)

columnsCount = len(cols)
sizes = [0] * columnsCount
for line in fObj:
    cols = line.strip('\n').split(';', columnsCount)
    for index, col in enumerate(cols):
        newLength = len(col)
        if (newLength > sizes[index]):
            sizes[index] = newLength

# Rewind to print data
fObj.seek(0)

header = fObj.readline().strip('\n')
headerCols = header.split(';')

count = 0

headerParts = [''] * columnsCount
for index, head in enumerate(headerCols):
    fillCount = sizes[index] - len(head)
    fill = ' ' * fillCount
    headerParts[index] = fill + head

glue = ' | '
headerRow = glue.join(headerParts)
print(headerRow)
hrLength = sum(sizes) + len(glue) * (len(sizes) - 1)
print('-' * hrLength)

for line in fObj:
    cols = line.strip('\n').split(';', columnsCount)
    for index, col in enumerate(cols):
        fillCount = sizes[index] - len(col)
        if index == columnsCount - 1:
            print(' ' * fillCount, col, sep='', end='')
        else:
            print(' ' * fillCount, col, sep='', end=' | ')
    print()
