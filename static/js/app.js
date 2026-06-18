// const avatar = "/static/img/boitata.png";
//  <img src="${avatar}"></img>

window.onload = function () {

    const input = document.getElementById("msg");

    input.addEventListener("keydown", function (event) {

        if (event.key === "Enter") {
            event.preventDefault();
            send();
        }

    });

};

async function send() {
    let input = document.getElementById("msg")
    let msg = input.value.trim()
    
    if(!msg) return;

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: msg
        })
    });

    let data = await response.json();

    document.getElementById("chat").innerHTML += `
        <p><b>Você:</b> ${msg}</p>
        <p><b>Boitatá:</b> ${data.response}</p>
    `;

    input.value = "";
    input.focus();
}