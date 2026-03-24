const toggleTrigger = document.querySelector('#toggle_header');
const headerElement = document.querySelector('header');

toggleTrigger.addEventListener('click', () => {
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
