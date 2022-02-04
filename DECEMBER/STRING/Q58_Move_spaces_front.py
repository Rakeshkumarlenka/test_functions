
class Move():
    def moveSpaces(self):
        noSpaces = [ch for ch in input if ch != ' ']
        space = len(input) - len(noSpaces)
        result = ' ' * space
        result = '"' + result + ''.join(noSpaces) + '"'
        print(result)



input = 'welcome to Python World '
result = Move()
result.moveSpaces()