# Project Euler


Collection of solutions in Python and Rust for problems sourced from [Project Euler](https://projecteuler.net).

If you want to add me on project Euler, my username is:

__Username:__ Amenability  
__Key:__ 1984933_0cZrgC66BxEYqN5CbjK27fsbJfjRBX6W

[Here](#reproduce-the-solutions), you can find a guide on how to reproduce the solutions, 
and [here](#list-of-solution-with-execution-time) you can find a list of solutions with execution time.

## Reproduce the solutions

### Python

From the root directory (`project_euler`), execute the following command:
```shell
% python python/main.py PROBLEM_NUMBER
```
where `PROBLEM_NUMBER` is the problem number for which you want to obtain the solution.
Example:
```shell
% python python/main.py 1
Problem 1 - Multiples of 3 or 5 
Description: https://projecteuler.net/problem=1 
Solution: 233168 
Time: 0.08225440979003906ms
```

### Rust

From the root directory (`project_euler`), execute the following commands:
```shell
% cd rust
% cargo build --release
```
this will compile the Rust scripts.
After that you can use the following command
```shell
% target/release/rust PROBLEM_NUMBER
```
to obtain the solution of the problem number `PROBLEM_NUMBER`.
Example
```shell
% target/release/rust 1
Problem 1 - Multiples of 3 or 5
Description: https://projecteuler.net/problem=1
Solution: 233168
Time: 2.13µs
```

## List of solution with execution time

| Problem Number | Problem Title                         | Solution        | Python Time | Rust Time |
|----------------|---------------------------------------|-----------------|-------------|-----------|
| 1              | Multiples of 3 and 5                  | 233_168         | 0.36ms      | 2.13µs    |
| 2              | Even Fibonacci number                 | 4_613_732       | 0.25ms      | 125ns     |
| 3              | Largest prime factor                  | 6_857           | 38ms        |
| 4              | Largest palindrome product            | 906_609         | 290ms       |
| 5              | Smallest multiple                     | 232_792_560     | 0.23ms      |
| 6              | Sum square difference                 | 25_164_150      | 279ms       |
| 7              | 10001st prime                         | 104_743         | 65          |
| 8              | Largest product in a series           | 23_514_624_000  | 290         |
| 9              | Special Pythagoren triplet            | 31_875_000      | 92          |
| 10             | Summation of primes                   | 142_913_828_922 | 2_975       |  
| 11             | Largest product in a grid             | 70_600_674      | 300         |
| 12             | Highly divisible triangular number    | 76_576_500      | 3_000       |
| 13             | Large sum                             | 5_537_376_230   | 283         |
| 14             | Longest Collatz sequence              | 837_799         | 1_692       |
| 15             | Lattice paths                         | 137_846_528_820 | 2           |
| 16             | Power digit sum                       | 1_366           | 1.5         |
| 17             | Number Letter Counts                  | 21_124          | 0.5         |
| 18             | Maximum path sum I                    | 1_074           | 6           |
| 20             | Factorial digit sum                   | 648             | 5           |
| 21             | Amicable numbers                      | 31_626          | 57          |
| 22             | Names scores                          | 871_198_282     | 16          |
| 23             | Non-abundant sums                     | 4_179_871       | 1_898       |
| 24             | Lexicographic permutations            | 2_783_915_460   | 600         |
| 25             | 1000-digit Fibonacci number           | 4_782           | 30          |
| 26             | Reciprocal cycles                     | 983             | 143         |
| 27             | Quadratic primes                      | -59_231         | 61          |
| 28             | Number spiral diagonals               | 669_171_001     | 9           |
| 29             | Distinct powers                       | 9_183           | 6           |
| 30             | Digit fifth powers                    | 443_839         | 421         |
| 31             | Coin Sums                             | 73_682          | 4           |
| 33             | Digit cancelling fractions            | 100             | 277         |
| 34             | Digit factorials                      | 40_730          | 535         |
| 35             | Circular primes                       | 55              | 1_700       |
| 36             | Double-base palindromes               | 872_187         | 380         |
| 37             | Truncable primes                      | 748_317         | 269         |
| 39             | Integer right triangles               | 840             | 160         |
| 40             | Champernowne's constant               | 210             | 88          |
| 41             | Pandigital prime                      | 7_652_413       | 32          |
| 42             | Coded triangle numbers                | 162             | 9           |
| 44             | Pentagon numbers                      | 5_482_660       | 1_475       |
| 45             | Triangular, pentagonal, and hexagonal | 1_533_776_805   | 37          |
| 48             | Self powers                           | 9_110_846_700   | 52          |
| 52             | Permuted Multiples                    | 142857          | 103         |
| 53             | Combinatoric Selections               | 4075            | 8           |
| 55             | Lychrel Numbers                       | 249             | 46          |
| 56             | Powerful digit sum                    | 972             | 74          |
| 62             | Cubic Permutations                    | 12_703_5954_683 | 13          |
| 63             | Powerful digit counts                 | 49              | 3           |
| 65             | Convergents of e                      | 272             | 7           |
| 67             | Maximum path sum II                   | 7_273           | 11          |
| 69             | Totient maximum                       | 510_510         | 4           |
| 71             | Ordered fractions                     | 428_570         | 3           |
| 74             | Digit factorial chains                | 402             | 25_000      |
| 76             | Counting Summations                   | 190_569_291     | 10          |
| 92             | Square digit chains                   | 8_581_146       | 19_500      |
| 97             | Large Non-Marsenne Prime              | 8_739_992_577   | 879         |
| 99             | Largest Exponential                   | 709             | 6           |
| 145            | Reversible Numbers                    | 608_720         | 3           |
| 836            | A Bold proposition                    | aprilfoolsjoke  | 0.24        |
