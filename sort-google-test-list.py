"""
Google Test List Sorter

Sorts list of tests produced by the `--gtest_list_tests` option. Sorts in alphabetical order.

Usage on Windows:

    UnitTests.exe --gtest_list_tests | python sort-google-test-list.py

Usage on Ubuntu:

    ./UnitTests --gtest_list_tests | python3 sort-google-test-list.py
"""

tests = {}
current_test = ''

while True:
    try:
        test = input()
    except EOFError:
        break

    if not test:
        continue

    if test.startswith('  '):
        tests[current_test].append(test.strip())
    else:
        current_test = test.strip().strip('.')
        tests[current_test] = []

for key in sorted(tests.keys(), key=str.lower):
    print(key)
    for value in sorted(tests[key], key=str.lower):
        print('  ' + value)
