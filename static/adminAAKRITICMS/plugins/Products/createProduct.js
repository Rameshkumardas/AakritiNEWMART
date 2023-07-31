$(".AddBestOffer").click(function () {
    const target = $(".target").val()
    const type = $(".offertype").val()
    const name = $(".offer").val()
    const start_date = $(".start_date").val()
    const end_date = $(".end_date").val()
    const URL = window.location.host+$(".TARGETURL").val()
    alert(URL);

    if (target == ""){
      Toast.fire({
          icon: 'error',
          title: '<p id="messages" style="margin-top:12px !important; margin-left:8px !important;"><b> Target Not Define </b></p>'
      }) 
  }
  if (name == ""){
      Toast.fire({
          icon: 'error',
          title: '<p id="messages" style="margin-top:12px !important; margin-left:8px !important;"><b> Name is Empty </b></p>'
      }) 
  }
  $.ajax({                      
      type: "POST",                   
      url: "{% url 'AddBestOffer' %}",                    
      data: {
        csrfmiddlewaretoken: "{{ csrf_token }}",
        'offertype': type,
        'offer':name,       
        'product':target, 
        'start_date':start_date, 
        'end_date':end_date, 
        
      },
      success: function(data) {   
          if (data.status == 1){
              Toast.fire({
              icon: 'success',
              title: '<p id="messages" style="margin-top: 12px !important; margin-left:8px !important;"><b>'+ data.message +'</b></p>'
              }) 
          }
          else if (data.status == 0){
              Toast.fire({
              icon: 'error',
              title: '<p id="messages" style="margin-top: 12px !important; margin-left:8px !important;"><b>'+ data.message +'</b></p>'
              }) 
          }       
      },
  });
});