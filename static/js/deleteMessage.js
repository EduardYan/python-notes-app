/**
 * This is a small code for delete the message
 * showed it.
 */

/**
 * Execute the code for delete the message
 */
function main() {
  const conteiner = document.querySelector('.principal-container');
  const message = document.querySelector('.messages-view');
  conteiner.removeChild(message);

}

// for execute after 3 seconds
setTimeout(() => {
  main()  
}, 3000);