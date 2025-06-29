document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('.try-form').addEventListener('submit', function (e) {
    e.preventDefault();
    this.style.display = 'none';
    const thankYou = document.createElement('div');
    thankYou.textContent = 'Thanks for submitting!';
    thankYou.style.fontSize = '2rem';
    thankYou.style.color = '#ffb300';
    thankYou.style.textAlign = 'center';
    thankYou.style.marginTop = '40px';
    this.parentNode.appendChild(thankYou);
  });
});