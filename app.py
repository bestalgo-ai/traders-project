# # # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # # import json, os

# # # # # app = Flask(__name__)
# # # # # app.secret_key = "infocap_secret_2025"  # required for session

# # # # # DATA_FILE = os.path.join(os.path.dirname(__file__), "users.json")

# # # # # if not os.path.exists(DATA_FILE):
# # # # #     with open(DATA_FILE, "w") as f:
# # # # #         json.dump([], f)

# # # # # def load_users():
# # # # #     with open(DATA_FILE, "r") as f:
# # # # #         return json.load(f)

# # # # # def save_users(users):
# # # # #     with open(DATA_FILE, "w") as f:
# # # # #         json.dump(users, f, indent=4)

# # # # # @app.route("/")
# # # # # def home():
# # # # #     return render_template("login.html")

# # # # # # ========== SIGNUP ==========
# # # # # @app.route("/signup", methods=["POST"])
# # # # # def signup():
# # # # #     data = request.get_json(force=True)
# # # # #     name = data.get("name")
# # # # #     email = data.get("email")
# # # # #     mobile = data.get("mobile")
# # # # #     password = data.get("password")

# # # # #     users = load_users()
# # # # #     if any(u["email"] == email for u in users):
# # # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # # #     users.append({
# # # # #         "name": name,
# # # # #         "email": email,
# # # # #         "mobile": mobile,
# # # # #         "password": password,
# # # # #         "details": {}  # Placeholder for API info
# # # # #     })
# # # # #     save_users(users)
# # # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # # ========== LOGIN ==========
# # # # # @app.route("/login", methods=["POST"])
# # # # # def login():
# # # # #     data = request.get_json(force=True)
# # # # #     email = data.get("email")
# # # # #     password = data.get("password")

# # # # #     users = load_users()
# # # # #     for u in users:
# # # # #         if u["email"] == email and u["password"] == password:
# # # # #             session["user"] = email
# # # # #             return jsonify({"status": "success", "message": "Login successful!"})
# # # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # # # ========== USER DETAILS PAGE ==========
# # # # # @app.route("/details")
# # # # # def details_page():
# # # # #     if "user" not in session:
# # # # #         return redirect(url_for("home"))
# # # # #     return render_template("user_details.html", user=session["user"])

# # # # # @app.route("/save_details", methods=["POST"])
# # # # # def save_details():
# # # # #     if "user" not in session:
# # # # #         return jsonify({"status": "error", "message": "Not logged in"})

# # # # #     data = request.get_json(force=True)
# # # # #     users = load_users()

# # # # #     for u in users:
# # # # #         if u["email"] == session["user"]:
# # # # #             u["details"] = {
# # # # #                 "user_id": data.get("user_id"),
# # # # #                 "password": data.get("password"),
# # # # #                 "api_key": data.get("api_key"),
# # # # #                 "secret_key": data.get("secret_key"),
# # # # #                 "totp": data.get("totp")
# # # # #             }
# # # # #             save_users(users)
# # # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})

# # # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # @app.route("/logout")
# # # # # def logout():
# # # # #     session.pop("user", None)
# # # # #     return redirect(url_for("home"))

# # # # # if __name__ == "__main__":
# # # # #     app.run(debug=True)

# # # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # # import json, os

# # # # # app = Flask(__name__)
# # # # # app.secret_key = "infocap_secret_2025"

# # # # # DATA_FILE = os.path.abspath("users.json")

# # # # # # -------------------- Basic JSON Load/Save --------------------
# # # # # if not os.path.exists(DATA_FILE):
# # # # #     with open(DATA_FILE, "w") as f:
# # # # #         json.dump([], f)

# # # # # def load_users():
# # # # #     with open(DATA_FILE, "r") as f:
# # # # #         return json.load(f)

# # # # # def save_users(users):
# # # # #     with open(DATA_FILE, "w") as f:
# # # # #         json.dump(users, f, indent=4)


# # # # # # -------------------- LOGIN PAGE --------------------
# # # # # @app.route("/")
# # # # # def home():
# # # # #     return render_template("login.html")


# # # # # # -------------------- SIGNUP --------------------
# # # # # @app.route("/signup", methods=["POST"])
# # # # # def signup():
# # # # #     data = request.get_json(force=True)
# # # # #     name = data.get("name")
# # # # #     email = data.get("email")
# # # # #     mobile = data.get("mobile")
# # # # #     password = data.get("password")

# # # # #     users = load_users()
# # # # #     if any(u["email"] == email for u in users):
# # # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # # #     users.append({
# # # # #         "name": name,
# # # # #         "email": email,
# # # # #         "mobile": mobile,
# # # # #         "password": password,
# # # # #         "details": {}
# # # # #     })
# # # # #     save_users(users)
# # # # #     return jsonify({"status": "success", "message": "Signup successful!"})


# # # # # # -------------------- LOGIN --------------------
# # # # # @app.route("/login", methods=["POST"])
# # # # # def login():
# # # # #     data = request.get_json(force=True)
# # # # #     email = data.get("email")
# # # # #     password = data.get("password")

# # # # #     users = load_users()
# # # # #     for u in users:
# # # # #         if u["email"] == email and u["password"] == password:
# # # # #             session["user"] = email
# # # # #             return jsonify({"status": "success", "message": "Login successful!"})
# # # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})


# # # # # # -------------------- USER DETAILS PAGE --------------------
# # # # # @app.route("/details")
# # # # # def details_page():
# # # # #     if "user" not in session:
# # # # #         return redirect(url_for("home"))
# # # # #     return render_template("user_details.html", user=session["user"])


# # # # # @app.route("/save_details", methods=["POST"])
# # # # # def save_details():
# # # # #     if "user" not in session:
# # # # #         return jsonify({"status": "error", "message": "Not logged in"})

# # # # #     data = request.get_json(force=True)
# # # # #     users = load_users()

# # # # #     for u in users:
# # # # #         if u["email"] == session["user"]:
# # # # #             u["details"] = {
# # # # #                 "user_id": data.get("user_id"),
# # # # #                 "password": data.get("password"),
# # # # #                 "api_key": data.get("api_key"),
# # # # #                 "secret_key": data.get("secret_key"),
# # # # #                 "totp": data.get("totp")
# # # # #             }
# # # # #             save_users(users)
# # # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})

# # # # #     return jsonify({"status": "error", "message": "User not found!"})


# # # # # # -------------------- ✅ ADD THIS SERVER CONNECT SECTION HERE --------------------
# # # # # @app.route("/server_connect")
# # # # # def server_connect_page():
# # # # #     if "user" not in session:
# # # # #         return redirect(url_for("home"))
# # # # #     return render_template("server_connect.html")


# # # # # @app.route("/start_server", methods=["POST"])
# # # # # def start_server():
# # # # #     from kiteconnect import KiteConnect
# # # # #     users = load_users()

# # # # #     # Find the logged-in user
# # # # #     current_user = None
# # # # #     for u in users:
# # # # #         if u["email"] == session["user"]:
# # # # #             current_user = u
# # # # #             break

# # # # #     if not current_user or "details" not in current_user:
# # # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # # #     details = current_user["details"]

# # # # #     try:
# # # # #         kite = KiteConnect(api_key=details["api_key"])
# # # # #         # Simulate token creation for now
# # # # #         access_token = "mock_access_token_" + details["user_id"]

# # # # #         current_user["details"]["access_token"] = access_token
# # # # #         save_users(users)

# # # # #         return jsonify({"status": "success", "message": "Server connected successfully!"})
# # # # #     except Exception as e:
# # # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})


# # # # # # -------------------- LOGOUT --------------------
# # # # # @app.route("/logout")
# # # # # def logout():
# # # # #     session.pop("user", None)
# # # # #     return redirect(url_for("home"))


# # # # # # -------------------- RUN APP --------------------
# # # # # if __name__ == "__main__":
# # # # #     app.run(debug=True)

# # # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # # import json, os, time

# # # # # app = Flask(__name__)
# # # # # app.secret_key = "infocap_secret_2025"

# # # # # DATA_FILE = os.path.abspath("users.json")

# # # # # # -------------------- Utility --------------------
# # # # # if not os.path.exists(DATA_FILE):
# # # # #     with open(DATA_FILE, "w") as f:
# # # # #         json.dump([], f)

# # # # # def load_users():
# # # # #     with open(DATA_FILE, "r") as f:
# # # # #         return json.load(f)

# # # # # def save_users(users):
# # # # #     with open(DATA_FILE, "w") as f:
# # # # #         json.dump(users, f, indent=4)

# # # # # # -------------------- LOGIN PAGE --------------------
# # # # # @app.route("/")
# # # # # def home():
# # # # #     return render_template("login.html")

# # # # # # -------------------- SIGNUP --------------------
# # # # # @app.route("/signup", methods=["POST"])
# # # # # def signup():
# # # # #     data = request.get_json(force=True)
# # # # #     name, email, mobile, password = (
# # # # #         data.get("name"),
# # # # #         data.get("email"),
# # # # #         data.get("mobile"),
# # # # #         data.get("password"),
# # # # #     )
# # # # #     users = load_users()
# # # # #     if any(u["email"] == email for u in users):
# # # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # # #     users.append({
# # # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # # #     })
# # # # #     save_users(users)
# # # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # # -------------------- LOGIN --------------------
# # # # # @app.route("/login", methods=["POST"])
# # # # # def login():
# # # # #     data = request.get_json(force=True)
# # # # #     email = data.get("email")
# # # # #     password = data.get("password")

# # # # #     users = load_users()
# # # # #     for u in users:
# # # # #         if u["email"] == email and u["password"] == password:
# # # # #             session["user"] = email

# # # # #             # ✅ If user has no broker details yet → first time login
# # # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # # #                 return jsonify({
# # # # #                     "status": "redirect",
# # # # #                     "message": "First-time login. Please fill your broker details.",
# # # # #                     "redirect_url": url_for("details_page")
# # # # #                 })

# # # # #             # ✅ Otherwise → go straight to server_connect
# # # # #             return jsonify({
# # # # #                 "status": "redirect",
# # # # #                 "message": "Login successful!",
# # # # #                 "redirect_url": url_for("server_connect_page")
# # # # #             })

# # # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})


# # # # # # -------------------- USER DETAILS PAGE --------------------
# # # # # @app.route("/details")
# # # # # def details_page():
# # # # #     if "user" not in session:
# # # # #         return redirect(url_for("home"))
# # # # #     return render_template("user_details.html", user=session["user"])

# # # # # @app.route("/save_details", methods=["POST"])
# # # # # def save_details():
# # # # #     if "user" not in session:
# # # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # # #     data = request.get_json(force=True)
# # # # #     users = load_users()
# # # # #     for u in users:
# # # # #         if u["email"] == session["user"]:
# # # # #             u["details"] = {
# # # # #                 "user_id": data.get("user_id"),
# # # # #                 "password": data.get("password"),
# # # # #                 "api_key": data.get("api_key"),
# # # # #                 "secret_key": data.get("secret_key"),
# # # # #                 "totp": data.get("totp"),
# # # # #             }
# # # # #             save_users(users)
# # # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # # @app.route("/server_connect")
# # # # # def server_connect_page():
# # # # #     if "user" not in session:
# # # # #         return redirect(url_for("home"))
# # # # #     return render_template("server_connect.html")

# # # # # # -------------------- START SERVER (REAL ACCESS TOKEN) --------------------
# # # # # @app.route("/start_server", methods=["POST"])
# # # # # def start_server():
# # # # #     from kiteconnect import KiteConnect
# # # # #     import pyotp, time
# # # # #     from selenium import webdriver
# # # # #     from selenium.webdriver.common.by import By
# # # # #     from selenium.webdriver.firefox.service import Service
# # # # #     from selenium.webdriver.firefox.options import Options
# # # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # # #     from selenium.webdriver.support import expected_conditions as EC

# # # # #     users = load_users()
# # # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # # #     if not current_user or "details" not in current_user:
# # # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # # #     d = current_user["details"]
# # # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # # #         d.get("user_id"),
# # # # #         d.get("password"),
# # # # #         d.get("api_key"),
# # # # #         d.get("secret_key"),
# # # # #         d.get("totp"),
# # # # #     )

# # # # #     try:
# # # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # # #         options = Options()
# # # # #         options.binary_location = firefox_path
# # # # #         # options.add_argument("--headless")  # optional: hide browser
# # # # #         service = Service(gecko_path)
# # # # #         driver = webdriver.Firefox(service=service, options=options)

# # # # #         kite = KiteConnect(api_key=api_key)
# # # # #         driver.get(kite.login_url())

# # # # #         # Step 1: Login credentials
# # # # #         WebDriverWait(driver, 25).until(
# # # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # # #         ).send_keys(user_id)
# # # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # # #         time.sleep(3)

# # # # #         # Step 2: Wait for the "External TOTP" section
# # # # #         WebDriverWait(driver, 30).until(
# # # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # # #         )

# # # # #         # Step 3: Generate the TOTP
# # # # #         totp = pyotp.TOTP(totp_secret).now()
# # # # #         print(f"Generated TOTP: {totp}")

# # # # #         # Step 4: Inject into any visible masked field (React input)
# # # # #         driver.execute_script("""
# # # # #             let boxes = document.querySelectorAll('input');
# # # # #             for (let i of boxes) {
# # # # #                 if (i.offsetParent !== null) {
# # # # #                     i.value = arguments[0];
# # # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # # #                 }
# # # # #             }
# # # # #         """, totp)

# # # # #         # Step 5: Click Continue button
# # # # #         time.sleep(1)
# # # # #         try:
# # # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # # #         except:
# # # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # # #         # Step 6: Wait for redirect to URL with request_token
# # # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # # #         current_url = driver.current_url
# # # # #         driver.quit()

# # # # #         if "request_token=" not in current_url:
# # # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # # #         # Step 7: Exchange request_token for access_token
# # # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # # #         access_token = data["access_token"]

# # # # #         # Step 8: Save the access_token
# # # # #         current_user["details"]["access_token"] = access_token
# # # # #         save_users(users)

# # # # #         return jsonify({
# # # # #             "status": "success",
# # # # #             "message": f"Server connected successfully ✅<br><b>Access Token:</b> {access_token}"
# # # # #         })

# # # # #     except Exception as e:
# # # # #         try:
# # # # #             driver.save_screenshot("server_error.png")
# # # # #         except:
# # # # #             pass
# # # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})


# # # # # # -------------------- LOGOUT --------------------
# # # # # @app.route("/logout")
# # # # # def logout():
# # # # #     session.pop("user", None)
# # # # #     return redirect(url_for("home"))

# # # # # # -------------------- RUN APP --------------------
# # # # # if __name__ == "__main__":
# # # # #     app.run(debug=True)


# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)

# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)

# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("login.html")

# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email

# # # #             # ✅ If user has no broker details yet → first time login
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })

# # # #             # ✅ Otherwise → go straight to server_connect
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })

# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("user_details.html", user=session["user"])

# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #             }
# # # #             save_users(users)
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("server_connect.html")

# # # # # -------------------- START SERVER (REAL ACCESS TOKEN) --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp, time
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         # options.add_argument("--headless")  # optional: hide browser
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())

# # # #         # Step 1: Login credentials
# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         # Step 2: Wait for the "External TOTP" section
# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         # Step 3: Generate the TOTP
# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         print(f"Generated TOTP: {totp}")

# # # #         # Step 4: Inject into any visible masked field (React input)
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         # Step 5: Click Continue button
# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         # Step 6: Wait for redirect to URL with request_token
# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         # Step 7: Exchange request_token for access_token
# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         # Step 8: Save the access_token
# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         # ✅ Redirect to dashboard after access token is generated
# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})

# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return redirect(url_for("home"))

# # # #     details = current_user.get("details", {})
# # # #     return render_template("dashboard.html", user=current_user["name"], details=details)

# # # # # -------------------- LOGOUT --------------------
# # # # @app.route("/logout")
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("home"))

# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)


# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)

# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)

# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("login.html")

# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email

# # # #             # ✅ If user has no broker details yet → first time login
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })

# # # #             # ✅ Otherwise → go straight to server_connect
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })

# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("user_details.html", user=session["user"])

# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #             }
# # # #             save_users(users)
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("server_connect.html")

# # # # # -------------------- START SERVER (REAL ACCESS TOKEN) --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp, time
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         # options.add_argument("--headless")  # optional: hide browser
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())

# # # #         # Step 1: Login credentials
# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         # Step 2: Wait for the "External TOTP" section
# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         # Step 3: Generate the TOTP
# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         print(f"Generated TOTP: {totp}")

# # # #         # Step 4: Inject into any visible masked field (React input)
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         # Step 5: Click Continue button
# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         # Step 6: Wait for redirect to URL with request_token
# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         # Step 7: Exchange request_token for access_token
# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         # Step 8: Save the access_token
# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         # ✅ Redirect to dashboard after access token is generated
# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})

# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return redirect(url_for("home"))

# # # #     details = current_user.get("details", {})
# # # #     return render_template("dashboard.html", user=current_user["name"], details=details)

# # # # # -------------------- REAL-TIME LTP FETCH --------------------
# # # # @app.route("/get_ltp")
# # # # def get_ltp():
# # # #     from kiteconnect import KiteConnect

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})

# # # #     details = current_user.get("details", {})
# # # #     api_key = details.get("api_key")
# # # #     access_token = details.get("access_token")

# # # #     if not api_key or not access_token:
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})

# # # #     try:
# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         # ✅ Try both index names to be safe
# # # #         try:
# # # #             ltp_data = kite.ltp("NSE:NIFTY 50")
# # # #         except:
# # # #             ltp_data = kite.ltp("NSE:NIFTY")

# # # #         ltp = list(ltp_data.values())[0]["last_price"]

# # # #         # ✅ Margin details
# # # #         margin_data = kite.margins()
# # # #         available_margin = margin_data["equity"]["available"]["cash"]

# # # #         return jsonify({"ltp": ltp, "margin": available_margin})

# # # #     except Exception as e:
# # # #         print(f"LTP Error: {e}")
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})

# # # # # -------------------- LOGOUT --------------------
# # # # @app.route("/logout")
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("home"))

# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)

# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)

# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("login.html")

# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email

# # # #             # ✅ If user has no broker details yet → first time login
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })

# # # #             # ✅ Otherwise → go straight to server_connect
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })

# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("user_details.html", user=session["user"])

# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #             }
# # # #             save_users(users)
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("server_connect.html")

# # # # # -------------------- START SERVER (REAL ACCESS TOKEN) --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp, time
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())

# # # #         # Step 1: Login credentials
# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         # Step 2: Wait for the "External TOTP" section
# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         # Step 3: Generate the TOTP
# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         print(f"Generated TOTP: {totp}")

# # # #         # Step 4: Inject TOTP
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         # Step 5: Continue
# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         # Step 6: Wait for request_token
# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         # Step 7: Exchange for access_token
# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         # Step 8: Save the access_token
# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})

# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return redirect(url_for("home"))

# # # #     details = current_user.get("details", {})

# # # #     # ✅ Read access_token and fetch real-time LTP
# # # #     ltp = "Error"
# # # #     margin = "Error"
# # # #     try:
# # # #         from kiteconnect import KiteConnect
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if api_key and access_token:
# # # #             kite = KiteConnect(api_key=api_key)
# # # #             kite.set_access_token(access_token)
# # # #             try:
# # # #                 ltp_data = kite.ltp("NSE:NIFTY 50")
# # # #             except:
# # # #                 ltp_data = kite.ltp("NSE:NIFTY")
# # # #             ltp = list(ltp_data.values())[0]["last_price"]

# # # #             margin_data = kite.margins()
# # # #             margin = margin_data["equity"]["available"]["cash"]
# # # #     except Exception as e:
# # # #         print(f"LTP fetch error in dashboard: {e}")

# # # #     # Pass LTP + Margin to HTML
# # # #     return render_template(
# # # #         "dashboard.html",
# # # #         user=current_user["name"],
# # # #         details=details,
# # # #         ltp=ltp,
# # # #         margin=margin
# # # #     )

# # # # # -------------------- LOGOUT --------------------
# # # # @app.route("/logout")
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("home"))

# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)


# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)

# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)

# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("login.html")

# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email

# # # #             # ✅ If user has no broker details yet → first time login
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })

# # # #             # ✅ Otherwise → go straight to server_connect
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })

# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("user_details.html", user=session["user"])

# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #             }
# # # #             save_users(users)
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("server_connect.html")

# # # # # -------------------- START SERVER (REAL ACCESS TOKEN) --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp, time
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())

# # # #         # Step 1: Login credentials
# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         # Step 2: Wait for the "External TOTP" section
# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         # Step 3: Generate the TOTP
# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         print(f"Generated TOTP: {totp}")

# # # #         # Step 4: Inject TOTP
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         # Step 5: Continue
# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         # Step 6: Wait for request_token
# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         # Step 7: Exchange for access_token
# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         # Step 8: Save the access_token
# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})

# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return redirect(url_for("home"))

# # # #     details = current_user.get("details", {})

# # # #     # ✅ Read access_token and fetch real-time LTP
# # # #     ltp = "Error"
# # # #     margin = "Error"
# # # #     try:
# # # #         from kiteconnect import KiteConnect
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if api_key and access_token:
# # # #             kite = KiteConnect(api_key=api_key)
# # # #             kite.set_access_token(access_token)

