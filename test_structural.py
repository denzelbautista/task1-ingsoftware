import pytest
import example


def test_cannot_call_existing_endpoints_of_the_API():
  try:
    ret = example.get_coordinates("Lima,Perú")
    assert(ret is not None)
  except:
    assert False, "Exception while calling an existing function"

def test_cannot_call_existing_endpoints_of_the_API():
  try:
    ret = example.something_not_existent("bla bla")
    assert False, "Exception not raised"
  except:
    pass
