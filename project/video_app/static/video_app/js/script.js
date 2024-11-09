function _(id) {
    return document.getElementById(id);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function postFile() {

    axios({
        method: 'post',
        url: '/main/',
        data: {
            "file": _('id_file').files[0]
        },
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "content-type": "multipart/form-data"
        },
        onUploadProgress: (progressEvent) => {
            const totalLength = progressEvent.lengthComputable ? progressEvent.total :
                                progressEvent.target.getResponseHeader('content-length') ||
                                progressEvent.target.getResponseHeader('x-decompressed-content-length');
            if (totalLength !== null) {
                percent = Math.round((progressEvent.loaded * 100) / totalLength);
                _('progress-bar-file').style.width = percent + '%';
                _('progress-bar-file').innerHTML = percent + '%';
            }
        }
    }).then((response) => {
        console.log(response);
        setTimeout(() => {
            fetch('/').then((response) => document.ht);
        }, 2 * 1000);
    });
}