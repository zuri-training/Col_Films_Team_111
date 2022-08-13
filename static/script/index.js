  /* hamburger menu */
  let body = document.getElementsByTagName('body')
  let menu = document.getElementById('menu')
  let menuBar = document.getElementById('hamburger')
  let close = document.getElementById('close-icon')
  let menuItems = document.getElementsByClassName('menu-items')
  
  function openNavbar() {
      menu.classList.toggle('active')
  }
  function closeNavbar() {
      menu.classList.toggle('active')
  }
  
  menuBar.addEventListener("click", openNavbar)
  close.addEventListener("click", closeNavbar)
  
  
  /* modal */
  
  // Get the modal
  var modal = document.getElementById("myModal");
  
  // Get the button that opens the modal
  var btn = document.getElementById("openModalButton");
  
  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];
  
  // When the user clicks on the button, open the modal
  btn.onclick = function() {
    modal.style.display = "block";
  }
  
  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
  }
  
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }