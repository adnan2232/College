function validateForm(){
    let a = document.forms["submissionForm"];

    for(let x of a){
        if(x.value == ""){
            alert("Please fill all the fields");
            return false;
        }
        if(x.className == "emailName"){
            console.log(x);
            if(x.value.includes("@") && x.value.includes(".")){
                ;
            }
            else{
                alert("Please provide proper email");
                return false;
            }
        }
    }
    return true;
}