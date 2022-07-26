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

}

function editPost(){
    title = document.getElementById("newTitle").value
    price = document.getElementById("newPrice").value
    description = document.getElementById("newDescription").value
    axios.put("", {title : title, price : price, description : description }).then((response) => {
        window.location.href = "../../../../"
    })

}

function deletePost(){
    
    post_id = document.getElementById("newTitle").value
    axios.post("", {post_id:post_id }).then((response) => {
        window.location.href = "../../"
    })
    console.log(post_id)

}
function deleteCategory(category_id){
    category_id = document.getElementById("delete_cat").value;
    axios.post("", {category_id:category_id }).then((response) => {
        window.location.href = "../../"
    })

    console.log('Deleted')
}
function editCategory(){
    name = document.getElementById("newName").value
    console.log(name)
    axios.put("", {name:name }).then((response) => {
        window.location.href = "../../"
    })

    console.log('Deleted')
}