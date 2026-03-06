import re

with open('app.js', 'r') as f:
    app_js = f.read()

# Fix the auth state change logic. Right now, checkSession() and onAuthStateChange might race and cause double initialization or hanging state.

old_auth_logic = r"""async function checkSession\(\) \{.*?\}\);"""

new_auth_logic = """async function checkSession() {
    if (!supabaseClient) { return mostrarLogin(); }
    try {
        const result = await supabaseClient.auth.getSession();
        if (result.error) throw result.error;
        const session = result.data.session;
        if (session) {
            await initializeUser(session.user);
        } else {
            mostrarLogin();
        }
    } catch (e) {
        console.error("Supabase no configurado o falló:", e);
        mostrarLogin();
        return;
    }
}

if (supabaseClient) supabaseClient.auth.onAuthStateChange(async (event, session) => {
    if (event === 'SIGNED_IN') {
        // Only initialize if not already initialized
        if (!State.user || State.user.id !== session.user.id) {
            await initializeUser(session.user);
        }
    } else if (event === 'SIGNED_OUT') {
        State.user = null;
        State.profile = null;
        mostrarLogin();
    }
});"""

app_js = re.sub(old_auth_logic, new_auth_logic, app_js, flags=re.DOTALL)

with open('app.js', 'w') as f:
    f.write(app_js)
