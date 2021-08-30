import os, random, pygame, time, collections

pygame.init()
winx = 600
winy = 600
pygame.display.set_caption("Tic-Tac-Toe")
screen = pygame.display.set_mode((winx, winy))
gameSurface = pygame.Surface((winx, winy))
gameSurface.set_colorkey((0, 0, 0))
gameSurface.set_alpha(128)

class Agent:
    def __init__(self, symbol):
        self.symbol = symbol
    def move(self, grid):

        # count = 0
        # for row in grid:
        #     count += row.count(None)

        # minMax(count, grid)
        for row in grid:
            for cell in row:
                print(cell.id)

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)

            if grid[x][y].symbol == None:
                grid[x][y].symbol = self.symbol
                updateGrid(grid)
                pygame.display.update()
                return



class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class Cell:
    def __init__(self, id):
        self.id = id
        self.symbol = None
    def assign(self, symbol):
        self.symbol = symbol

# def minMax(count, grid):

#     if count == 0:
#         return
    
#     mmgrid = grid.copy()

#     for row in mmgrid:
#         for cell in row:
#             if cell == None:
#                 minMax(count - 1, mmgrid)
    
                

def drawGrid():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (195, 15, 15, 570), 0)
    pygame.draw.rect(screen, (255, 255, 255), (390, 15, 15, 570), 0)

    pygame.draw.rect(screen, (255, 255, 255), (15, 195, 570, 15), 0)
    pygame.draw.rect(screen, (255, 255, 255), (15, 390, 570, 15), 0)

def drawSymbol(x, y, symbol):
    if symbol == 'X':
        pygame.draw.line(screen, (255, 255, 255), (30 + 195 * x, 30 + 195 * y), (180 + 195 * x, 180 + 195 * y), 15)
        pygame.draw.line(screen, (255, 255, 255), (180 + (195 * x), 30 + (195 * y)), (30 + (195 * x), 180 + (195 * y)), 15)
    elif symbol == 'O':
        pygame.draw.circle(screen, (255, 255, 255), (105 + 195 * x, 105 + 195 * y), 75, 15)

def updateGrid(grid):
    drawGrid()
    for i in range(3):
        for j in range (3):
            if grid[i][j].symbol != None:
                drawSymbol(j, i, grid[i][j].symbol) 

def printWinner(winner):
    if winner == None:
        writeOnScreen('TIC-TAC-TOE', 50, 0, -40)
    elif winner == 'Tie':
        writeOnScreen('TIE!', 50, 0, -40)
    else:
        writeOnScreen(winner + ' is the winner!', 50, 0, -40)

    writeOnScreen('Play as "X"', 35, -100, 20)
    writeOnScreen('Play as "O"', 35, 100, 20)


def writeOnScreen(txt, size, offsetX, offsetY):
    font = pygame.font.SysFont("Arial", size)
    txt = font.render(txt, 1, (255, 255, 255))
    x = (winx - txt.get_rect().width) / 2
    y = (winy - txt.get_rect().height) / 2
    screen.blit(txt, (int(x) + offsetX, (int(y) + offsetY)))    

def checkWinner(grid):
    for i in range(3):
        if grid[i][0].symbol == grid[i][1].symbol == grid[i][2].symbol != None:
            return grid[i][0].symbol, 'end'
        elif grid[0][i].symbol == grid[1][i].symbol == grid[2][i].symbol != None:
            return grid[0][i].symbol, 'end'
    if grid[0][0].symbol == grid[1][1].symbol == grid[2][2].symbol != None:
        return grid[0][0].symbol, 'end'
    elif grid[2][0].symbol == grid[1][1].symbol == grid[0][2].symbol != None:
        return grid[2][0].symbol, 'end'
    
    for row in grid:
        for symbol in row:
            if symbol.symbol == None:
                return None, 'game'
    
    return 'Tie', 'end'

def main():
    winner = None

    while True:
        # grid = [[None for i in range(3)] for j in range(3)]
        grid = [[Cell(i + (j * 3)) for i in range(3)] for j in range(3)]
        isXTurn = True
        gamePhase = 'start'

        screen.fill((0, 0, 0))

        printWinner(winner)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if gamePhase == 'game':
                            if (isXTurn and player.symbol == 'X') or (not isXTurn and player.symbol == 'O'):
                                x = event.pos[0] // 200
                                y = event.pos[1] // 200

                                if isXTurn:
                                    grid[y][x].assign('X')
                                else:
                                    grid[y][x].assign('O')

                                # print(grid)
                                updateGrid(grid)
                                # print(checkWinner(grid))
                                winner, gamePhase = checkWinner(grid)
                                isXTurn = not isXTurn
                        elif gamePhase == 'start':
                            x = event.pos[0]
                            y = event.pos[1]

                            if y > 295 and y < 345:
                                if x < 300:
                                    agent = Agent('O')
                                    player = Player('X')
                                    gamePhase = 'game'
                                    drawGrid()
                                elif x > 300:
                                    agent = Agent('X')
                                    player = Player('O')
                                    gamePhase = 'game'
                                    drawGrid()

                        pygame.display.update()
                
            if gamePhase == 'end':
                time.sleep(0.5)
                grid.clear()
                break

            if gamePhase == 'game' and ((isXTurn and agent.symbol == 'X') or (not isXTurn and agent.symbol == 'O')):
                time.sleep(0.5)
                agent.move(grid)
                isXTurn = not isXTurn
                # print(grid)
                # print(checkWinner(grid))
                winner, gamePhase = checkWinner(grid)

main()