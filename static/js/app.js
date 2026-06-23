let canSend = true;

window.onload = function () {
    const input = document.getElementById("msg");

    input.addEventListener("keydown", function (event) {

        if (event.key === "Enter") {
            event.preventDefault();
            send();
        }

    });

};

function clearChat() {
    if (!canSend) return;
    document.getElementById("chat").innerHTML = "";
}

async function send() {

    if (!canSend) {
        return;
    }

    const input = document.getElementById("msg");
    const chat = document.getElementById("chat");

    let msg = input.value.trim();

    if (!msg) {
        return;
    }

    if (msg.toLowerCase() === "limpar") {
        chat.innerHTML = "";
        input.value = "";
        return;
    }

    canSend = false;
    input.disabled = true;

    chat.innerHTML += `
        <p><b>Você:</b> ${msg}</p>
    `;

    chat.scrollTop = chat.scrollHeight;

    input.value = "";

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: msg
            })
        });

        const data = await response.json();

        chat.innerHTML += `
            <div id="typing">
                <b>procurando melhor resposta...</b>
            </div>
        `;

        chat.scrollTop = chat.scrollHeight;

        setTimeout(() => {

            const typing = document.getElementById("typing");

            if (typing) {
                typing.remove();
            }

            chat.innerHTML += `
                <div style="display:flex;align-items:center;gap:10px;margin:10px 0;">
                    <span><b>Boitatá:</b> ${data.response}</span>
                </div>
            `;

            chat.scrollTop = chat.scrollHeight;

            canSend = true;
            input.disabled = false;
            input.focus();

        }, 2000);

    } catch (error) {

        chat.innerHTML += `
            <p>Alguma coisa fora do lugar, arrume!.</p>
        `;

        console.error(error);

        canSend = true;
        input.disabled = false;
        input.focus();
    }
}