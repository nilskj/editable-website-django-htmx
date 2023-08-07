let editor = new MediumEditor('.editable');

function saveEditable(page_path, editable) {
    const element_name = editable.classList[1] // hacky n brittle for now
    htmx.ajax('POST', `/update/${page_path}/`, {
        target: "#feedback",
        values: {
            [element_name]: editable.innerHTML.trim()
        }
    })
}

function saveAllEditables(page_path) {
    const allEditors = document.querySelectorAll('.editable');
    allEditors.forEach(function (item) {
        saveEditable(page_path, item)
    })
}