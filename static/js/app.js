async function send() {
    let msg = document.getElementById("msg").value;
    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: msg
        })
    });
    // const avatar = "/static/img/boitata.png";
    
    //  <img src="${avatar}"></img>

    let data = await response.json();
    document.getElementById("chat").innerHTML += `
       <p><b>Você:</b> ${msg}</p> 
        <p><b>Boitata:</b> ${data.response}</p>
    `;
}