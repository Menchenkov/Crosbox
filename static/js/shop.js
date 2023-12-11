
// Получаем кнопку "Добавить в корзину"
const addToCartBtn = document.querySelector('.add-to-cart-btn');

// Добавляем обработчик события "click" на кнопку
addToCartBtn.addEventListener('click', function() {
  // Получаем ID товара из атрибута "data-product-id"
  const productId = this.getAttribute('data-product-id');

  // Добавляем товар в корзину
  addToCart(productId);
});

// Функция для добавления товара в корзину
function addToCart(productId) {
  // Получаем текущее состояние корзины из localStorage
  let cart = JSON.parse(localStorage.getItem('cart')) || [];

  // Проверяем, есть ли уже такой товар в корзине
  const existingProductIndex = cart.findIndex(product => product.id === productId);

  if (existingProductIndex !== -1) {
    // Если товар уже есть в корзине, увеличиваем его количество на 1
    cart[existingProductIndex].quantity += 1;
  } else {
    // Если товара еще нет в корзине, добавляем его со значением количества 1
    cart.push({ id: productId, quantity: 1 });
  }

  // Сохраняем обновленное состояние корзины в localStorage
  localStorage.setItem('cart', JSON.stringify(cart));

  // Обновляем отображение корзины на странице
  updateCartView();
}

// Функция для обновления отображения корзины на странице
function updateCartView() {
  // Получаем элемент, в котором будет отображаться список товаров в корзине
  const cartItemsList = document.querySelector('.cart-items-list');

  // Получаем текущее состояние корзины из localStorage
  const cart = JSON.parse(localStorage.getItem('cart')) || [];

  // Очищаем список товаров в корзине
  cartItemsList.innerHTML = '';

  // Добавляем каждый товар из корзины в список
  cart.forEach(product => {
    const productElement = document.createElement('li');
    productElement.textContent = `Товар ${product.id}, количество: ${product.quantity}`;
    cartItemsList.appendChild(productElement);
  });
}