# # # #             # ✅ Correct symbol for NIFTY 50 index
# # # #             ltp_data = kite.ltp("NSE:NIFTY")
# # # #             ltp = list(ltp_data.values())[0]["last_price"]

# # # #             # ✅ Safe margin fetch
# # # #             margin_data = kite.margins()
# # # #             equity = margin_data.get("equity", {})
# # # #             available = equity.get("available", {})
# # # #             margin = available.get("cash", equity.get("net", "Error"))

# # # #     except Exception as e:
# # # #         print(f"LTP fetch error in dashboard: {e}")

# # # #     # Pass LTP + Margin to HTML
# # # #     return render_template(
# # # #         "dashboard.html",
# # # #         user=current_user["name"],
# # # #         details=details,
# # # #         ltp=ltp,
# # # #         margin=margin
# # # #     )

# # # # # -------------------- LOGOUT --------------------
# # # # @app.route("/logout")
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("home"))

# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)

# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)

# # # # # ✅ New Function: Fetch NIFTY LTP using stored access_token
# # # # def get_nifty_ltp_from_users(user_email):
# # # #     """Reads users.json → gets API key & access_token → returns NIFTY LTP"""
# # # #     from kiteconnect import KiteConnect

# # # #     try:
# # # #         with open(DATA_FILE, "r") as f:
# # # #             users = json.load(f)

# # # #         current_user = next((u for u in users if u["email"] == user_email), None)
# # # #         if not current_user:
# # # #             return {"ltp": "Error", "symbol": None, "error": "User not found"}

# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return {"ltp": "Error", "symbol": None, "error": "Missing API key or token"}

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         # Try multiple symbols
# # # #         symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #         for symbol in symbols_to_try:
# # # #             try:
# # # #                 data = kite.ltp(symbol)
# # # #                 ltp = list(data.values())[0]["last_price"]
# # # #                 return {"ltp": ltp, "symbol": symbol, "error": None}
# # # #             except Exception:
# # # #                 continue
# # # #         return {"ltp": "Error", "symbol": None, "error": "No symbol returned data"}
# # # #     except Exception as e:
# # # #         return {"ltp": "Error", "symbol": None, "error": str(e)}

# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("login.html")

# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })
# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("user_details.html", user=session["user"])

# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #             }
# # # #             save_users(users)
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("server_connect.html")

# # # # # -------------------- START SERVER --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())

# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})

# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return redirect(url_for("home"))

# # # #     details = current_user.get("details", {})
# # # #     api_key = details.get("api_key")
# # # #     access_token = details.get("access_token")

# # # #     ltp = "Error"
# # # #     margin = "Error"
# # # #     symbol_used = None

# # # #     if api_key and access_token:
# # # #         try:
# # # #             from kiteconnect import KiteConnect
# # # #             kite = KiteConnect(api_key=api_key)
# # # #             kite.set_access_token(access_token)

# # # #             # ✅ Use the same tested logic from your working script
# # # #             symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #             for sym in symbols_to_try:
# # # #                 try:
# # # #                     data = kite.ltp(sym)
# # # #                     ltp = list(data.values())[0]["last_price"]
# # # #                     symbol_used = sym
# # # #                     print(f"✅ Working Symbol: {sym} | LTP: {ltp}")
# # # #                     break
# # # #                 except Exception as e:
# # # #                     print(f"⚠️ Tried {sym} → {e}")
# # # #                     continue

# # # #             # ✅ Get margin (optional)
# # # #             try:
# # # #                 margin_data = kite.margins()
# # # #                 margin = margin_data.get("equity", {}).get("available", {}).get("cash", "Error")
# # # #             except Exception as e:
# # # #                 print(f"⚠️ Margin fetch failed: {e}")

# # # #         except Exception as e:
# # # #             print(f"❌ Kite connection failed: {e}")
# # # #     else:
# # # #         print("❌ Missing API key or Access token.")

# # # #     # ✅ Print debug info in terminal
# # # #     print(f"[DEBUG] Final symbol={symbol_used}, LTP={ltp}, Margin={margin}")

# # # #     return render_template(
# # # #         "dashboard.html",
# # # #         user=current_user["name"],
# # # #         details=details,
# # # #         ltp=ltp,
# # # #         margin=margin
# # # #     )
# # # # # -------------------- FETCH LTP (AJAX endpoint for live refresh) --------------------
# # # # # -------------------- FETCH LTP (with improved margin handling) --------------------
# # # # # -------------------- FETCH LTP (with improved margin handling) --------------------
# # # # @app.route("/fetch_ltp")
# # # # def fetch_ltp():
# # # #     if "user" not in session:
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})

# # # #     try:
# # # #         users = load_users()
# # # #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #         if not current_user:
# # # #             return jsonify({"ltp": "Error", "margin": "Error"})

# # # #         from kiteconnect import KiteConnect
# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return jsonify({"ltp": "Error", "margin": "Error"})

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         # ✅ Try all possible NIFTY variants
# # # #         symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #         ltp = "Error"
# # # #         for symbol in symbols_to_try:
# # # #             try:
# # # #                 data = kite.ltp(symbol)
# # # #                 ltp = list(data.values())[0]["last_price"]
# # # #                 print(f"✅ Symbol OK: {symbol} | LTP: {ltp}")
# # # #                 break
# # # #             except Exception as e:
# # # #                 print(f"⚠️ Tried {symbol} → {e}")

# # # #         # ✅ Handle margin safely (fetch all layers)
# # # #         margin = "Error"
# # # #         try:
# # # #             m = kite.margins()
# # # #             eq = m.get("equity", {})
# # # #             avail = eq.get("available", {})
# # # #             # Check possible fields
# # # #             margin = (
# # # #                 avail.get("cash")
# # # #                 or avail.get("live_balance")
# # # #                 or avail.get("opening_balance")
# # # #                 or eq.get("net")
# # # #                 or "0"
# # # #             )
# # # #             print(f"✅ Margin: {margin}")
# # # #         except Exception as e:
# # # #             print(f"⚠️ Margin fetch failed: {e}")

# # # #         return jsonify({"ltp": ltp, "margin": margin})

# # # #     except Exception as e:
# # # #         print(f"❌ fetch_ltp error: {e}")
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})
    
# # # # @app.route("/trade")
# # # # def trade_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("trade.html")

# # # # @app.route("/save_trade_settings", methods=["POST"])
# # # # def save_trade_settings():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})

# # # #     data = request.get_json(force=True)
# # # #     entry_time = data.get("entry_time")
# # # #     exit_time = data.get("exit_time")
# # # #     target = data.get("target")
# # # #     stoploss = data.get("stoploss")
# # # #     instrument = data.get("instrument")

# # # #     TRADE_FILE = os.path.abspath("trade_settings.json")

# # # #     # Load existing records if any
# # # #     if os.path.exists(TRADE_FILE):
# # # #         with open(TRADE_FILE, "r") as f:
# # # #             trades = json.load(f)
# # # #     else:
# # # #         trades = []

# # # #     # Append the current user's settings
# # # #     trades.append({
# # # #         "user": session["user"],
# # # #         "instrument": instrument,
# # # #         "entry_time": entry_time,
# # # #         "exit_time": exit_time,
# # # #         "target": target,
# # # #         "stoploss": stoploss,
# # # #         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
# # # #     })

# # # #     # Save file
# # # #     with open(TRADE_FILE, "w") as f:
# # # #         json.dump(trades, f, indent=4)

# # # #     return jsonify({"status": "success", "message": "✅ Trade settings saved successfully!"})



# # # # # -------------------- LOGOUT --------------------
# # # # @app.route("/logout")
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("home"))

# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)


# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)


# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)


# # # # # ✅ Utility to get LTP using saved credentials
# # # # def get_nifty_ltp_from_users(user_email):
# # # #     """Reads users.json → gets API key & access_token → returns NIFTY LTP"""
# # # #     from kiteconnect import KiteConnect
# # # #     try:
# # # #         with open(DATA_FILE, "r") as f:
# # # #             users = json.load(f)

# # # #         current_user = next((u for u in users if u["email"] == user_email), None)
# # # #         if not current_user:
# # # #             return {"ltp": "Error", "symbol": None, "error": "User not found"}

# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return {"ltp": "Error", "symbol": None, "error": "Missing API key or token"}

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #         for symbol in symbols_to_try:
# # # #             try:
# # # #                 data = kite.ltp(symbol)
# # # #                 ltp = list(data.values())[0]["last_price"]
# # # #                 return {"ltp": ltp, "symbol": symbol, "error": None}
# # # #             except Exception:
# # # #                 continue
# # # #         return {"ltp": "Error", "symbol": None, "error": "No symbol returned data"}
# # # #     except Exception as e:
# # # #         return {"ltp": "Error", "symbol": None, "error": str(e)}


# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("login.html")


# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})


# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })
# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})


# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("user_details.html", user=session["user"])


# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #             }
# # # #             save_users(users)
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})


# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("server_connect.html")


# # # # # -------------------- START SERVER --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())

# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})


# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return redirect(url_for("home"))

# # # #     details = current_user.get("details", {})
# # # #     api_key = details.get("api_key")
# # # #     access_token = details.get("access_token")

# # # #     ltp = "Error"
# # # #     margin = "Error"
# # # #     symbol_used = None

# # # #     if api_key and access_token:
# # # #         try:
# # # #             from kiteconnect import KiteConnect
# # # #             kite = KiteConnect(api_key=api_key)
# # # #             kite.set_access_token(access_token)

# # # #             symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #             for sym in symbols_to_try:
# # # #                 try:
# # # #                     data = kite.ltp(sym)
# # # #                     ltp = list(data.values())[0]["last_price"]
# # # #                     symbol_used = sym
# # # #                     print(f"[INFO] Working Symbol: {sym} | LTP: {ltp}")
# # # #                     break
# # # #                 except Exception as e:
# # # #                     print(f"[WARN] Tried {sym} → {e}")
# # # #                     continue

# # # #             try:
# # # #                 margin_data = kite.margins()
# # # #                 margin = margin_data.get("equity", {}).get("available", {}).get("cash", "Error")
# # # #             except Exception as e:
# # # #                 print(f"[WARN] Margin fetch failed: {e}")

# # # #         except Exception as e:
# # # #             print(f"[ERROR] Kite connection failed: {e}")
# # # #     else:
# # # #         print("[ERROR] Missing API key or Access token.")

# # # #     print(f"[DEBUG] Final symbol={symbol_used}, LTP={ltp}, Margin={margin}")

# # # #     return render_template(
# # # #         "dashboard.html",
# # # #         user=current_user["name"],
# # # #         details=details,
# # # #         ltp=ltp,
# # # #         margin=margin
# # # #     )


# # # # # -------------------- FETCH LTP (AJAX endpoint for live refresh) --------------------
# # # # @app.route("/fetch_ltp")
# # # # def fetch_ltp():
# # # #     if "user" not in session:
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})

# # # #     try:
# # # #         users = load_users()
# # # #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #         if not current_user:
# # # #             return jsonify({"ltp": "Error", "margin": "Error"})

# # # #         from kiteconnect import KiteConnect
# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return jsonify({"ltp": "Error", "margin": "Error"})

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #         ltp = "Error"
# # # #         for symbol in symbols_to_try:
# # # #             try:
# # # #                 data = kite.ltp(symbol)
# # # #                 ltp = list(data.values())[0]["last_price"]
# # # #                 print(f"[INFO] Symbol OK: {symbol} | LTP: {ltp}")
# # # #                 break
# # # #             except Exception as e:
# # # #                 print(f"[WARN] Tried {symbol} → {e}")

# # # #         margin = "Error"
# # # #         try:
# # # #             m = kite.margins()
# # # #             eq = m.get("equity", {})
# # # #             avail = eq.get("available", {})
# # # #             margin = (
# # # #                 avail.get("cash")
# # # #                 or avail.get("live_balance")
# # # #                 or avail.get("opening_balance")
# # # #                 or eq.get("net")
# # # #                 or "0"
# # # #             )
# # # #             print(f"[INFO] Margin: {margin}")
# # # #         except Exception as e:
# # # #             print(f"[WARN] Margin fetch failed: {e}")

# # # #         return jsonify({"ltp": ltp, "margin": margin})

# # # #     except Exception as e:
# # # #         print(f"[ERROR] fetch_ltp error: {e}")
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})
    
# # # # # -------------------- LIVE LTP FOR TRADE SETTINGS --------------------
# # # # @app.route("/get_trade_ltp")
# # # # def get_trade_ltp():
# # # #     """Fetch LTP of the instrument saved in trade_settings.json for current user"""
# # # #     import sys
# # # #     sys.stdout.reconfigure(encoding='utf-8')

# # # #     if "user" not in session:
# # # #         return jsonify({"ltp": "Error", "instrument": None})

# # # #     TRADE_FILE = os.path.abspath("trade_settings.json")
# # # #     if not os.path.exists(TRADE_FILE):
# # # #         return jsonify({"ltp": "Error", "instrument": None})

# # # #     try:
# # # #         # Load user's last trade setting
# # # #         with open(TRADE_FILE, "r") as f:
# # # #             trades = json.load(f)

# # # #         user_trade = next((t for t in trades if t["user"] == session["user"]), None)
# # # #         if not user_trade:
# # # #             return jsonify({"ltp": "Error", "instrument": None})

# # # #         instrument = user_trade.get("instrument", "NIFTY").upper()

# # # #         # Load API credentials
# # # #         users = load_users()
# # # #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #         if not current_user:
# # # #             return jsonify({"ltp": "Error", "instrument": instrument})

# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return jsonify({"ltp": "Error", "instrument": instrument})

# # # #         from kiteconnect import KiteConnect
# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         # Map to valid symbols
# # # #         instrument_map = {
# # # #             "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
# # # #             "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
# # # #             "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
# # # #         }

# # # #         ltp = "Error"
# # # #         tried = []
# # # #         for sym in instrument_map.get(instrument, ["NSE:NIFTY 50"]):
# # # #             try:
# # # #                 data = kite.ltp(sym)
# # # #                 ltp = list(data.values())[0]["last_price"]
# # # #                 print(f"[TRADE] {instrument} OK → {sym} = {ltp}")
# # # #                 break
# # # #             except Exception as e:
# # # #                 tried.append(sym)
# # # #                 print(f"[WARN] Tried {sym} → {e}")
# # # #                 continue

# # # #         if ltp == "Error":
# # # #             print(f"[ERROR] No working symbol found for {instrument}, tried {tried}")
# # # #             return jsonify({"ltp": "Error", "instrument": instrument})

# # # #         return jsonify({"ltp": ltp, "instrument": instrument})

# # # #     except Exception as e:
# # # #         print(f"[ERROR] Trade LTP fetch failed: {e}")
# # # #         return jsonify({"ltp": "Error", "instrument": None})



# # # # # -------------------- TRADE SETTINGS --------------------
# # # # @app.route("/trade")
# # # # def trade_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("trade.html")


# # # # @app.route("/save_trade_settings", methods=["POST"])
# # # # def save_trade_settings():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})

# # # #     data = request.get_json(force=True)
# # # #     entry_time = data.get("entry_time")
# # # #     exit_time = data.get("exit_time")
# # # #     target = data.get("target")
# # # #     stoploss = data.get("stoploss")
# # # #     instrument = data.get("instrument")

# # # #     TRADE_FILE = os.path.abspath("trade_settings.json")

# # # #     if os.path.exists(TRADE_FILE):
# # # #         with open(TRADE_FILE, "r") as f:
# # # #             trades = json.load(f)
# # # #     else:
# # # #         trades = []

# # # #     trades.append({
# # # #         "user": session["user"],
# # # #         "instrument": instrument,
# # # #         "entry_time": entry_time,
# # # #         "exit_time": exit_time,
# # # #         "target": target,
# # # #         "stoploss": stoploss,
# # # #         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
# # # #     })

# # # #     with open(TRADE_FILE, "w") as f:
# # # #         json.dump(trades, f, indent=4)

# # # #     return jsonify({"status": "success", "message": "Trade settings saved successfully!"})


# # # # # -------------------- LOGOUT --------------------
# # # # @app.route("/logout")
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("home"))


# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)



# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time, logging

# # # # # -------------------- Logging Setup --------------------
# # # # logging.basicConfig(
# # # #     level=logging.DEBUG,
# # # #     format="%(asctime)s [%(levelname)s] %(message)s",
# # # #     handlers=[logging.StreamHandler()]
# # # # )

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)

# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)

# # # # # ✅ Global log before every request
# # # # @app.before_request
# # # # def log_request():
# # # #     app.logger.info(f"➡️ {request.method} {request.path}")

# # # # # ✅ Utility to get LTP using saved credentials
# # # # def get_nifty_ltp_from_users(user_email):
# # # #     """Reads users.json → gets API key & access_token → returns NIFTY LTP"""
# # # #     from kiteconnect import KiteConnect
# # # #     try:
# # # #         with open(DATA_FILE, "r") as f:
# # # #             users = json.load(f)

# # # #         current_user = next((u for u in users if u["email"] == user_email), None)
# # # #         if not current_user:
# # # #             return {"ltp": "Error", "symbol": None, "error": "User not found"}

# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return {"ltp": "Error", "symbol": None, "error": "Missing API key or token"}

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #         for symbol in symbols_to_try:
# # # #             try:
# # # #                 data = kite.ltp(symbol)
# # # #                 ltp = list(data.values())[0]["last_price"]
# # # #                 return {"ltp": ltp, "symbol": symbol, "error": None}
# # # #             except Exception:
# # # #                 continue
# # # #         return {"ltp": "Error", "symbol": None, "error": "No symbol returned data"}
# # # #     except Exception as e:
# # # #         app.logger.error(f"[get_nifty_ltp_from_users] Error: {e}")
# # # #         return {"ltp": "Error", "symbol": None, "error": str(e)}

# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     app.logger.info("Rendering login page")
# # # #     return render_template("login.html")

# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         app.logger.warning(f"Signup failed: {email} already exists")
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     app.logger.info(f"New signup: {email}")
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email
# # # #             app.logger.info(f"✅ Login successful: {email}")
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })
# # # #     app.logger.warning(f"❌ Invalid login attempt: {email}")
# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     app.logger.info(f"Opening details page for {session['user']}")
# # # #     return render_template("user_details.html", user=session["user"])

# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #             }
# # # #             save_users(users)
# # # #             app.logger.info(f"Broker details saved for {session['user']}")
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     app.logger.info(f"Opening server connect page for {session['user']}")
# # # #     return render_template("server_connect.html")

# # # # # -------------------- START SERVER --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())
# # # #         app.logger.info(f"Launching login URL for {user_id}")

# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         app.logger.info(f"Access token generated successfully for {session['user']}")
# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         app.logger.error(f"[start_server] Error: {e}")
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})

# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user:
# # # #         return redirect(url_for("home"))

# # # #     details = current_user.get("details", {})
# # # #     api_key = details.get("api_key")
# # # #     access_token = details.get("access_token")

# # # #     ltp = "Error"
# # # #     margin = "Error"
# # # #     symbol_used = None

# # # #     if api_key and access_token:
# # # #         try:
# # # #             from kiteconnect import KiteConnect
# # # #             kite = KiteConnect(api_key=api_key)
# # # #             kite.set_access_token(access_token)

# # # #             symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #             for sym in symbols_to_try:
# # # #                 try:
# # # #                     data = kite.ltp(sym)
# # # #                     ltp = list(data.values())[0]["last_price"]
# # # #                     symbol_used = sym
# # # #                     app.logger.info(f"[INFO] Working Symbol: {sym} | LTP: {ltp}")
# # # #                     break
# # # #                 except Exception as e:
# # # #                     app.logger.warning(f"[WARN] Tried {sym} → {e}")
# # # #                     continue

# # # #             try:
# # # #                 margin_data = kite.margins()
# # # #                 margin = margin_data.get("equity", {}).get("available", {}).get("cash", "Error")
# # # #             except Exception as e:
# # # #                 app.logger.warning(f"[WARN] Margin fetch failed: {e}")

# # # #         except Exception as e:
# # # #             app.logger.error(f"[ERROR] Kite connection failed: {e}")
# # # #     else:
# # # #         app.logger.error("[ERROR] Missing API key or Access token.")

# # # #     app.logger.debug(f"[DEBUG] Final symbol={symbol_used}, LTP={ltp}, Margin={margin}")

# # # #     return render_template(
# # # #         "dashboard.html",
# # # #         user=current_user["name"],
# # # #         details=details,
# # # #         ltp=ltp,
# # # #         margin=margin
# # # #     )

# # # # # -------------------- FETCH LTP --------------------
# # # # @app.route("/fetch_ltp")
# # # # def fetch_ltp():
# # # #     if "user" not in session:
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})

# # # #     try:
# # # #         users = load_users()
# # # #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #         if not current_user:
# # # #             return jsonify({"ltp": "Error", "margin": "Error"})

# # # #         from kiteconnect import KiteConnect
# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return jsonify({"ltp": "Error", "margin": "Error"})

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         kite.set_access_token(access_token)

