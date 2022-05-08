loadUsers()

//validation data -------------------------------------------------
function validation() {

    let userId = $('#user_id').val();
    let userName = $('#user_name').val();
    let userAmount = $('#user_amount').val();


    if (userId == '') {
        alert("please enter user id number");
        return false;
    }
    if (userName == '') {
        alert("please enter user name");
        return false;
    }
    if (userAmount == '') {
        alert("please enter your amount");
        return false;
    } else {
        alert("save user success..!")
        loadUsers()
    }
}

//load all data from table----------------------------------------
function loadUsers() {
    $('#user_table_body').empty();
    $.ajax({
        url: 'http://127.0.0.1:5000/get_user',
        method: 'GET',
        async: false,
        dataType: 'json',
        success: function (res) {
            let values = res;
            for (i in values) {
                let id = values[i].id;
                let name = values[i].name;
                let amount = values[i].amount;
                $('#user_table_body').append(`<tr><td>${id}</td><td>${name}</td><td>${amount}</td></tr>`)
            }
        }
    });
}

