from os.path import exists


def test_resume_markdown_file_exists():
    assert exists(f'./../resume/RESUME.md')


def test_styles_exist():
    assert exists(f'./../assets/styles/simple-style.css')
    assert exists(f'./../assets/styles/bar-style.css')
    assert exists(f'./../assets/styles/structurdd-style.css')
