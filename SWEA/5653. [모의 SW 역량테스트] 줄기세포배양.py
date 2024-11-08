import sys

sys.stdin = open("/mnt/c/Users/jws/repos/interviews/SWEA/sample_input.txt", "r")  # Reading from input file

# Directions for reproduction: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())  # N, M, and K input
    primary_arr = [list(map(int, input().split())) for _ in range(N)]  # N x M grid input

    # Initialize a dictionary to track cells; keys are (i, j) coordinates, values are (life, state)
    cells = {}
    active_cells = []  # List to track cells to process for activation and reproduction

    # Add initial cells to the grid and list
    print(f"\n--- Test Case {test_case} ---")
    for i in range(N):
        for j in range(M):
            if primary_arr[i][j] > 0:
                life = primary_arr[i][j]
                cells[(i, j)] = (life, 'deactivated')  # Initially all cells are deactivated
                active_cells.append((life, i, j, life))  # Add to active list (life, row, col, time to activate)
                print(f"Cell added at ({i}, {j}) with life {life} (deactivated)")

    # Simulate hour by hour
    for hour in range(1, K + 1):
        print(f"\nHour {hour}:")
        new_cells = {}  # Dictionary to track potential new cells by (row, col)

        # Process the current list of cells
        current_active_cells = []
        for life, row, col, remaining_time in active_cells:
            if remaining_time == hour:
                # Activate the cell
                if cells[(row, col)][1] == 'deactivated':
                    cells[(row, col)] = (life, 'activated')
                    print(f"Cell at ({row}, {col}) activated with life {life}")

            # Reproduce during the first hour **after** activation
            if cells[(row, col)][1] == 'activated' and (hour - remaining_time == 1):
                print(f"Cell at ({row}, {col}) reproducing with life {life}")
                # Attempt to reproduce in 4 directions (only into empty spots)
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) not in cells or cells[(nr, nc)][1] == 'empty':
                        # Register reproduction attempt in this direction
                        if (nr, nc) not in new_cells:
                            new_cells[(nr, nc)] = life
                        else:
                            # If multiple cells try to reproduce into the same spot, keep the higher life value
                            new_cells[(nr, nc)] = max(new_cells[(nr, nc)], life)
                        print(f"Cell attempting reproduction at ({nr}, {nc}) with life {life}")

            # Keep track of cells that are still active or deactivated
            if cells[(row, col)][1] == 'deactivated' or (cells[(row, col)][1] == 'activated' and (hour - remaining_time) < life):
                current_active_cells.append((life, row, col, remaining_time))

            # Mark the cell as dead after it has been activated for its life duration
            if cells[(row, col)][1] == 'activated' and (hour - remaining_time) >= life:
                cells[(row, col)] = (life, 'dead')
                print(f"Cell at ({row}, {col}) died")

        # Process all reproduction attempts and add the highest life cells to the grid
        for (nr, nc), life in new_cells.items():
            cells[(nr, nc)] = (life, 'deactivated')  # The highest-life cell wins the spot
            current_active_cells.append((life, nr, nc, hour + life))
            print(f"Cell reproduced at ({nr}, {nc}) with life {life}")

        # Update the list of active cells for the next hour
        active_cells = current_active_cells
        print(f"Total active cells after hour {hour}: {len(active_cells)}")

    # Count the living cells after K hours (either deactivated or activated)
    non_dead_cells = sum(1 for state in cells.values() if state[1] in ('activated', 'deactivated'))

    # Output the result for each test case
    print(f"#{test_case} {non_dead_cells}")
