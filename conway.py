import random, sys, copy, time
def conway_game(height, width):
    #create an initial configuration using the random module
    config = []
    for x in range(width):
        column = []
        for y in range(height):
            if random.randint(0, 1) == 1:
                column.append('#') #add a living cell
            else:
                column.append(' ') #add a dead cell
        config.append(column)

    #Game begins and continues as long as user does not press CTRL-C
    try:
        while True:
            print('\n\n\n') #separate each configuration with newlines
            new_config = copy.deepcopy(config) #make a copy of the current cell configuration
            #print cells on the screen
            for y in range(height):
                for x in range(width):
                    print(config[x][y], end='')
                print()
            
            #determine which cells die or live
            for x in range(width):
                for y in range(height):
                    #get the neighboring coordinates
                    left_coord = (x - 1) % width
                    right_coord = (x + 1 ) % width
                    above_coord = (y - 1) % height
                    below_coord = (y + 1) % height

                    #count number of living cells
                    numCells = 0
                    if new_config[left_coord][above_coord] == '#':
                        numCells += 1
                    if new_config[x][above_coord] == '#':
                        numCells += 1
                    if new_config[right_coord][above_coord] == '#':
                        numCells += 1
                    if new_config[right_coord][y] == '#':
                        numCells += 1
                    if new_config[right_coord][below_coord] == '#':
                        numCells += 1
                    if new_config[x][below_coord] == '#':
                        numCells += 1
                    if new_config[left_coord][below_coord] == '#':
                        numCells += 1
                    if new_config[left_coord][y] == '#':
                        numCells += 1

                    #use the rules to determing which cells live and which die or stay dead
                    if new_config[x][y] == '#' and (numCells == 2 or numCells == 3):
                        #if cell is alive and number of living neighboring cells are either 2 or 3, it stays alive
                        config[x][y] = '#'
                    elif new_config[x][y] == ' ' and numCells == 3:
                        #if cell is dead and number of living neighbouring cells is exactl 3, it comes alive
                        config[x][y] = '#'
                    else:
                        #everything else dies or stays dead
                        config[x][y] = ' '
            #let there be a pause after each step
            time.sleep(1)                
        
    except KeyboardInterrupt:
        sys.exit()

def main():
    try:
        height= int(input("Enter the height of our Conway graph: "))
        width= int(input("Enter the width of our Conway graph: "))
        conway_game(height, width)
    except (ValueError, TypeError):
        print("Input must be an integer.")
        option = input("To Continue, type Y and click Enter\nTo Quit, press any other letter and click Enter\n")
        if option == 'Y' or option == 'y':
            main()
        else:
            print("Bye!")
            sys.exit()

if __name__ == "__main__":
    main()
