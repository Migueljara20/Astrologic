function toggleText(button) {
    const card = button.closest(".descripcion");
    const shortText = card.querySelector(".short-text");
    const fullText = card.querySelector(".full-text");

    if (fullText.classList.contains("hidden")) {
        shortText.style.display = "none";
        fullText.classList.remove("hidden");
        button.innerText = "Ver menos";
    } else {
        shortText.style.display = "block";
        fullText.classList.add("hidden");
        button.innerText = "Ver más";
    }
}

