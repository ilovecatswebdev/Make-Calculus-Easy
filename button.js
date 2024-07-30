document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('displayansbutton');
    var image = document.getElementById('panswer'); 
    var image2 = document.getElementById('panswer2'); 
    toggleButton.addEventListener('click', function() {
      image.classList.toggle('hidden');
    });
    toggleButton.addEventListener('click', function() {
      image2.classList.toggle('shidden');
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('displayansbutton');
    var image = document.getElementById('panswer2');  
    toggleButton.addEventListener('click', function() {
      image.classList.toggle('shidden');
    });
  });

