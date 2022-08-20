# Site Testing <!-- omit in toc -->

## Authentication
### Account Sign Up
- Attempting to sign up with an email address already in use by another user results in an error:  
![Email Already Used](./assets/testing/auth_signup_email_taken.png)
- Entering mismatched email addresses in the sign up form results in an error:  
![Email Fields Don't Match](./assets/testing/auth_signup_email_mismatch.png)  
- Entering a user name that includes invalid characters shows an error:  
![User Name Invalid](./assets/testing/auth_signup_username_invalid.png)  
- Entering a weak password (such as `password`) shows an error:  
![Weak Password](./assets/testing/auth_signup_weak_password.png)
- Entering mismatched passwords shows an error:  
![Password Fields Don't Match](./assets/testing/auth_signup_password_mismatch.png)
- Filling in the form with valid details successfully creates an account and sends a verification email:  
![Account Created Verification Sent](./assets/testing/auth_signup_verify_email.png)  
![Account Created In Django Admin](./assets/testing/auth_signup_user_created_admin.png)  
![Email Verification Received](./assets/testing/auth_signup_email_verification.png)  
- Attempting to log in without verifying email address fails:
  - The same email verification page is shown to the user as was originally shown when they created the account.
- Clicking the verify link in the email successfully verifies the account and allows the user to log in:  
![Confirm Email Address](./assets/testing/auth_signup_confirm_email.png)  
![Email Address Confirmed](./assets/testing/auth_signup_email_confirmed.png)  
### Account Sign In
- Attempting to sign in with an invalid email address shows an error:  
![Invalid Email Address](./assets/testing/auth_signin_invalid_email.png)  
- Attempting to sign in with a valid email address but invalid password shows an error:  
![Invalid Password](./assets/testing/auth_signin_invalid_password.png)  
- Signing in with valid credentials successfully logs the user into the site:  
![Sign In Success](./assets/testing/auth_signin_success.png)  
### Protected Site Pages
- When signed in as an authenticated user, protected areas of the site are accessible:  
  - My Profile:  
![Account Menu Changes](./assets/testing/auth_protected_account_menu.png)  
![Your Profile Page](./assets/testing/auth_protected_profile.png)  
  - Request Page:  
![Request Page](./assets/testing/auth_protected_request.png)  
- When signed out, protected areas of the site are no longer accessible:  
  - My Profile:  
![Account Menu Signed Out](./assets/testing/auth_protected_signedout_menu.png)  
  - Attempting to access `/profile/` redirects to the Sign In page:  
![Profile Redirect To Sign In](./assets/testing/auth_protected_profile_redirect.png)  
  - Request Page:
![Request Page Signed Out](./assets/testing/auth_protected_signedout_request.png)  
- When signed in as a regular user, the `/admin/` areas of the site are not accessible:  
![Admin Protected](./assets/testing/auth_protected_admin.png)  
- When signed in as a site administrator, the "add event" form is visible on the Markets page:  
![Admin Add Event](./assets/testing/auth_protected_admin_add_event.png)  
- When signed in as a user that is not a site administrator, the "add event" form is not visible on the Markets page:  
![Non Admin Can't Add Event](./assets/testing/auth_protected_nonadmin_events.png)  
### Account Sign Out
- The user can easily sign out of the site using the account menu:  
![Account Menu Sign Out](./assets/testing/auth_signout_account_menu.png)  
![Sign Out Page](./assets/testing/auth_signout_page.png)  
![Signed Out Success](./assets/testing/auth_signout_signed_out.png)  
### Profile
- Entering details into the profile page saves those details:  
  - New profile, no details are saved:  
![Profile With No Details](./assets/testing/auth_profile_no_details.png)  
  - Entering details and clicking the form button saves the details, which are then loaded into the form on subsequent viewing:    
![Profile Details Entered](./assets/testing/auth_profile_enter_details.png)  
![Profile Details Saved](./assets/testing/auth_profile_details_saved.png)  
- Going to a purchase checkout auto completes the checkout form with these details:  
![Checkout Autocompletes Details](./assets/testing/auth_profile_checkout.png)  
- Changing the details during the checkout process updates in the profile page when the save button is ticked:  
![Checkout Save New Details](./assets/testing/auth_profile_checkout_change_details.png)  
![Profile Details Saved From Checkout](./assets/testing/auth_profile_details_saved_from_checkout.png)  
## Purchase Journey
### Basket
- Products can be added to and removed from the basket: 
  - The basket total and grand total update accordingly when items are added and removed.  
![Item Added To Basket](./assets/testing/purchase_basket_add_item.png)  
![Basket With 2 Items](./assets/testing/purchase_basket.png)  
![Item Removed From Basket](./assets/testing/purchase_basket_remove_item.png)  
- Multiple identical items can be added to the basket and the quantity increases:  
![Identical Items In Basket](./assets/testing/purchase_basket_identical_items.png)  
- Multiple items of the same type but different sizes can be added to the basket but do not combine:  
![Identical Items Different Sizes](./assets/testing/purchase_basket_different_size_items.png)  
- Removing all items from the basket shows the user that the basket is empty:  
![All Items Removed From Basket](./assets/testing/purchase_basket_all_items_removed.png)  
### Checkout
- Not entering a required field on the details form shows an error:  
![Checkout Details Required Field Missing](./assets/testing/purchase_checkout_missing_required_field.png)  
- Entering an invalid card number shows an error:  
![Invalid Card Number](./assets/testing/purchase_checkout_invalid_card_number.png)  
- Not entering all fields on the card details shows an error:  
![Missing Card Number](./assets/testing/purchase_checkout_missing_card_number.png)  
![Missing Expiry Date](./assets/testing/purchase_checkout_missing_expiry.png)  
![Missing CVC Number](./assets/testing/purchase_checkout_missing_cvc.png)  
- Entering all fields on the form correctly successfully places an order:  
![Order Placed Successfully](./assets/testing/purchase_checkout_success.png)  
- An order confirmation email is sent to the user when an order is successfully placed:  
![Order Confirmation Email](./assets/testing/purchase_checkout_confirmation_email.png)  
- If the order is placed as a signed in user, the order is now visible in the user's profile page:  
![Order Visible In Order History](./assets/testing/purchase_checkout_order_history.png)  




Admin can add, update and remove products.

Add to basket
Add multiple to basket
Delete from basket


Go to checkout
No details filled on first purchase
Form validation
Complete checkout
Card validation
Email received
Save details viewable in profile
Edit details in profile
Admin can create events
Non admin but authenticated can't create events.
Admin can delete events
Events in the past not shown

Authenticated user can create requests
Authenticated user can see own requests and not others
User can delete and ammend own requests.
Newsletter signup saves in DB

Product filters work.
No products on filters shows helpful page.