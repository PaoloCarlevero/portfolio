import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private static final double CONFIDENCE_LEVEL_VALUE = 1.96;
    private double[] results;
    private int sideLength;
    private int numOfTrials;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        // Assigning value to instance variables
        sideLength = n;
        numOfTrials = trials;
        // Exception handling
        // Side's lenght must be bigger than zero
        if (sideLength <= 0) {
            throw new IllegalArgumentException("Side's length must be bigger than zero");
        }
        // Number of trials bust be bigger than zero
        if (numOfTrials <= 0) {
            throw new IllegalArgumentException("Number of trials must be bigger than zero");
        }
        // Main logic
        // Setting the size of the results'array to the number of trials
        results = new double[numOfTrials];
        // Looping for the number of trials
        for (int i = 0; i < numOfTrials; i++) {
            // Istance of percolation class
            Percolation trial = new Percolation(sideLength);
            // Opening cites untill the system percolates
            while (!trial.percolates()) {
                // Genrating random coordinates for the cite to open
                int row = StdRandom.uniformInt(sideLength);
                int col = StdRandom.uniformInt(sideLength);
                trial.open(row+1, col+1);
            }
            // Getting the number of open and cating it as a double
            double numberOfOpenSites = trial.numberOfOpenSites();
            // Inserting the percolation threshold at the corresponding index of the results array
            results[i] = numberOfOpenSites / (sideLength*sideLength);
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(results);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(results);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - (CONFIDENCE_LEVEL_VALUE*stddev()/Math.sqrt(numOfTrials));
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + (CONFIDENCE_LEVEL_VALUE*stddev()/Math.sqrt(numOfTrials));
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats stats = new PercolationStats(n, trials);
        System.out.println("mean                    = " + stats.mean());
        System.out.println("stddev                  = " + stats.stddev());
        System.out.println("95% confidence interval = " + "[" + stats.confidenceLo() + "," + stats.confidenceHi() + "]");
   }
}
