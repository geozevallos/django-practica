function showFormErrors(errors){
    let html = '';
    if(typeof(errors)==='object'){
        let html2 = ''
        for (const property in errors) {
            errors[property].forEach(element => {
               html2 += `<li>${property}: ${element}</li>` 
            });
        }
        html = `<ul>${html2}</ul>`
    } else {
        html = `<p>${errors}</p>`
    }

    Swal.fire({
        title: 'Error',
        html: html,
        icon: 'error'
      })
}

function sendMessage(title, text, icon){
    return new Promise((resolve, reject) => {
        resolve(
            Swal.fire({
                title: title,
                text: text,
                icon: icon
              })
        )
    })
}

function confirmMessage(url, fetchMethod, form, callback){
    Swal.fire({
        title: '¿Estás seguro de realizar esta acción?',
        text: "No podrás revertir esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.value) {
            fetch(url, {method: fetchMethod, body: form}).then(rpta => rpta.json()).then(result => {
                if(!result.hasOwnProperty('error')){
                    Swal.fire({
                    title: 'Creado correctamente!',
                    icon: 'success',
                    // html: 'I will close in <b></b> milliseconds.',
                    timer: 2000,
                    timerProgressBar: true,
                    showConfirmButton: false,
                    }).then((result) => {
                    if (result.dismiss === Swal.DismissReason.timer) {
                      callback();
                      }
                    })
          
                  } else {
                    console.log(result)
                    showFormErrors(result.error);
                  }
            }).catch(error => console.error('Error:', error));
        }
      })
}