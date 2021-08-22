from _pytest.pytester import Pytester


def test_sensitive(pytester: Pytester):
    pytester.makepyfile("""
    def test_sensitive():
        secret = "hide_this"
        print(f"This is secret: {secret}")
    """)
    result = pytester.runpytest("-s")
    assert "hide_this" not in str(result.stdout)
