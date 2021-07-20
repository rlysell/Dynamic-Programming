#include <iostream>
#include <cmath>
#include <string>
#include <ctime>
#include <iomanip>

std::string toBinary(int num, std::string result = ""){
    if (num == 1)
        return "1";
    result = std::to_string(num % 2);
    return toBinary(num / 2, result) + result;
}

int main(){
    int decimal;
    std::cout << "Choose number to convert to binary: ";
    std::cin >> decimal;
    std::clock_t start = std::clock();
    std::string binary = toBinary(decimal);
    std::clock_t time = std::clock() - start;
    std::cout << "The binary representation of " << decimal << " is " << binary << std::endl;
    std::cout << "And the computational time was " << std::fixed << 1.0 / 1000 * time << std::setprecision (20) << " seconds" << std::endl;
}