# # # #         symbols_to_try = ["NSE:NIFTY 50", "NSE:NIFTY", "NSE:NIFTYBANK"]
# # # #         ltp = "Error"
# # # #         for symbol in symbols_to_try:
# # # #             try:
# # # #                 data = kite.ltp(symbol)
# # # #                 ltp = list(data.values())[0]["last_price"]
# # # #                 app.logger.info(f"[INFO] Symbol OK: {symbol} | LTP: {ltp}")
# # # #                 break
# # # #             except Exception as e:
# # # #                 app.logger.warning(f"[WARN] Tried {symbol} → {e}")

# # # #         margin = "Error"
# # # #         try:
# # # #             m = kite.margins()
# # # #             eq = m.get("equity", {})
# # # #             avail = eq.get("available", {})
# # # #             margin = (
# # # #                 avail.get("cash")
# # # #                 or avail.get("live_balance")
# # # #                 or avail.get("opening_balance")
# # # #                 or eq.get("net")
# # # #                 or "0"
# # # #             )
# # # #             app.logger.info(f"[INFO] Margin: {margin}")
# # # #         except Exception as e:
# # # #             app.logger.warning(f"[WARN] Margin fetch failed: {e}")

# # # #         return jsonify({"ltp": ltp, "margin": margin})

# # # #     except Exception as e:
# # # #         app.logger.error(f"[ERROR] fetch_ltp error: {e}")
# # # #         return jsonify({"ltp": "Error", "margin": "Error"})

# # # # # -------------------- TRADE SETTINGS, LOGOUT, ETC. --------------------
# # # # # (Remaining routes unchanged from your code)

# # # # @app.route("/logout")
# # # # def logout():
# # # #     user = session.pop("user", None)
# # # #     app.logger.info(f"User logged out: {user}")
# # # #     return redirect(url_for("home"))

# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# # # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # # import json, os, time, logging
# # # # from kiteconnect import KiteConnect

# # # # # -------------------- Logging Setup --------------------
# # # # logging.basicConfig(
# # # #     level=logging.DEBUG,
# # # #     format="%(asctime)s [%(levelname)s] %(message)s",
# # # #     handlers=[logging.StreamHandler()]
# # # # )

# # # # app = Flask(__name__)
# # # # app.secret_key = "infocap_secret_2025"

# # # # DATA_FILE = os.path.abspath("users.json")
# # # # TRADE_FILE = os.path.abspath("trade_settings.json")

# # # # # -------------------- Utility --------------------
# # # # if not os.path.exists(DATA_FILE):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # if not os.path.exists(TRADE_FILE):
# # # #     with open(TRADE_FILE, "w") as f:
# # # #         json.dump([], f)

# # # # def load_users():
# # # #     with open(DATA_FILE, "r") as f:
# # # #         return json.load(f)

# # # # def save_users(users):
# # # #     with open(DATA_FILE, "w") as f:
# # # #         json.dump(users, f, indent=4)

# # # # # ✅ Global log before every request
# # # # @app.before_request
# # # # def log_request():
# # # #     app.logger.info(f"➡️ {request.method} {request.path}")

# # # # # ✅ Utility: Get LTP for any instrument
# # # # def get_ltp_for_instrument(instrument, api_key, access_token):
# # # #     kite = KiteConnect(api_key=api_key)
# # # #     kite.set_access_token(access_token)

# # # #     instrument_map = {
# # # #         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
# # # #         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
# # # #         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
# # # #     }

# # # #     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
# # # #         try:
# # # #             data = kite.ltp(sym)
# # # #             return list(data.values())[0]["last_price"], sym
# # # #         except Exception as e:
# # # #             app.logger.warning(f"[LTP] Failed {sym} → {e}")
# # # #     return "Error", None


# # # # # -------------------- LOGIN PAGE --------------------
# # # # @app.route("/")
# # # # def home():
# # # #     app.logger.info("Rendering login page")
# # # #     return render_template("login.html")


# # # # # -------------------- SIGNUP --------------------
# # # # @app.route("/signup", methods=["POST"])
# # # # def signup():
# # # #     data = request.get_json(force=True)
# # # #     name, email, mobile, password = (
# # # #         data.get("name"),
# # # #         data.get("email"),
# # # #         data.get("mobile"),
# # # #         data.get("password"),
# # # #     )
# # # #     users = load_users()
# # # #     if any(u["email"] == email for u in users):
# # # #         app.logger.warning(f"Signup failed: {email} already exists")
# # # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # # #     users.append({
# # # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # # #     })
# # # #     save_users(users)
# # # #     app.logger.info(f"New signup: {email}")
# # # #     return jsonify({"status": "success", "message": "Signup successful!"})


# # # # # -------------------- LOGIN --------------------
# # # # @app.route("/login", methods=["POST"])
# # # # def login():
# # # #     data = request.get_json(force=True)
# # # #     email = data.get("email")
# # # #     password = data.get("password")

# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == email and u["password"] == password:
# # # #             session["user"] = email
# # # #             app.logger.info(f"✅ Login successful: {email}")
# # # #             if not u.get("details") or not u["details"].get("user_id"):
# # # #                 return jsonify({
# # # #                     "status": "redirect",
# # # #                     "message": "First-time login. Please fill your broker details.",
# # # #                     "redirect_url": url_for("details_page")
# # # #                 })
# # # #             return jsonify({
# # # #                 "status": "redirect",
# # # #                 "message": "Login successful!",
# # # #                 "redirect_url": url_for("server_connect_page")
# # # #             })
# # # #     app.logger.warning(f"❌ Invalid login attempt: {email}")
# # # #     return jsonify({"status": "error", "message": "Invalid email or password!"})


# # # # # -------------------- USER DETAILS PAGE --------------------
# # # # @app.route("/details")
# # # # def details_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     app.logger.info(f"Opening details page for {session['user']}")
# # # #     return render_template("user_details.html", user=session["user"])


# # # # @app.route("/save_details", methods=["POST"])
# # # # def save_details():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})
# # # #     data = request.get_json(force=True)
# # # #     users = load_users()
# # # #     for u in users:
# # # #         if u["email"] == session["user"]:
# # # #             u["details"] = {
# # # #                 "user_id": data.get("user_id"),
# # # #                 "password": data.get("password"),
# # # #                 "api_key": data.get("api_key"),
# # # #                 "secret_key": data.get("secret_key"),
# # # #                 "totp": data.get("totp"),
# # # #                 "access_token": data.get("access_token", "")
# # # #             }
# # # #             save_users(users)
# # # #             app.logger.info(f"Broker details saved for {session['user']}")
# # # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # # #     return jsonify({"status": "error", "message": "User not found!"})


# # # # # -------------------- SERVER CONNECT PAGE --------------------
# # # # @app.route("/server_connect")
# # # # def server_connect_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     app.logger.info(f"Opening server connect page for {session['user']}")
# # # #     return render_template("server_connect.html")


# # # # # -------------------- START SERVER --------------------
# # # # @app.route("/start_server", methods=["POST"])
# # # # def start_server():
# # # #     from kiteconnect import KiteConnect
# # # #     import pyotp
# # # #     from selenium import webdriver
# # # #     from selenium.webdriver.common.by import By
# # # #     from selenium.webdriver.firefox.service import Service
# # # #     from selenium.webdriver.firefox.options import Options
# # # #     from selenium.webdriver.support.ui import WebDriverWait
# # # #     from selenium.webdriver.support import expected_conditions as EC

# # # #     users = load_users()
# # # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #     if not current_user or "details" not in current_user:
# # # #         return jsonify({"status": "error", "message": "User details not found"})

# # # #     d = current_user["details"]
# # # #     user_id, password, api_key, api_secret, totp_secret = (
# # # #         d.get("user_id"),
# # # #         d.get("password"),
# # # #         d.get("api_key"),
# # # #         d.get("secret_key"),
# # # #         d.get("totp"),
# # # #     )

# # # #     try:
# # # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # # #         options = Options()
# # # #         options.binary_location = firefox_path
# # # #         service = Service(gecko_path)
# # # #         driver = webdriver.Firefox(service=service, options=options)

# # # #         kite = KiteConnect(api_key=api_key)
# # # #         driver.get(kite.login_url())
# # # #         app.logger.info(f"Launching login URL for {user_id}")

# # # #         WebDriverWait(driver, 25).until(
# # # #             EC.visibility_of_element_located((By.ID, "userid"))
# # # #         ).send_keys(user_id)
# # # #         driver.find_element(By.ID, "password").send_keys(password)
# # # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # # #         time.sleep(3)

# # # #         WebDriverWait(driver, 30).until(
# # # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # # #         )

# # # #         totp = pyotp.TOTP(totp_secret).now()
# # # #         driver.execute_script("""
# # # #             let boxes = document.querySelectorAll('input');
# # # #             for (let i of boxes) {
# # # #                 if (i.offsetParent !== null) {
# # # #                     i.value = arguments[0];
# # # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # # #                 }
# # # #             }
# # # #         """, totp)

# # # #         time.sleep(1)
# # # #         try:
# # # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # # #         except:
# # # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # # #         current_url = driver.current_url
# # # #         driver.quit()

# # # #         if "request_token=" not in current_url:
# # # #             return jsonify({"status": "error", "message": "Request token not found — login may have failed."})

# # # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # # #         access_token = data["access_token"]

# # # #         current_user["details"]["access_token"] = access_token
# # # #         save_users(users)

# # # #         app.logger.info(f"Access token generated successfully for {session['user']}")
# # # #         return jsonify({
# # # #             "status": "redirect",
# # # #             "message": "Server connected successfully! Redirecting to your dashboard...",
# # # #             "redirect_url": url_for("dashboard_page")
# # # #         })

# # # #     except Exception as e:
# # # #         app.logger.error(f"[start_server] Error: {e}")
# # # #         try:
# # # #             driver.save_screenshot("server_error.png")
# # # #         except:
# # # #             pass
# # # #         return jsonify({"status": "error", "message": f"Connection failed: {str(e)}"})


# # # # # -------------------- DASHBOARD PAGE --------------------
# # # # @app.route("/dashboard")
# # # # def dashboard_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))
# # # #     return render_template("dashboard.html")


# # # # # -------------------- TRADE PAGE --------------------
# # # # @app.route("/trade")
# # # # def trade_page():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("home"))

# # # #     try:
# # # #         with open(TRADE_FILE, "r") as f:
# # # #             trades = json.load(f)
# # # #     except:
# # # #         trades = []

# # # #     trade = next((t for t in trades if t["user"] == session["user"]), None)
# # # #     instrument = trade["instrument"] if trade else ""
# # # #     entry_time = trade["entry_time"] if trade else "9:15 AM"
# # # #     exit_time = trade["exit_time"] if trade else "3:30 PM"
# # # #     target = trade["target"] if trade else ""
# # # #     stoploss = trade["stoploss"] if trade else ""

# # # #     return render_template("trade.html",
# # # #                            instrument=instrument,
# # # #                            entry_time=entry_time,
# # # #                            exit_time=exit_time,
# # # #                            target=target,
# # # #                            stoploss=stoploss)


# # # # # -------------------- SAVE TRADE SETTINGS --------------------
# # # # @app.route("/save_trade_settings", methods=["POST"])
# # # # def save_trade_settings():
# # # #     if "user" not in session:
# # # #         return jsonify({"status": "error", "message": "Not logged in"})

# # # #     data = request.get_json(force=True)
# # # #     instrument = data.get("instrument")
# # # #     entry_time = data.get("entry_time")
# # # #     exit_time = data.get("exit_time")
# # # #     target = data.get("target")
# # # #     stoploss = data.get("stoploss")

# # # #     if os.path.exists(TRADE_FILE):
# # # #         with open(TRADE_FILE, "r") as f:
# # # #             trades = json.load(f)
# # # #     else:
# # # #         trades = []

# # # #     trades = [t for t in trades if t["user"] != session["user"]]
# # # #     trades.append({
# # # #         "user": session["user"],
# # # #         "instrument": instrument,
# # # #         "entry_time": entry_time,
# # # #         "exit_time": exit_time,
# # # #         "target": target,
# # # #         "stoploss": stoploss,
# # # #         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
# # # #     })

# # # #     with open(TRADE_FILE, "w") as f:
# # # #         json.dump(trades, f, indent=4)

# # # #     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument})")
# # # #     return jsonify({"status": "success", "message": "Trade settings saved successfully!"})


# # # # # -------------------- GET TRADE LTP --------------------
# # # # @app.route("/get_trade_ltp")
# # # # def get_trade_ltp():
# # # #     if "user" not in session:
# # # #         return jsonify({"instrument": None, "ltp": "Error"})

# # # #     try:
# # # #         with open(TRADE_FILE, "r") as f:
# # # #             trades = json.load(f)
# # # #         trade = next((t for t in trades if t["user"] == session["user"]), None)
# # # #         instrument = trade["instrument"] if trade else "NIFTY"

# # # #         users = load_users()
# # # #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# # # #         if not current_user:
# # # #             return jsonify({"instrument": instrument, "ltp": "Error"})

# # # #         details = current_user.get("details", {})
# # # #         api_key = details.get("api_key")
# # # #         access_token = details.get("access_token")

# # # #         if not api_key or not access_token:
# # # #             return jsonify({"instrument": instrument, "ltp": "Error"})

# # # #         ltp, symbol = get_ltp_for_instrument(instrument, api_key, access_token)
# # # #         app.logger.info(f"[TRADE] {instrument} LTP = {ltp}")
# # # #         return jsonify({"instrument": instrument, "ltp": ltp})

# # # #     except Exception as e:
# # # #         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
# # # #         return jsonify({"instrument": None, "ltp": "Error"})


# # # # # -------------------- LOGOUT --------------------
# # # # @app.route("/logout")
# # # # def logout():
# # # #     user = session.pop("user", None)
# # # #     app.logger.info(f"User logged out: {user}")
# # # #     return redirect(url_for("home"))


# # # # # -------------------- RUN APP --------------------
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # import json, os, time, logging
# # # from kiteconnect import KiteConnect

# # # # -------------------- Logging Setup --------------------
# # # logging.basicConfig(
# # #     level=logging.DEBUG,
# # #     format="%(asctime)s [%(levelname)s] %(message)s",
# # #     handlers=[logging.StreamHandler()]
# # # )

# # # app = Flask(__name__)
# # # app.secret_key = "infocap_secret_2025"

# # # DATA_FILE = os.path.abspath("users.json")
# # # TRADE_FILE = os.path.abspath("trade_settings.json")

# # # # -------------------- Utility --------------------
# # # if not os.path.exists(DATA_FILE):
# # #     with open(DATA_FILE, "w") as f:
# # #         json.dump([], f)

# # # if not os.path.exists(TRADE_FILE):
# # #     with open(TRADE_FILE, "w") as f:
# # #         json.dump([], f)

# # # def load_users():
# # #     with open(DATA_FILE, "r") as f:
# # #         return json.load(f)

# # # def save_users(users):
# # #     with open(DATA_FILE, "w") as f:
# # #         json.dump(users, f, indent=4)

# # # # ✅ Global log before every request
# # # @app.before_request
# # # def log_request():
# # #     app.logger.info(f"➡️ {request.method} {request.path}")

# # # # ✅ Utility: Get LTP for any instrument
# # # def get_ltp_for_instrument(instrument, api_key, access_token):
# # #     """Fetch live LTP from Kite for given instrument"""
# # #     kite = KiteConnect(api_key=api_key)
# # #     kite.set_access_token(access_token)

# # #     instrument_map = {
# # #         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
# # #         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
# # #         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
# # #     }

# # #     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
# # #         try:
# # #             data = kite.ltp(sym)
# # #             price = list(data.values())[0]["last_price"]
# # #             app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
# # #             return price, sym
# # #         except Exception as e:
# # #             app.logger.warning(f"[LTP FAIL] {sym} → {e}")
# # #     return "Error", None

# # # # -------------------- LOGIN PAGE --------------------
# # # @app.route("/")
# # # def home():
# # #     app.logger.info("Rendering login page")
# # #     return render_template("login.html")

# # # # -------------------- SIGNUP --------------------
# # # @app.route("/signup", methods=["POST"])
# # # def signup():
# # #     data = request.get_json(force=True)
# # #     name, email, mobile, password = (
# # #         data.get("name"),
# # #         data.get("email"),
# # #         data.get("mobile"),
# # #         data.get("password"),
# # #     )
# # #     users = load_users()
# # #     if any(u["email"] == email for u in users):
# # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # #     users.append({
# # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # #     })
# # #     save_users(users)
# # #     app.logger.info(f"New signup: {email}")
# # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # -------------------- LOGIN --------------------
# # # @app.route("/login", methods=["POST"])
# # # def login():
# # #     data = request.get_json(force=True)
# # #     email = data.get("email")
# # #     password = data.get("password")

# # #     users = load_users()
# # #     for u in users:
# # #         if u["email"] == email and u["password"] == password:
# # #             session["user"] = email
# # #             if not u.get("details") or not u["details"].get("user_id"):
# # #                 return jsonify({
# # #                     "status": "redirect",
# # #                     "message": "First-time login. Please fill your broker details.",
# # #                     "redirect_url": url_for("details_page")
# # #                 })
# # #             return jsonify({
# # #                 "status": "redirect",
# # #                 "message": "Login successful!",
# # #                 "redirect_url": url_for("server_connect_page")
# # #             })
# # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # -------------------- USER DETAILS PAGE --------------------
# # # @app.route("/details")
# # # def details_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))
# # #     return render_template("user_details.html", user=session["user"])

# # # @app.route("/save_details", methods=["POST"])
# # # def save_details():
# # #     if "user" not in session:
# # #         return jsonify({"status": "error", "message": "Not logged in"})
# # #     data = request.get_json(force=True)
# # #     users = load_users()
# # #     for u in users:
# # #         if u["email"] == session["user"]:
# # #             u["details"] = {
# # #                 "user_id": data.get("user_id"),
# # #                 "password": data.get("password"),
# # #                 "api_key": data.get("api_key"),
# # #                 "secret_key": data.get("secret_key"),
# # #                 "totp": data.get("totp"),
# # #                 "access_token": data.get("access_token", "")
# # #             }
# # #             save_users(users)
# # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # -------------------- SERVER CONNECT PAGE --------------------
# # # @app.route("/server_connect")
# # # def server_connect_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))
# # #     return render_template("server_connect.html")

# # # # -------------------- START SERVER --------------------
# # # @app.route("/start_server", methods=["POST"])
# # # def start_server():
# # #     from kiteconnect import KiteConnect
# # #     import pyotp
# # #     from selenium import webdriver
# # #     from selenium.webdriver.common.by import By
# # #     from selenium.webdriver.firefox.service import Service
# # #     from selenium.webdriver.firefox.options import Options
# # #     from selenium.webdriver.support.ui import WebDriverWait
# # #     from selenium.webdriver.support import expected_conditions as EC

# # #     users = load_users()
# # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # #     if not current_user or "details" not in current_user:
# # #         return jsonify({"status": "error", "message": "User details not found"})

# # #     d = current_user["details"]
# # #     user_id, password, api_key, api_secret, totp_secret = (
# # #         d.get("user_id"),
# # #         d.get("password"),
# # #         d.get("api_key"),
# # #         d.get("secret_key"),
# # #         d.get("totp"),
# # #     )

# # #     try:
# # #         gecko_path = r"C:\Users\Dell\Documents\traders project\geckodriver.exe"
# # #         firefox_path = r"C:\Users\Dell\Documents\traders project\Mozilla Firefox\firefox.exe"
# # #         options = Options()
# # #         options.binary_location = firefox_path
# # #         service = Service(gecko_path)
# # #         driver = webdriver.Firefox(service=service, options=options)

# # #         kite = KiteConnect(api_key=api_key)
# # #         driver.get(kite.login_url())

# # #         WebDriverWait(driver, 25).until(
# # #             EC.visibility_of_element_located((By.ID, "userid"))
# # #         ).send_keys(user_id)
# # #         driver.find_element(By.ID, "password").send_keys(password)
# # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # #         time.sleep(3)

# # #         WebDriverWait(driver, 30).until(
# # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # #         )

# # #         totp = pyotp.TOTP(totp_secret).now()
# # #         driver.execute_script("""
# # #             let boxes = document.querySelectorAll('input');
# # #             for (let i of boxes) {
# # #                 if (i.offsetParent !== null) {
# # #                     i.value = arguments[0];
# # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # #                 }
# # #             }
# # #         """, totp)

# # #         time.sleep(1)
# # #         try:
# # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # #         except:
# # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # #         current_url = driver.current_url
# # #         driver.quit()

# # #         if "request_token=" not in current_url:
# # #             return jsonify({"status": "error", "message": "Request token not found"})

# # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # #         access_token = data["access_token"]

# # #         current_user["details"]["access_token"] = access_token
# # #         save_users(users)

# # #         return jsonify({
# # #             "status": "redirect",
# # #             "message": "Server connected successfully! Redirecting to dashboard...",
# # #             "redirect_url": url_for("dashboard_page")
# # #         })

# # #     except Exception as e:
# # #         app.logger.error(f"[start_server] Error: {e}")
# # #         return jsonify({"status": "error", "message": str(e)})

# # # # -------------------- DASHBOARD --------------------
# # # @app.route("/dashboard")
# # # def dashboard_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))
# # #     return render_template("dashboard.html")

