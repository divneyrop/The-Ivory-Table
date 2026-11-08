(() => {
    const form = document.getElementById("orderForm");
    const status = document.getElementById("orderStatus");
    const summary = document.getElementById("orderSummaryItems");
    const subtotal = document.getElementById("orderSubtotal");
    const fulfilmentNote = document.getElementById("orderFulfilmentNote");
    const addressField = document.getElementById("deliveryAddressField");
    const address = document.getElementById("deliveryAddress");
    const takeoutNote = document.getElementById("takeoutAddressNote");
    const submitOrderButton = document.getElementById("submitOrderButton");
    const quantities = Array.from(document.querySelectorAll(".order-quantity"));

    if (!form || !status || !summary || !subtotal || !submitOrderButton) return;

    const money = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" });
    const method = () => form.querySelector('input[name="fulfilment"]:checked')?.value || "";
    const clearStatus = () => { status.hidden = true; status.textContent = ""; };

    function updateAddressField() {
        const isDelivery = method() === "delivery";
        addressField.hidden = !isDelivery;
        address.required = isDelivery;
        address.disabled = !isDelivery;
        takeoutNote.hidden = isDelivery;
    }

    function updateSummary() {
        const chosen = [];
        let total = 0;
        let itemCount = 0;

        quantities.forEach((input) => {
            const quantity = Number.parseInt(input.value, 10) || 0;
            const lineTotal = quantity * Number(input.dataset.price);
            const line = document.getElementById(`line-${input.id}`);
            if (line) line.textContent = money.format(lineTotal);
            if (quantity > 0) {
                chosen.push({ name: input.dataset.name, quantity, total: lineTotal });
                total += lineTotal;
                itemCount += quantity;
            }
        });

        summary.replaceChildren();
        if (!chosen.length) {
            const empty = document.createElement("li");
            empty.className = "order-summary__empty";
            empty.textContent = "Add dishes to see them here.";
            summary.append(empty);
        } else {
            chosen.forEach((item) => {
                const row = document.createElement("li");
                const label = document.createElement("span");
                const amount = document.createElement("strong");
                label.textContent = `${item.quantity} × ${item.name}`;
                amount.textContent = money.format(item.total);
                row.append(label, amount);
                summary.append(row);
            });
        }

        subtotal.textContent = money.format(total);
        fulfilmentNote.textContent = method() === "delivery"
            ? "Delivery selected. Add your address below."
            : method() === "takeout"
                ? "Takeout selected. We’ll contact you when it’s ready."
                : "Choose delivery or takeout to continue.";
        return { itemCount };
    }

    function updatePage() {
        clearStatus();
        updateAddressField();
        updateSummary();
    }

    function showOrderConfirmation() {
        const order = updateSummary();
        if (!order.itemCount) {
            status.textContent = "Please choose at least one meal before placing your order.";
            status.hidden = false;
            return;
        }
        if (!form.reportValidity()) return;

        const name = form.elements.namedItem("customer_name").value.trim();
        const reply = method() === "takeout"
            ? `Your takeout order has been received, ${name}. We’ll contact you when it’s ready for collection.`
            : `Your delivery order has been received, ${name}. We’ll deliver it to ${address.value.trim()}.`;
        status.textContent = `${reply} Thank you for choosing The Ivory Table!`;
        status.hidden = false;
    }

    form.addEventListener("input", updatePage);
    form.addEventListener("change", updatePage);
    form.addEventListener("submit", (event) => event.preventDefault());
    submitOrderButton.addEventListener("click", showOrderConfirmation);
    updateAddressField();
    updateSummary();
})();
