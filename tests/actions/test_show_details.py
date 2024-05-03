from pro_filer.actions.main_actions import show_details  # NOQA
import os
from datetime import date


def test_show_details(tmp_path, capsys):
    file = tmp_path / "test_file.txt"
    with open(file, "w") as f:
        f.write("This is a test file")
    file_created = date.fromtimestamp(os.path.getctime(file))
    context = {'base_path': str(file)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = f"File name: {file.name}\nFile size in bytes: 19\nFile type: file\nFile extension: .txt\nLast modified date: {file_created}\n"
    assert captured.out == expected_output


def test_show_details_without_extension(tmp_path, capsys):
    file = tmp_path / "test_file"
    with open(file, "w") as f:
        f.write("This is a test file")
    file_created = date.fromtimestamp(os.path.getctime(file))
    context = {'base_path': str(file)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = f"File name: {file.name}\nFile size in bytes: 19\nFile type: file\nFile extension: [no extension]\nLast modified date: {file_created}\n"
    assert captured.out == expected_output


def test_show_details_without_file(capsys):
    context = {'base_path': "/home/trybe/???"}
    show_details(context)
    captured = capsys.readouterr().out
    assert captured == "File '???' does not exist\n"