# # # # -------------------- TRADE PAGE --------------------
# # # @app.route("/trade")
# # # def trade_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))

# # #     try:
# # #         with open(TRADE_FILE, "r") as f:
# # #             trades = json.load(f)
# # #     except:
# # #         trades = []

# # #     trade = next((t for t in trades if t["user"] == session["user"]), None)
# # #     instrument = trade["instrument"] if trade else ""
# # #     entry_time = trade["entry_time"] if trade else "9:15 AM"
# # #     exit_time = trade["exit_time"] if trade else "3:30 PM"
# # #     target = trade["target"] if trade else ""
# # #     stoploss = trade["stoploss"] if trade else ""

# # #     return render_template("trade.html",
# # #                            instrument=instrument,
# # #                            entry_time=entry_time,
# # #                            exit_time=exit_time,
# # #                            target=target,
# # #                            stoploss=stoploss)
    

# # # # -------------------- SAVE TRADE SETTINGS --------------------
# # # @app.route("/save_trade_settings", methods=["POST"])
# # # def save_trade_settings():
# # #     if "user" not in session:
# # #         return jsonify({"status": "error", "message": "Not logged in"})

# # #     data = request.get_json(force=True)
# # #     instrument = data.get("instrument")
# # #     entry_time = data.get("entry_time")
# # #     exit_time = data.get("exit_time")
# # #     target = data.get("target")
# # #     stoploss = data.get("stoploss")

# # #     if os.path.exists(TRADE_FILE):
# # #         with open(TRADE_FILE, "r") as f:
# # #             trades = json.load(f)
# # #     else:
# # #         trades = []

# # #     trades = [t for t in trades if t["user"] != session["user"]]
# # #     trades.append({
# # #         "user": session["user"],
# # #         "instrument": instrument,
# # #         "entry_time": entry_time,
# # #         "exit_time": exit_time,
# # #         "target": target,
# # #         "stoploss": stoploss,
# # #         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
# # #     })

# # #     with open(TRADE_FILE, "w") as f:
# # #         json.dump(trades, f, indent=4)

# # #     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument})")
# # #     return jsonify({
# # #     "status": "redirect",
# # #     "message": "Trade settings saved successfully!",
# # #     "redirect_url": url_for("terminal_page")
# # # })




# # # # -------------------- GET TRADE LTP --------------------
# # # @app.route("/get_trade_ltp")
# # # def get_trade_ltp():
# # #     """Read trade_settings.json and fetch live LTP"""
# # #     if "user" not in session:
# # #         return jsonify({"instrument": None, "ltp": "Error"})

# # #     try:
# # #         # Read selected instrument from trade_settings.json
# # #         if os.path.exists(TRADE_FILE):
# # #             with open(TRADE_FILE, "r") as f:
# # #                 trades = json.load(f)
# # #             trade = next((t for t in trades if t["user"] == session["user"]), None)
# # #             instrument = trade["instrument"] if trade else "NIFTY"
# # #         else:
# # #             instrument = "NIFTY"

# # #         # Load user credentials
# # #         users = load_users()
# # #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# # #         if not current_user:
# # #             return jsonify({"instrument": instrument, "ltp": "Error"})

# # #         details = current_user.get("details", {})
# # #         api_key = details.get("api_key")
# # #         access_token = details.get("access_token")

# # #         if not api_key or not access_token:
# # #             app.logger.error("[TRADE] Missing API key or access token.")
# # #             return jsonify({"instrument": instrument, "ltp": "Error"})

# # #         # Fetch LTP
# # #         ltp, symbol = get_ltp_for_instrument(instrument, api_key, access_token)
# # #         return jsonify({"instrument": instrument, "ltp": ltp})

# # #     except Exception as e:
# # #         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
# # #         return jsonify({"instrument": None, "ltp": "Error"})

# # # # -------------------- LOGOUT --------------------
# # # @app.route("/logout")
# # # def logout():
# # #     user = session.pop("user", None)
# # #     app.logger.info(f"User logged out: {user}")
# # #     return redirect(url_for("home"))
# # # # -------------------- TERMINAL PAGE --------------------

# # # # -------------------- TERMINAL PAGE --------------------
# # # @app.route("/terminal")
# # # def terminal_page():
# # #     print("✅ Terminal route reached!")  # Add this log
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))
# # #     return render_template("terminal.html")


# # # # -------------------- RUN APP --------------------
# # # if __name__ == "__main__":
# # #     app.run(debug=True)

# # # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # # import json, os, time, logging
# # # from kiteconnect import KiteConnect

# # # # -------------------- Logging Setup --------------------
# # # logging.basicConfig(
# # #     level=logging.DEBUG,
# # #     format="%(asctime)s [%(levelname)s] %(message)s",
# # #     handlers=[logging.StreamHandler()]
# # # )

# # # # ✅ Explicitly specify templates folder
# # # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # # TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# # # app = Flask(__name__, template_folder=TEMPLATES_DIR)
# # # app.secret_key = "infocap_secret_2025"

# # # DATA_FILE = os.path.join(BASE_DIR, "users.json")
# # # TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

# # # # -------------------- Utility --------------------
# # # if not os.path.exists(DATA_FILE):
# # #     with open(DATA_FILE, "w") as f:
# # #         json.dump([], f)

# # # if not os.path.exists(TRADE_FILE):
# # #     with open(TRADE_FILE, "w") as f:
# # #         json.dump([], f)

# # # def load_users():
# # #     with open(DATA_FILE, "r") as f:
# # #         return json.load(f)

# # # def save_users(users):
# # #     with open(DATA_FILE, "w") as f:
# # #         json.dump(users, f, indent=4)

# # # # ✅ Log every request
# # # @app.before_request
# # # def log_request():
# # #     app.logger.info(f"➡️ {request.method} {request.path}")

# # # # ✅ Utility: Get LTP for any instrument
# # # def get_ltp_for_instrument(instrument, api_key, access_token):
# # #     kite = KiteConnect(api_key=api_key)
# # #     kite.set_access_token(access_token)

# # #     instrument_map = {
# # #         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
# # #         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
# # #         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
# # #     }

# # #     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
# # #         try:
# # #             data = kite.ltp(sym)
# # #             price = list(data.values())[0]["last_price"]
# # #             app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
# # #             return price, sym
# # #         except Exception as e:
# # #             app.logger.warning(f"[LTP FAIL] {sym} → {e}")
# # #     return "Error", None

# # # # -------------------- LOGIN PAGE --------------------
# # # @app.route("/")
# # # def home():
# # #     app.logger.info("Rendering login page")
# # #     return render_template("login.html")

# # # # -------------------- SIGNUP --------------------
# # # @app.route("/signup", methods=["POST"])
# # # def signup():
# # #     data = request.get_json(force=True)
# # #     name, email, mobile, password = (
# # #         data.get("name"),
# # #         data.get("email"),
# # #         data.get("mobile"),
# # #         data.get("password"),
# # #     )
# # #     users = load_users()
# # #     if any(u["email"] == email for u in users):
# # #         return jsonify({"status": "error", "message": "Email already registered!"})

# # #     users.append({
# # #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# # #     })
# # #     save_users(users)
# # #     app.logger.info(f"New signup: {email}")
# # #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # # -------------------- LOGIN --------------------
# # # @app.route("/login", methods=["POST"])
# # # def login():
# # #     data = request.get_json(force=True)
# # #     email = data.get("email")
# # #     password = data.get("password")

# # #     users = load_users()
# # #     for u in users:
# # #         if u["email"] == email and u["password"] == password:
# # #             session["user"] = email
# # #             if not u.get("details") or not u["details"].get("user_id"):
# # #                 return jsonify({
# # #                     "status": "redirect",
# # #                     "message": "First-time login. Please fill your broker details.",
# # #                     "redirect_url": url_for("details_page")
# # #                 })
# # #             return jsonify({
# # #                 "status": "redirect",
# # #                 "message": "Login successful!",
# # #                 "redirect_url": url_for("server_connect_page")
# # #             })
# # #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # # -------------------- USER DETAILS PAGE --------------------
# # # @app.route("/details")
# # # def details_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))
# # #     return render_template("user_details.html", user=session["user"])

# # # @app.route("/save_details", methods=["POST"])
# # # def save_details():
# # #     if "user" not in session:
# # #         return jsonify({"status": "error", "message": "Not logged in"})
# # #     data = request.get_json(force=True)
# # #     users = load_users()
# # #     for u in users:
# # #         if u["email"] == session["user"]:
# # #             u["details"] = {
# # #                 "user_id": data.get("user_id"),
# # #                 "password": data.get("password"),
# # #                 "api_key": data.get("api_key"),
# # #                 "secret_key": data.get("secret_key"),
# # #                 "totp": data.get("totp"),
# # #                 "access_token": data.get("access_token", "")
# # #             }
# # #             save_users(users)
# # #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# # #     return jsonify({"status": "error", "message": "User not found!"})

# # # # -------------------- SERVER CONNECT PAGE --------------------
# # # @app.route("/server_connect")
# # # def server_connect_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))
# # #     return render_template("server_connect.html")

# # # # -------------------- START SERVER --------------------
# # # @app.route("/start_server", methods=["POST"])
# # # def start_server():
# # #     from kiteconnect import KiteConnect
# # #     import pyotp
# # #     from selenium import webdriver
# # #     from selenium.webdriver.common.by import By
# # #     from selenium.webdriver.firefox.service import Service
# # #     from selenium.webdriver.firefox.options import Options
# # #     from selenium.webdriver.support.ui import WebDriverWait
# # #     from selenium.webdriver.support import expected_conditions as EC

# # #     users = load_users()
# # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # #     if not current_user or "details" not in current_user:
# # #         return jsonify({"status": "error", "message": "User details not found"})

# # #     d = current_user["details"]
# # #     user_id, password, api_key, api_secret, totp_secret = (
# # #         d.get("user_id"),
# # #         d.get("password"),
# # #         d.get("api_key"),
# # #         d.get("secret_key"),
# # #         d.get("totp"),
# # #     )

# # #     try:
# # #         gecko_path = os.path.join(BASE_DIR, "geckodriver.exe")
# # #         firefox_path = os.path.join(BASE_DIR, "Mozilla Firefox", "firefox.exe")
# # #         options = Options()
# # #         options.binary_location = firefox_path
# # #         service = Service(gecko_path)
# # #         driver = webdriver.Firefox(service=service, options=options)

# # #         kite = KiteConnect(api_key=api_key)
# # #         driver.get(kite.login_url())

# # #         WebDriverWait(driver, 25).until(
# # #             EC.visibility_of_element_located((By.ID, "userid"))
# # #         ).send_keys(user_id)
# # #         driver.find_element(By.ID, "password").send_keys(password)
# # #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# # #         time.sleep(3)

# # #         WebDriverWait(driver, 30).until(
# # #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# # #         )

# # #         totp = pyotp.TOTP(totp_secret).now()
# # #         driver.execute_script("""
# # #             let boxes = document.querySelectorAll('input');
# # #             for (let i of boxes) {
# # #                 if (i.offsetParent !== null) {
# # #                     i.value = arguments[0];
# # #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# # #                 }
# # #             }
# # #         """, totp)

# # #         time.sleep(1)
# # #         try:
# # #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# # #         except:
# # #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# # #         current_url = driver.current_url
# # #         driver.quit()

# # #         if "request_token=" not in current_url:
# # #             return jsonify({"status": "error", "message": "Request token not found"})

# # #         request_token = current_url.split("request_token=")[1].split("&")[0]
# # #         data = kite.generate_session(request_token, api_secret=api_secret)
# # #         access_token = data["access_token"]

# # #         current_user["details"]["access_token"] = access_token
# # #         save_users(users)

# # #         return jsonify({
# # #             "status": "redirect",
# # #             "message": "Server connected successfully! Redirecting to dashboard...",
# # #             "redirect_url": url_for("dashboard_page")
# # #         })

# # #     except Exception as e:
# # #         app.logger.error(f"[start_server] Error: {e}")
# # #         return jsonify({"status": "error", "message": str(e)})

# # # # -------------------- DASHBOARD --------------------
# # # @app.route("/dashboard")
# # # def dashboard_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))

# # #     users = load_users()
# # #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# # #     details = current_user.get("details", {}) if current_user else {}

# # #     return render_template("dashboard.html", details=details)


# # # # -------------------- TRADE PAGE --------------------
# # # @app.route("/trade")
# # # def trade_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))

# # #     try:
# # #         with open(TRADE_FILE, "r") as f:
# # #             trades = json.load(f)
# # #     except:
# # #         trades = []

# # #     trade = next((t for t in trades if t["user"] == session["user"]), None)
# # #     instrument = trade["instrument"] if trade else ""
# # #     entry_time = trade["entry_time"] if trade else "9:15 AM"
# # #     exit_time = trade["exit_time"] if trade else "3:30 PM"
# # #     target = trade["target"] if trade else ""
# # #     stoploss = trade["stoploss"] if trade else ""

# # #     return render_template("trade.html",
# # #                            instrument=instrument,
# # #                            entry_time=entry_time,
# # #                            exit_time=exit_time,
# # #                            target=target,
# # #                            stoploss=stoploss)

# # # # -------------------- SAVE TRADE SETTINGS --------------------
# # # @app.route("/save_trade_settings", methods=["POST"])
# # # def save_trade_settings():
# # #     if "user" not in session:
# # #         return jsonify({"status": "error", "message": "Not logged in"})

# # #     data = request.get_json(force=True)
# # #     instrument = data.get("instrument")
# # #     entry_time = data.get("entry_time")
# # #     exit_time = data.get("exit_time")
# # #     target = data.get("target")
# # #     stoploss = data.get("stoploss")

# # #     if os.path.exists(TRADE_FILE):
# # #         with open(TRADE_FILE, "r") as f:
# # #             trades = json.load(f)
# # #     else:
# # #         trades = []

# # #     trades = [t for t in trades if t["user"] != session["user"]]
# # #     trades.append({
# # #         "user": session["user"],
# # #         "instrument": instrument,
# # #         "entry_time": entry_time,
# # #         "exit_time": exit_time,
# # #         "target": target,
# # #         "stoploss": stoploss,
# # #         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
# # #     })

# # #     with open(TRADE_FILE, "w") as f:
# # #         json.dump(trades, f, indent=4)

# # #     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument})")
# # #     return jsonify({
# # #         "status": "redirect",
# # #         "message": "Trade settings saved successfully!",
# # #         "redirect_url": url_for("terminal_page")
# # #     })

# # # # -------------------- GET TRADE LTP --------------------
# # # @app.route("/get_trade_ltp")
# # # def get_trade_ltp():
# # #     if "user" not in session:
# # #         return jsonify({"instrument": None, "ltp": "Error"})

# # #     try:
# # #         if os.path.exists(TRADE_FILE):
# # #             with open(TRADE_FILE, "r") as f:
# # #                 trades = json.load(f)
# # #             trade = next((t for t in trades if t["user"] == session["user"]), None)
# # #             instrument = trade["instrument"] if trade else "NIFTY"
# # #         else:
# # #             instrument = "NIFTY"

# # #         users = load_users()
# # #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# # #         if not current_user:
# # #             return jsonify({"instrument": instrument, "ltp": "Error"})

# # #         details = current_user.get("details", {})
# # #         api_key = details.get("api_key")
# # #         access_token = details.get("access_token")

# # #         if not api_key or not access_token:
# # #             app.logger.error("[TRADE] Missing API key or access token.")
# # #             return jsonify({"instrument": instrument, "ltp": "Error"})

# # #         ltp, symbol = get_ltp_for_instrument(instrument, api_key, access_token)
# # #         return jsonify({"instrument": instrument, "ltp": ltp})

# # #     except Exception as e:
# # #         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
# # #         return jsonify({"instrument": None, "ltp": "Error"})

# # # # -------------------- TERMINAL PAGE --------------------
# # # @app.route("/terminal")
# # # def terminal_page():
# # #     if "user" not in session:
# # #         return redirect(url_for("home"))
# # #     return render_template("terminal.html")


# # # # -------------------- LOGOUT --------------------
# # # @app.route("/logout")
# # # def logout():
# # #     user = session.pop("user", None)
# # #     app.logger.info(f"User logged out: {user}")
# # #     return redirect(url_for("home"))

# # # print("✅ ROUTES LOADED:", [str(r) for r in app.url_map.iter_rules()])


# # # # -------------------- RUN APP --------------------
# # # if __name__ == "__main__":
# # #     app.logger.info("🚀 Flask server starting...")
# # #     app.run(debug=True)

# # from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# # import json, os, time, logging
# # from kiteconnect import KiteConnect

# # # -------------------- Logging Setup --------------------
# # logging.basicConfig(
# #     level=logging.DEBUG,
# #     format="%(asctime)s [%(levelname)s] %(message)s",
# #     handlers=[logging.StreamHandler()]
# # )

# # # ✅ Explicitly specify templates folder
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# # app = Flask(__name__, template_folder=TEMPLATES_DIR)
# # app.secret_key = "infocap_secret_2025"

# # DATA_FILE = os.path.join(BASE_DIR, "users.json")
# # TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

# # # -------------------- Utility --------------------
# # if not os.path.exists(DATA_FILE):
# #     with open(DATA_FILE, "w") as f:
# #         json.dump([], f)

# # if not os.path.exists(TRADE_FILE):
# #     with open(TRADE_FILE, "w") as f:
# #         json.dump([], f)

# # def load_users():
# #     with open(DATA_FILE, "r") as f:
# #         return json.load(f)

# # def save_users(users):
# #     with open(DATA_FILE, "w") as f:
# #         json.dump(users, f, indent=4)

# # # ✅ Log every request
# # @app.before_request
# # def log_request():
# #     app.logger.info(f"➡️ {request.method} {request.path}")

# # # ✅ Utility: Get LTP for any instrument
# # def get_ltp_for_instrument(instrument, api_key, access_token):
# #     kite = KiteConnect(api_key=api_key)
# #     kite.set_access_token(access_token)

# #     instrument_map = {
# #         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
# #         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
# #         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
# #     }

# #     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
# #         try:
# #             data = kite.ltp(sym)
# #             price = list(data.values())[0]["last_price"]
# #             app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
# #             return price, sym
# #         except Exception as e:
# #             app.logger.warning(f"[LTP FAIL] {sym} → {e}")
# #     return "Error", None

# # # -------------------- LOGIN PAGE --------------------
# # @app.route("/")
# # def home():
# #     app.logger.info("Rendering login page")
# #     return render_template("login.html")

# # # -------------------- SIGNUP --------------------
# # @app.route("/signup", methods=["POST"])
# # def signup():
# #     data = request.get_json(force=True)
# #     name, email, mobile, password = (
# #         data.get("name"),
# #         data.get("email"),
# #         data.get("mobile"),
# #         data.get("password"),
# #     )
# #     users = load_users()
# #     if any(u["email"] == email for u in users):
# #         return jsonify({"status": "error", "message": "Email already registered!"})

# #     users.append({
# #         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
# #     })
# #     save_users(users)
# #     app.logger.info(f"New signup: {email}")
# #     return jsonify({"status": "success", "message": "Signup successful!"})

# # # -------------------- LOGIN --------------------
# # @app.route("/login", methods=["POST"])
# # def login():
# #     data = request.get_json(force=True)
# #     email = data.get("email")
# #     password = data.get("password")

# #     users = load_users()
# #     for u in users:
# #         if u["email"] == email and u["password"] == password:
# #             session["user"] = email
# #             if not u.get("details") or not u["details"].get("user_id"):
# #                 return jsonify({
# #                     "status": "redirect",
# #                     "message": "First-time login. Please fill your broker details.",
# #                     "redirect_url": url_for("details_page")
# #                 })
# #             return jsonify({
# #                 "status": "redirect",
# #                 "message": "Login successful!",
# #                 "redirect_url": url_for("server_connect_page")
# #             })
# #     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # # -------------------- USER DETAILS PAGE --------------------
# # @app.route("/details")
# # def details_page():
# #     if "user" not in session:
# #         return redirect(url_for("home"))
# #     return render_template("user_details.html", user=session["user"])

# # @app.route("/save_details", methods=["POST"])
# # def save_details():
# #     if "user" not in session:
# #         return jsonify({"status": "error", "message": "Not logged in"})
# #     data = request.get_json(force=True)
# #     users = load_users()
# #     for u in users:
# #         if u["email"] == session["user"]:
# #             u["details"] = {
# #                 "user_id": data.get("user_id"),
# #                 "password": data.get("password"),
# #                 "api_key": data.get("api_key"),
# #                 "secret_key": data.get("secret_key"),
# #                 "totp": data.get("totp"),
# #                 "access_token": data.get("access_token", "")
# #             }
# #             save_users(users)
# #             return jsonify({"status": "success", "message": "Details saved successfully!"})
# #     return jsonify({"status": "error", "message": "User not found!"})

# # # -------------------- SERVER CONNECT PAGE --------------------
# # @app.route("/server_connect")
# # def server_connect_page():
# #     if "user" not in session:
# #         return redirect(url_for("home"))
# #     return render_template("server_connect.html")

