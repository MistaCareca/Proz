const tituloElement = document.getElementById('titulo');
const listaNaoOrdenadaElement = document.querySelector('ul');
const linkElement = document.querySelector('a');
const listaOrdenadaElement = document.getElementById('lista-ordenada');

tituloElement.innerText = 'Título da Página';
linkElement.innerText = 'Visite a ProZ Educação';

listaNaoOrdenadaElement.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>`;

listaOrdenadaElement.innerHTML = `
    <li><a href="https://www.google.com">Google</a></li>
    <li><a href="https://www.youtube.com">YouTube</a></li>
    <li><a href="https://www.github.com">GitHub</a></li>`;