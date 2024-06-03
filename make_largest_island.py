def largestIsland(grid) -> int:
    N = len(grid)
    visited = {}
    area_map = {}
    index = 2
    largest = 0
    def check(row, col, index):
        area = 0
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            visited[(r, c)] = index
            area += 1
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1),  (r, c-1)):
                if (nr, nc) not in visited:
                    if 0<=nr<N and 0<=nc<N and grid[nr][nc]:
                        stack.append((nr, nc))   
        return area
    
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 1 and (row, col) not in visited:
                area_map[index] = check(row, col, index)
                index+= 1 
    
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                index_inc = set()
                curr_area = 1
                for nrow, ncol in ((row+1,col), (row-1,col), (row,col+1), (row,col-1)):
                    if (nrow, ncol) in visited and visited[(nrow, ncol)] not in index_inc:
                        curr_area += area_map[visited[(nrow, ncol)]]
                        index_inc.add(visited[(nrow, ncol)])
                print(curr_area)
                largest = max(largest, curr_area)
                        
                    
    # print(area_map)
    # print(visited)
    return largest

grid = [[1,1,1,0,1],[0, 1, 0,0,1],[0, 0, 0,0,0],[0, 1, 0,0,0],[1, 1, 1,0,1]]
print(largestIsland(grid))