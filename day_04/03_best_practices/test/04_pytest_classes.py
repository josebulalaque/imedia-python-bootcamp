class TestClass:
    def test_one(self):
        word = "this"
        assert "h" in word

    def test_two(self):
        word = "hello"
        assert not hasattr(word, "check")
