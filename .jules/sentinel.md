## 2024-05-14 - XSS Sanitization in Dashboard Rendering
**Learning:** Data fetched from a database (even if previously validated) should always be treated as untrusted when rendering it into HTML via `.innerHTML`. Unsanitized fields like `profiles.first_name` could lead to Stored XSS if compromised.
**Action:** Enforced the strict use of the `escapeHTML()` utility when building string templates for the `tablaAuditoria` in `renderizarTablaAuditoria`, ensuring all dynamic string fields fetched from Supabase are safely encoded.

## 2026-03-05 - Infinite Recursion in Supabase RLS Policies
**Learning:** Using the current table inside a policy on that same table (e.g., `department = profiles.department` inside `profiles` policy) can easily trigger an infinite recursion error.
**Action:** Replaced the direct recursive query with `SECURITY DEFINER` functions (`get_my_role` and `get_my_department`) that bypass RLS to lookup the current user's profile information without triggering the policy again.
