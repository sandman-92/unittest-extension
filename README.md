# unittest-extension
extensions to the unittest python module

These extensions allow the dynamic creation of unittest.TestCases in scrips.
The result class saves successful results. I have also added a NULL test function, this is
useful for cases where you may need to see whatever data in the results, but a pass/fail unit
test is not required.


use case
```
import TestCaseExtension
import TestResultExtension

#list of test instructions:
instruction = [{'test_objects':[1,1],'use_method':'assertEqual'},
                {'test_objects':[<>,<>], 'use_method':"NULL"},
                ]
                
result = TestResultExtension()

for test_instruction in instructions:
    test = TestCaseExtention(**test_instruction)
    test.run(result)
    
print(result)
```
