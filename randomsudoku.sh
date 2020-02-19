cat sudoku.csv | tail -n +2 | tr ',' ' ' | awk '{print $1}' | shuf -n 1
