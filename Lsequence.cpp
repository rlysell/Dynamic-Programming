#include <iostream>
#include <string>
#include <map>
#include <ctime>
#include <iomanip>

int LS(std::string X, std::string Y, int n, int m, std::map<std::string, int> &memo){

    std::string key = std::to_string(n) + "," + std::to_string(m);
    
    if (n == 0 || m == 0)
        return 0;
    
    if (memo.count(key))
        return memo[key];
    
    if (X[n - 1] == Y[m - 1]){
        memo [key] = LS (X, Y, n - 1, m - 1, memo) + 1;
        return memo[key];

    }
    
    memo[key] = std::max(LS(X, Y, n - 1, m, memo), LS(X, Y, n, m - 1, memo));
    return memo[key];
}


int main(){
    std::string X = "ABAGKFHJDLONVGJGKKDPWMMDPWMJDLEPDDLFLWPKDNVMLSWLELDKGKKSJEPDJKGJJGRK";
    std::string Y = "CHKWSLLWVVABGJDSHKJRHGLJSDKLGJEIKDJHDGRSUFNBFDJGHUVVBDSHFGYRSAFGSHDAVBM";
    int n = X.length();
    int m = Y.length();
    std::map <std::string, int> map;
    std::clock_t start = std::clock ();
    int ls = LS(X, Y, n, m, map);
    std::clock_t end = std::clock ();
    std::cout << "Longest sequence is: " << ls << std::endl;
    std::cout << "Computation time: " << std::fixed << 1.0 / 1000 * (end - start) << std::setprecision (20) << " seconds" << std::endl;

    return 0;
}