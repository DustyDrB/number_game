$(document).ready(function(){
  $('form.guess').submit(function(event){
    event.preventDefault()

    $.ajax({
      url: '/answer',
      method: 'post',
      data: $(this).serialize(),
      success: function(response){
        $('body').html(response)
      }
    })
  })





})
