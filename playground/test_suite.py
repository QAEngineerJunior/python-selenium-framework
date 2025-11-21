def is_even(number):
    """Return True if the number is even, otherwise False"""
    return number % 2 == 0

# ---- Test Suite ----
Test_cases = [2,3,10,11,100,101]

passed = 0
Failed = 0

for number in Test_cases:
    result =is_even(number)
    if result:
        print(f"PASS: {number} is even")
        passed +=1
    else:
        print(f"FAIL: {number} is not even")

print("\n---- FINAL RESULTS ----")
print(f"Passed tests: {passed}")
print(f"Failed tests: {Failed}")

              

