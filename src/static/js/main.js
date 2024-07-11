const aboutHeader = document.getElementById("aboutHeader")

if (aboutHeader){
    setInterval(() => {
        aboutHeader.style.color = '#' + Math.floor(Math.random()*16777215).toString(16);
    }, 3000);
}

// ----------------------------------------------------------------

function confirmDelete() {
    const ok = confirm("Are you sure you want to delete this product?");
    if (!ok) event.preventDefault();
}

const messagedDiv = document.querySelector(".messages");

if (messagedDiv) {
    setTimeout(() => {
        // messagedDiv.parentNode.removeChild(messagedDiv);
        messagedDiv.style.display = "none";
    }, 4000);
}

// ----------------------------------------------------------------

async function showProductList() {

    const url = "http://127.0.0.1:8000/api/products";
    const products = await getJson(url);
    
    let html = `
        <table class="table table-hover table-bordered">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Stock</th>
                    <th>Release Date</th>
                </tr>
            </thead>
            <tbody>
    `;

    for(const p of products) {
        html += `
            <tr>
                <td>${p.name}</td>
                <td>${p.price}</td>
                <td>${p.stock}</td>
                <td>${p.release_date}</td>
            </tr>
        `;
    }

    html += `
            </tbody>
        </table>    
    `;

    const containerDiv = document.getElementById("containerDiv");
    containerDiv.innerHTML = html;
}

async function getJson(url) {
    const response = await fetch(url);
    const json = await response.json();
    return json
}