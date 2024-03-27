from CaseManagement.CreateCaseType_CaseReason import Refresh, Material_Trigger_Event, New, Non_Material_Trigger_Event, \
    Offboarding, Re_open
from CaseManagement.CreateCase_MandatoryFields import Optional_fields_, Name_Is_Mandatory, Type_Is_Mandatory, \
    LegalEntityName_Is_Mandatory, Jurisdiction_Is_Mandatory, LegalEntityName_is_MandatoryJurisdiction_is_Mandatory, \
    Jurisdiction_is_Invalid, Jurisdiction_is_LowerCase, Name_With_Numerics_Char, Name_With_Special_Char, \
    Name_at_least_3_alphanumeric
from CaseManagement.Create_Update_Delete_Product import Get_Product
from CaseManagement.Create_A_Case import Create_a_Case



def test_Optional_fields_():
    Optional_fields_()
test_Optional_fields_()

def test_Get_Product():
    Get_Product()
test_Get_Product()

def test_Create_A_Case():
    Create_a_Case()
test_Create_A_Case()

def test_Optional_fields_():
    Optional_fields_()
test_Optional_fields_()

def test_Name_Is_Mandatory():
    Name_Is_Mandatory()
test_Name_Is_Mandatory()

def test_Type_Is_Mandatory():
    Type_Is_Mandatory()
test_Type_Is_Mandatory()

def test_LegalEntityName_Is_Mandatory():
    LegalEntityName_Is_Mandatory()
test_LegalEntityName_Is_Mandatory()

def test_Jurisdiction_Is_Mandatory():
    Jurisdiction_Is_Mandatory()
test_Jurisdiction_Is_Mandatory()

def test_LegalEntityName_is_MandatoryJurisdiction_is_Mandatory():
    LegalEntityName_is_MandatoryJurisdiction_is_Mandatory()
test_LegalEntityName_is_MandatoryJurisdiction_is_Mandatory()

def test_Jurisdiction_is_Invalid():
    Jurisdiction_is_Invalid()
test_Jurisdiction_is_Invalid()

def test_Jurisdiction_is_LowerCase():
    Jurisdiction_is_LowerCase()
test_Jurisdiction_is_LowerCase()

def test_Name_With_Numerics_Char():
    Name_With_Numerics_Char()
test_Name_With_Numerics_Char()

def test_Name_With_Special_Char():
    Name_With_Special_Char()
test_Name_With_Special_Char()

def test_Name_at_least_3_alphanumeric():
    Name_at_least_3_alphanumeric()
test_Name_at_least_3_alphanumeric()

def test_Refresh():
    Refresh()
test_Refresh()

def test_Material_Trigger_Event():
    Material_Trigger_Event()
test_Material_Trigger_Event()

def test_New():
    New()
test_New()

def test_Non_Material_Trigger_Event():
    Non_Material_Trigger_Event()
test_Non_Material_Trigger_Event()

def test_Offboarding():
    Offboarding()
test_Offboarding()

def test_Re_open():
    Re_open()
test_Re_open()


