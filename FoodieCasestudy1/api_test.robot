*** Settings ***
Documentation     Complete API Test Suite for Foodie App
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}       http://127.0.0.1:5000/api/v1

*** Test Cases ***

# --- RESTAURANT MODULE ---

Register Restaurant
    [Documentation]    Req #1: Register a new restaurant
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary    name=Global Delight    location=Hyderabad    category=Multi-cuisine    contact=9876543210
    ${resp}=    POST On Session    foodie    /restaurants    json=${body}    expected_status=201
    ${id}=      Set Variable    ${resp.json()["id"]}
    Set Suite Variable    ${REST_ID}    ${id}

Register Restaurant Conflict
    [Documentation]    Req #1: Verify 409 Conflict for duplicate name
    ${body}=    Create Dictionary    name=Global Delight    location=Hyderabad
    POST On Session    foodie    /restaurants    json=${body}    expected_status=409

Update Restaurant Details
    [Documentation]    Req #2: Update restaurant location
    ${body}=    Create Dictionary    location=Vijayawada
    ${resp}=    PUT On Session    foodie    /restaurants/${REST_ID}    json=${body}    expected_status=200
    Should Be Equal As Strings    ${resp.json()["location"]}    Vijayawada

Disable Restaurant
    [Documentation]    Req #3: Disable restaurant
    PUT On Session    foodie    /restaurants/${REST_ID}/disable    expected_status=200

Get Restaurant Profile
    [Documentation]    Req #4: View restaurant details
    GET On Session    foodie    /restaurants/${REST_ID}    expected_status=200

# --- DISH MODULE ---

Add Dish to Restaurant
    [Documentation]    Req #5: Add a new dish
    ${body}=    Create Dictionary    name=Biryani    type=Non-Veg    price=${250}
    ${resp}=    POST On Session    foodie    /restaurants/${REST_ID}/dishes    json=${body}    expected_status=201
    ${id}=      Set Variable    ${resp.json()["id"]}
    Set Suite Variable    ${DISH_ID}    ${id}

Update Dish Details
    [Documentation]    Req #6: Update dish price
    ${body}=    Create Dictionary    price=${280}
    ${resp}=    PUT On Session    foodie    /dishes/${DISH_ID}    json=${body}    expected_status=200
    Should Be Equal As Integers    ${resp.json()["price"]}    280

Toggle Dish Status
    [Documentation]    Req #7: Enable/Disable dish status
    ${body}=    Create Dictionary    enabled=${False}
    PUT On Session    foodie    /dishes/${DISH_ID}/status    json=${body}    expected_status=200

Delete Dish
    [Documentation]    Req #8: Delete a dish
    DELETE On Session    foodie    /dishes/${DISH_ID}    expected_status=200

# --- ADMIN MODULE ---

Admin Approve Restaurant
    [Documentation]    Req #9: Approve restaurant registration
    PUT On Session    foodie    /admin/restaurants/${REST_ID}/approve    expected_status=200

Admin Disable Restaurant
    [Documentation]    Req #10: Admin level disable
    PUT On Session    foodie    /admin/restaurants/${REST_ID}/disable    expected_status=200

Admin View Feedbacks
    [Documentation]    Req #11: View all user feedbacks
    GET On Session    foodie    /admin/feedback    expected_status=200

Admin View All Orders
    [Documentation]    Req #12: View all orders in system
    GET On Session    foodie    /admin/orders    expected_status=200

# --- USER & ORDER MODULE ---

Register User
    [Documentation]    Req #13: Customer registration
    ${body}=    Create Dictionary    name=Alice    email=alice_new@example.com    password=password123
    ${resp}=    POST On Session    foodie    /users/register    json=${body}    expected_status=201
    ${id}=      Set Variable    ${resp.json()["id"]}
    Set Suite Variable    ${USER_ID}    ${id}

Search Restaurants
    [Documentation]    Req #14: Search by name and location (Fixes the URL error)
    ${params}=    Create Dictionary    name=Global    location=Vijayawada
    GET On Session    foodie    url=/restaurants/search    params=${params}    expected_status=200

Place Order
    [Documentation]    Req #15: User places an order
    # Note: Using a valid dish ID is required. If dish 1 was deleted, use a new one.
    ${items}=    Evaluate    [{"dish_id": 1, "qty": 2}]
    ${body}=    Create Dictionary    user_id=${USER_ID}    restaurant_id=${REST_ID}    items=${items}
    ${resp}=    POST On Session    foodie    /orders    json=${body}    expected_status=201
    ${id}=      Set Variable    ${resp.json()["id"]}
    Set Suite Variable    ${ORDER_ID}    ${id}

Give Rating
    [Documentation]    Req #16: User rates an order
    ${body}=    Create Dictionary    order_id=${ORDER_ID}    rating=${5}    comment=Excellent
    POST On Session    foodie    /ratings    json=${body}    expected_status=201

View Orders by Restaurant
    [Documentation]    Req #17: Restaurant owner views their orders
    GET On Session    foodie    /restaurants/${REST_ID}/orders    expected_status=200

View Orders by User
    [Documentation]    Req #18: Customer views their history
    GET On Session    foodie    /users/${USER_ID}/orders    expected_status=200