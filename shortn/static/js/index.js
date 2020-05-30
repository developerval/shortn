function shorten() {
    fetch(`${window.origin}/success`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify('entry'),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
        .then(function (response) {
            if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                document.getElementById('new-url').value = 'shortn.site/' + data;
            });
        })
        .catch(function (error) {
            console.log("Fetch error: " + error);
        });
}

function copylink() {
    var copyText = document.querySelector("#new-url");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");
}

document.querySelector("#copy-url").addEventListener("click", copylink);
document.querySelector("#url-input").addEventListener("click", shorten);