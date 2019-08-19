## Unit Testing Assignment

by Sivanat Subpaisarn


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| [1,2,2,3,4,4]          |  [1, 2, 3, 4]       |
| ['ei', 'ei', 'ei']     |  ['ei']             |
| ['wao!']               |  ['wao!']         |
| [ ]              | [ ]  |
| 10000   |  TypeError      |


## Test Cases for Fraction

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Fraction(1, 0)                  |  infinity           |
| Fraction(-1, 0)                  |  negative infinity  |
| Fraction(3, 7)                 |  3 / 7              |
| Fraction(1, [ ]) | TypeError|
| Fraction('Mek eiei', 2 )         |TypeError |
| 3 / 7 == 6 / 14        |  True               |
| 7 / 3                  |  7 / 3              |
| 1/2 + 1/2              |  1                  |
| 1/2 * 1/2              |  1/4                |
