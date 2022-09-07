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
}

function removeWishlist(ProductID) {
    deleteProduct.deleteProductWishlist(ProductID)
}

function removeBasket(ProductID) {
    deleteProduct_Basket.deleteProductBasket(ProductID)
}
