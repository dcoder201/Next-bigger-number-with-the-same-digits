def next_bigger(n):
    num_str = str(n)
    num_len = len(num_str)
    for i in range(num_len-2, -1, -1):
        if num_str[i] < num_str[i+1]:
            break
    else:
        return -1
    
    for j in range(num_len-1, i, -1):
        if num_str[j] > num_str[i]:
            break
    
    num_str = list(num_str)
    num_str[i], num_str[j] = num_str[j], num_str[i]
    num_str[i+1:] = sorted(num_str[i+1:])
    return int("".join(num_str))
  
  from solution import next_bigger
import codewars_test as test

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Examples")
    def examples():    
        test.assert_equals(next_bigger(  12),   21)
        test.assert_equals(next_bigger(  21),   -1)
        test.assert_equals(next_bigger( 513),  531)
        test.assert_equals(next_bigger(2017), 2071)
        test.assert_equals(next_bigger( 414),  441)
        test.assert_equals(next_bigger( 144),  414)
