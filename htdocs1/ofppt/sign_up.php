<!DOCTYPE html>
<html lang="en">
  <html>
    <head>
      <title>Sign Up</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta charset="utf-8" />
      <link rel="stylesheet" type="text/css" href="sign_up.css" />
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
      />

    <body class="body">
      <div class="login-page">
        <div class="form">
          <form>
            <lottie-player
              src="https://assets4.lottiefiles.com/datafiles/XRVoUu3IX4sGWtiC3MPpFnJvZNq7lVWDCa8LSqgS/profile.json"
              background="transparent"
              speed="1"
              style="justify-content: center"
              loop
              autoplay
            ></lottie-player>
            <input type="text" placeholder="full name" />
            <input type="text" placeholder="email address" />
            <input type="text" placeholder=" username" />
            <input type="password" id="password" placeholder="set a password" />
            <i class="fas fa-eye" onclick="show()"></i>
            <br>
            <br>
          </form>

          <form class="login-form">
            <button type="button" onclick="window.location.href='login.html'">
              SIGN UP
            </button>
          </form>
        </div>
      </div>
    </body>

  </html>
</html>