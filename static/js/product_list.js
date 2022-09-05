const categoryFilter = {
  url: `${location.origin}/api/products/`,

  filterProduct(categoryId) {
    let url = this.url;
    if (categoryId) {
      url += `?categoryId=${categoryId}`;
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('products-list').innerHTML = ''
      for (let i in data) {;
        for (let x in data[i].category) {
          if (data[i]['category'][x] == categoryId || data[i]['p_category'] == categoryId) {
            document.getElementById('products-list').innerHTML += `
            <li class="item first">
              <div class="product-image"> <a href="/product/${data[i].id}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
              <div class="product-shop">
                <h2 class="product-name"><a href="/product/${data[i].id}" title="HTC Rhyme Sense">${data[i]['name']}</a></h2>
                <div class="desc std">
                  <p>${data[i]['overview']}</p>
                </div>
                <div class="price-box"> 
                  <p class="special-price"> <span class="price-label"></span> <span class="price"> ${data[i]['price'].toFixed(2)}</span> </p>
                </div>
                <div class="actions">
                <button class="button btn-cart ajx-cart" title="Add to Cart" type="button" data="${data[i].id}"><span data="${data[i].id}">Add to Cart</span></button>
                <span class="add-to-links"> <a title="Add to Wishlist" class="button link-wishlist" href="#" data="${data[i].id}"><span data="${data[i].id}">Add to Wishlist</span></a> </span> </div>
              </div>
            </li>
            `
          }
        }
      }
    })
  }
}

let filterCategory = document.getElementsByClassName('category-field');
for (let i = 0; i < filterCategory.length; i++) {
  filterCategory[i].onclick = function () {
    const categoryId = this.getAttribute('data');
    categoryFilter.filterProduct(categoryId);
  }
}

const manufacturerFilter = {
  url: `${location.origin}/api/products/`,

  filterManufacturerProduct(manufacturerId) {
    let url = this.url;
    if (manufacturerId) {
      url += `?manufacturer=${manufacturerId}`;
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('products-list').innerHTML = ''
      for (let i in data) {
          if (data[i]['manufacturer'] == manufacturerId) {
            document.getElementById('products-list').innerHTML += `
            <li class="item first">
              <div class="product-image"> <a href="/product/${data[i].id}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
              <div class="product-shop">
                <h2 class="product-name"><a href="/product/${data[i].id}" title="HTC Rhyme Sense">${data[i]['name']}</a></h2>
                <div class="desc std">
                  <p>${data[i]['overview']}</p>
                </div>
                <div class="price-box"> 
                  <p class="special-price"> <span class="price-label"></span> <span class="price"> ${data[i]['price'].toFixed(2)}</span> </p>
                </div>
                <div class="actions">
                  <button class="button btn-cart ajx-cart" title="Add to Cart" type="button"><span>Add to Cart</span></button>
                  <span class="add-to-links"> <a title="Add to Wishlist" class="button link-wishlist" href="#" data="${data[i].id}"><span data="${data[i].id}">Add to Wishlist</span></a> </span> </div>
              </div>
            </li>
            `
        }
      }
    })
}}

let filterManufacturer = document.getElementsByClassName('manufacturer-category');
for (let i = 0; i < filterManufacturer.length; i++) {
  filterManufacturer[i].onclick = function () {
    const ManufacturerId = this.getAttribute('data');
    manufacturerFilter.filterManufacturerProduct(ManufacturerId);
  }
}

const colorFilter = {
  url: `${location.origin}/api/product_versions/`,

  filterColorProduct(ColorId) {
    let url = this.url;
    if (ColorId) {
      url += `?color=${ColorId}`;
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('products-list').innerHTML = ''
      for (let i in data) {
          if (data[i]['color'] == ColorId) {
            document.getElementById('products-list').innerHTML += `
            <li class="item first">
              <div class="product-image"> <a href="/product/${data[i].id}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['product']['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
              <div class="product-shop">
                <h2 class="product-name"><a href="/product/${data[i].id}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                <div class="desc std">
                  <p>${data[i]['product']['overview']}</p>
                </div>
                <div class="price-box"> 
                  <p class="special-price"> <span class="price-label"></span> <span class="price"> ${data[i]['product']['price'].toFixed(2)}</span> </p>
                </div>
                <div class="actions">
                  <button class="button btn-cart ajx-cart" title="Add to Cart" type="button"><span>Add to Cart</span></button>
                  <span class="add-to-links"> <a title="Add to Wishlist" class="button link-wishlist" href="#" data="${data[i].id}"><span data="${data[i].id}">Add to Wishlist</span></a> </span> </div>
              </div>
            </li>
            `
        }
      }
    })
}}

let filterColor = document.getElementsByClassName('color-category');
for (let i = 0; i < filterColor.length; i++) {
  filterColor[i].onclick = function () {
    const ColorId = this.getAttribute('data');
    colorFilter.filterColorProduct(ColorId);
  }
}