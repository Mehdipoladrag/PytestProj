document.querySelectorAll("input").forEach(input => {
    input.addEventListener("blur", () => {
        if (input.value.trim() !== "") {
            input.classList.add("filled");
        } else {
            input.classList.remove("filled");
        }
    });
});
