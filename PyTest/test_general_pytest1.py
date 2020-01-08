
def setup_module(module):
    print("\nInside Setup_Module!!")

def teardown_module(module):
    print("\nInside TearDown_Module!!")

def test_first():
    print("\nMy First PyTest!!")
    assert 1==1
