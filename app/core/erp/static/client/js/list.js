$(function () {
    const tableData = $('#tableData').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "names"},
            {"data": "surnames"},
            {"data": "dni"},
            {"data": "date_birthday"},
            {"data": "gender.name"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat" rel="edit"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat" rel="delete"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
    
    const btnAdd = document.querySelector('.btnAdd')
    const form = document.querySelector('form');
    const inputAction = document.querySelector('#inputAction');
    
    
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        myForm = new FormData(e.target);

        fetch(
            // '{% url "erp:category_add" %}',
            window.location.pathname,
             {
            method: "POST",
            body: myForm,
          }).then(rpta => rpta.json()).then(result => 
            {
            if(!result.hasOwnProperty('error')){
                sendMessage('Registrado', 'Registrado correctamente', 'success').then(()=> {
                    // location.reload();
                    tableData.ajax.reload()
                    $('#myModalClient').modal('hide');
                })
            } else {
              console.log(result)
              showFormErrors(result.error);
            }
          }
          ).catch(error => console.error('Error:', error));
    })

    btnAdd.addEventListener('click', () => {
        form.reset()
        $('#myModalClient').modal('show');
        inputAction.setAttribute("value", 'add')
    })
    
    $('#tableData tbody').on('click', 'a[rel="edit"]', function(){
        const data = tableData.row($(this).parents('tr')).data()
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="names"]').val(data.names);
        $('input[name="surnames"]').val(data.surnames);
        $('input[name="dni"]').val(data.dni);
        $('input[name="date_birthday"]').val(data.date_birthday);
        $('input[name="address"]').val(data.address);
        $('select[name="gender"]').val(data.gender.id);
        $('#myModalClient').modal('show');
    })
    .on('click', 'a[rel="delete"]', function(){
        const data = tableData.row($(this).parents('tr')).data()
        const parameters = new FormData()
        parameters.append("id", data.id);
        parameters.append("action", "delete");

        confirmMessage(window.location.pathname, 'POST', parameters, 'eliminado', () => {
            tableData.ajax.reload()
        })
    })

});

