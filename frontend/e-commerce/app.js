// cardEL = document.querySelector('.card')
const priceEl  = document.querySelectorAll('.price'),
titleEl = document.querySelectorAll('.card-title'),
categoryEl = document.querySelectorAll('.category'),
descriptionEl = document.querySelectorAll('.description'),
imgEl = document.querySelectorAll('.card-img-top'),
cardsEl = document.querySelector('.cards');
// console.log(cardsEl)


// Assign the URL into a variable 
const url = 'https://dummyjson.com/products/'

// function to return data from the API
async function getData(){
    // retrieve API data 
    const response = await fetch(url);

    // convert API data to JSON
    const productsData = await response.json();
    // console.log(productData.products);

    return productsData;


}

async function populatePage(){
    const productsData = await getData();
    // console.log(productsData);

    // populate the card content with the products data
    
    //  iterator that circles through the array
    let index;

    let products = productsData.products
    let contentArea = "";
    let currency = '$';
    for (index=0; index<products.length;index++){
        contentArea += `
            <div class="card">
            <div class="card-body">
                <h5 class="card-title">${products[index].title}</h5>
                <img class="card-img-top" src=${products[index].images[0]} alt="Card image cap">
                <p class="description">${'Description: ' + products[index].description}</p>
                <p class="category">${'Category: ' + products[index].category}</p>
                <p class="price">${'Price: ' + currency + products[index].price}</p>
                <p class="rating">${'Ratings: ' +  products[index].rating}</p>
                <div class="small-font">
                    <a id='description-link' href="index.html">Learn more</a>
                </div>
            </div>
        </div>
        `;
    }
        
    // Append the contents into the card
    cardsEl.innerHTML = contentArea;


        // productsData.products.forEach(product =>{
        // console.log(product.price);
        // titleEl[index].textContent = product.title;
        // priceEl[index].textContent = 'Price: ' + product.price;
        // categoryEl[index].textContent = 'Category: ' + product.category;
        // descriptionEl[index].textContent = 'Description: ' + product.description;
        // imgEl[index].style.backgroundImage = product.images[0];

        // index++;
    // });


}


populatePage()

async function getDetails(){
    const productsData = await getData();
    let index = 0;
    productsData.products.forEach(product =>{
        // console.log(product.description);
        // query the button element 
        // return product.description;
//     const descriptionLink = document.getElementById('description-link')

// // // Attach a click event listener to the link
//     descriptionLink.addEventListener('click',function(event){
//         event.preventDefault();
//     })
// 

        // console.log(product.description);
        index++;


    })

}

getDetails()
// add event listener to the description link 
// get the reference to the link element
const descriptionLink = document.getElementById('description-link')

// // Attach a click event listener to the link
descriptionLink.addEventListener('click',getDetails)
// 
