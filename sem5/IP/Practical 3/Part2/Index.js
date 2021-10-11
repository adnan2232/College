
$(function(){
    $("form[name='submissionForm']").validate({
        onclick: false,
        onkeyup: false,
        rules: {
            name:"required",
            Branch:"required",
            dob:"required",
            email:{
                required:true,
                email:true
            },
            gender:"required"
        },
        
        submitHandler: function(form){
            form.submit();
        },
        
        errorPlacement: function(error, element) {
            alert(error.text());
          }

    });
});