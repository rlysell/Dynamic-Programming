#include <iostream>
#include <map>
#include <ctime>
#include <iomanip>

double knapsack(double value[], double weight[], int n, double maxweight, std::map <int, double> &memo){
    if (maxweight < 0)
        return INT16_MIN;
    
    if (n < 0 || maxweight == 0)
        return 0;
    
    if (memo.count(n))
        return memo[n];

    double include = value[n] + knapsack(value, weight, n - 1, maxweight - weight[n], memo);
    double exclude = knapsack(value, weight, n - 1, maxweight, memo);

    memo[n] = std::max(include, exclude);
    return memo[n];
}

int main(){
    double value [ ] = { 20, 5, 10, 40, 15, 25};
    double weight [ ] = { 1, 2, 3, 8, 7, 4};
    double maxweight = 1000;
    std::map <int, double> map;
    std::clock_t start = std::clock();
    double sol = knapsack(value, weight, sizeof(value)/sizeof(value[0]) - 1, maxweight, map);
    std::clock_t end = std::clock();
    std::cout << sol << "\t" << std::fixed << 1.0 / 1000 * (end - start) << std::setprecision (20) << std::endl;
    return 0;
}

// Without catche O(2^n)
// With catche O(n*maxweight)