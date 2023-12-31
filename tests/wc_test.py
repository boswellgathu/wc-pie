import subprocess
import pytest

@pytest.mark.parametrize(
    "option, expected_value",
    [
        ('-c', '342190'),
        ('-l', '7145'),
        ('-w', '58164')
    ]
)
def test_wc_option_returns_expected_value(option, expected_value):
    command = f"python wc.py {option} test.txt"
    expected_output = f'{expected_value}\ttest.txt'

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    actual_output = output.decode().strip()

    assert process.returncode == 0
    assert actual_output == expected_output

def test_wc_no_options_returns_default():
    command = "python wc.py test.txt"
    expected_output = '7145\t58164\t342190 \ttest.txt'

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    actual_output = output.decode().strip()

    assert process.returncode == 0
    assert actual_output == expected_output

def test_wc_can_read_from_stdin_when_file_is_not_provided():
    echo_command = subprocess.Popen(['echo', 'githeri'], stdout=subprocess.PIPE)
    command = "python wc.py"
    expected_output = '1\t1\t8'

    process = subprocess.Popen(command.split(), stdin=echo_command.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    actual_output = output.decode().strip()
    assert actual_output == expected_output

@pytest.mark.parametrize(
    "file_path, expected_error",
    [
        ("notfound.txt", b"wc: No such file or directory: 'notfound.txt'"),
        ("./tests", b"wc: An unexpected error occurred:"),
    ],
)
def test_wc_error_handling(file_path, expected_error):
    command = f"python wc.py {file_path}"

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stderr = process.communicate()

    assert process.returncode != 0
    assert expected_error in stderr

