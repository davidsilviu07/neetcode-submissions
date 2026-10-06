from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque()
        proaspete = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    proaspete += 1

        minute = 0
        directii = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and proaspete > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directii:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        proaspete -= 1
                        q.append((nr, nc))
            minute += 1

        return minute if proaspete == 0 else -1