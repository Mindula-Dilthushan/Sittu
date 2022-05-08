function validation() {

    let userId = $('#user_id').val();
    let userName = $('#user_name').val();
    let userAmount = $('#user_amount').val();

    if (userId == '') {
        alert("please enter user id number")
        return false;
    }
    if (userName == '') {
        alert("please enter user name")
        return false;
    }
    if (userAmount == '') {
        alert("please enter your amount")
        return false;
    } else {
        alert("User Save Success...!")
    }
}

function clear() {
    $("#user_id").val('')
    $("#user_name").val('')
    $("#user_amount").val('')
}
