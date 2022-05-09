loadUsers()


//button actions -------------------------------------------------
$('.btn-user-01-search').click(function () {
    getUserId('#userId_1', '#userName_1', '#userAmount_1')
});

$('.btn-user-02-search').click(function () {
    getUserId('#userId_2', '#userName_2', '#userAmount_2')
});

$('.btn-user-03-search').click(function () {
    getUserId('#userId_3', '#userName_3', '#userAmount_3')
});

$('.btn-loan-amount').click(function () {
    getMax()
});


//button text clear ----------------------------------------------
$('.btn-user-01-clear').click(function () {
    clearUser('#userId_1', '#userName_1', '#userAmount_1')
});

$('.btn-user-02-clear').click(function () {
    clearUser('#userId_2', '#userName_2', '#userAmount_2')
});

$('.btn-user-03-clear').click(function () {
    clearUser('#userId_3', '#userName_3', '#userAmount_3')
});

//validation data ------------------------------------------------
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
        url: 'http://127.0.0.1:5000/get_all_user',
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

//search user ----------------------------------------------------
function getUserId(id, name, amount) {
    $.ajax({
        url: 'http://127.0.0.1:5000/get_user',
        method: 'GET',
        async: false,
        dataType: 'json',
        success: function (res) {
            let values = res;
            let input = $(id).val();
            for (i in values) {
                let id = values[i].id;
                if (input == id) {
                    $(name).val(values[i].name);
                    $(amount).val(values[i].amount);
                    break
                }

            }
        }
    });
}

//clear user 1  text ---------------------------------------------
function clearUser(id, name, amount) {
    $(id).val('');
    $(name).val('');
    $(amount).val('');
}


//testing------------------------------------------
function getMax() {
    let user1 = $('#userAmount_2').val();
    let user2 = $('#userAmount_3').val();
    let usersAmoutTot = $('#usersAmoutTot').val();
    let max_amount = $('#loanMax').val();
    let i_want_value = $('#you_want_amount').val();

    if (max_amount >= i_want_value) {
        let user1Amount = (i_want_value * user1) / usersAmoutTot;
        let user2Amount = (i_want_value * user2) / usersAmoutTot;

        let user1Am = parseFloat(user1Amount).toFixed(2);
        let user2Am = parseFloat(user2Amount).toFixed(2);

        $('#user_1_last_amount').val(user1Am);
        $('#user_2_last_amount').val(user2Am);
    }else {
        alert("You can't get loan...!\ncheck maximum amount...\nplease try again...!")
    }


}