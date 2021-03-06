$(document).ready(function () {
    $('input[type=file]').change(function () {
        $('#btnUpload').show();
        $('#divFiles').html('');
        for (var i = 0; i < this.files.length; i++) { //Progress bar and status label's for each file genarate dynamically
            var fileId = i;
            $("#divFiles").append('<div class="col-md-12">' +
                '<div class="progress-bar progress-bar-striped active" id="progressbar_' + fileId + '" role="progressbar" aria-valuemin="0" aria-valuemax="100" style="width:0%"></div>' +
                '</div>' +
                '<div class="col-md-12">' +
                '<div class="col-md-6">' +
                '<input type="button" class="btn btn-danger" style="display:none;line-height:6px;height:25px" id="cancel_' + fileId + '" value="cancel">' +
                '</div>' +
                '<div class="col-md-6">' +
                '<p class="progress-status" style="text-align: right;margin-right:-15px;font-weight:bold;color:saddlebrown" id="status_' + fileId + '"></p>' +
                '</div>' +
                '</div>' +
                '<div class="col-md-12">' +
                '<p id="notify_' + fileId + '" style="text-align: right;"></p>' +
                '</div>');
        }
    })
    function uploadFiles() {
        var file = document.getElementById("fileUploader")//All files
        for (var i = 0; i < file.files.length; i++) {
            uploadSingleFile(file.files[i], i);
        }
    }
    function uploadSingleFile(file, i) {
        var fileId = i;
        var ajax = new XMLHttpRequest();
        //Progress Listener
        ajax.upload.addEventListener("progress", function (e) {
            var percent = (e.loaded / e.total) * 100;
            $("#status_" + fileId).text(Math.round(percent) + "% uploaded, please wait...");
            $('#progressbar_' + fileId).css("width", percent + "%")
            $("#notify_" + fileId).text("Uploaded " + (e.loaded / 1048576).toFixed(2) + " MB of " + (e.total / 1048576).toFixed(2) + " MB ");
        }, false);
        //Load Listener
        ajax.addEventListener("load", function (e) {
            $("#status_" + fileId).text(event.target.responseText);
            $('#progressbar_' + fileId).css("width", "100%")

            //Hide cancel button
            var _cancel = $('#cancel_' + fileId);
            _cancel.hide();
        }, false);
        //Error Listener
        ajax.addEventListener("error", function (e) {
            $("#status_" + fileId).text("Upload Failed");
        }, false);
        //Abort Listener
        ajax.addEventListener("abort", function (e) {
            $("#status_" + fileId).text("Upload Aborted");
        }, false);

        ajax.open("POST", "/api/upload/UploadFiles"); // Your API .net, php

        var uploaderForm = new FormData(); // Create new FormData
        uploaderForm.append("file", file); // append the next file for upload
        ajax.send(uploaderForm);

        //Cancel button
        var _cancel = $('#cancel_' + fileId);
        _cancel.show();

        _cancel.on('click', function () {
            ajax.abort();
        })
    }
});