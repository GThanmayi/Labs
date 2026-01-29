*** Settings ***
Library    BuiltIn

*** Variables ***
${GREETING}      Hello, World!
@{FRUITS}        Apple    Banana    Orange

*** Test Cases ***
Log Messages With Variables
    Log           This is a log message from Robot Framework
    Log To Console    ${GREETING}
    Log           The list of fruits: ${FRUITS}

List Variable Logging
    Log To Console    List items individually:
    Log Many      @{FRUITS}
    Log To Console    Scalar variable again: ${GREETING}
