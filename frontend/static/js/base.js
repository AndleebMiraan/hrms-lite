$(function () {

    // ajax form submission
    $(document).on("submit", ".ajax-form", e => {
        e.preventDefault();
        const f = e.target;
        if (!f.checkValidity()) {
            const invalidFields = Array.from(f.querySelectorAll(":invalid"));
            const messages = invalidFields.map(invalid => {
                const label = f.querySelector(`label[for="${invalid.id}"]`);
                const fieldName = label ? label.innerText : invalid.name;
                return `${fieldName} cannot be empty.`;
            });
            return alert(messages.join("\n"));
        }

        const { method = "POST", url, redirect, errorMessage, csrf } = f.dataset;
        $.ajax({
            type: method,
            url: url,
            data: new FormData(f),
            processData: false,
            contentType: false,
            headers: { "X-CSRFToken": csrf },
            success: r => redirect && (location.href = redirect),
            error: xhr => {
                const msg = xhr.responseJSON
                    ? Object.entries(xhr.responseJSON)
                        .map(([k, v]) => `${k}: ${v.join(", ")}`)
                        .join("\n")
                    : errorMessage || "Error submitting form.";
                alert(`Error ${xhr.status}:\n${msg}`);
            }
        });
    });


    // universal Choices init
    $("select[data-choices]").each(function () {
        new Choices(this, {
            searchEnabled: true,
            itemSelectText: "",
            placeholder: true,
            placeholderValue: this.dataset.placeholder || "Select",
            shouldSort: false,
        });
    });

    // universal delete handler
    $(document).on("click", ".delete-btn", function () {
        const id = $(this).data("id");
        const modelUrl = $(this).data("model-url") || "item";
        const modelName = $(this).data("model-name") || "item";
        if (!confirm(`Are you sure you want to delete this ${modelName}?`)) return;

        $.ajax({
            url: `/api/${modelUrl}/${id}/`,
            type: "DELETE",
            headers: { "X-CSRFToken": $(this).data("csrf") },
            success: () => location.reload(),
            error: () => alert(`Failed to delete ${modelName}.`),
        });
    });

    flatpickr(".flatpickr", { dateFormat: "Y-m-d", maxDate: "today" });
});

function getCustomModel(modelName, data) {
    var result = null;
    $.ajax({
        url: "/api/custom/" + modelName + "/",
        method: "GET",
        data: data,
        async: false,
        success: function (data) { result = data; },
        error: function (xhr) { console.error(xhr.responseText); }
    });
    return result;
}

function mapToChoices(array) {
    return array.map(item => ({ value: item.id, label: item.name }));
}
