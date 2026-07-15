document.querySelectorAll('input[type="checkbox"]').forEach((checkbox, index) => {
    const key = `checkbox-${index}`;

    function updateStrike() {
        const li = checkbox.closest("li");
        if (!li) return;

        if (checkbox.checked) {
            li.classList.add("task-completed");
        } else {
            li.classList.remove("task-completed");
        }
    }

    // Restore saved state
    checkbox.checked = localStorage.getItem(key) === "true";
    updateStrike();

    checkbox.addEventListener("change", () => {
        localStorage.setItem(key, checkbox.checked);
        updateStrike();
    });
});
