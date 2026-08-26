const container = document.getElementById('cards');

async function loadUsers() {
  try {
    const res = await fetch('http://localhost:8000/api/users?limit=9');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const users = await res.json();
    render(users);
  } catch (err) {
    container.innerHTML = `<p class="error">No se pudo conectar con la API en localhost:8000. ¿Está corriendo? (${err.message})</p>`;
  }
}

function render(users) {
  container.innerHTML = users
    .map(
      (user) => `
        <article class="card">
          <img src="${user.avatar_url}" alt="${user.name}" />
          <h3>${user.name}</h3>
          <p class="job">${user.job_title}</p>
          <p class="company">${user.company}</p>
        </article>
      `
    )
    .join('');
}

loadUsers();
