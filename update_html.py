import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove the top nav-menu
content = re.sub(r'<nav id="navMenu".*?</nav>', '', content, flags=re.DOTALL)

# Add the bottom navigation just before the closing </body> tag
bottom_nav = """
    <!-- Bottom Navigation Bar (Mobile) -->
    <nav id="navMenu" class="bottom-nav" style="display: none;">
        <button class="nav-btn active" data-target="vistaRegistro">
            <span class="nav-icon">📝</span>
            <span class="nav-text">Registro</span>
        </button>
        <button class="nav-btn" data-target="vistaDashboard" id="btnNavDashboard" style="display: none;">
            <span class="nav-icon">📊</span>
            <span class="nav-text">Equipo</span>
        </button>
        <button class="nav-btn" data-target="vistaCatalogos" id="btnNavCatalogos" style="display: none;">
            <span class="nav-icon">📁</span>
            <span class="nav-text">Catálogos</span>
        </button>
    </nav>
"""

content = content.replace('</body>', bottom_nav + '\n</body>')

with open('index.html', 'w') as f:
    f.write(content)
