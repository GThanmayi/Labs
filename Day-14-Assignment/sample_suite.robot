*** Settings ***
Library     BuiltIn
Suite Setup     Suite Start
Suite Teardown      Suite End
Test Setup      Test Start
Test Teardown       Test End

*** Keywords ***
Suite Start
    Log To Console    === Suite Setup Executed ===

Suite End
    Log To Console    === Suite Teardown Executed ===

Test Start
    Log To Console    --- Test Setup Executed ---

Test End
    Log To Console    --- Test Teardown Executed ---

*** Test Cases ***
Addition Test
    [Tags]    smoke    math
    ${result}=    Evaluate    2 + 3
    Should Be Equal As Integers    ${result}    5

String Length Test
    [Tags]    regression
    ${length}=    Get Length    Hello
    Should Be Equal As Integers    ${length}    5