# # # -------------------- START SERVER --------------------
# # @app.route("/start_server", methods=["POST"])
# # def start_server():
# #     from kiteconnect import KiteConnect
# #     import pyotp
# #     from selenium import webdriver
# #     from selenium.webdriver.common.by import By
# #     from selenium.webdriver.firefox.service import Service
# #     from selenium.webdriver.firefox.options import Options
# #     from selenium.webdriver.support.ui import WebDriverWait
# #     from selenium.webdriver.support import expected_conditions as EC

# #     users = load_users()
# #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# #     if not current_user or "details" not in current_user:
# #         return jsonify({"status": "error", "message": "User details not found"})

# #     d = current_user["details"]
# #     user_id, password, api_key, api_secret, totp_secret = (
# #         d.get("user_id"),
# #         d.get("password"),
# #         d.get("api_key"),
# #         d.get("secret_key"),
# #         d.get("totp"),
# #     )

# #     try:
# #         gecko_path = os.path.join(BASE_DIR, "geckodriver.exe")
# #         firefox_path = os.path.join(BASE_DIR, "Mozilla Firefox", "firefox.exe")
# #         options = Options()
# #         options.binary_location = firefox_path
# #         service = Service(gecko_path)
# #         driver = webdriver.Firefox(service=service, options=options)

# #         kite = KiteConnect(api_key=api_key)
# #         driver.get(kite.login_url())

# #         WebDriverWait(driver, 25).until(
# #             EC.visibility_of_element_located((By.ID, "userid"))
# #         ).send_keys(user_id)
# #         driver.find_element(By.ID, "password").send_keys(password)
# #         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# #         time.sleep(3)

# #         WebDriverWait(driver, 30).until(
# #             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
# #         )

# #         totp = pyotp.TOTP(totp_secret).now()
# #         driver.execute_script("""
# #             let boxes = document.querySelectorAll('input');
# #             for (let i of boxes) {
# #                 if (i.offsetParent !== null) {
# #                     i.value = arguments[0];
# #                     i.dispatchEvent(new Event('input', { bubbles: true }));
# #                 }
# #             }
# #         """, totp)

# #         time.sleep(1)
# #         try:
# #             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
# #         except:
# #             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# #         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
# #         current_url = driver.current_url
# #         driver.quit()

# #         if "request_token=" not in current_url:
# #             return jsonify({"status": "error", "message": "Request token not found"})

# #         request_token = current_url.split("request_token=")[1].split("&")[0]
# #         data = kite.generate_session(request_token, api_secret=api_secret)
# #         access_token = data["access_token"]

# #         current_user["details"]["access_token"] = access_token
# #         save_users(users)

# #         return jsonify({
# #             "status": "redirect",
# #             "message": "Server connected successfully! Redirecting to dashboard...",
# #             "redirect_url": url_for("dashboard_page")
# #         })

# #     except Exception as e:
# #         app.logger.error(f"[start_server] Error: {e}")
# #         return jsonify({"status": "error", "message": str(e)})

# # # -------------------- DASHBOARD --------------------
# # @app.route("/dashboard")
# # def dashboard_page():
# #     if "user" not in session:
# #         return redirect(url_for("home"))

# #     users = load_users()
# #     current_user = next((u for u in users if u["email"] == session["user"]), None)
# #     details = current_user.get("details", {}) if current_user else {}

# #     return render_template("dashboard.html", details=details)

# # # -------------------- TRADE PAGE --------------------
# # @app.route("/trade")
# # def trade_page():
# #     if "user" not in session:
# #         return redirect(url_for("home"))

# #     try:
# #         with open(TRADE_FILE, "r") as f:
# #             trades = json.load(f)
# #     except:
# #         trades = []

# #     trade = next((t for t in trades if t["user"] == session["user"]), None)
# #     instrument = trade["instrument"] if trade else ""
# #     entry_time = trade["entry_time"] if trade else "9:15 AM"
# #     exit_time = trade["exit_time"] if trade else "3:30 PM"
# #     target = trade["target"] if trade else ""
# #     stoploss = trade["stoploss"] if trade else ""

# #     return render_template("trade.html",
# #                            instrument=instrument,
# #                            entry_time=entry_time,
# #                            exit_time=exit_time,
# #                            target=target,
# #                            stoploss=stoploss)

# # # -------------------- SAVE TRADE SETTINGS --------------------
# # @app.route("/save_trade_settings", methods=["POST"])
# # def save_trade_settings():
# #     if "user" not in session:
# #         return jsonify({"status": "error", "message": "Not logged in"})

# #     data = request.get_json(force=True)
# #     instrument = data.get("instrument")
# #     entry_time = data.get("entry_time")
# #     exit_time = data.get("exit_time")
# #     target = data.get("target")
# #     stoploss = data.get("stoploss")

# #     if os.path.exists(TRADE_FILE):
# #         with open(TRADE_FILE, "r") as f:
# #             trades = json.load(f)
# #     else:
# #         trades = []

# #     trades = [t for t in trades if t["user"] != session["user"]]
# #     trades.append({
# #         "user": session["user"],
# #         "instrument": instrument,
# #         "entry_time": entry_time,
# #         "exit_time": exit_time,
# #         "target": target,
# #         "stoploss": stoploss,
# #         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
# #     })

# #     with open(TRADE_FILE, "w") as f:
# #         json.dump(trades, f, indent=4)

# #     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument})")
# #     return jsonify({
# #         "status": "redirect",
# #         "message": "Trade settings saved successfully!",
# #         "redirect_url": url_for("terminal_page")
# #     })

# # # -------------------- GET TRADE LTP + MARGIN --------------------
# # @app.route("/get_trade_ltp")
# # def get_trade_ltp():
# #     """Fetch LTP and margin info safely across all Kite API versions"""
# #     if "user" not in session:
# #         return jsonify({"instrument": None, "ltp": "Error", "margin": "--"})

# #     try:
# #         # Read selected instrument
# #         if os.path.exists(TRADE_FILE):
# #             with open(TRADE_FILE, "r") as f:
# #                 trades = json.load(f)
# #             trade = next((t for t in trades if t["user"] == session["user"]), None)
# #             instrument = trade["instrument"] if trade else "NIFTY"
# #         else:
# #             instrument = "NIFTY"

# #         # Load credentials
# #         users = load_users()
# #         current_user = next((u for u in users if u["email"] == session["user"]), None)
# #         if not current_user:
# #             return jsonify({"instrument": instrument, "ltp": "Error", "margin": "--"})

# #         details = current_user.get("details", {})
# #         api_key = details.get("api_key")
# #         access_token = details.get("access_token")

# #         if not api_key or not access_token:
# #             return jsonify({"instrument": instrument, "ltp": "Error", "margin": "--"})

# #         # ✅ Initialize Kite
# #         kite = KiteConnect(api_key=api_key)
# #         kite.set_access_token(access_token)

# #         # ✅ Get LTP
# #         ltp, _ = get_ltp_for_instrument(instrument, api_key, access_token)

# #         # ✅ Get Margin (handles all API formats)
# #         margin_display = "--"
# #         try:
# #             margin_data = kite.margins(segment="equity")

# #             if isinstance(margin_data, dict):
# #                 if "data" in margin_data:
# #                     margin_data = margin_data["data"]

# #                 if "net" in margin_data:
# #                     available = margin_data["net"].get("available")
# #                     if isinstance(available, (int, float)):
# #                         margin_display = f"₹{available:,.2f}"
# #                     elif isinstance(available, dict) and "cash" in available:
# #                         margin_display = f"₹{available['cash']:,.2f}"
# #                 else:
# #                     # fallback: maybe only total available
# #                     if isinstance(margin_data.get("available"), (int, float)):
# #                         margin_display = f"₹{margin_data['available']:,.2f}"

# #             elif isinstance(margin_data, (int, float)):
# #                 margin_display = f"₹{margin_data:,.2f}"

# #         except Exception as e:
# #             app.logger.warning(f"[MARGIN FAIL SAFE] {e}")
# #             margin_display = "--"

# #         return jsonify({
# #             "instrument": instrument,
# #             "ltp": ltp,
# #             "margin": margin_display
# #         })

# #     except Exception as e:
# #         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
# #         return jsonify({"instrument": None, "ltp": "Error", "margin": "--"})

# # # -------------------- TERMINAL PAGE --------------------
# # @app.route("/terminal")
# # def terminal_page():
# #     if "user" not in session:
# #         return redirect(url_for("home"))
# #     return render_template("terminal.html")

# # # -------------------- LOGOUT --------------------
# # @app.route("/logout")
# # def logout():
# #     user = session.pop("user", None)
# #     app.logger.info(f"User logged out: {user}")
# #     return redirect(url_for("home"))

# # print("✅ ROUTES LOADED:", [str(r) for r in app.url_map.iter_rules()])

# # # -------------------- RUN APP --------------------
# # if __name__ == "__main__":
# #     app.logger.info("🚀 Flask server starting...")
# #     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# import json, os, time, logging
# from kiteconnect import KiteConnect

# # -------------------- Logging Setup --------------------
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     handlers=[logging.StreamHandler()]
# )

# # ✅ Explicitly specify templates folder
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# app = Flask(__name__, template_folder=TEMPLATES_DIR)
# app.secret_key = "infocap_secret_2025"

# DATA_FILE = os.path.join(BASE_DIR, "users.json")
# TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

# # -------------------- Utility --------------------
# if not os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "w") as f:
#         json.dump([], f)

# if not os.path.exists(TRADE_FILE):
#     with open(TRADE_FILE, "w") as f:
#         json.dump([], f)

# def load_users():
#     with open(DATA_FILE, "r") as f:
#         return json.load(f)

# def save_users(users):
#     with open(DATA_FILE, "w") as f:
#         json.dump(users, f, indent=4)

# # ✅ Log every request
# @app.before_request
# def log_request():
#     app.logger.info(f"➡️ {request.method} {request.path}")

# # ✅ Utility: Get LTP for any instrument
# def get_ltp_for_instrument(instrument, api_key, access_token):
#     kite = KiteConnect(api_key=api_key)
#     kite.set_access_token(access_token)

#     instrument_map = {
#         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
#         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
#         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
#     }

#     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
#         try:
#             data = kite.ltp(sym)
#             price = list(data.values())[0]["last_price"]
#             app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
#             return price, sym
#         except Exception as e:
#             app.logger.warning(f"[LTP FAIL] {sym} → {e}")
#     return "Error", None

# # -------------------- LOGIN PAGE --------------------
# @app.route("/")
# def home():
#     app.logger.info("Rendering login page")
#     return render_template("login.html")

# # -------------------- SIGNUP --------------------
# @app.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json(force=True)
#     name, email, mobile, password = (
#         data.get("name"),
#         data.get("email"),
#         data.get("mobile"),
#         data.get("password"),
#     )
#     users = load_users()
#     if any(u["email"] == email for u in users):
#         return jsonify({"status": "error", "message": "Email already registered!"})

#     users.append({
#         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
#     })
#     save_users(users)
#     app.logger.info(f"New signup: {email}")
#     return jsonify({"status": "success", "message": "Signup successful!"})

# # -------------------- LOGIN --------------------
# @app.route("/login", methods=["POST"])
# def login():
#     data = request.get_json(force=True)
#     email = data.get("email")
#     password = data.get("password")

#     users = load_users()
#     for u in users:
#         if u["email"] == email and u["password"] == password:
#             session["user"] = email
#             if not u.get("details") or not u["details"].get("user_id"):
#                 return jsonify({
#                     "status": "redirect",
#                     "message": "First-time login. Please fill your broker details.",
#                     "redirect_url": url_for("details_page")
#                 })
#             return jsonify({
#                 "status": "redirect",
#                 "message": "Login successful!",
#                 "redirect_url": url_for("server_connect_page")
#             })
#     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # -------------------- USER DETAILS PAGE --------------------
# @app.route("/details")
# def details_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("user_details.html", user=session["user"])

# @app.route("/save_details", methods=["POST"])
# def save_details():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})
#     data = request.get_json(force=True)
#     users = load_users()
#     for u in users:
#         if u["email"] == session["user"]:
#             u["details"] = {
#                 "user_id": data.get("user_id"),
#                 "password": data.get("password"),
#                 "api_key": data.get("api_key"),
#                 "secret_key": data.get("secret_key"),
#                 "totp": data.get("totp"),
#                 "access_token": data.get("access_token", "")
#             }
#             save_users(users)
#             return jsonify({"status": "success", "message": "Details saved successfully!"})
#     return jsonify({"status": "error", "message": "User not found!"})

# # -------------------- SERVER CONNECT PAGE --------------------
# @app.route("/server_connect")
# def server_connect_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("server_connect.html")

# # -------------------- START SERVER --------------------
# @app.route("/start_server", methods=["POST"])
# def start_server():
#     from kiteconnect import KiteConnect
#     import pyotp
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.firefox.service import Service
#     from selenium.webdriver.firefox.options import Options
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     if not current_user or "details" not in current_user:
#         return jsonify({"status": "error", "message": "User details not found"})

#     d = current_user["details"]
#     user_id, password, api_key, api_secret, totp_secret = (
#         d.get("user_id"),
#         d.get("password"),
#         d.get("api_key"),
#         d.get("secret_key"),
#         d.get("totp"),
#     )

#     try:
#         gecko_path = os.path.join(BASE_DIR, "geckodriver.exe")
#         firefox_path = os.path.join(BASE_DIR, "Mozilla Firefox", "firefox.exe")
#         options = Options()
#         options.binary_location = firefox_path
#         service = Service(gecko_path)
#         driver = webdriver.Firefox(service=service, options=options)

#         kite = KiteConnect(api_key=api_key)
#         driver.get(kite.login_url())

#         WebDriverWait(driver, 25).until(
#             EC.visibility_of_element_located((By.ID, "userid"))
#         ).send_keys(user_id)
#         driver.find_element(By.ID, "password").send_keys(password)
#         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#         time.sleep(3)

#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
#         )

#         totp = pyotp.TOTP(totp_secret).now()
#         driver.execute_script("""
#             let boxes = document.querySelectorAll('input');
#             for (let i of boxes) {
#                 if (i.offsetParent !== null) {
#                     i.value = arguments[0];
#                     i.dispatchEvent(new Event('input', { bubbles: true }));
#                 }
#             }
#         """, totp)

#         time.sleep(1)
#         try:
#             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
#         except:
#             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
#         current_url = driver.current_url
#         driver.quit()

#         if "request_token=" not in current_url:
#             return jsonify({"status": "error", "message": "Request token not found"})

#         request_token = current_url.split("request_token=")[1].split("&")[0]
#         data = kite.generate_session(request_token, api_secret=api_secret)
#         access_token = data["access_token"]

#         current_user["details"]["access_token"] = access_token
#         save_users(users)

#         return jsonify({
#             "status": "redirect",
#             "message": "Server connected successfully! Redirecting to dashboard...",
#             "redirect_url": url_for("dashboard_page")
#         })

#     except Exception as e:
#         app.logger.error(f"[start_server] Error: {e}")
#         return jsonify({"status": "error", "message": str(e)})

# # -------------------- DASHBOARD --------------------
# @app.route("/dashboard")
# def dashboard_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     details = current_user.get("details", {}) if current_user else {}

#     return render_template("dashboard.html", details=details)

# # -------------------- TRADE PAGE --------------------
# @app.route("/trade")
# def trade_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     try:
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     except:
#         trades = []

#     trade = next((t for t in trades if t["user"] == session["user"]), None)
#     instrument = trade["instrument"] if trade else ""
#     entry_time = trade["entry_time"] if trade else "9:15 AM"
#     exit_time = trade["exit_time"] if trade else "3:30 PM"
#     target = trade["target"] if trade else ""
#     stoploss = trade["stoploss"] if trade else ""

#     return render_template("trade.html",
#                            instrument=instrument,
#                            entry_time=entry_time,
#                            exit_time=exit_time,
#                            target=target,
#                            stoploss=stoploss)

# # -------------------- SAVE TRADE SETTINGS --------------------
# @app.route("/save_trade_settings", methods=["POST"])
# def save_trade_settings():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})

#     data = request.get_json(force=True)
#     instrument = data.get("instrument")
#     entry_time = data.get("entry_time")
#     exit_time = data.get("exit_time")
#     target = data.get("target")
#     stoploss = data.get("stoploss")

#     if os.path.exists(TRADE_FILE):
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     else:
#         trades = []

#     trades = [t for t in trades if t["user"] != session["user"]]
#     trades.append({
#         "user": session["user"],
#         "instrument": instrument,
#         "entry_time": entry_time,
#         "exit_time": exit_time,
#         "target": target,
#         "stoploss": stoploss,
#         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
#     })

#     with open(TRADE_FILE, "w") as f:
#         json.dump(trades, f, indent=4)

#     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument})")
#     return jsonify({
#         "status": "redirect",
#         "message": "Trade settings saved successfully!",
#         "redirect_url": url_for("terminal_page")
#     })

# # -------------------- GET TRADE LTP + MARGIN --------------------
# @app.route("/get_trade_ltp")
# def get_trade_ltp():
#     """Fetch LTP and margin info safely across all Kite API versions"""
#     if "user" not in session:
#         return jsonify({"instrument": None, "ltp": "Error", "margin": "--"})

#     try:
#         # Read selected instrument
#         if os.path.exists(TRADE_FILE):
#             with open(TRADE_FILE, "r") as f:
#                 trades = json.load(f)
#             trade = next((t for t in trades if t["user"] == session["user"]), None)
#             instrument = trade["instrument"] if trade else "NIFTY"
#         else:
#             instrument = "NIFTY"

#         # Load credentials
#         users = load_users()
#         current_user = next((u for u in users if u["email"] == session["user"]), None)
#         if not current_user:
#             return jsonify({"instrument": instrument, "ltp": "Error", "margin": "--"})

#         details = current_user.get("details", {})
#         api_key = details.get("api_key")
#         access_token = details.get("access_token")

#         if not api_key or not access_token:
#             return jsonify({"instrument": instrument, "ltp": "Error", "margin": "--"})

#         # ✅ Initialize Kite
#         kite = KiteConnect(api_key=api_key)
#         kite.set_access_token(access_token)

#         # ✅ Get LTP
#         ltp, _ = get_ltp_for_instrument(instrument, api_key, access_token)

#         # ✅ Improved Margin Handling (Fixed)
#         margin_display = "--"
#         try:
#             margin_data = kite.margins(segment="equity")
#             app.logger.debug(f"[MARGIN RAW DATA] {margin_data}")

#             if isinstance(margin_data, (int, float)):
#                 margin_display = f"₹{margin_data:,.2f}"

#             elif isinstance(margin_data, dict):
#                 data = margin_data.get("data", margin_data)
#                 if "net" in data:
#                     available = data["net"].get("available")
#                     if isinstance(available, dict) and "cash" in available:
#                         margin_display = f"₹{available['cash']:,.2f}"
#                     elif isinstance(available, (int, float)):
#                         margin_display = f"₹{available:,.2f}"
#                 elif "available" in data:
#                     val = data["available"]
#                     if isinstance(val, (int, float)):
#                         margin_display = f"₹{val:,.2f}"
#                     elif isinstance(val, dict) and "cash" in val:
#                         margin_display = f"₹{val['cash']:,.2f}"

#         except Exception as e:
#             app.logger.warning(f"[MARGIN FAIL FIXED] {e}")
#             margin_display = "--"

#         return jsonify({
#             "instrument": instrument,
#             "ltp": ltp,
#             "margin": margin_display
#         })

#     except Exception as e:
#         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
#         return jsonify({"instrument": None, "ltp": "Error", "margin": "--"})

# # -------------------- TERMINAL PAGE --------------------
# @app.route("/terminal")
# def terminal_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("terminal.html")

# # -------------------- LOGOUT --------------------
# @app.route("/logout")
# def logout():
#     user = session.pop("user", None)
#     app.logger.info(f"User logged out: {user}")
#     return redirect(url_for("home"))

# print("✅ ROUTES LOADED:", [str(r) for r in app.url_map.iter_rules()])

# # -------------------- RUN APP --------------------
# if __name__ == "__main__":
#     app.logger.info("🚀 Flask server starting...")
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# import json, os, time, logging
# from kiteconnect import KiteConnect

# # -------------------- Logging Setup --------------------
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     handlers=[logging.StreamHandler()]
# )

# # ✅ Explicitly specify templates folder
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# app = Flask(__name__, template_folder=TEMPLATES_DIR)
# app.secret_key = "infocap_secret_2025"

# DATA_FILE = os.path.join(BASE_DIR, "users.json")
# TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

# # -------------------- Utility --------------------
# if not os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "w") as f:
#         json.dump([], f)

# if not os.path.exists(TRADE_FILE):
#     with open(TRADE_FILE, "w") as f:
#         json.dump([], f)

# def load_users():
#     with open(DATA_FILE, "r") as f:
#         return json.load(f)

# def save_users(users):
#     with open(DATA_FILE, "w") as f:
#         json.dump(users, f, indent=4)

# # ✅ Log every request
# @app.before_request
# def log_request():
#     app.logger.info(f"➡️ {request.method} {request.path}")

# # ✅ Utility: Get LTP for any instrument
# def get_ltp_for_instrument(instrument, api_key, access_token):
#     kite = KiteConnect(api_key=api_key)
#     kite.set_access_token(access_token)

#     instrument_map = {
#         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
#         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
#         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
#     }

