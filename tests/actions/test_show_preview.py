from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/utils/helpers.py",
            "src/tests/__init__.py"
        ],
        "all_dirs": [
            "src",
            "src/utils",
            "src/tests"
        ],
    }

    expected_output = (
        "Found 5 files and 3 directories\n"
        "First 5 files:"
        " ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py',"
        " 'src/utils/helpers.py', 'src/tests/__init__.py'"
        "]\n"
        "First 5 directories: ['src', 'src/utils', 'src/tests']\n"
    )

    show_preview(context)

    result = capsys.readouterr()
    assert result.out == expected_output


def test_show_preview_empty_content(capsys):

    empty_context = {
        "all_files": [],
        "all_dirs": [],
    }

    expected_output = "Found 0 files and 0 directories\n"
    show_preview(empty_context)

    result = capsys.readouterr()
    assert result.out == expected_output


def test_show_preview_more_than_5(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/utils/helpers.py",
            "src/tests/__init__.py",
            "src/routes/__init__.py"
        ],
        "all_dirs": [
            "src",
            "src/utils",
            "src/tests",
            "src/routes",
            "src/pages",
            "src/middlewares"
        ],
    }

    expected_output = (
        "Found 6 files and 6 directories\n"
        "First 5 files:"
        " ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py',"
        " 'src/utils/helpers.py', 'src/tests/__init__.py'"
        "]\n"
        "First 5 directories:"
        " ['src', 'src/utils', 'src/tests', 'src/routes', 'src/pages']\n"
    )

    show_preview(context)

    result = capsys.readouterr()
    assert result.out == expected_output
