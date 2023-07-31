
//“upload image and display in upload image field with jquery” Code Answer
const IMG1 = document.querySelector("#IMG1");
var uploaded_image = "";
IMG1.addEventListener("change", function() {  
    console.log(IMG1.value);
    const reader = new FileReader();   
    reader.addEventListener("load", () => {    
        const uploaded_image = reader.result;  
        document.getElementById("NoObjectIMG1").style.display='none';
        document.getElementById("NoObjectIMG1").style.visibility='hidden';
        document.getElementById("display_imageIMG1").style.display='';
        document.getElementById("display_imageIMG1").style.visibility='';
        document.querySelector("#display_imageIMG1").style.backgroundImage = `url(${uploaded_image})`;
    });   
        reader.readAsDataURL(this.files[0]);
});

const IMG2 = document.querySelector("#IMG2");
var uploaded_image = "";
IMG2.addEventListener("change", function() {  
    console.log(IMG2.value);
    const reader = new FileReader();   
    reader.addEventListener("load", () => {    
        const uploaded_image = reader.result;  
        document.getElementById("NoObjectIMG2").style.display='none';
        document.getElementById("NoObjectIMG2").style.visibility='hidden';
        document.getElementById("display_imageIMG2").style.display='';
        document.getElementById("display_imageIMG2").style.visibility='';
        document.querySelector("#display_imageIMG2").style.backgroundImage = `url(${uploaded_image})`;
    });   
        reader.readAsDataURL(this.files[0]);
});

const IMG3 = document.querySelector("#IMG3");
var uploaded_image = "";
IMG3.addEventListener("change", function() {  
    console.log(IMG3.value);
    const reader = new FileReader();   
    reader.addEventListener("load", () => {    
        const uploaded_image = reader.result;  
        document.getElementById("NoObjectIMG3").style.display='none';
        document.getElementById("NoObjectIMG3").style.visibility='hidden';
        document.getElementById("display_imageIMG3").style.display='';
        document.getElementById("display_imageIMG3").style.visibility='';
        document.querySelector("#display_imageIMG3").style.backgroundImage = `url(${uploaded_image})`;
    });   
        reader.readAsDataURL(this.files[0]);
});


const IMG4 = document.querySelector("#IMG4");
var uploaded_image = "";
IMG4.addEventListener("change", function() {  
    console.log(IMG4.value);
    const reader = new FileReader();   
    reader.addEventListener("load", () => {    
        const uploaded_image = reader.result;  
        document.getElementById("NoObjectIMG4").style.display='none';
        document.getElementById("NoObjectIMG4").style.visibility='hidden';
        document.getElementById("display_imageIMG4").style.display='';
        document.getElementById("display_imageIMG4").style.visibility='';
        document.querySelector("#display_imageIMG4").style.backgroundImage = `url(${uploaded_image})`;
    });   
        reader.readAsDataURL(this.files[0]);
});