const API_URL = "http://localhost:5000/api/books";

let editingId = null;

// Carregar livros
async function loadBooks() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("Erro ao carregar livros");
    const books = await response.json();

    const tbody = document.querySelector("#booksTable tbody");
    tbody.innerHTML = ""; // limpa antes de preencher

    books.forEach((book) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${book.id}</td>
        <td>${book.title}</td>
        <td>${book.author || "Desconhecido"}</td>
        <td>${book.pages || 0}</td>
        <td>
          <button onclick="editBook(${book.id}, '${book.title}', '${book.author}', ${book.pages})">✏️ Editar</button>
          <button onclick="deleteBook(${book.id})">🗑️ Excluir</button>
        </td>
      `;
      tbody.appendChild(tr);
    });
  } catch (err) {
    console.error("Erro:", err);
  }
}

// Adicionar/Editar livro
document.querySelector("#bookForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = document.querySelector("#title").value;
  const author = document.querySelector("#author").value;
  const pages = parseInt(document.querySelector("#pages").value, 10);

  try {
    if (editingId) {
      // PUT
      const response = await fetch(`${API_URL}/${editingId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, author, pages }),
      });
      if (!response.ok) throw new Error("Erro ao atualizar livro");
      editingId = null;
      document.querySelector("#formTitle").innerText = "Adicionar Novo Livro";
      document.querySelector("#cancelEdit").style.display = "none";
    } else {
      // POST
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, author, pages }),
      });
      if (!response.ok) throw new Error("Erro ao adicionar livro");
    }

    // resetar campos
    document.querySelector("#bookForm").reset();
    loadBooks(); // recarrega tabela
  } catch (err) {
    console.error("Erro:", err);
  }
});

// Cancelar edição
document.querySelector("#cancelEdit").addEventListener("click", () => {
  editingId = null;
  document.querySelector("#bookForm").reset();
  document.querySelector("#formTitle").innerText = "Adicionar Novo Livro";
  document.querySelector("#cancelEdit").style.display = "none";
});

// Editar livro
function editBook(id, title, author, pages) {
  editingId = id;
  document.querySelector("#title").value = title;
  document.querySelector("#author").value = author;
  document.querySelector("#pages").value = pages;
  document.querySelector("#formTitle").innerText = "Editar Livro";
  document.querySelector("#cancelEdit").style.display = "inline";
}

// Excluir livro
async function deleteBook(id) {
  if (!confirm("Tem certeza que deseja excluir este livro?")) return;
  try {
    const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    if (!response.ok) throw new Error("Erro ao excluir livro");
    loadBooks();
  } catch (err) {
    console.error("Erro:", err);
  }
}

// carregar lista ao abrir
loadBooks();
