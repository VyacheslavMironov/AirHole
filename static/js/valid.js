var name = document.getElementById('name');
var surname = document.getElementById('surname');
var email = document.getElementById('exampleInputEmail');
var password = document.getElementById('exampleInputPassword');
var password1 = document.getElementById('exampleInputPassword1');


function input_length(ev, data, count){
    if(ev == "name" || ev == "surname"){
        if (data.length > count){
            return true
        }
    }
}

function registration_valid(
    event, x=1,
    input_name=document.getElementById('name'),
    input_surname=document.getElementById('surname')
)
{

    if(event == "name"){
        if (input_length(event, input_name.value, x) == true)
        {
            document.getElementById("ok-name").style.display = 'initial';
        }
        else
        {
            document.getElementById("ok-name").style.display = 'none';
        }
    }

    else if (event == "surname"){
        if (input_length(event, input_surname.value, x) == true)
        {
            document.getElementById("ok-surname").style.display = 'initial';
        }
        else
        {
            document.getElementById("ok-surname").style.display = 'none';
        }
    }
}


function valid_email(event){
    let el = document.getElementById(event).value;

    if (String(el).includes('@') == true){
        document.getElementById("ok-email").style.display = 'initial';
    } else{
        document.getElementById("ok-email").style.display = 'none';
    }
}

var arr = [];
function password_is(){
    x = arr[arr.length - 1];

    if (arr.length > 6){
        if(document.getElementById('exampleInputPassword').value == document.getElementById('exampleInputPassword1').value){
            document.getElementById('btn').removeAttribute('disabled');
        }
    }

}

function valid_password(event){
    let el = document.getElementById(event).value;
    arr.push(el);
    password_is();
}

