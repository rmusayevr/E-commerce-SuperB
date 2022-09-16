function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const addCart = {
 
    addProductCart(ProductID) {
        url = `${location.origin}/api/basket/`
        fetch(url).then(response => response.json()).then(data => {
        document.getElementsByClassName('mini-products-list')[0].innerHTML = ''
        if (data['is_active'] === true) {
            for (let i in data) {
                for (let x in data[i]) {
                    if (data[i][x]['in_sale'] == true) {
                        document.getElementsByClassName('mini-products-list')[0].innerHTML += `
                        <li class="item first">
                            <div class="item-inner"><a class="product-image" title="${data[i][x]['name']}" href="{% url 'product_detail' pk=item.pk %}"><img alt="${data[i][x]['name']}" src="${data[i][x]['cover_image']}"></a>
                            <div class="product-details">
                                <strong>${data[i][x]['quantity']}</strong> x <span class="price">${data[i][x]['new_price'].toFixed(2)}</span>
                                <p class="product-name"><a href="{% url 'product_detail' pk=item.pk %}">${data[i][x]['name']}</a></p>
                            </div>
                        </div>
                    </li>`
                    }
                    else {
                        document.getElementsByClassName('mini-products-list')[0].innerHTML += `
                        <li class="item first">
                            <div class="item-inner"><a class="product-image" title="${data[i][x]['name']}" href="{% url 'product_detail' pk=item.pk %}"><img alt="${data[i][x]['name']}" src="${data[i][x]['cover_image']}"></a>
                            <div class="product-details">
                                <strong>${data[i][x]['quantity']}</strong> x <span class="price">${data[i][x]['price'].toFixed(2)}</span>
                                <p class="product-name"><a href="{% url 'product_detail' pk=item.pk %}">${data[i][x]['name']}</a></p>
                            </div>
                        </div>
                    </li>`
                    }
                }
            }
        }
        })
    }
}

const addProduct = {
    addProductWishlist(ProductID) {
        return fetch(`${location.origin}/api/wishlist/`, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': [ 
                    ProductID
                ]
            })
        });
    }
}

const deleteProduct = {
    deleteProductWishlist(ProductID) {
        return fetch(`${location.origin}/api/wishlist`, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': [ 
                    ProductID
                ]
            })
        });
    }
}

const addProduct_Basket = {
    addProductBasket(ProductID) {
        return fetch(`${location.origin}/api/basket/`, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': [ 
                    ProductID
                ]
            })
        });
    }
}

const deleteProduct_Basket = {
    deleteProductBasket(ProductID) {
        return fetch(`${location.origin}/api/basket/`, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': [ 
                    ProductID
                ]
            })
        });
    }
}

function functionAddToWishlist(ProductID) {
    addProduct.addProductWishlist(ProductID);
}

function functionAddToBasket(ProductID) {
    addProduct_Basket.addProductBasket(ProductID);
    addCart.addProductCart(ProductID);

}

function removeWishlist(ProductID) {
    deleteProduct.deleteProductWishlist(ProductID)
}

function removeBasket(ProductID) {
    deleteProduct_Basket.deleteProductBasket(ProductID)
}
