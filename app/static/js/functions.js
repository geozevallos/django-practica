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