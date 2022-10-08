import pytest
from codeWars import digitalRoot
from codeWars import splitNumberAppend


@pytest.mark.parametrize(
    "test_input,expected_result", [(16, 7), (942, 6), (132189, 6), (493193, 2)]
)
def test_digital_root(test_input, expected_result):
    result = digitalRoot(test_input)

    assert result == expected_result

@pytest.mark.parametrize('test_input,expected_result', [(19920, (1, 9, 9, 2, 0)), (9, (9,)), (19, (1, 9)), (3567, (3, 5, 6, 7))])
def test_split_large_int_to_single_digits(test_input, expected_result):
    # test_large_int = 19920
    # expected_result = (1, 9, 9, 2, 0)
    result = splitNumberAppend(test_input)

    assert result == expected_result
