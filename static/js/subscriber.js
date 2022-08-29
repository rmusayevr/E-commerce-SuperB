let form = document.getElementById("newsletter-validate-detail")
form.addEventListener('submit', async function(event) {

    let postData = {
        email: form.email.value,
    }

    let response = await fetch(`${location.origin}/api/subscribers/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    })
})