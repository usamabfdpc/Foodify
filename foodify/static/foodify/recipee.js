window.addEventListener('load', function () {
  (function ($) {  
    
    let price_field_box = $('#id_price')
    let recipee_quantaty = $('#recipee_quantay')
    let price_field_checkbox = $('#id_price_set_by_size')
    let price_set_field = $('.field-price_set_by_size')
    let inline = $('.inline-group')

    $('.inline').hide()

    if(price_field_checkbox[0].checked ==true){
      $('#id_price').hide()
    }
    
    if(price_field_checkbox[0].checked ==false){
      $('#id_price').show()
    }
    
        
        price_set_field.change(function(){
          
          if(price_field_checkbox[0].checked ==true){
            price_field_box.hide()            
            inline.show()
          }
          else{
            inline.hide()
            price_field_box.show()  
          } 
        
        })
      })
      (django.jQuery);

});