#     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
#         try:
#             data = kite.ltp(sym)
#             price = list(data.values())[0]["last_price"]
#             app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
#             return price, sym
#         except Exception as e:
#             app.logger.warning(f"[LTP FAIL] {sym} → {e}")
#     return "Error", None

# # -------------------- LOGIN PAGE --------------------
# @app.route("/")
# def home():
#     app.logger.info("Rendering login page")
#     return render_template("login.html")

# # -------------------- SIGNUP --------------------
# @app.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json(force=True)
#     name, email, mobile, password = (
#         data.get("name"),
#         data.get("email"),
#         data.get("mobile"),
#         data.get("password"),
#     )
#     users = load_users()
#     if any(u["email"] == email for u in users):
#         return jsonify({"status": "error", "message": "Email already registered!"})

#     users.append({
#         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
#     })
#     save_users(users)
#     app.logger.info(f"New signup: {email}")
#     return jsonify({"status": "success", "message": "Signup successful!"})

# # -------------------- LOGIN --------------------
# @app.route("/login", methods=["POST"])
# def login():
#     data = request.get_json(force=True)
#     email = data.get("email")
#     password = data.get("password")

#     users = load_users()
#     for u in users:
#         if u["email"] == email and u["password"] == password:
#             session["user"] = email
#             if not u.get("details") or not u["details"].get("user_id"):
#                 return jsonify({
#                     "status": "redirect",
#                     "message": "First-time login. Please fill your broker details.",
#                     "redirect_url": url_for("details_page")
#                 })
#             return jsonify({
#                 "status": "redirect",
#                 "message": "Login successful!",
#                 "redirect_url": url_for("server_connect_page")
#             })
#     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # -------------------- USER DETAILS PAGE --------------------
# @app.route("/details")
# def details_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("user_details.html", user=session["user"])

# @app.route("/save_details", methods=["POST"])
# def save_details():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})
#     data = request.get_json(force=True)
#     users = load_users()
#     for u in users:
#         if u["email"] == session["user"]:
#             u["details"] = {
#                 "user_id": data.get("user_id"),
#                 "password": data.get("password"),
#                 "api_key": data.get("api_key"),
#                 "secret_key": data.get("secret_key"),
#                 "totp": data.get("totp"),
#                 "access_token": data.get("access_token", "")
#             }
#             save_users(users)
#             return jsonify({"status": "success", "message": "Details saved successfully!"})
#     return jsonify({"status": "error", "message": "User not found!"})

# # -------------------- SERVER CONNECT PAGE --------------------
# @app.route("/server_connect")
# def server_connect_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("server_connect.html")

# # -------------------- START SERVER --------------------
# @app.route("/start_server", methods=["POST"])
# def start_server():
#     from kiteconnect import KiteConnect
#     import pyotp
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.firefox.service import Service
#     from selenium.webdriver.firefox.options import Options
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     if not current_user or "details" not in current_user:
#         return jsonify({"status": "error", "message": "User details not found"})

#     d = current_user["details"]
#     user_id, password, api_key, api_secret, totp_secret = (
#         d.get("user_id"),
#         d.get("password"),
#         d.get("api_key"),
#         d.get("secret_key"),
#         d.get("totp"),
#     )

#     try:
#         gecko_path = os.path.join(BASE_DIR, "geckodriver.exe")
#         firefox_path = os.path.join(BASE_DIR, "Mozilla Firefox", "firefox.exe")
#         options = Options()
#         options.binary_location = firefox_path
#         service = Service(gecko_path)
#         driver = webdriver.Firefox(service=service, options=options)

#         kite = KiteConnect(api_key=api_key)
#         driver.get(kite.login_url())

#         WebDriverWait(driver, 25).until(
#             EC.visibility_of_element_located((By.ID, "userid"))
#         ).send_keys(user_id)
#         driver.find_element(By.ID, "password").send_keys(password)
#         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#         time.sleep(3)

#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
#         )

#         totp = pyotp.TOTP(totp_secret).now()
#         driver.execute_script("""
#             let boxes = document.querySelectorAll('input');
#             for (let i of boxes) {
#                 if (i.offsetParent !== null) {
#                     i.value = arguments[0];
#                     i.dispatchEvent(new Event('input', { bubbles: true }));
#                 }
#             }
#         """, totp)

#         time.sleep(1)
#         try:
#             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
#         except:
#             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
#         current_url = driver.current_url
#         driver.quit()

#         if "request_token=" not in current_url:
#             return jsonify({"status": "error", "message": "Request token not found"})

#         request_token = current_url.split("request_token=")[1].split("&")[0]
#         data = kite.generate_session(request_token, api_secret=api_secret)
#         access_token = data["access_token"]

#         current_user["details"]["access_token"] = access_token
#         save_users(users)

#         return jsonify({
#             "status": "redirect",
#             "message": "Server connected successfully! Redirecting to dashboard...",
#             "redirect_url": url_for("dashboard_page")
#         })

#     except Exception as e:
#         app.logger.error(f"[start_server] Error: {e}")
#         return jsonify({"status": "error", "message": str(e)})

# # -------------------- DASHBOARD --------------------
# @app.route("/dashboard")
# def dashboard_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     details = current_user.get("details", {}) if current_user else {}

#     return render_template("dashboard.html", details=details)

# # -------------------- TRADE PAGE --------------------
# @app.route("/trade")
# def trade_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     try:
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     except:
#         trades = []

#     trade = next((t for t in trades if t["user"] == session["user"]), None)
#     instrument = trade["instrument"] if trade else ""
#     entry_time = trade["entry_time"] if trade else "9:15 AM"
#     exit_time = trade["exit_time"] if trade else "3:30 PM"
#     target = trade["target"] if trade else ""
#     stoploss = trade["stoploss"] if trade else ""

#     return render_template("trade.html",
#                            instrument=instrument,
#                            entry_time=entry_time,
#                            exit_time=exit_time,
#                            target=target,
#                            stoploss=stoploss)

# # -------------------- SAVE TRADE SETTINGS --------------------
# @app.route("/save_trade_settings", methods=["POST"])
# def save_trade_settings():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})

#     data = request.get_json(force=True)
#     instrument = data.get("instrument")
#     entry_time = data.get("entry_time")
#     exit_time = data.get("exit_time")
#     target = data.get("target")
#     stoploss = data.get("stoploss")

#     if os.path.exists(TRADE_FILE):
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     else:
#         trades = []

#     trades = [t for t in trades if t["user"] != session["user"]]
#     trades.append({
#         "user": session["user"],
#         "instrument": instrument,
#         "entry_time": entry_time,
#         "exit_time": exit_time,
#         "target": target,
#         "stoploss": stoploss,
#         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
#     })

#     with open(TRADE_FILE, "w") as f:
#         json.dump(trades, f, indent=4)

#     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument})")
#     return jsonify({
#         "status": "redirect",
#         "message": "Trade settings saved successfully!",
#         "redirect_url": url_for("terminal_page")
#     })

# # -------------------- GET TRADE LTP + MARGIN --------------------
# @app.route("/get_trade_ltp")
# def get_trade_ltp():
#     """Fetch LTP and margin info safely across all Kite API versions"""
#     if "user" not in session:
#         return jsonify({"instrument": None, "ltp": "Error", "margin": "--"})

#     try:
#         if os.path.exists(TRADE_FILE):
#             with open(TRADE_FILE, "r") as f:
#                 trades = json.load(f)
#             trade = next((t for t in trades if t["user"] == session["user"]), None)
#             instrument = trade["instrument"] if trade else "NIFTY"
#         else:
#             instrument = "NIFTY"

#         users = load_users()
#         current_user = next((u for u in users if u["email"] == session["user"]), None)
#         if not current_user:
#             return jsonify({"instrument": instrument, "ltp": "Error", "margin": "--"})

#         details = current_user.get("details", {})
#         api_key = details.get("api_key")
#         access_token = details.get("access_token")

#         if not api_key or not access_token:
#             return jsonify({"instrument": instrument, "ltp": "Error", "margin": "--"})

#         kite = KiteConnect(api_key=api_key)
#         kite.set_access_token(access_token)

#         ltp, _ = get_ltp_for_instrument(instrument, api_key, access_token)

#         # ✅ Fixed margin display
#         margin_display = "--"
#         try:
#             margin_data = kite.margins(segment="equity")
#             app.logger.debug(f"[MARGIN RAW DATA] {margin_data}")

#             # New logic to read correct keys
#             if isinstance(margin_data, dict):
#                 data = margin_data.get("available", {})
#                 cash = data.get("cash", 0)
#                 collateral = data.get("collateral", 0)
#                 live_balance = data.get("live_balance", 0)
#                 total = cash + collateral + live_balance
#                 margin_display = f"₹{total:,.2f}"
#             elif isinstance(margin_data, (int, float)):
#                 margin_display = f"₹{margin_data:,.2f}"

#         except Exception as e:
#             app.logger.warning(f"[MARGIN FAIL FIXED] {e}")
#             margin_display = "--"

#         return jsonify({
#             "instrument": instrument,
#             "ltp": ltp,
#             "margin": margin_display
#         })

#     except Exception as e:
#         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
#         return jsonify({"instrument": None, "ltp": "Error", "margin": "--"})

# # -------------------- TERMINAL PAGE --------------------
# @app.route("/terminal")
# def terminal_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("terminal.html")

# # -------------------- LOGOUT --------------------
# @app.route("/logout")
# def logout():
#     user = session.pop("user", None)
#     app.logger.info(f"User logged out: {user}")
#     return redirect(url_for("home"))

# print("✅ ROUTES LOADED:", [str(r) for r in app.url_map.iter_rules()])

# # -------------------- RUN APP --------------------
# if __name__ == "__main__":
#     app.logger.info("🚀 Flask server starting...")
#     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# import json, os, time, logging
# from kiteconnect import KiteConnect

# # -------------------- Logging Setup --------------------
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     handlers=[logging.StreamHandler()]
# )

# # ✅ Explicitly specify templates folder
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# app = Flask(__name__, template_folder=TEMPLATES_DIR)
# app.secret_key = "infocap_secret_2025"

# DATA_FILE = os.path.join(BASE_DIR, "users.json")
# TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

# # -------------------- Utility --------------------
# if not os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "w") as f:
#         json.dump([], f)

# if not os.path.exists(TRADE_FILE):
#     with open(TRADE_FILE, "w") as f:
#         json.dump([], f)

# def load_users():
#     with open(DATA_FILE, "r") as f:
#         return json.load(f)

# def save_users(users):
#     with open(DATA_FILE, "w") as f:
#         json.dump(users, f, indent=4)

# # ✅ Log every request
# @app.before_request
# def log_request():
#     app.logger.info(f"➡️ {request.method} {request.path}")

# # ✅ Utility: Get LTP for any instrument
# def get_ltp_for_instrument(instrument, api_key, access_token):
#     kite = KiteConnect(api_key=api_key)
#     kite.set_access_token(access_token)

#     instrument_map = {
#         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
#         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
#         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
#     }

#     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
#         try:
#             data = kite.ltp(sym)
#             price = list(data.values())[0]["last_price"]
#             app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
#             return price, sym
#         except Exception as e:
#             app.logger.warning(f"[LTP FAIL] {sym} → {e}")
#     return "Error", None

# # -------------------- LOGIN PAGE --------------------
# @app.route("/")
# def home():
#     app.logger.info("Rendering login page")
#     return render_template("login.html")

# # -------------------- SIGNUP --------------------
# @app.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json(force=True)
#     name, email, mobile, password = (
#         data.get("name"),
#         data.get("email"),
#         data.get("mobile"),
#         data.get("password"),
#     )
#     users = load_users()
#     if any(u["email"] == email for u in users):
#         return jsonify({"status": "error", "message": "Email already registered!"})

#     users.append({
#         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
#     })
#     save_users(users)
#     app.logger.info(f"New signup: {email}")
#     return jsonify({"status": "success", "message": "Signup successful!"})

# # -------------------- LOGIN --------------------
# @app.route("/login", methods=["POST"])
# def login():
#     data = request.get_json(force=True)
#     email = data.get("email")
#     password = data.get("password")

#     users = load_users()
#     for u in users:
#         if u["email"] == email and u["password"] == password:
#             session["user"] = email
#             if not u.get("details") or not u["details"].get("user_id"):
#                 return jsonify({
#                     "status": "redirect",
#                     "message": "First-time login. Please fill your broker details.",
#                     "redirect_url": url_for("details_page")
#                 })
#             return jsonify({
#                 "status": "redirect",
#                 "message": "Login successful!",
#                 "redirect_url": url_for("server_connect_page")
#             })
#     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # -------------------- USER DETAILS PAGE --------------------
# @app.route("/details")
# def details_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("user_details.html", user=session["user"])

# @app.route("/save_details", methods=["POST"])
# def save_details():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})
#     data = request.get_json(force=True)
#     users = load_users()
#     for u in users:
#         if u["email"] == session["user"]:
#             u["details"] = {
#                 "user_id": data.get("user_id"),
#                 "password": data.get("password"),
#                 "api_key": data.get("api_key"),
#                 "secret_key": data.get("secret_key"),
#                 "totp": data.get("totp"),
#                 "access_token": data.get("access_token", "")
#             }
#             save_users(users)
#             return jsonify({"status": "success", "message": "Details saved successfully!"})
#     return jsonify({"status": "error", "message": "User not found!"})

# # -------------------- SERVER CONNECT PAGE --------------------
# @app.route("/server_connect")
# def server_connect_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("server_connect.html")

# # -------------------- START SERVER --------------------
# @app.route("/start_server", methods=["POST"])
# def start_server():
#     from kiteconnect import KiteConnect
#     import pyotp
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.firefox.service import Service
#     from selenium.webdriver.firefox.options import Options
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     if not current_user or "details" not in current_user:
#         return jsonify({"status": "error", "message": "User details not found"})

#     d = current_user["details"]
#     user_id, password, api_key, api_secret, totp_secret = (
#         d.get("user_id"),
#         d.get("password"),
#         d.get("api_key"),
#         d.get("secret_key"),
#         d.get("totp"),
#     )

#     try:
#         gecko_path = os.path.join(BASE_DIR, "geckodriver.exe")
#         firefox_path = os.path.join(BASE_DIR, "Mozilla Firefox", "firefox.exe")
#         options = Options()
#         options.binary_location = firefox_path
#         service = Service(gecko_path)
#         driver = webdriver.Firefox(service=service, options=options)

#         kite = KiteConnect(api_key=api_key)
#         driver.get(kite.login_url())

#         WebDriverWait(driver, 25).until(
#             EC.visibility_of_element_located((By.ID, "userid"))
#         ).send_keys(user_id)
#         driver.find_element(By.ID, "password").send_keys(password)
#         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#         time.sleep(3)

#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
#         )

#         totp = pyotp.TOTP(totp_secret).now()
#         driver.execute_script("""
#             let boxes = document.querySelectorAll('input');
#             for (let i of boxes) {
#                 if (i.offsetParent !== null) {
#                     i.value = arguments[0];
#                     i.dispatchEvent(new Event('input', { bubbles: true }));
#                 }
#             }
#         """, totp)

#         time.sleep(1)
#         try:
#             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
#         except:
#             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
#         current_url = driver.current_url
#         driver.quit()

#         if "request_token=" not in current_url:
#             return jsonify({"status": "error", "message": "Request token not found"})

#         request_token = current_url.split("request_token=")[1].split("&")[0]
#         data = kite.generate_session(request_token, api_secret=api_secret)
#         access_token = data["access_token"]

#         current_user["details"]["access_token"] = access_token
#         save_users(users)

#         return jsonify({
#             "status": "redirect",
#             "message": "Server connected successfully! Redirecting to dashboard...",
#             "redirect_url": url_for("dashboard_page")
#         })

#     except Exception as e:
#         app.logger.error(f"[start_server] Error: {e}")
#         return jsonify({"status": "error", "message": str(e)})

# # -------------------- DASHBOARD --------------------
# @app.route("/dashboard")
# def dashboard_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     details = current_user.get("details", {}) if current_user else {}

#     return render_template("dashboard.html", details=details)

# # -------------------- TRADE PAGE --------------------
# @app.route("/trade")
# def trade_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     try:
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     except:
#         trades = []

#     trade = next((t for t in trades if t["user"] == session["user"]), None)
#     instrument = trade["instrument"] if trade else ""
#     entry_time = trade["entry_time"] if trade else "9:15 AM"
#     exit_time = trade["exit_time"] if trade else "3:30 PM"
#     target = trade["target"] if trade else ""
#     stoploss = trade["stoploss"] if trade else ""

#     return render_template("trade.html",
#                            instrument=instrument,
#                            entry_time=entry_time,
#                            exit_time=exit_time,
#                            target=target,
#                            stoploss=stoploss)

# # -------------------- SAVE TRADE SETTINGS --------------------
# @app.route("/save_trade_settings", methods=["POST"])
# def save_trade_settings():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})

#     data = request.get_json(force=True)
#     instrument = data.get("instrument")
#     company = data.get("company")  # ✅ added
#     entry_time = data.get("entry_time")
#     exit_time = data.get("exit_time")
#     target = data.get("target")
#     stoploss = data.get("stoploss")

#     if os.path.exists(TRADE_FILE):
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     else:
#         trades = []

#     trades = [t for t in trades if t["user"] != session["user"]]
#     trades.append({
#         "user": session["user"],
#         "instrument": instrument,
#         "company": company,  # ✅ added
#         "entry_time": entry_time,
#         "exit_time": exit_time,
#         "target": target,
#         "stoploss": stoploss,
#         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
#     })

#     with open(TRADE_FILE, "w") as f:
#         json.dump(trades, f, indent=4)

#     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument} - {company})")
#     return jsonify({
#         "status": "redirect",
#         "message": "Trade settings saved successfully!",
#         "redirect_url": url_for("terminal_page")
#     })

# # -------------------- GET TRADE LTP + MARGIN --------------------
# @app.route("/get_trade_ltp")
# def get_trade_ltp():
#     """Fetch LTP and margin info safely across all Kite API versions"""
#     if "user" not in session:
#         return jsonify({"instrument": None, "company": None, "ltp": "Error", "margin": "--"})

#     try:
#         if os.path.exists(TRADE_FILE):
#             with open(TRADE_FILE, "r") as f:
#                 trades = json.load(f)
#             trade = next((t for t in trades if t["user"] == session["user"]), None)
#             instrument = trade["instrument"] if trade else "NIFTY"
#             company = trade.get("company") if trade else None  # ✅ added
#         else:
#             instrument = "NIFTY"
#             company = None

#         users = load_users()
#         current_user = next((u for u in users if u["email"] == session["user"]), None)
#         if not current_user:
#             return jsonify({"instrument": instrument, "company": company, "ltp": "Error", "margin": "--"})

#         details = current_user.get("details", {})
#         api_key = details.get("api_key")
#         access_token = details.get("access_token")

#         if not api_key or not access_token:
#             return jsonify({"instrument": instrument, "company": company, "ltp": "Error", "margin": "--"})

#         kite = KiteConnect(api_key=api_key)
#         kite.set_access_token(access_token)

#         # ✅ Fetch company-specific LTP if selected
#         if company:
#             try:
#                 symbol = f"NSE:{company.upper()}"
#                 data = kite.ltp(symbol)
#                 ltp = list(data.values())[0]["last_price"]
#                 app.logger.info(f"[LTP SUCCESS] {symbol} = {ltp}")
#             except Exception as e:
#                 app.logger.warning(f"[LTP FAIL] {company} → {e}")
#                 ltp = "Error"
#         else:
#             ltp, _ = get_ltp_for_instrument(instrument, api_key, access_token)

#         # ✅ Fixed margin display
#         margin_display = "--"
#         try:
#             margin_data = kite.margins(segment="equity")
#             app.logger.debug(f"[MARGIN RAW DATA] {margin_data}")

#             if isinstance(margin_data, dict):
#                 data = margin_data.get("available", {})
#                 cash = data.get("cash", 0)
#                 collateral = data.get("collateral", 0)
#                 live_balance = data.get("live_balance", 0)
#                 total = cash + collateral + live_balance
#                 margin_display = f"₹{total:,.2f}"
#             elif isinstance(margin_data, (int, float)):
#                 margin_display = f"₹{margin_data:,.2f}"

#         except Exception as e:
#             app.logger.warning(f"[MARGIN FAIL FIXED] {e}")
#             margin_display = "--"

#         return jsonify({
#             "instrument": instrument,
#             "company": company,
#             "ltp": ltp,
#             "margin": margin_display
#         })

#     except Exception as e:
#         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
#         return jsonify({"instrument": None, "company": None, "ltp": "Error", "margin": "--"})

# # -------------------- GET SINGLE COMPANY LTP --------------------
# @app.route("/get_ltp")
# def get_ltp_single():
#     """Fetch LTP for a specific symbol (used for multi-company view)"""
#     symbol = request.args.get("symbol")
#     if not symbol:
#         return jsonify({"ltp": "--"})
#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session.get("user")), None)
#     if not current_user:
#         return jsonify({"ltp": "--"})
#     details = current_user.get("details", {})
#     api_key = details.get("api_key")
#     access_token = details.get("access_token")
#     try:
#         kite = KiteConnect(api_key=api_key)
#         kite.set_access_token(access_token)
#         data = kite.ltp(f"NSE:{symbol.upper()}")
#         ltp = list(data.values())[0]["last_price"]
#         return jsonify({"ltp": ltp})
#     except Exception as e:
#         app.logger.warning(f"[LTP ERROR] {symbol}: {e}")
#         return jsonify({"ltp": "--"})


