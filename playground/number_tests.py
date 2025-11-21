def is_even(number):
    return number % 2 == 0
def is_positive(number):
    return number > 0

test_cases = [2,-3,0,10,-1,5, "hello", None, [1, 2], "123"]
passed = 0
failed = 0 

for number in test_cases:
    print(f"\nTesting number: {number}")
    try:
        expected_even = (number % 2 == 0)
        result_even = is_even(number)
        if result_even == expected_even:
            print(" PASS: is_even() returned the correct result")
            passed +=1
        else:
            print(" FAIL: is_even() returned the wrong result")
            failed += 1
        expected_positive = (number > 0) 
        result_positive = is_positive(number)
        if result_positive == expected_positive:
            print(" PASS: is_positive() returned the correct result")
            passed += 1
        else:
            print(" FAIL: is_positive() returned the wrong result")
            failed += 1 
    except Exception as e:
        print(f" ERROR: Test failed for input '{number}' ({type(number).__name__}): {e}")
        failed += 2  # Count both tests as failed   
    
print("\n---- FINAL RESULTS ----") 
print(f"Total passed tests: {passed}")
print(f"Total failed tests: {failed}")


