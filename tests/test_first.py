from wheel_proj.first import First


def test_return_string():
  obj = First()
  assert obj.get() == "asdc"
