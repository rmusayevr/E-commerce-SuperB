const categoryFilter = {
  url: `${location.origin}/api/product_versions/`,

  filterProduct(categoryId) {
    let url = this.url;
    if (categoryId) {
      url += `?categoryId=${categoryId}`;
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('products-list').innerHTML = ''
      for (let i in data) {;
        for (let x in data[i]['product'].category) {
          if (data[i]['product']['category'][x] == categoryId) {
            console.log(data[i]);
            document.getElementById('products-list').innerHTML += `
            <li class="item first">
              <div class="product-image"> <a href="{% url 'product_detail' product.pk %}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
              <div class="product-shop">
                <h2 class="product-name"><a href="{% url 'product_detail' product.pk %}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                <div class="desc std">
                  <p>${data[i]['product']['overview']}</p>
                </div>
                <div class="price-box"> 
                  <p class="special-price"> <span class="price-label"></span> <span class="price"> ${data[i]['price']}</span> </p>
                </div>
                <div class="actions">
                  <button class="button btn-cart ajx-cart" title="Add to Cart" type="button"><span>Add to Cart</span></button>
                  <span class="add-to-links"> <a title="Add to Wishlist" class="button link-wishlist" href="#"><span>Add to Wishlist</span></a> </span> </div>
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