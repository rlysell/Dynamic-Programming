#include <iostream>
#include <map>
#include <ctime>
#include <iomanip>

long double Fibonacci(int x, std::map<int, long double> &memo){
    if (memo.count(x)) {
        return memo[x];
    }
    if (x <= 2){
        return 1;
    }
    memo [x] = Fibonacci (x - 1, memo) + Fibonacci (x - 2, memo);
    return memo[x];
}

int main(){

    std::cout << "Choose number: ";
    int x;
    std::cin >> x;
    std::map<int, long double> map;
    std::clock_t start = std::clock ( );
    long double sol = Fibonacci (x, map);
    std::clock_t end = std::clock ();
    std::cout << "The " << x << "th number in the Fibonacci sequence is " << sol << std::endl;
    std::cout << "And it took " << std::fixed << 1.0 / 1000 * (end - start) << std::setprecision (20) << " seconds\n";
    
    return 0;
}