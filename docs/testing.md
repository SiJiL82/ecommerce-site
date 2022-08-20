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
### Account Sign Out
- The user can easily sign out of the site using the account menu:  
![Account Menu Sign Out](./assets/testing/auth_signout_account_menu.png)  
![Sign Out Page](./assets/testing/auth_signout_page.png)  
![Signed Out Success](./assets/testing/auth_signout_signed_out.png)  




sign out
Can't view authenticated areas
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
Non authenticated user can't create requests
Authenticated user can create requests
Authenticated user can see own requests and not others
User can delete and ammend own requests.
Newsletter signup saves in DB
Admin can add, update and remove products.
Product filters work.
No products on filters shows helpful page.