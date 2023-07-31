$("#mainCat").change(function () {
    const url = $("#FormData").attr("LoadsubCat");  // get the url of the `LoadsubCat` view
    const mainCatID = $(this).val();  // get the selected mainCat ID from the HTML input
    
    console.log("URLs :-", url);
    console.log("mainCatID :-", mainCatID);
  
    $.ajax({                       // initialize an AJAX request
        type: "POST",                   
        url: url,                    // set the url of the request (= /persons/ajax/load-SubCategory/ )
        data: {
          csrfmiddlewaretoken: "{{ csrf_token }}",
          'mainCat': mainCatID       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_SubCategory` view function
            $("#subCatLoaded").html(data);  // replace the contents of the city input with the data that came from the server
        }
    });
  });