const API_URL = "http://localhost:5000/api/books";

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
      `;
      tbody.appendChild(tr);
    });
  } catch (err) {
    console.error("Erro:", err);
  }
}

// Adicionar livro
document.querySelector("#bookForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = document.querySelector("#title").value;
  const author = document.querySelector("#author").value;
  const pages = parseInt(document.querySelector("#pages").value, 10);

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, author, pages }),
    });

    if (!response.ok) throw new Error("Erro ao adicionar livro");

    document.querySelector("#title").value = "";
    document.querySelector("#author").value = "";
    document.querySelector("#pages").value = "";

    loadBooks(); // recarrega tabela
  } catch (err) {
    console.error("Erro:", err);
  }
});

// carregar lista ao abrir
loadBooks();
