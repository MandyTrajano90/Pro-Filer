import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_files(tmp_path):
    text_file_1 = tmp_path / "test_file_1.txt"
    text_file_1.write_text("Hello, World!")
    text_file_2 = tmp_path / "test_file_2.txt"
    text_file_2.write_text("Hello, World!")
    text_file_3 = tmp_path / "test_file_3.txt"
    text_file_3.write_text("I love Python!")

    context = {"all_files": [str(text_file_1), str(text_file_3)]}
    assert find_duplicate_files(context) == []

    context = {"all_files": [str(text_file_1), str(text_file_2)]}
    assert find_duplicate_files(context) == [(str(text_file_1), str(text_file_2))]

    context = {"all_files": [str(text_file_1), 'non_existent_file']}
    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
