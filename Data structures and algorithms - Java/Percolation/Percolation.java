import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private static final int TOP = 0; // Topcells index
    private int bottom;
    private final int sideLength;
    private final int gridSize;
    private int numberOfOpenSites = 0;
    private boolean[] opened;
    private WeightedQuickUnionUF wqu;


    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {

        // Throws IllegalArgumentException if the grid size is less or equal to 0
        if (n <= 0) {
            throw new IllegalArgumentException("n must be bigger than 0");
        }

        sideLength = n; 
        gridSize = sideLength * sideLength;
        bottom = gridSize + 1;

        opened = new boolean[bottom+1];
        opened[TOP] = true;
        opened[bottom] = true;


        wqu = new WeightedQuickUnionUF(bottom+1);
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        // Validate imput parameters for exceptions
        validateInput(row, col);

        // Main logic
        if (!isOpen(row, col)) {

            // get the index associated with the coordinates
            int i = getIndex(row, col);

            // Open the site
            opened[i] = true;

            // Increment the umber of open sites
            numberOfOpenSites++;

            // Edge case -> First row connect to TOP
            if (row == 1) {
                wqu.union(col, TOP);
            }
            
            // Edge case -> last row connnect to bottom
            if (row == sideLength) {
                wqu.union(i, bottom);
            }

            // Same row, previsour column
            if (col > 1 && isOpen(row, col - 1)) {
                wqu.union(i, i-1);
            }

            // Same row, next column
            if (col < sideLength && isOpen(row, col + 1)) {
                wqu.union(i, i+1);
            }
            
            // Same column, previsour row
            if (row > 1 && isOpen(row-1, col)) {
                wqu.union(i, i-sideLength);
            }

            // Same column, next row
            if (row < sideLength && isOpen(row+1, col)) {
                wqu.union(i, i+sideLength);
            }
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        // Validate imput parameters for exceptions
        validateInput(row, col);

        // Main logic
        return opened[getIndex(row, col)];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        // Validate imput parameters for exceptions
        validateInput(row, col);
        
        // Main logic
        // By definition, a full site is open
        if (!isOpen(row, col)) {
            return false;
        }

        return wqu.find(getIndex(row, col)) == wqu.find(TOP);
    }

    // return the number of open sites
    public int numberOfOpenSites() {
        return numberOfOpenSites;
    }

    // does the system percolate?
    public boolean percolates() {
        return wqu.find(TOP) == wqu.find(bottom);
    }

    private void validateInput(int row, int col) {

        // Row number equal or less than 0
        if (row <= 0) {
            throw new IllegalArgumentException("Row number must be grater than 0");
        }

        // Column number equal or less than 0
        if (col <= 0) {
            throw new IllegalArgumentException("Column number must be grater than 0");
        }
        
        // Row number bigger than side length
        if (row > sideLength) {
            throw new IllegalArgumentException("Row numeber bust be less than side length");
        }

        if (col > sideLength) {
            throw new IllegalArgumentException("Column numeber bust be less than side length");
        }
    }

    // Return the index associated with the given coordiantes
    private int getIndex(int row, int col) {
        return (row-1)*sideLength + col;
    }

    public static void main(String[] args) {
    }
}