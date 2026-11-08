(() => {
    const form = document.getElementById("reservationForm");
    const preview = document.getElementById("reservationPreviewText");
    const status = document.getElementById("reservationStatus");
    const reviewButton = document.getElementById("submitForReview");

    if (!form || !preview || !status || !reviewButton) return;

    const field = (name) => form.elements.namedItem(name);
    const value = (name, fallback) => field(name).value.trim() || fallback;

    const displayDate = (rawDate) => {
        if (!rawDate) return "your preferred date";
        const [year, month, day] = rawDate.split("-").map(Number);
        return new Intl.DateTimeFormat(undefined, { dateStyle: "long" }).format(
            new Date(year, month - 1, day)
        );
    };

    const displayTime = (rawTime) => {
        if (!rawTime) return "your preferred time";
        const [hour, minute] = rawTime.split(":").map(Number);
        return new Intl.DateTimeFormat(undefined, {
            hour: "numeric",
            minute: "2-digit",
        }).format(new Date(2000, 0, 1, hour, minute));
    };

    const updatePreview = () => {
        const guestSelect = field("guests");
        const guestCount = guestSelect.value
            ? guestSelect.options[guestSelect.selectedIndex].textContent.trim()
            : "your party";
        const name = value("guest_name", "your name");
        const email = value("email", "your email address");
        const phone = value("phone", "your phone number");
        const date = displayDate(field("date").value);
        const time = displayTime(field("time").value);
        const requests = value("requests", "");

        let message = `Hello, I’d like to request a table for ${guestCount} on ${date} at ${time}. My name is ${name}. You can reach me at ${phone} or ${email}.`;
        if (requests) message += ` Additional requests: ${requests}`;
        preview.textContent = message;
    };

    let updateTimer;
    const clearStatus = () => {
        status.hidden = true;
        status.textContent = "";
    };

    form.addEventListener("input", () => {
        clearStatus();
        window.clearTimeout(updateTimer);
        updateTimer = window.setTimeout(updatePreview, 500);
    });
    form.addEventListener("change", () => {
        clearStatus();
        updatePreview();
    });
    const prepareReviewMessage = () => {
        if (!form.reportValidity()) return;

        status.textContent = "Your reservation request is ready for review. We’ll get back to you within 24 hours.";
        status.hidden = false;
    };

    reviewButton.addEventListener("click", prepareReviewMessage);
    form.addEventListener("submit", (event) => event.preventDefault());
})();
