import io
import re
import sys

from src.TimeSpent import DecoPrint

def test_print_time_decorator():
    expected_result = "@timeFn: sleep1sFn spent * seconds\n"
    expected_time_spent = 1
    
    capturedOutput = io.StringIO()          
    sys.stdout = capturedOutput
    DecoPrint.sleep1sFn()
    sys.stdout = sys.__stdout__
    result = capturedOutput.getvalue()

    # extract the time spent
    
    time_spent_regex = re.compile('\s(?P<time>\d)\.\d+\s')
    time_spent_result = time_spent_regex.search(result)
    assert int(time_spent_result.group('time')) == expected_time_spent

    # test the rest of the output
    result_format = time_spent_regex.sub(' * ', result)
    assert result_format == expected_result
