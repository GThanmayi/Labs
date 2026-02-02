*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Test Browser
Suite Teardown    Close Browser

*** Variables ***
${URL}        https://testautomationpractice.blogspot.com/
${BROWSER}    chrome

*** Test Cases ***
Form Interaction Test
    Wait Until Element Is Visible    id:name    10s
    Input Text    id:name     Harika
    Input Text    id:email    harika@example.com

    Wait Until Element Is Visible    id:female    15s
    Click Element    id:female

    Wait Until Element Is Visible    id:sunday    15s
    Click Element    id:sunday

    Wait Until Element Is Visible    id:country    15s
    Select From List By Label    id:country    India

    Run Keyword If    '${BROWSER}' == 'chrome'    Log    Running on Chrome browser

*** Keywords ***
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window