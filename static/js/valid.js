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
    event, 
    input_name=document.getElementById('name'),
    input_surname=document.getElementById('surname')
)
{
    let x = 1;
    let y = 5;

    if(event == "name"){
        if (input_length(event, input_name.value, x) == true)
        {
            document.getElementById("ok-name").style.display = 'initial';
        }
    }
    input_length(event, input_surname.value, y);

}
