
// Tag Complete
$(document).ready(function(){
    var maxField = 5; //Input fields increment limitation
    var addButton = $('.addTag'); //Add button selector
    var wrapper = $('.TagArea'); //Input field wrapper

    var fieldHTML = '<div class="input-group remove mt-2" style="cursor:pointer;"><div class="input-group-prepend remove_Tag"><span class="input-group-text " data-toggle="tooltip" data-placement="top" title="Hit: For Remove Input Field!" ><i class="far fa-times-circle nav-icon text-danger"></i></span></div><input type="text" name="tag" value="" class="form-control" id="" placeholder="Add Tags"><div class="input-group-append"><div class="input-group-text remove_Tag"><i class="fas fa-tags"></i></div></div></div>';
    var x = 1; //Initial field counter is 1

    //Once add button is clicked
    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });
    //Once remove button is clicked
    $(wrapper).on('click', '.remove_Tag', function(e){
        e.preventDefault();
        $(this).parent('.remove').remove(); //Remove field html
        x--; //Decrement field counter
    });
});



 $(function () {
  $('[data-toggle="tooltip"]').tooltip()
})



// “upload image and display in upload image field with jquery” Code Answer
const image_input = document.querySelector("#image_input");

var uploaded_image = "";
image_input.addEventListener("change", function() {  
    // console.log(image_input.value);
    const reader = new FileReader();   
    reader.addEventListener("load", () => {    
        const uploaded_image = reader.result;  

        document.getElementById("NoObject").style.display='none';
        document.getElementById("NoObject").style.visibility='hidden';

        document.getElementById("display_image").style.display='';
        document.getElementById("display_image").style.visibility='';

        document.querySelector("#display_image").style.backgroundImage = `url(${uploaded_image})`;



    });   
        reader.readAsDataURL(this.files[0]);
});


// var Toast = Swal.mixin({
//     toast: true,
//     position: 'top-end',
//     showConfirmButton: false,
//     timer: 3000
//   });


  $(document).ready(function(){
    var maxField = 9; //Input fields increment limitation
    var addButton = $('.add_skill'); //Add button selector
    var wrapper = $('.add_skill_area'); //Input field wrapper

    var fieldHTML = '<div class="input-group remove-skills mt-2" style="cursor:pointer;"><div class="input-group-prepend remove_skill"><span class="input-group-text "><i class="far fa-times-circle nav-icon text-danger"></i></span></div><input type="text" name="requirements" value="" class="form-control" id="" placeholder="Add Requirements"><div class="input-group-append"><div class="input-group-text remove_skill"><i class="fas fa-book-medical"></i></div></div></div>';
    var x = 0; //Initial field counter is 1

    //Once add button is clicked
    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });
    //Once remove button is clicked
    $(wrapper).on('click', '.remove_skill', function(e){
        e.preventDefault();
        $(this).parent('.remove-skills').remove(); //Remove field html
        x--; //Decrement field counter
    });
});



// Short Intro Count
document.getElementById("stringlength").innerHTML = 300;
function stringCount() {
    var x = document.getElementById("exampleFormControlTextarea4").value;
    let length = x.length;
    let max = 300;
    let current = max-length;
    if ((current<301) & (current>-1)){
        document.getElementById("stringlength").innerHTML = current;
        document.getElementById("stringlength").style.color = '';

        document.getElementById("publisher").style.display='';
        document.getElementById("publisher").style.visibility='';

    }else{
        // .style.color
        document.getElementById("stringlength").style.color = '#d00';
        document.getElementById("stringlength").innerHTML = current;

        document.getElementById("publisher").style.display='none';
        document.getElementById("publisher").style.visibility='hidden';
        
    }

}

document.getElementById("TagDescriptionstringlength").innerHTML = 190;
function TagDescriptionstringCount() {
    var x = document.getElementById("exampleFormControlTextarea4").value;
    let length = x.length;
    let max = 170;
    let current = max-length;
    if ((current<301) & (current>-1)){
        document.getElementById("TagDescriptionstringlength").innerHTML = current;
        document.getElementById("TagDescriptionstringlength").style.color = '';

        document.getElementById("publisher").style.display='';
        document.getElementById("publisher").style.visibility='';

    }else{
        // .style.color
        document.getElementById("TagDescriptionstringlength").style.color = '#d00';
        document.getElementById("TagDescriptionstringlength").innerHTML = current;

        document.getElementById("publisher").style.display='none';
        document.getElementById("publisher").style.visibility='hidden';
        
    }

}

// DescriptionStringCount
document.getElementById("DescriptionStringCountShow").innerHTML = 6000;

function DescriptionStringCountShow1() {

    var x = document.getElementsByClassName("DescriptionStringCount").value;
    let length = x.length;

    let max = 6000;
    let current = max-length;

    if ((current<6001) & (current>-1)){
        document.getElementById("DescriptionStringCountShow").innerHTML = current;
        document.getElementById("DescriptionStringCountShow").style.color = '';

        document.getElementById("publisher").style.display='';
        document.getElementById("publisher").style.visibility='';

    }else{
        // .style.color
        document.getElementById("DescriptionStringCountShow").style.color = '#d00';
        document.getElementById("DescriptionStringCountShow").innerHTML = current;

        document.getElementById("publisher").style.display='none';
        document.getElementById("publisher").style.visibility='hidden';
        
    }

}

// Short TagDescStringCount
document.getElementById("tag-description").innerHTML = 200;
function TagDescStringCount() {

    var x = document.getElementById("TagDescriptions").value;
    let length = x.length;
    let max = 200;
    let current = max-length;
    if ((current<201) & (current>-1)){
        document.getElementById("tag-description").innerHTML = current;
        document.getElementById("tag-description").style.color = '';

        document.getElementById("publisher").style.display='';
        document.getElementById("publisher").style.visibility='';
    }else{
        // .style.color
        document.getElementById("tag-description").style.color = '#d00';
        document.getElementById("tag-description").innerHTML = current;

        document.getElementById("publisher").style.display='none';
        document.getElementById("publisher").style.visibility='hidden';   
    }
}

// NameStringCount
document.getElementById("NameStringCount").innerHTML = 65;
function NameStringCount() {
    var x = document.getElementById("input-field").value;
    let length = x.length;
    let max = 60;
    let current = max-length;

    if ((current<151) & (current>-1)){
        document.getElementById("NameStringCount").innerHTML = current;
        document.getElementById("NameStringCount").style.color = '';

        document.getElementById("publisher").style.display='';
        document.getElementById("publisher").style.visibility='';

    }else{
        // .style.color
        document.getElementById("NameStringCount").style.color = '#d00';
        document.getElementById("NameStringCount").innerHTML = current;

        document.getElementById("publisher").style.display='none';
        document.getElementById("publisher").style.visibility='hidden';
    }

}


