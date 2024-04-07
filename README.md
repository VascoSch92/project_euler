# Project Euler


Collection of solutions in Python and Rust for problems sourced from [Project Euler](https://projecteuler.net).

If you want to add me on project Euler, my username is:

__Username:__ Amenability  
__Key:__ 1984933_0cZrgC66BxEYqN5CbjK27fsbJfjRBX6W

[Here](#reproduce-the-solutions), you can find a guide on how to reproduce the solutions, 
and [here](#list-of-solution-with-execution-time) you can find a list of solutions with execution time.

## Reproduce the solutions

### Python

To reproduce the results with Python, you first need to create a Conda environment with the correct packages. 
To do so, run the following command from the root directory: (`project_euler`).
```shell
conda env create -f environment.yml
```

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

| Problem Number | Problem Title                         | Solution        | Python Time | Rust Time  |
|----------------|---------------------------------------|-----------------|-------------|------------|
| 1              | Multiples of 3 and 5                  | 233_168         | 0.36ms      | 2.13µs     |
| 2              | Even Fibonacci number                 | 4_613_732       | 0.25ms      | 125ns      |
| 3              | Largest prime factor                  | 6_857           | 38ms        | 2.07ms     |
| 4              | Largest palindrome product            | 906_609         | 290ms       | 53ms       | 
| 5              | Smallest multiple                     | 232_792_560     | 0.23ms      | 334ns      |
| 6              | Sum square difference                 | 25_164_150      | 279ms       | 1.33µs     |
| 7              | 10001st prime                         | 104_743         | 65ms        | 8.23ms     |
| 8              | Largest product in a series           | 23_514_624_000  | 290ms       |
| 9              | Special Pythagorean triplet           | 31_875_000      | 92ms        | 588.00µs   |
| 10             | Summation of primes                   | 142_913_828_922 | 2_975ms     | 169.85ms   |
| 11             | Largest product in a grid             | 70_600_674      | 300ms       |
| 12             | Highly divisible triangular number    | 76_576_500      | 3_000ms     | 301.85ms   |
| 13             | Large sum                             | 5_537_376_230   | 283ms       |
| 14             | Longest Collatz sequence              | 837_799         | 1_692ms     |
| 15             | Lattice paths                         | 137_846_528_820 | 2ms         |
| 16             | Power digit sum                       | 1_366           | 1.5ms       |
| 17             | Number Letter Counts                  | 21_124          | 0.5ms       |
| 18             | Maximum path sum I                    | 1_074           | 6ms         |
| 20             | Factorial digit sum                   | 648             | 5ms         |
| 21             | Amicable numbers                      | 31_626          | 57ms        |
| 22             | Names scores                          | 871_198_282     | 16ms        |
| 23             | Non-abundant sums                     | 4_179_871       | 1_898ms     |
| 24             | Lexicographic permutations            | 2_783_915_460   | 600ms       |
| 25             | 1000-digit Fibonacci number           | 4_782           | 30ms        |
| 26             | Reciprocal cycles                     | 983             | 143ms       |
| 27             | Quadratic primes                      | -59_231         | 61ms        |
| 28             | Number spiral diagonals               | 669_171_001     | 9ms         |
| 29             | Distinct powers                       | 9_183           | 6ms         |
| 30             | Digit fifth powers                    | 443_839         | 421ms       |
| 31             | Coin Sums                             | 73_682          | 4ms         |
| 33             | Digit cancelling fractions            | 100             | 277ms       |
| 34             | Digit factorials                      | 40_730          | 535ms       |
| 35             | Circular primes                       | 55              | 1_700ms     |
| 36             | Double-base palindromes               | 872_187         | 380ms       |
| 37             | Truncable primes                      | 748_317         | 269ms       |
| 39             | Integer right triangles               | 840             | 160ms       |
| 40             | Champernowne's constant               | 210             | 88ms        |
| 41             | Pandigital prime                      | 7_652_413       | 32ms        |
| 42             | Coded triangle numbers                | 162             | 9ms         |
| 44             | Pentagon numbers                      | 5_482_660       | 1_475ms     | 11.36ms    |
| 45             | Triangular, pentagonal, and hexagonal | 1_533_776_805   | 37ms        |
| 48             | Self powers                           | 9_110_846_700   | 52ms        |
| 52             | Permuted Multiples                    | 142857          | 103ms       |
| 53             | Combinatoric Selections               | 4075            | 8ms         |
| 55             | Lychrel Numbers                       | 249             | 46ms        |
| 56             | Powerful digit sum                    | 972             | 74ms        |
| 62             | Cubic Permutations                    | 12_703_5954_683 | 13ms        |
| 63             | Powerful digit counts                 | 49              | 3ms         |
| 65             | Convergents of e                      | 272             | 7ms         |
| 67             | Maximum path sum II                   | 7_273           | 11ms        |
| 69             | Totient maximum                       | 510_510         | 4ms         |
| 71             | Ordered fractions                     | 428_570         | 3ms         |
| 74             | Digit factorial chains                | 402             | 25_000ms    |
| 76             | Counting Summations                   | 190_569_291     | 10ms        |
| 92             | Square digit chains                   | 8_581_146       | 19_500ms    |
| 97             | Large Non-Marsenne Prime              | 8_739_992_577   | 879ms       |
| 99             | Largest Exponential                   | 709             | 6ms         |
| 145            | Reversible Numbers                    | 608_720         | 3ms         |
| 836            | A Bold proposition                    | aprilfoolsjoke  | 0.24ms      | 167.00ns   |
