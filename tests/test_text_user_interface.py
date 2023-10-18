import pytest
from app.TextUserInterface import TextUserInterface as TUI


@pytest.fixture
def myTUI():
    tui = TUI()
    return tui 


def test_Text_User_Interface_Raises_Value_Error_On_None(myTUI):
    with pytest.raises(TypeError):
        myTUI.elaborateChoice(None)

def test_Text_User_Interface_Raises_Value_Error_On_Out_Of_Bound_Choice(myTUI):
    with pytest.raises(ValueError):
        myTUI.elaborateChoice(199)

def test_Text_User_Interface_Assign_Correct_Value_To_Choice(myTUI):
    myTUI.elaborateChoice(1)
    assert 1 == myTUI.choice