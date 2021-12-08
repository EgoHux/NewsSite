function keyPressInput(input) {
    console.log("change");
    input.value = input.value + document.getElementsByName(input.name)[0].textContent;
}

function change_input(target){
	var input = target.parentElement.getElementsByClassName('input')[0];
    var text = target.parentElement.getElementsByTagName("a")[0];

    var current_value = target.parentElement.getElementsByTagName("label")[0];
    
	if (input.readOnly) {
		text.textContent = "Отменить";
		input.readOnly = false;
	} else {
		text.textContent = "Изменить";
		input.readOnly = true;
        input.value = current_value.textContent;
	}
}

function change_input_file(event) {
    var selectedFile = event.target.files[0];
    var reader = new FileReader();

    var imgtag = document.getElementsByClassName("left")[0].getElementsByTagName("img")[0];
    imgtag.title = selectedFile.name;

    reader.onload = function(event) {
        imgtag.src = event.target.result;
    };

    reader.readAsDataURL(selectedFile);

}

function change_file(target) {
    input_file = document.getElementsByName("file")[0];
    var current_value = target.parentElement.getElementsByTagName("label")[0];
    var text = target.parentElement.getElementsByTagName("a")[0];
    var img = document.getElementsByClassName("left")[0].getElementsByTagName("img")[0];

    if (input_file.disabled) {
		text.textContent = "Отменить";
		input_file.disabled = false;
	} else {
		text.textContent = "Изменить";
		input_file.disabled = true;
        img.src = current_value.textContent;
        input_file.value = "";
	}
}

function controller_password() {
    button = document.getElementsByClassName("password_controller")[0];

    input_password = button.parentElement.getElementsByClassName("input")[0];

    if (button.textContent == "(Показать пароль)") {
        button.textContent = "(Скрыть пароль)";
        input_password.type = "text";
    }
    else {
        button.textContent = "(Показать пароль)";
        input_password.type = "password";
    }
}

function onSubmit(){
    preventDefault();
    form = document.getElementsByTagName("form")[0];

    wrapper_login = document.getElementsByName("login")[0].parentElement;
    result_login = wrapper_login.getElementsByTagName("label").textContent == wrapper_login.getElementsByClassName("input").value;

    wrapper_age = document.getElementsByName("age")[0].parentElement;
    result_age = wrapper_age.getElementsByTagName("label").textContent == wrapper_age.getElementsByClassName("input").value;

    wrapper_email = document.getElementsByName("email")[0].parentElement;
    result_email = wrapper_email.getElementsByTagName("label").textContent == wrapper_email.getElementsByClassName("input").value;

    wrapper_password = document.getElementsByName("password")[0].parentElement;
    result_password = wrapper_password.getElementsByTagName("label").textContent == wrapper_password.getElementsByClassName("input").value;

    if  (result_login && result_age && result_email && result_password) {
        alert("Данные не изменились");
        return 
    }
}


