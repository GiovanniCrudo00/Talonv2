import pytest
from app.TextUserInterface import TextUserInterface as TUI
import warnings


@pytest.fixture(autouse=True)
def disable_warnings():
    warnings.simplefilter("ignore")

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

def test_Text_User_Interface_do_not_modify_choice_if_wrong_input_and_rises_exception(myTUI):
    myTUI.elaborateChoice(1)
    with pytest.raises(ValueError):
        myTUI.elaborateChoice(199)
    assert 1 == myTUI.choice
