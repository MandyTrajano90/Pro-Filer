from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage(tmp_path, capsys):
    text_file_1 = tmp_path / "test_file_1.txt"
    text_file_1.write_text("This is the first test file")
    text_file_2 = tmp_path / "test_file_2.txt"
    text_file_2.write_text("This is the second test file")

    context = {"all_files": [str(text_file_1), str(text_file_2)]}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out.replace(" ", "").endswith("Totalsize:55\n")
    assert captured.out.replace(" ", "").split("\n")[0].endswith("28(50%)") 
    assert captured.out.replace(" ", "").split("\n")[1].endswith("27(49%)")
