from flask import Flask, request

app = Flask(__name__)

emails_file = "emails.txt"


HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Octo Waitlist</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    body {
      margin: 0;
      font-family: Arial;
      background: #05070D;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .container {
      text-align: center;
      max-width: 500px;
      padding: 20px;
    }

    h1 {
      font-size: 40px;
      background: linear-gradient(90deg, #22D3EE, #2563EB);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    p {
      color: #A3B3C2;
      font-size: 14px;
    }

    input {
      padding: 12px;
      width: 70%;
      border-radius: 10px;
      border: 1px solid #22D3EE;
      background: #0B1220;
      color: white;
    }

    button {
      padding: 12px 16px;
      border-radius: 10px;
      border: none;
      background: linear-gradient(90deg, #22D3EE, #2563EB);
      cursor: pointer;
      font-weight: bold;
    }

    .box {
      margin-top: 20px;
    }

    .success {
      color: #22D3EE;
      margin-top: 15px;
    }

  </style>
</head>

<body>

<div class="container">

  <h1>Build your own AI team</h1>

  <p>Create AI agents that plan, code, and ship projects for you.</p>

  <form method="POST" action="/join">
    <div class="box">
      <input type="email" name="email" placeholder="Enter your email" required>
      <button type="submit">Join Waitlist</button>
    </div>
  </form>

  {%message%}

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return HTML.replace("{%message%}", "")


@app.route("/join", methods=["POST"])
def join():
    email = request.form.get("email")

    if email:
        with open(emails_file, "a") as f:
            f.write(email + "\n")

        msg = "<p class='success'>You're on the waitlist 🚀</p>"
        return HTML.replace("{%message%}", msg)

    return HTML.replace("{%message%}", "<p style='color:red;'>Invalid email</p>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)