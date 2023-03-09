function preview() {
    img_preview.src = URL.createObjectURL(event.target.files[0]);
}

function clearImage() {
    document.getElementById('id_photo').value = null;
    img_preview.src = "";
}