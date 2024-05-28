import pytest
import example

def test_can_call_existing_endpoints_of_the_API():
  ret = example.get_coordinates("Lima,Perú")
  assert(ret is not None)
