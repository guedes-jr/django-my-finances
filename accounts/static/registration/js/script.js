document.addEventListener('DOMContentLoaded', function() {
    const fileUploadDefault = document.querySelector('.file-upload-default');
    const fileUploadBrowse = document.querySelector('.file-upload-browse');
    const fileUploadInfo = document.querySelector('.file-upload-info');
    const imagePreview = document.getElementById('imagePreview');

    fileUploadBrowse.addEventListener('click', function() {
        fileUploadDefault.click();
    });

    fileUploadDefault.addEventListener('change', function() {
        if (fileUploadDefault.files.length > 0) {
            const file = fileUploadDefault.files[0];
            fileUploadInfo.value = file.name;

            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });
});
