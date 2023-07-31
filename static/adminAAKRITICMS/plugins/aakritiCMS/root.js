function SideBarChange() {

    document.getElementById("main_cat").className += " menu-open"; 
    document.getElementById("sub_cat").className += " active"; 
    document.getElementById("sub_sub_cat").className += " active"; 
}


$(document).ready(function(){   

    // $(".quizz-type").click(function(){
    $(window).on('load', function(){    

      var category = $(this).attr("cat-target");
      var target = $(this).attr("target-link");

    
      if(category == "blogs"){

        // document.getElementById("blogs").className += " menu-open"; 

        // var element = document.getElementById("myDIV");

// Other examples on how to get the class name of an element:
        // var x = document.getElementsByClassName("mystyle")[0].className;
        // document.getElementById("myDIV").className = "newClassName"; 
        // var y = document.getElementById("myDIV").className; 
        // var x = document.getElementById("myDIV").className; 
        // document.getElementById("myDIV").className = "mystyle"; 

        // document.getElementById("myDIV").className += " anotherClass"; 

        element.classList.add("active");

          if (target == "All-Blogs"){

          }
      }

      if(quizz_type=="objective"){
    
    
        document.getElementById("objective").style.display='';
        document.getElementById("objective").style.visibility='';
    
        document.getElementById("subjective").style.display='none';
        document.getElementById("subjective").style.visibility='hidden';
        
        document.getElementById("fillblank").style.display='none';
        document.getElementById("fillblank").style.visibility='hidden';
    
        document.getElementById("coding-quizz").style.display='none';
        document.getElementById("coding-quizz").style.visibility='hidden';
    
      }else if(quizz_type=="subjective"){
    
        document.getElementById("objective").style.display='none';
        document.getElementById("objective").style.visibility='hidden';
        
        document.getElementById("subjective").style.display='';
        document.getElementById("subjective").style.visibility='';
    
        document.getElementById("fillblank").style.display='none';
        document.getElementById("fillblank").style.visibility='hidden';
    
        document.getElementById("coding-quizz").style.display='none';
        document.getElementById("coding-quizz").style.visibility='hidden';
    
      }else if(quizz_type=="fillblank"){
        
        document.getElementById("objective").style.display='none';
        document.getElementById("objective").style.visibility='hidden';
        
        document.getElementById("subjective").style.display='none';
        document.getElementById("subjective").style.visibility='hidden';
    
        document.getElementById("fillblank").style.display='';
        document.getElementById("fillblank").style.visibility='';
    
        document.getElementById("coding-quizz").style.display='none';
        document.getElementById("coding-quizz").style.visibility='hidden';
      }else if(quizz_type=="coding-quizz"){
    
        document.getElementById("objective").style.display='none';
        document.getElementById("objective").style.visibility='hidden';
        
        document.getElementById("subjective").style.display='none';
        document.getElementById("subjective").style.visibility='hidden';
    
        document.getElementById("fillblank").style.display='none';
        document.getElementById("fillblank").style.visibility='hidden';
    
        document.getElementById("coding-quizz").style.display='';
        document.getElementById("coding-quizz").style.visibility='';
    
      }else{
    
        document.getElementById("objective").style.display='none';
        document.getElementById("objective").style.visibility='hidden';
        
        document.getElementById("subjective").style.display='none';
        document.getElementById("subjective").style.visibility='hidden';
    
        document.getElementById("fillblank").style.display='none';
        document.getElementById("fillblank").style.visibility='hidden';
    
        document.getElementById("coding-quizz").style.display='none';
        document.getElementById("coding-quizz").style.visibility='hidden';
    
      }
    });
    });
    
    