# # -------------------- PLACE BUY/SELL ORDER --------------------
# @app.route("/place_order", methods=["POST"])
# def place_order():
#     """Handles Buy/Sell order placement"""
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Login required"})

#     data = request.get_json(force=True)
#     symbol = data.get("symbol")
#     side = data.get("side")

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     if not current_user:
#         return jsonify({"status": "error", "message": "User not found"})

#     details = current_user.get("details", {})
#     api_key = details.get("api_key")
#     access_token = details.get("access_token")

#     if not api_key or not access_token:
#         return jsonify({"status": "error", "message": "API key or access token missing"})

#     kite = KiteConnect(api_key=api_key)
#     kite.set_access_token(access_token)

#     try:
#         order = kite.place_order(
#             variety=kite.VARIETY_REGULAR,
#             exchange="NSE",
#             tradingsymbol=symbol.upper(),
#             transaction_type=kite.TRANSACTION_TYPE_BUY if side == "BUY" else kite.TRANSACTION_TYPE_SELL,
#             quantity=1,
#             order_type=kite.ORDER_TYPE_MARKET,
#             product=kite.PRODUCT_CNC
#         )
#         app.logger.info(f"[ORDER] {side} order placed for {symbol}")
#         return jsonify({"status": "success", "message": f"{side} order placed for {symbol}"})
#     except Exception as e:
#         app.logger.error(f"[ORDER ERROR] {symbol}: {e}")
#         return jsonify({"status": "error", "message": str(e)})


# # -------------------- TERMINAL PAGE --------------------
# @app.route("/terminal")
# def terminal_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("terminal.html")

# # -------------------- LOGOUT --------------------
# @app.route("/logout")
# def logout():
#     user = session.pop("user", None)
#     app.logger.info(f"User logged out: {user}")
#     return redirect(url_for("home"))

# print("✅ ROUTES LOADED:", [str(r) for r in app.url_map.iter_rules()])

# # -------------------- RUN APP --------------------
# if __name__ == "__main__":
#     app.logger.info("🚀 Flask server starting...")
#     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify, redirect, url_for, session
# import json, os, time, logging
# from kiteconnect import KiteConnect

# # -------------------- Logging Setup --------------------
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     handlers=[logging.StreamHandler()]
# )

# # ✅ Explicitly specify templates folder
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# app = Flask(__name__, template_folder=TEMPLATES_DIR)
# app.secret_key = "infocap_secret_2025"

# DATA_FILE = os.path.join(BASE_DIR, "users.json")
# TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

# # -------------------- Utility --------------------
# if not os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "w") as f:
#         json.dump([], f)

# if not os.path.exists(TRADE_FILE):
#     with open(TRADE_FILE, "w") as f:
#         json.dump([], f)

# def load_users():
#     with open(DATA_FILE, "r") as f:
#         return json.load(f)

# def save_users(users):
#     with open(DATA_FILE, "w") as f:
#         json.dump(users, f, indent=4)

# # ✅ Log every request
# @app.before_request
# def log_request():
#     app.logger.info(f"➡️ {request.method} {request.path}")

# # ✅ Utility: Get LTP for any instrument
# def get_ltp_for_instrument(instrument, api_key, access_token):
#     kite = KiteConnect(api_key=api_key)
#     kite.set_access_token(access_token)

#     instrument_map = {
#         "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
#         "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
#         "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
#     }

#     for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
#         try:
#             data = kite.ltp(sym)
#             price = list(data.values())[0]["last_price"]
#             app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
#             return price, sym
#         except Exception as e:
#             app.logger.warning(f"[LTP FAIL] {sym} → {e}")
#     return "Error", None

# # -------------------- LOGIN PAGE --------------------
# @app.route("/")
# def home():
#     app.logger.info("Rendering login page")
#     return render_template("login.html")

# # -------------------- SIGNUP --------------------
# @app.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json(force=True)
#     name, email, mobile, password = (
#         data.get("name"),
#         data.get("email"),
#         data.get("mobile"),
#         data.get("password"),
#     )
#     users = load_users()
#     if any(u["email"] == email for u in users):
#         return jsonify({"status": "error", "message": "Email already registered!"})

#     users.append({
#         "name": name, "email": email, "mobile": mobile, "password": password, "details": {}
#     })
#     save_users(users)
#     app.logger.info(f"New signup: {email}")
#     return jsonify({"status": "success", "message": "Signup successful!"})

# # -------------------- LOGIN --------------------
# @app.route("/login", methods=["POST"])
# def login():
#     data = request.get_json(force=True)
#     email = data.get("email")
#     password = data.get("password")

#     users = load_users()
#     for u in users:
#         if u["email"] == email and u["password"] == password:
#             session["user"] = email
#             if not u.get("details") or not u["details"].get("user_id"):
#                 return jsonify({
#                     "status": "redirect",
#                     "message": "First-time login. Please fill your broker details.",
#                     "redirect_url": url_for("details_page")
#                 })
#             return jsonify({
#                 "status": "redirect",
#                 "message": "Login successful!",
#                 "redirect_url": url_for("server_connect_page")
#             })
#     return jsonify({"status": "error", "message": "Invalid email or password!"})

# # -------------------- USER DETAILS PAGE --------------------
# @app.route("/details")
# def details_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("user_details.html", user=session["user"])

# @app.route("/save_details", methods=["POST"])
# def save_details():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})
#     data = request.get_json(force=True)
#     users = load_users()
#     for u in users:
#         if u["email"] == session["user"]:
#             u["details"] = {
#                 "user_id": data.get("user_id"),
#                 "password": data.get("password"),
#                 "api_key": data.get("api_key"),
#                 "secret_key": data.get("secret_key"),
#                 "totp": data.get("totp"),
#                 "access_token": data.get("access_token", "")
#             }
#             save_users(users)
#             return jsonify({"status": "success", "message": "Details saved successfully!"})
#     return jsonify({"status": "error", "message": "User not found!"})

# # -------------------- SERVER CONNECT PAGE --------------------
# @app.route("/server_connect")
# def server_connect_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("server_connect.html")

# # -------------------- START SERVER --------------------
# @app.route("/start_server", methods=["POST"])
# def start_server():
#     from kiteconnect import KiteConnect
#     import pyotp
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.firefox.service import Service
#     from selenium.webdriver.firefox.options import Options
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     if not current_user or "details" not in current_user:
#         return jsonify({"status": "error", "message": "User details not found"})

#     d = current_user["details"]
#     user_id, password, api_key, api_secret, totp_secret = (
#         d.get("user_id"),
#         d.get("password"),
#         d.get("api_key"),
#         d.get("secret_key"),
#         d.get("totp"),
#     )

#     try:
#         gecko_path = os.path.join(BASE_DIR, "geckodriver.exe")
#         firefox_path = os.path.join(BASE_DIR, "Mozilla Firefox", "firefox.exe")
#         options = Options()
#         options.binary_location = firefox_path
#         service = Service(gecko_path)
#         driver = webdriver.Firefox(service=service, options=options)

#         kite = KiteConnect(api_key=api_key)
#         driver.get(kite.login_url())

#         WebDriverWait(driver, 25).until(
#             EC.visibility_of_element_located((By.ID, "userid"))
#         ).send_keys(user_id)
#         driver.find_element(By.ID, "password").send_keys(password)
#         driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#         time.sleep(3)

#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
#         )

#         totp = pyotp.TOTP(totp_secret).now()
#         driver.execute_script("""
#             let boxes = document.querySelectorAll('input');
#             for (let i of boxes) {
#                 if (i.offsetParent !== null) {
#                     i.value = arguments[0];
#                     i.dispatchEvent(new Event('input', { bubbles: true }));
#                 }
#             }
#         """, totp)

#         time.sleep(1)
#         try:
#             driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
#         except:
#             driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#         WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
#         current_url = driver.current_url
#         driver.quit()

#         if "request_token=" not in current_url:
#             return jsonify({"status": "error", "message": "Request token not found"})

#         request_token = current_url.split("request_token=")[1].split("&")[0]
#         data = kite.generate_session(request_token, api_secret=api_secret)
#         access_token = data["access_token"]

#         current_user["details"]["access_token"] = access_token
#         save_users(users)

#         return jsonify({
#             "status": "redirect",
#             "message": "Server connected successfully! Redirecting to dashboard...",
#             "redirect_url": url_for("dashboard_page")
#         })

#     except Exception as e:
#         app.logger.error(f"[start_server] Error: {e}")
#         return jsonify({"status": "error", "message": str(e)})

# # -------------------- DASHBOARD --------------------
# @app.route("/dashboard")
# def dashboard_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     details = current_user.get("details", {}) if current_user else {}

#     return render_template("dashboard.html", details=details)

# # -------------------- TRADE PAGE --------------------
# @app.route("/trade")
# def trade_page():
#     if "user" not in session:
#         return redirect(url_for("home"))

#     try:
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     except:
#         trades = []

#     trade = next((t for t in trades if t["user"] == session["user"]), None)
#     instrument = trade["instrument"] if trade else ""
#     entry_time = trade["entry_time"] if trade else "9:15 AM"
#     exit_time = trade["exit_time"] if trade else "3:30 PM"
#     target = trade["target"] if trade else ""
#     stoploss = trade["stoploss"] if trade else ""
#     quantity = trade["quantity"] if trade else 1  # ✅ added

#     return render_template("trade.html",
#                            instrument=instrument,
#                            entry_time=entry_time,
#                            exit_time=exit_time,
#                            target=target,
#                            stoploss=stoploss,
#                            quantity=quantity)

# # -------------------- SAVE TRADE SETTINGS --------------------
# @app.route("/save_trade_settings", methods=["POST"])
# def save_trade_settings():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Not logged in"})

#     data = request.get_json(force=True)
#     instrument = data.get("instrument")
#     company = data.get("company")
#     quantity = int(data.get("quantity", 1))  # ✅ added
#     entry_time = data.get("entry_time")
#     exit_time = data.get("exit_time")
#     target = data.get("target")
#     stoploss = data.get("stoploss")

#     if os.path.exists(TRADE_FILE):
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#     else:
#         trades = []

#     trades = [t for t in trades if t["user"] != session["user"]]
#     trades.append({
#         "user": session["user"],
#         "instrument": instrument,
#         "company": company,
#         "quantity": quantity,  # ✅ added
#         "entry_time": entry_time,
#         "exit_time": exit_time,
#         "target": target,
#         "stoploss": stoploss,
#         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
#     })

#     with open(TRADE_FILE, "w") as f:
#         json.dump(trades, f, indent=4)

#     app.logger.info(f"[TRADE] Saved settings for {session['user']} ({instrument} - {company})")
#     return jsonify({
#         "status": "redirect",
#         "message": "Trade settings saved successfully!",
#         "redirect_url": url_for("terminal_page")
#     })

# # -------------------- GET TRADE LTP + MARGIN --------------------
# @app.route("/get_trade_ltp")
# def get_trade_ltp():
#     if "user" not in session:
#         return jsonify({"instrument": None, "company": None, "ltp": "Error", "margin": "--"})

#     try:
#         if os.path.exists(TRADE_FILE):
#             with open(TRADE_FILE, "r") as f:
#                 trades = json.load(f)
#             trade = next((t for t in trades if t["user"] == session["user"]), None)
#             instrument = trade["instrument"] if trade else "NIFTY"
#             company = trade.get("company") if trade else None
#             quantity = trade.get("quantity") if trade else 1  # ✅ added
#         else:
#             instrument = "NIFTY"
#             company = None
#             quantity = 1

#         users = load_users()
#         current_user = next((u for u in users if u["email"] == session["user"]), None)
#         if not current_user:
#             return jsonify({"instrument": instrument, "company": company, "ltp": "Error", "margin": "--"})

#         details = current_user.get("details", {})
#         api_key = details.get("api_key")
#         access_token = details.get("access_token")

#         if not api_key or not access_token:
#             return jsonify({"instrument": instrument, "company": company, "ltp": "Error", "margin": "--"})

#         kite = KiteConnect(api_key=api_key)
#         kite.set_access_token(access_token)

#         # ✅ Fetch company-specific LTP if selected
#         if company:
#             try:
#                 symbol = f"NSE:{company.upper()}"
#                 data = kite.ltp(symbol)
#                 ltp = list(data.values())[0]["last_price"]
#                 app.logger.info(f"[LTP SUCCESS] {symbol} = {ltp}")
#             except Exception as e:
#                 app.logger.warning(f"[LTP FAIL] {company} → {e}")
#                 ltp = "Error"
#         else:
#             ltp, _ = get_ltp_for_instrument(instrument, api_key, access_token)

#         # ✅ Margin display
#         margin_display = "--"
#         try:
#             margin_data = kite.margins(segment="equity")
#             app.logger.debug(f"[MARGIN RAW DATA] {margin_data}")

#             if isinstance(margin_data, dict):
#                 data = margin_data.get("available", {})
#                 cash = data.get("cash", 0)
#                 collateral = data.get("collateral", 0)
#                 live_balance = data.get("live_balance", 0)
#                 total = cash + collateral + live_balance
#                 margin_display = f"₹{total:,.2f}"
#             elif isinstance(margin_data, (int, float)):
#                 margin_display = f"₹{margin_data:,.2f}"

#         except Exception as e:
#             app.logger.warning(f"[MARGIN FAIL FIXED] {e}")
#             margin_display = "--"

#         return jsonify({
#             "instrument": instrument,
#             "company": company,
#             "quantity": quantity,  # ✅ added
#             "ltp": ltp,
#             "margin": margin_display
#         })

#     except Exception as e:
#         app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
#         return jsonify({"instrument": None, "company": None, "ltp": "Error", "margin": "--"})

# # -------------------- PLACE BUY/SELL ORDER --------------------
# @app.route("/place_order", methods=["POST"])
# def place_order():
#     if "user" not in session:
#         return jsonify({"status": "error", "message": "Login required"})

#     data = request.get_json(force=True)
#     symbol = data.get("symbol")
#     side = data.get("side")

#     users = load_users()
#     current_user = next((u for u in users if u["email"] == session["user"]), None)
#     if not current_user:
#         return jsonify({"status": "error", "message": "User not found"})

#     details = current_user.get("details", {})
#     api_key = details.get("api_key")
#     access_token = details.get("access_token")

#     if not api_key or not access_token:
#         return jsonify({"status": "error", "message": "API key or access token missing"})

#     kite = KiteConnect(api_key=api_key)
#     kite.set_access_token(access_token)

#     # ✅ Load saved trade quantity
#     try:
#         with open(TRADE_FILE, "r") as f:
#             trades = json.load(f)
#         user_trade = next((t for t in trades if t["user"] == session["user"]), None)
#         quantity = user_trade.get("quantity", 1) if user_trade else 1
#     except:
#         quantity = 1

#     try:
#         order = kite.place_order(
#             variety=kite.VARIETY_REGULAR,
#             exchange="NSE",
#             tradingsymbol=symbol.upper(),
#             transaction_type=kite.TRANSACTION_TYPE_BUY if side == "BUY" else kite.TRANSACTION_TYPE_SELL,
#             quantity=quantity,  # ✅ use saved qty
#             order_type=kite.ORDER_TYPE_MARKET,
#             product=kite.PRODUCT_MIS
#         )
#         app.logger.info(f"[ORDER] {side} order placed for {symbol} ({quantity})")
#         return jsonify({"status": "success", "message": f"{side} order placed for {symbol} ({quantity})"})
#     except Exception as e:
#         app.logger.error(f"[ORDER ERROR] {symbol}: {e}")
#         return jsonify({"status": "error", "message": str(e)})

# # -------------------- TERMINAL PAGE --------------------
# @app.route("/terminal")
# def terminal_page():
#     if "user" not in session:
#         return redirect(url_for("home"))
#     return render_template("terminal.html")

# # -------------------- LOGOUT --------------------
# @app.route("/logout")
# def logout():
#     user = session.pop("user", None)
#     app.logger.info(f"User logged out: {user}")
#     return redirect(url_for("home"))

# print("✅ ROUTES LOADED:", [str(r) for r in app.url_map.iter_rules()])

# # -------------------- RUN APP --------------------
# if __name__ == "__main__":
#     app.logger.info("🚀 Flask server starting...")
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS  
import json, os, time, logging
from datetime import datetime

import threading

from kiteconnect import KiteConnect

# -------------------- Logging Setup --------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# ✅ Explicitly specify templates folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATES_DIR)
CORS(app)

stop_monitor_flag = False   # ✅ Global flag to stop old monitor threads

app.secret_key = "infocap_secret_2025"

DATA_FILE = os.path.join(BASE_DIR, "users.json")
TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

# -------------------- Utility --------------------
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

if not os.path.exists(TRADE_FILE):
    with open(TRADE_FILE, "w") as f:
        json.dump([], f)

def load_users():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ✅ Log every request
@app.before_request
def log_request():
    app.logger.info(f"➡️ {request.method} {request.path}")

# ✅ Utility: Get LTP for any instrument
def get_ltp_for_instrument(instrument, api_key, access_token):
    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)

    instrument_map = {
        "NIFTY": ["NSE:NIFTY 50", "NSE:NIFTY"],
        "BANKNIFTY": ["NSE:NIFTY BANK", "NSE:NIFTYBANK"],
        "FINNIFTY": ["NSE:FINNIFTY", "NSE:FINNIFTY 50"]
    }

    for sym in instrument_map.get(instrument.upper(), ["NSE:NIFTY 50"]):
        try:
            data = kite.ltp(sym)
            price = list(data.values())[0]["last_price"]
            app.logger.info(f"[LTP SUCCESS] {sym} = {price}")
            return price, sym
        except Exception as e:
            app.logger.warning(f"[LTP FAIL] {sym} → {e}")
    return "Error", None

# -------------------- LOGIN PAGE --------------------
@app.route("/")
def home():
    app.logger.info("Rendering login page")
    return render_template("index.html")

# -------------------- SIGNUP --------------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True)
    name = data.get("name")
    email = data.get("email")
    mobile = data.get("mobile")
    password = data.get("password")
    role = data.get("role")  # ✅ new field

    users = load_users()
    if any(u["email"] == email for u in users):
        return jsonify({"status": "error", "message": "Email already registered!"})

    users.append({
        "name": name,
        "email": email,
        "mobile": mobile,
        "password": password,
        "role": role,  # ✅ store role
        "details": {}
    })
    save_users(users)
    app.logger.info(f"New signup: {email} as {role}")
    return jsonify({"status": "success", "message": f"Signup successful as {role}!"})

# -------------------- LOGIN --------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    email = data.get("email")
    password = data.get("password")

    users = load_users()
    for u in users:
        if u["email"] == email and u["password"] == password:
            session["user"] = email
            if not u.get("details") or not u["details"].get("user_id"):
                return jsonify({
                    "status": "redirect",
                    "message": "First-time login. Please fill your broker details.",
                    "redirect_url": url_for("details_page")
                })
            return jsonify({
                "status": "redirect",
                "message": "Login successful!",
                "redirect_url": url_for("server_connect_page")
            })
    return jsonify({"status": "error", "message": "Invalid email or password!"})

# -------------------- USER DETAILS PAGE --------------------
@app.route("/details")
def details_page():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("user_details.html", user=session["user"])

@app.route("/save_details", methods=["POST"])
def save_details():
    if "user" not in session:
        return jsonify({"status": "error", "message": "Not logged in"})
    data = request.get_json(force=True)
    users = load_users()
    for u in users:
        if u["email"] == session["user"]:
            u["details"] = {
                "user_id": data.get("user_id"),
                "password": data.get("password"),
                "api_key": data.get("api_key"),
                "secret_key": data.get("secret_key"),
                "totp": data.get("totp"),
                "access_token": data.get("access_token", "")
            }
            save_users(users)
            return jsonify({"status": "success", "message": "Details saved successfully!"})
    return jsonify({"status": "error", "message": "User not found!"})

# -------------------- SERVER CONNECT PAGE --------------------
@app.route("/server_connect")
def server_connect_page():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("server_connect.html")

