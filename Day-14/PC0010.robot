*** Variables ***
@{USERS}    admin    user
@{PWDS}     admin123    user123

*** Test Cases ***
FOR Loop Zip
    FOR    ${u}    ${p}    IN ZIP    @{USERS}    @{PWDS}
        Log    ${u} / ${p}
    END

