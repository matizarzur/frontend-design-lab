/* ejemplo-02 — interacciones de la landing "Cauce" */

const STORAGE_KEY = 'cauce-theme';
const root = document.documentElement;

/* ---------- Tema claro / oscuro ---------- */
function applyTheme(theme) {
  root.setAttribute('data-theme', theme);
  const btn = document.getElementById('theme-toggle');
  if (btn) {
    btn.setAttribute('aria-label', theme === 'dark' ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro');
  }
}

function currentTheme() {
  return root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
}

document.getElementById('theme-toggle')?.addEventListener('click', () => {
  const next = currentTheme() === 'dark' ? 'light' : 'dark';
  applyTheme(next);
  try {
    localStorage.setItem(STORAGE_KEY, next);
  } catch (e) {
    /* modo privado o storage bloqueado: el cambio vale solo para esta sesión */
  }
});

// Sincroniza el aria-label con lo que el script del <head> ya dejó aplicado.
applyTheme(currentTheme());

/* ---------- FAQ: una sola respuesta abierta a la vez ---------- */
const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach((item) => {
  item.addEventListener('toggle', () => {
    if (!item.open) return;
    faqItems.forEach((other) => {
      if (other !== item) other.open = false;
    });
  });
});

/* ---------- Formulario de demo (maqueta, no envía nada) ---------- */
document.querySelector('.cta-form')?.addEventListener('submit', (event) => {
  event.preventDefault();
  const input = event.currentTarget.querySelector('input[type="email"]');
  const legal = event.currentTarget.querySelector('.cta-legal');
  if (!input || !legal) return;

  if (!input.value.includes('@')) {
    legal.textContent = 'Ingresá un email válido para continuar.';
    input.focus();
    return;
  }

  legal.textContent = `Listo — te escribimos a ${input.value} dentro de las 24 h hábiles.`;
  input.value = '';
});