# -------------------- START SERVER --------------------
@app.route("/start_server", methods=["POST"])
def start_server():
    from kiteconnect import KiteConnect
    import pyotp
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    users = load_users()
    current_user = next((u for u in users if u["email"] == session["user"]), None)
    if not current_user or "details" not in current_user:
        return jsonify({"status": "error", "message": "User details not found"})

    d = current_user["details"]
    user_id, password, api_key, api_secret, totp_secret = (
        d.get("user_id"),
        d.get("password"),
        d.get("api_key"),
        d.get("secret_key"),
        d.get("totp"),
    )

    try:
        gecko_path = os.path.join(BASE_DIR, "geckodriver.exe")
        firefox_path = os.path.join(BASE_DIR, "Mozilla Firefox", "firefox.exe")
        options = Options()
        options.binary_location = firefox_path
        service = Service(gecko_path)
        driver = webdriver.Firefox(service=service, options=options)

        kite = KiteConnect(api_key=api_key)
        driver.get(kite.login_url())

        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((By.ID, "userid"))
        ).send_keys(user_id)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'External TOTP')]"))
        )

        totp = pyotp.TOTP(totp_secret).now()
        driver.execute_script("""
            let boxes = document.querySelectorAll('input');
            for (let i of boxes) {
                if (i.offsetParent !== null) {
                    i.value = arguments[0];
                    i.dispatchEvent(new Event('input', { bubbles: true }));
                }
            }
        """, totp)

        time.sleep(1)
        try:
            driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
        except:
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        WebDriverWait(driver, 30).until(lambda d: "request_token=" in d.current_url)
        current_url = driver.current_url
        driver.quit()

        if "request_token=" not in current_url:
            return jsonify({"status": "error", "message": "Request token not found"})

        request_token = current_url.split("request_token=")[1].split("&")[0]
        data = kite.generate_session(request_token, api_secret=api_secret)
        access_token = data["access_token"]

        current_user["details"]["access_token"] = access_token
        save_users(users)

        return jsonify({
            "status": "redirect",
            "message": "Server connected successfully! Redirecting to dashboard...",
            "redirect_url": url_for("dashboard_page")
        })

    except Exception as e:
        app.logger.error(f"[start_server] Error: {e}")
        return jsonify({"status": "error", "message": str(e)})

# -------------------- DASHBOARD --------------------
# -------------------- DASHBOARD PAGE --------------------
@app.route("/dashboard")
def dashboard_page():
    if "user" not in session:
        return redirect(url_for("login_page"))

    users = load_users()
    current_user = next((u for u in users if u["email"] == session["user"]), None)

    if not current_user:
        return redirect(url_for("logout"))

    # ✅ Pass user's name and details to HTML
    user_name = current_user.get("name", "User")
    details = current_user.get("details", {})

    return render_template("dashboard.html", user=user_name, details=details)


# -------------------- TRADE PAGE --------------------
@app.route("/trade")
def trade_page():
    if "user" not in session:
        return redirect(url_for("home"))

    try:
        with open(TRADE_FILE, "r") as f:
            trades = json.load(f)
    except:
        trades = []

    trade = next((t for t in trades if t["user"] == session["user"]), None)

    instrument = trade["instrument"] if trade else ""
    entry_time = trade["entry_time"] if trade else "09:15:00"
    exit_time = trade["exit_time"] if trade else "15:30:00"
    target = trade["target"] if trade else ""
    stoploss = trade["stoploss"] if trade else ""
    quantity = trade["quantity"] if trade else 75   # default

    # ✅ override from trade_settings.json (latest admin update)
    try:
        trade_settings_file = os.path.join(BASE_DIR, "trade_settings.json")
        if os.path.exists(trade_settings_file):
            with open(trade_settings_file, "r") as f:
                trade_settings = json.load(f)
            for setting in trade_settings:
                if setting.get("user") == session["user"]:
                    quantity = setting.get("quantity", quantity)
                    break
    except Exception as e:
        app.logger.warning(f"[TRADE] Could not load trade_settings.json: {e}")

    app.logger.info(f"[TRADE PAGE] User={session['user']} Quantity={quantity}")

    return render_template(
        "trade.html",
        instrument=instrument,
        entry_time=entry_time,
        exit_time=exit_time,
        target=target,
        stoploss=stoploss,
        quantity=quantity
    )


# -------------------- SAVE TRADE SETTINGS --------------------
@app.route("/save_trade_settings", methods=["POST"])
def save_trade_settings():
    if "user" not in session:
        return jsonify({"status": "error", "message": "Not logged in"})

    data = request.get_json(force=True)
    segment = data.get("segment")  # ✅ NEW FIELD
    instrument = data.get("instrument")
    company = data.get("company")
    quantity = int(data.get("quantity", 1))
    entry_time = data.get("entry_time")
    exit_time = data.get("exit_time")

    # ✅ Convert target & stoploss to float
    try:
        target = float(data.get("target") or 0)
    except:
        target = 0.0
    try:
        stoploss = float(data.get("stoploss") or 0)
    except:
        stoploss = 0.0

    # ✅ Load existing trades
    if os.path.exists(TRADE_FILE):
        with open(TRADE_FILE, "r") as f:
            trades = json.load(f)
    else:
        trades = []

    # ✅ Remove old record for this user
    trades = [t for t in trades if t["user"] != session["user"]]

    # ✅ Append new record including numeric target/stoploss
    trades.append({
        "user": session["user"],
        "segment": segment,
        "instrument": instrument,
        "company": company,
        "quantity": quantity,
        "entry_time": entry_time,
        "exit_time": exit_time,
        "target": target,         # ✅ Stored as number
        "stoploss": stoploss,     # ✅ Stored as number
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    # ✅ Save to file
    with open(TRADE_FILE, "w") as f:
        json.dump(trades, f, indent=4)

    app.logger.info(f"[TRADE] Saved settings for {session['user']} ({segment} - {instrument} - {company})")

    return jsonify({
        "status": "redirect",
        "message": "Trade settings saved successfully!",
        "redirect_url": url_for("terminal_page")
    })
@app.route("/get_user_role")
def get_user_role():
    if "user" not in session:
        return jsonify({"role": None})
    users = load_users()
    user = next((u for u in users if u["email"] == session["user"]), None)
    role = user.get("role", "user") if user else "user"
    return jsonify({"role": role})

# -------------------- GET TRADE LTP + MARGIN --------------------
@app.route("/get_trade_ltp")
def get_trade_ltp():
    if "user" not in session:
        return jsonify({
            "instrument": None,
            "company": None,
            "ltp": "Error",
            "margin": "--",
            "status": "Not logged in"
        })

    try:
        # ✅ Load user trade data
        if os.path.exists(TRADE_FILE):
            with open(TRADE_FILE, "r") as f:
                trades = json.load(f)
            trade = next((t for t in trades if t["user"] == session["user"]), None)
            instrument = trade["instrument"] if trade else "NIFTY"
            company = trade.get("company") if trade else None
            quantity = trade.get("quantity") if trade else 1
            entry_time = trade.get("entry_time", "09:15:00")
            exit_time = trade.get("exit_time", "15:30:00")
        else:
            instrument, company, quantity = "NIFTY", None, 1
            entry_time, exit_time = "09:15:00", "15:30:00"

        # ✅ Time comparison logic
        now = datetime.now().strftime("%H:%M:%S")
        try:
            now_t = datetime.strptime(now, "%H:%M:%S").time()
            entry_t = datetime.strptime(entry_time, "%H:%M:%S").time()
            exit_t = datetime.strptime(exit_time, "%H:%M:%S").time()
        except Exception:
            # Fallback if time format is HH:MM only
            now_t = datetime.strptime(now, "%H:%M:%S").time()
            entry_t = datetime.strptime(entry_time, "%H:%M").time()
            exit_t = datetime.strptime(exit_time, "%H:%M").time()

        # 🕒 Before entry → waiting
        if now_t < entry_t:
            return jsonify({
                "instrument": instrument,
                "company": company,
                "ltp": "WAIT",
                "margin": "--",
                "status": "Waiting for entry time"
            })

        # 🕔 After exit → closed
        if now_t > exit_t:
            return jsonify({
                "instrument": instrument,
                "company": company,
                "ltp": "CLOSED",
                "margin": "--",
                "status": "Trading window closed"
            })

        # ✅ User auth
        users = load_users()
        current_user = next((u for u in users if u["email"] == session["user"]), None)
        if not current_user:
            return jsonify({
                "instrument": instrument,
                "company": company,
                "ltp": "Error",
                "margin": "--",
                "status": "User not found"
            })

        details = current_user.get("details", {})
        api_key = details.get("api_key")
        access_token = details.get("access_token")
        if not api_key or not access_token:
            return jsonify({
                "instrument": instrument,
                "company": company,
                "ltp": "Error",
                "margin": "--",
                "status": "API key or token missing"
            })

        kite = KiteConnect(api_key=api_key)
        kite.set_access_token(access_token)

        # ✅ Get LTP
        if company:
            try:
                symbol = f"NSE:{company.upper()}"
                data = kite.ltp(symbol)
                ltp = list(data.values())[0]["last_price"]
                app.logger.info(f"[LTP SUCCESS] {symbol} = {ltp}")
            except Exception as e:
                app.logger.warning(f"[LTP FAIL] {company} → {e}")
                ltp = "Error"
                symbol = company
        else:
            ltp, symbol = get_ltp_for_instrument(instrument, api_key, access_token)

        # ✅ Safe margin display
        margin_display = "--"
        try:
            margin_data = kite.margins(segment="equity")
            if isinstance(margin_data, dict):
                avail = margin_data.get("available", {})
                total = sum([
                    avail.get("cash", 0),
                    avail.get("collateral", 0),
                    avail.get("live_balance", 0)
                ])
                margin_display = f"₹{total:,.2f}"
        except Exception as e:
            app.logger.warning(f"[MARGIN FAIL FIXED] {e}")

        return jsonify({
            "instrument": instrument,
            "company": company,
            "quantity": quantity,
            "ltp": round(ltp, 2) if isinstance(ltp, (int, float)) else ltp,
            "symbol": symbol,
            "margin": margin_display,
            "status": "Active"
        })

    except Exception as e:
        app.logger.error(f"[TRADE] get_trade_ltp error: {e}")
        return jsonify({
            "instrument": None,
            "company": None,
            "ltp": "Error",
            "margin": "--",
            "status": "Error"
        })


# -------------------- PLACE BUY/SELL ORDER --------------------
# -------------------- PLACE BUY/SELL ORDER --------------------
@app.route("/place_order", methods=["POST"])
def place_order():
    global stop_monitor_flag  # ✅ ensure we use the global one
    if "user" not in session:
        return jsonify({"status": "error", "message": "Login required"})

    # ✅ STEP 1: stop old monitor & clear old log
    stop_monitor_flag = True
    time.sleep(0.5)
    stop_monitor_flag = False

    monitor_log_path = os.path.join(BASE_DIR, "monitor_log.json")
    try:
        with open(monitor_log_path, "w") as f:
            json.dump({"symbol": None, "status": None}, f)
        app.logger.info("[MONITOR LOG] Reset before new trade")
    except Exception as e:
        app.logger.warning(f"[MONITOR LOG RESET FAIL] {e}")

    # ✅ STEP 2: Load incoming data
    data = request.get_json(force=True)
    symbol = data.get("symbol")
    side = data.get("side")

    # ✅ Auto-load if missing
    if not symbol:
        try:
            with open(TRADE_FILE, "r") as f:
                trades = json.load(f)
            trade = next((t for t in trades if t["user"] == session["user"]), None)
            symbol = trade.get("company") if trade else None
        except:
            symbol = None
    if not symbol:
        return jsonify({"status": "error", "message": "No company selected for order"})

    users = load_users()
    current_user = next((u for u in users if u["email"] == session["user"]), None)
    if not current_user:
        return jsonify({"status": "error", "message": "User not found"})

    details = current_user.get("details", {})
    api_key = details.get("api_key")
    access_token = details.get("access_token")
    if not api_key or not access_token:
        return jsonify({"status": "error", "message": "API key or access token missing"})

    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)

    try:
        # ✅ Load trade settings
        with open(TRADE_FILE, "r") as f:
            trades = json.load(f)
        user_trade = next((t for t in trades if t["user"] == session["user"]), None)
        quantity = int(user_trade.get("quantity", 1)) if user_trade else 1
        entry_time = user_trade.get("entry_time", "")
        exit_time = user_trade.get("exit_time", "")
        target = float(user_trade.get("target") or 0)
        stoploss = float(user_trade.get("stoploss") or 0)
    except:
        quantity, entry_time, exit_time, target, stoploss = 1, "", "", 0, 0

    try:
        # ✅ Get LTP
        try:
            price_data = kite.ltp(f"NSE:{symbol.upper()}")
            current_price = list(price_data.values())[0]["last_price"]
        except Exception as e:
            app.logger.warning(f"[PRICE FETCH FAIL BEFORE ORDER] {e}")
            current_price = 0

        # ✅ Place order
        kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange="NSE",
            tradingsymbol=symbol.upper(),
            transaction_type=kite.TRANSACTION_TYPE_BUY if side == "BUY" else kite.TRANSACTION_TYPE_SELL,
            quantity=quantity,
            order_type=kite.ORDER_TYPE_MARKET,
            product=kite.PRODUCT_MIS
        )
        app.logger.info(f"[ORDER] {side} order placed for {symbol} ({quantity})")

        # ✅ Update entry price
        if side == "BUY":
            try:
                with open(TRADE_FILE, "r") as f:
                    trades = json.load(f)
                for t in trades:
                    if t["user"] == session["user"] and t["company"].upper() == symbol.upper():
                        t["entry_price"] = current_price
                        t["closed"] = False
                        break
                with open(TRADE_FILE, "w") as f:
                    json.dump(trades, f, indent=4)
                app.logger.info(f"[UPDATE] Entry price ₹{current_price} saved for {symbol}")
            except Exception as e:
                app.logger.warning(f"[UPDATE ENTRY PRICE FAIL] {e}")

        # ✅ Write CSV
        TRACK_FILE = os.path.join(BASE_DIR, "track_records.csv")
        record_exists = os.path.exists(TRACK_FILE)
        import csv
        with open(TRACK_FILE, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not record_exists:
                writer.writerow(["date", "user", "instrument", "side", "quantity",
                                 "entry_time", "exit_time", "entry_price", "exit_price", "ltp", "time"])
            now = time.strftime("%Y-%m-%d")
            current_time = time.strftime("%H:%M:%S")
            entry_price = current_price if side == "BUY" else ""
            exit_price = current_price if side == "SELL" else ""
            writer.writerow([now, session["user"], symbol.upper(), side, quantity,
                             entry_time, exit_time, entry_price, exit_price, current_price, current_time])

        app.logger.info(f"[TRACK] {side} {symbol} @ ₹{current_price}")

        # ✅ Auto-monitor for target/stoploss
        def auto_monitor(symbol, target, stoploss, quantity):
            try:
                kite_local = KiteConnect(api_key=api_key)
                kite_local.set_access_token(access_token)
                while True:
                    global stop_monitor_flag
                    if stop_monitor_flag:
                        app.logger.info(f"[MONITOR STOPPED] {symbol}")
                        break

                    # 🔄 Check latest price
                    price_data = kite_local.ltp(f"NSE:{symbol.upper()}")
                    ltp = list(price_data.values())[0]["last_price"]
                    app.logger.info(f"[MONITOR] {symbol} LTP ₹{ltp}")

                    # 🎯 Target Hit
                    if target > 0 and ltp >= target:
                        app.logger.info(f"[AUTO SELL] {symbol} Target ₹{ltp} hit")
                        kite_local.place_order(
                            variety=kite_local.VARIETY_REGULAR,
                            exchange="NSE",
                            tradingsymbol=symbol.upper(),
                            transaction_type=kite_local.TRANSACTION_TYPE_SELL,
                            quantity=quantity,
                            order_type=kite_local.ORDER_TYPE_MARKET,
                            product=kite_local.PRODUCT_MIS
                        )
                        log_data = {"symbol": symbol.upper(), "status": "Target Hit",
                                    "price": ltp, "time": time.strftime("%H:%M:%S"), "type": "target"}
                        with open("monitor_log.json", "w") as f:
                            json.dump(log_data, f, indent=4)
                        stop_monitor_flag = True  # ✅ stop immediately after target hit
                        break

                    # 🛑 Stoploss Hit
                    if stoploss > 0 and ltp <= stoploss:
                        app.logger.info(f"[AUTO SELL] {symbol} Stoploss ₹{ltp} hit")
                        kite_local.place_order(
                            variety=kite_local.VARIETY_REGULAR,
                            exchange="NSE",
                            tradingsymbol=symbol.upper(),
                            transaction_type=kite_local.TRANSACTION_TYPE_SELL,
                            quantity=quantity,
                            order_type=kite_local.ORDER_TYPE_MARKET,
                            product=kite_local.PRODUCT_MIS
                        )
                        log_data = {"symbol": symbol.upper(), "status": "Stoploss Hit",
                                    "price": ltp, "time": time.strftime("%H:%M:%S"), "type": "stoploss"}
                        with open("monitor_log.json", "w") as f:
                            json.dump(log_data, f, indent=4)
                        stop_monitor_flag = True  # ✅ stop immediately after SL hit
                        break

                    time.sleep(1)
            except Exception as e:
                app.logger.error(f"[AUTO MONITOR ERROR] {symbol}: {e}")

        # ✅ Start monitoring only for BUY orders
        if side == "BUY":
            threading.Thread(target=auto_monitor,
                             args=(symbol, target, stoploss, quantity),
                             daemon=True).start()

        return jsonify({"status": "success",
                        "message": f"{side} order placed for {symbol} ({quantity})",
                        "ltp": current_price})

    except Exception as e:
        app.logger.error(f"[ORDER ERROR] {symbol}: {e}")
        return jsonify({"status": "error", "message": str(e)})


@app.route("/monitor_status")
def monitor_status():
    log_path = os.path.join(BASE_DIR, "monitor_log.json")
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            data = json.load(f)

        # ✅ Clear the log immediately after sending it to frontend
        with open(log_path, "w") as f:
            json.dump({"symbol": None, "status": None}, f)

        return jsonify(data)
    else:
        return jsonify({"symbol": None, "status": None})
# ========== ADMIN PANEL ==========

def load_users():
    import json
    with open("users.json", "r") as f:
        return json.load(f)

def save_users(data):
    import json
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)


@app.route("/admin_panel")
def admin_panel():
    if "user" not in session:
        return redirect(url_for("login_page"))

    users = load_users()
    current_user = next((u for u in users if u["email"] == session["user"]), None)

    # Only Admin can open this
    if not current_user or current_user.get("role").lower() != "admin":
        return "Access Denied. Only Admins can view this page.", 403

    # Give all traders default quantity if missing
    for u in users:
        if u["role"].lower() == "trader" and "default_quantity" not in u:
            u["default_quantity"] = 75
    save_users(users)

    return render_template("admin_panel.html", users=users)


# -------------------- ADMIN UPDATE QUANTITY --------------------
@app.route("/update_quantity", methods=["POST"])
def update_quantity():
    if not session.get("admin"):
        return jsonify({"status": "error", "message": "Access Denied"})

    data = request.get_json()
    email = data.get("email")
    qty = int(data.get("qty", 0))

    # ✅ Load trade_settings.json
    TRADE_FILE = os.path.join(BASE_DIR, "trade_settings.json")

    if not os.path.exists(TRADE_FILE):
        return jsonify({"status": "error", "message": "Trade file missing"})

    try:
        with open(TRADE_FILE, "r") as f:
            trades = json.load(f)
    except Exception as e:
        return jsonify({"status": "error", "message": f"Read error: {e}"})

    # ✅ Find trader entry
    updated = False
    for trade in trades:
        if trade.get("user") == email:
            trade["quantity"] = qty
            updated = True
            break

    if not updated:
        # if not found, create a new record for that trader
        trades.append({
            "user": email,
            "quantity": qty
        })

    # ✅ Save back to trade_settings.json
    try:
        with open(TRADE_FILE, "w") as f:
            json.dump(trades, f, indent=4)
        return jsonify({"status": "success", "message": f"✅ Quantity updated to {qty} for {email}"})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Write error: {e}"})


@app.route("/get_trader_quantity")
def get_trader_quantity():
    if "user" not in session:
        return jsonify({"quantity": 75})
    users = load_users()
    user = next((u for u in users if u["email"] == session["user"]), None)
    qty = user.get("default_quantity", 75) if user else 75
    return jsonify({"quantity": qty})

# -------------------- ADMIN LOGIN SYSTEM --------------------

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # ✅ Load users.json
    users = load_users()

    admin_user = next(
        (u for u in users if u.get("email") == email and u.get("password") == password and u.get("role").lower() == "admin"),
        None
    )

    if admin_user:
        session["admin"] = True
        session["admin_email"] = admin_user["email"]
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Invalid admin credentials"})

@app.route("/secure_admin_panel")
def secure_admin_panel():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    users = load_users()

    # ✅ Load live trade quantities
    try:
        with open(TRADE_FILE, "r") as f:
            trade_data = json.load(f)
    except:
        trade_data = []

    # ✅ Merge live quantities into user list
    for u in users:
        if u.get("role", "").lower() == "trader":
            trade_entry = next((t for t in trade_data if t.get("user") == u.get("email")), None)
            if trade_entry:
                u["default_quantity"] = trade_entry.get("quantity", 75)
            else:
                u["default_quantity"] = 75  # fallback

    return render_template("admin_panel.html", users=users)


@app.route("/admin_logout")
def admin_logout():
    session.pop("admin", None)
    session.pop("admin_email", None)
    return redirect(url_for("admin_login"))


# -------------------- TERMINAL PAGE --------------------
@app.route("/terminal")
def terminal_page():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("terminal.html")

# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    user = session.pop("user", None)
    app.logger.info(f"User logged out: {user}")
    return redirect(url_for("home"))

print("✅ ROUTES LOADED:", [str(r) for r in app.url_map.iter_rules()])

# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.logger.info("🚀 Flask server starting...")
    app.run(debug=True)
