import java.util.ArrayList;

public class StockAnalyzer {
    // Calculates average price for array input
    // Takes float array of prices and returns average as float
    public static float calculateAveragePrice(float[] pricesArray) {
        float sum = 0;
        for (float price : pricesArray) {
            sum += price;
        }
        return sum / pricesArray.length;
    }

    // Calculates average price for ArrayList input
    // Takes ArrayList of Float prices and returns average as float
    public static float calculateAveragePrice(ArrayList<Float> pricesList) {
        float sum = 0;
        for (float price : pricesList) {
            sum += price;
        }
        return sum / pricesList.size();
    }

    // Finds maximum price in array input
    // Takes float array of prices and returns highest price as float
    public static float findMaximumPrice(float[] pricesArray) {
        float max = pricesArray[0];  // Start with first element as max
        for (float price : pricesArray) {
            if (price > max) {
                max = price;
            }
        }
        return max;
    }

    // Finds maximum price in ArrayList input
    // Takes ArrayList of Float prices and returns highest price as float
    public static float findMaximumPrice(ArrayList<Float> pricesList) {
        float max = pricesList.get(0);  // Start with first element as max
        for (float price : pricesList) {
            if (price > max) {
                max = price;
            }
        }
        return max;
    }

    // Counts occurrences of target price in array input
    // Takes float array of prices and target price, returns count as integer
    public static int countOccurrences(float[] pricesArray, float targetPrice) {
        int count = 0;
        for (float price : pricesArray) {
            if (price == targetPrice) {
                count++;
            }
        }
        return count;
    }

    // Counts occurrences of target price in ArrayList input
    // Takes ArrayList of Float prices and target price, returns count as integer
    public static int countOccurrences(ArrayList<Float> pricesList, float targetPrice) {
        int count = 0;
        for (float price : pricesList) {
            if (price == targetPrice) {
                count++;
            }
        }
        return count;
    }

    // Computes running sum of prices in ArrayList input
    // Takes ArrayList of Float prices and returns ArrayList of cumulative sums
    public static ArrayList<Float> computeCumulativeSum(ArrayList<Float> pricesList) {
        ArrayList<Float> cumulativeSum = new ArrayList<>();
        float sum = 0;
        for (float price : pricesList) {
            sum += price;
            cumulativeSum.add(sum);
        }
        return cumulativeSum;
    }

    // Main method to test all implementations
    public static void main(String[] args) {
        // Create test data
        float[] pricesArray = {10.5f, 11.2f, 12.0f, 11.2f, 10.8f};

        // Convert array to ArrayList for testing
        ArrayList<Float> pricesList = new ArrayList<>();
        for (float price : pricesArray) {
            pricesList.add(price);
        }

        // Test and display results for array implementation
        System.out.println("Array Implementation:");
        System.out.println("Average Price: " + calculateAveragePrice(pricesArray));
        System.out.println("Maximum Price: " + findMaximumPrice(pricesArray));
        System.out.println("Occurrences of 11.2: " + countOccurrences(pricesArray, 11.2f));
        System.out.println("Cumulative Sum: " + computeCumulativeSum(pricesList));

        // Test and display results for ArrayList implementation
        System.out.println("\nArrayList Implementation:");
        System.out.println("Average Price: " + calculateAveragePrice(pricesList));
        System.out.println("Maximum Price: " + findMaximumPrice(pricesList));
        System.out.println("Occurrences of 11.2: " + countOccurrences(pricesList, 11.2f));
        System.out.println("Cumulative Sum: " + computeCumulativeSum(pricesList));
    }
}
