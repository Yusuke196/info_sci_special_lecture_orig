import textwrap
import io
from edit_distance import main


def test_case_1(monkeypatch, capfd):
    arg_1 = textwrap.dedent('''
        acac
        acm
    ''').strip()
    arg_2 = '2'

    helper(monkeypatch, capfd, arg_1, arg_2)


def test_case_2(monkeypatch, capfd):
    arg_1 = textwrap.dedent('''
        cute
        cat
    ''').strip()
    arg_2 = '2'

    helper(monkeypatch, capfd, arg_1, arg_2)


# コンソールからの入力をシミュレートする
def helper(monkeypatch, capfd, input_s, output_s):
    monkeypatch.setattr('sys.stdin', io.StringIO(input_s))
    main()
    out, _ = capfd.readouterr()
    assert out.strip() == output_s
