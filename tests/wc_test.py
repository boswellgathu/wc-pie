import subprocess
import pytest

@pytest.mark.parametrize("option,value",
        [('-c', '342190'),
        ('-l', '7145'),
        ('-w', '58164')])
def test_wc_option_returns_expected_value(option, value):
    command = f"python wc.py {option} test.txt"
    expected_output = f'{value}\ttest.txt'

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    actual_output = output.decode().strip()

    assert actual_output == expected_output

def test_wc_no_options_returns_default():
    command = "python wc.py test.txt"
    expected_output = '7145\t58164\t342190 \ttest.txt'

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    actual_output = output.decode().strip()
    assert actual_output == expected_output

def test_wc_can_read_from_stdin():
    echo_command = subprocess.Popen(['echo', 'githeri'], stdout=subprocess.PIPE)
    command = "python wc.py"
    expected_output = '1\t1\t8'

    process = subprocess.Popen(command.split(), stdin=echo_command.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    actual_output = output.decode().strip()
    assert actual_output == expected_output
