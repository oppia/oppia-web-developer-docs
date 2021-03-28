As of April 2021, Oppia uses [Firebase](https://firebase.google.com/docs/auth) to handle user authentication. Log-in sessions are tracked using HTTP session cookies. The name of the session cookie is defined by `feconf.FIREBASE_SESSION_COOKIE_NAME = 'session'`.

For developers' convenience, the only thing needed to sign-in is an email address. A password will automatically be generated for the account. The password is the md5 hash of the email address. **This does not happen in production!** Production redirects users to the Google sign-in page instead (hence, _real_ Oppia users require a real Google account).

# Creating an Administrator account

## 1. Sign in with `testadmin@example.com`
![Signing in as testadmin@example.com](https://user-images.githubusercontent.com/5094060/112763949-8741b080-8fd4-11eb-9828-044d18b926b7.png)


## 2. Add custom claims to a Firebase account

1. Sign in with any email address.
![Signing in as a@a.com](https://user-images.githubusercontent.com/5094060/112763966-a04a6180-8fd4-11eb-9c21-58b6ba9f9b2f.png)

2. Go to the Firebase Emulator UI: http://localhost:4000/auth.
![Firebase emulator UI](https://user-images.githubusercontent.com/5094060/112764105-29619880-8fd5-11eb-915d-786ab229c563.png)

3. Find the corresponding Firebase account, click on the "3 dots" button, then click on **Edit user**.
![Finding the Edit user button](https://user-images.githubusercontent.com/5094060/112764057-f3bcaf80-8fd4-11eb-9561-8b4412cf9b23.png)

4. Set the Custom Claims value to `{"role":"super_admin"}` then click **Save**.
![Setting custom claims](https://user-images.githubusercontent.com/5094060/112764082-13ec6e80-8fd5-11eb-8508-a9bc24683e9f.png)

5. Logout and sign in again to refresh the session cookie.

6. **Done!** The account now has access to the Admin Page.
![Admin Page is now listed](https://user-images.githubusercontent.com/5094060/112764033-dc7dc200-8fd4-11eb-9256-3957584d4eee.png)