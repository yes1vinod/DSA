import java.util.ArrayList;
import java.util.List;

class IslandCounter {
    class Coords {
        int x;
        int y;

        public boolean equals(Object o) {
            Coords c = (Coords) o;
            return c.x == x && c.y == y;
        }

        public Coords(int x, int y) {
            super();
            this.x = x;
            this.y = y;
        }

        public int hashCode() {
            return new Integer(x + "0" + y);
        }
    }

    public int searchIsland(char[][] grid, int i, int j, List<Coords> checkedCoordinates, int rows, int cols) {
        int counter = 0;
        //if it finds all Zero increase the count
        System.out.println("counter >>" + counter);
        if ((grid[i][j]) == '1') {
            checkedCoordinates.add(new Coords(i, j));
            counter = 1;
            System.out.println("counter >>" + counter);
            if (i + 1 < rows) {
                if (!checkedCoordinates.contains(new Coords(i + 1, j))) {
                    searchIsland(grid, i + 1, j, checkedCoordinates, rows, cols);
                }
            }
            if (j + 1 < cols) {
                if (!checkedCoordinates.contains(new Coords(i, j + 1))) {
                    searchIsland(grid, i, j + 1, checkedCoordinates, rows, cols);
                }
            }
            if (i - 1 >= 0) {
                if (!checkedCoordinates.contains(new Coords(i - 1, j))) {
                    searchIsland(grid, i - 1, j, checkedCoordinates, rows, cols);
                }
            }
            if (j - 1 >= 0) {
                if (!checkedCoordinates.contains(new Coords(i, j - 1))) {
                    searchIsland(grid, i, j - 1, checkedCoordinates, rows, cols);
                }
            }
        } else {
            return 0;
        }
        return counter;
    }

    public int numIslands(char[][] grid) {
        int counter = 0;
        int rows = grid.length;
        int cols = 0;
        if (rows > 0) {
            cols = grid[0].length;
        }
        List<Coords> checkedCoordinates = new ArrayList<Coords>();
        int islandCount = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (!checkedCoordinates.contains(new Coords(i, j))) {
                    System.out.println("calling subfunction -->");
                    counter = counter + searchIsland(grid, i, j, checkedCoordinates, rows, cols);
                }
            }
        }
        System.out.println("rows ->" + rows + "| Cols -> " + cols + " | Result : "+ counter);
        return counter;
    }

    public static void main(String[] args) {

        IslandCounter sol = new IslandCounter();
        char[][] gridArray = {{'1', '1', '1'}, { '0', '1', '0'}, {'1', '1', '1'}};

        sol.numIslands(gridArray);

    }
}