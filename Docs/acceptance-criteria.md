GIVEN WHEN THEN SCENARIO 

1. User Registration
    
• Scenario 1: Seller Account Creation 
o Given a new user is on the registration page. 
o When they choose "Seller" and fill in their name, student email, password, 
shop name, and category of goods or services. 
o Then the system validates the student email against the simulated student 
database. 
o And if valid, sets up the seller profile and opens the seller dashboard.

• Scenario 2: Buyer Account Creation 
o Given a new user is on the registration page. 
o When they choose "Buyer" and enter their name, student email, and 
password. 
o Then the system validates the student email against the simulated student 
database. 
o And if valid, creates the account and opens the buyer dashboard. 

2. User Login 

• Scenario 3: Successful Login with Valid Credentials 
o Given a registered user is on the login page. 
o When they enter a valid student email and correct password. 
o Then the system logs them in and takes them to their dashboard. 

3. Product Search 

• Scenario 4: Item Found - Browsing and Comparing 
o Given a buyer enters an item in the search bar. 
o When matching listings exist. 
o Then the buyer is shown a scrollable list of results and can filter by price 
range. 
o And the buyer can compare prices, sellers, and ratings. 

• Scenario 5: Item Not Found - Showing Alternatives 
o Given a buyer enters an item they want to purchase in the search bar. 
o When no listing matches that exact search term. 
o Then the system displays a message that no exact match was found. 
o And shows alternative listings based on related or similar keywords, so the 
buyer can still compare available options. 

4. Shopping Cart
   
• Scenario 6: Adding an Item to the Cart 
o Given a buyer is viewing an available listing. 
o When they add it to their cart. 
o Then the listing is reserved and reflected in the buyer's cart. 

5. Confirming an Order

• Scenario 7: Buyer Confirms an Order 
o Given a buyer has a reserved item in their cart. 
o When they confirm the order. 
o Then an order is created with status "Awaiting Collection". 
o And the seller is notified. 

• Scenario 8: Order Confirmation Fails Because the Item Was Already Sold 
o Given a buyer has an item in their cart. 
o When the seller marks that item as sold before the buyer confirms. 
o Then the confirmation is rejected and no order is created. 
o And the item is automatically removed from the buyer's cart. 

6. Handoff & Meetup Coordination
   
• Scenario 9: Seller Proposes a Meetup Location 
o Given an order exists with status "Pending handoff". 
o When the seller opens the order and enters a location on campus and a 
time, then clicks "Send Handoff Details". 
o Then the buyer receives the location and time on their order page. 
o And the order status remains "Pending handoff".

• Scenario 10: Buyer Accepts Meetup Spot 
o Given a buyer sees a proposed meetup location and time from the seller. 
o When the buyer clicks "Confirm Meetup". 
o Then the system displays "Meetup confirmed!" 
o And the meeting details show up on both the buyer and seller dashboards.
