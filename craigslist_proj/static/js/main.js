console.log('Hello World')
function saveCategory(){
    category = document.getElementById("newCategory").value

    axios.post("", {category : category}).then((response) => {
        window.location.href = "../"
    })
}

function savePost(){
    title = document.getElementById("newTitle").value
    price = document.getElementById("newPrice").value
    description = document.getElementById("newDescription").value
    axios.post("", {title : title, price : price, description : description }).then((response) => {
        window.location.href = "../../../"
    })
    console.log('third')
}