# Google Test List Sorter

Sorts list of tests produced by the `--gtest_list_tests` option. Sorts in alphabetical order.

Usage on Windows:

    UnitTests.exe --gtest_list_tests | python sort-google-test-list.py
    
Usage on Ubuntu:

    ./UnitTests --gtest_list_tests | python3 sort-google-test-list.py 

## Example

Run on Ubuntu:

    cat list | python3 sort-google-test-list.py

Unsorted list:

    BBB.
      PPPP
      AAAA
      UUUU
    AAA.
      BBBB
      aaaa
      bbbb
      CCCC
    ZZZ.
      5555
      XXXX
      1111
      cccc

Sorted list:

    AAA
      aaaa
      BBBB
      bbbb
      CCCC
    BBB
      AAAA
      PPPP
      UUUU
    ZZZ
      1111
      5555
      cccc
      XXXX
