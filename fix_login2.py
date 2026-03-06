import re

with open('app.js', 'r') as f:
    app_js = f.read()

# Make sure error initializing profile also triggers mostrarLogin() so they don't get stuck in WSOD

old_catch = r"""    \} catch \(err\) \{
        console\.error\("Error initializing user profile:", err\.message\);
        // Fallback or error state
    \}"""

new_catch = """    } catch (err) {
        console.error("Error initializing user profile:", err.message);
        alert("Error de sesión: " + err.message);
        mostrarLogin();
    }"""

app_js = re.sub(old_catch, new_catch, app_js, flags=re.DOTALL)

with open('app.js', 'w') as f:
    f.write(app_js)
