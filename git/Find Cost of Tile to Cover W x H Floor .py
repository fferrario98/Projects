def tiles(series):
    total_cost = ((series[0]*series[1])/(series[2]*series[3]))*series[4]
    return total_cost

def main():
    series = []
    if len(series) < 1:
        series.extend([float(input('what is the width of the floor in cm?'))])
    if len(series) < 2:
        series.extend([float(input('what is the height of the floor in cm?'))])
    if len(series) < 3:
        series.extend([float(input('what is the width of the tile in cm?'))])
    if len(series) < 4:
        series.extend([float(input('what is the height of the tiles in cm?'))])
    if len(series) < 5:
        series.extend([float(input('How much does each tile cost in Euro/tile?'))])
    for i in range(len(series)):  # Convert the numbers to strings. The idea is that it puts the comma-less series with floats,
                                  # into a string with commas
        series[i] = str(series[i])
        series[i] = float(series[i])

    print('The total cost to cover the entire floor is',tiles(series),'Euro')

    print('You did it!!')

if __name__ == '__main__':
    main()




