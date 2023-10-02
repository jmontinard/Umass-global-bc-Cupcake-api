const url = "http://localhost:5000/api"

// make the html markup for cupcakes

function createCupcakeHtml(cupcake){
    return `
    <div data-cupcake-id=${cupcake.id}>
    <li class="list-group-item" >
      ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
      <button class="delete-button btn btn-danger">X</button>
    </li>
    <img class="Cupcake-img"
          src="${cupcake.image}"
          alt="(no image provided)">
  </div>
    `
}


// display our first cupcakes

async function displayCupcakes(){
    const res = await axios.get(`${url}/cupcakes`)

    for(let data of res.data.cupcake){
    let cupcake = $(createCupcakeHtml(data))
    $("#cupcakes-list").append(cupcake)
    }
}


// our form handling function
async function handleFormSubmit(e){
e.preventDefault();

let flavor = $("#form-flavor").val();
let rating = $("#form-rating").val();
let size = $("#form-size").val();
let image = $("#form-image").val();

const res = await axios.post(`${url}/cupcakes`, {flavor,rating,size,image})
let cupcake = $(createCupcakeHtml(res.data.cupcake))
$("#cupcakes-list").append(cupcake)
$("#new-cupcake-form").trigger("reset");
}

$("#new-cupcake-form").on("submit", handleFormSubmit)

// handle delete func
async function handleDelete(e){
    e.preventDefault();
    let $cupcake = $(e.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
    await axios.delete(`${url}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
} 
$("#cupcakes-list").on("click",".delete-button",handleDelete)
$(displayCupcakes)

